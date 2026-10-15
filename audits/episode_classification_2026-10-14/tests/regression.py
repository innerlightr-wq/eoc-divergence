#!/usr/bin/env python3
"""Regression suite.  Clean process, no cached state.  Exits nonzero on failure."""
import os, sys, math, resource
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'scripts'))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from fractions import Fraction as F
from eoc import *
alpha = math.log2(3)
fails = []
def chk(c, m):
    print(('PASS  ' if c else 'FAIL  ') + m)
    if not c: fails.append(m)

# Lemma A
bad = 0
for m0 in range(3, 20002, 2):
    d, S, m = orbit(m0, 10)
    for n in range(10):
        e = v2(m[n] + 1)
        if (d[n] == 1) != (e >= 2): bad += 1
        if d[n] == 1 and v2(m[n + 1] + 1) != e - 1: bad += 1
chk(bad == 0, "Lemma A: d_n=1 <=> v2(m_n+1)>=2, and the step decrements v2(m+1)")
bad = 0
for m0 in range(3, 20002, 2):
    d, _, _ = orbit(m0, 14)
    lead = 0
    while lead < 14 and d[lead] == 1: lead += 1
    if lead < 14 and lead != v2(m0 + 1) - 1: bad += 1
chk(bad == 0, "Lemma A: maximal ones-run from x has length exactly v2(x+1)-1")

# Lemma B
bad = 0
for m0 in range(3, 20002, 2):
    d, S, m = orbit(m0, 14)
    u = 0
    while u < 14 and d[u] == 1: u += 1
    if u and F(m[u] + 1) != F(3 ** u * (m0 + 1), 1 << u): bad += 1
    if u and (m0 + 1) % (1 << (u + 1)): bad += 1
chk(bad == 0, "Lemma B(a): y+1 = 3^u(x+1)/2^u exactly, and 2^{u+1} | x+1")

# Theorem C
Fk = lambda j: (alpha ** j + alpha - 2) / (alpha - 1) / (2 - alpha)
bad = 0
for m0 in (3, 7, 27, 31, 703, 10087, 35655, 285175, 381727, 626331):
    d, S, m = orbit(m0, 4000)
    N1 = next(n for n in range(len(m)) if m[n] == 1)
    j = sum(1 for (s, _) in runs(direction(d[:N1])) if s == 0)
    if N1 > Fk(max(j, 1)) * math.log2(m0 + 1): bad += 1
chk(bad == 0, "Theorem C holds on 10 real seeds up to arrival at 1")
chk(abs(Fk(1) - 4.818842) < 1e-5, f"F(k) coefficient at j=1 is 4.818842 (got {Fk(1):.6f})")

# D_L
bad = 0
for L in (1, 2, 3, 5, 8, 12):
    d = [3] + [1] * L + [L + 2]
    r, C, SN = least_realizer(d)
    dd, S, m = orbit(r, len(d))
    z = [F(1 << S[n], 3 ** n) for n in range(len(d) + 1)]
    ep = [(a, b) for (a, b, _) in episodes(S, len(d), 1)]
    W = sum(z[n] for n in range(2, L + 2))
    if tuple(dd) != tuple(d): bad += 1
    if ep != [(0, 1), (2, L + 2)]: bad += 1
    if W != F(16, 3) * (1 - F(2, 3) ** L): bad += 1
    if (r + 3) % (1 << (L + 4)): bad += 1
chk(bad == 0, "D_L: word, episodes [0,1)+[2,L+2), W_L=(16/3)(1-(2/3)^L), 2^{L+4}|r+3")

# Theorem D
def Amin(u, q, v):
    Mod = 1 << (q + v)
    a = (pow(pow(3, u + 1, Mod), -1, Mod) * ((1 - (1 << (q - 1))) % Mod)) % Mod
    if a == 0: a = Mod
    for cand in (a, a + Mod):
        Z = pow(3, u + 1) * cand
        if v2(Z - 1) != q - 1: continue
        if v2(((Z - 1) >> (q - 1)) + 1) == v + 1: return cand
    return None
def wp(x, u, q, v):
    d, S, m = orbit(x, u + v + 3)
    return (tuple(d[:u]) == (1,) * u and d[u] == q
            and tuple(d[u+1:u+1+v]) == (1,) * v and d[u+1+v] >= 2)
bad = 0; n = 0
for u in (1, 2, 3, 5):
    for q in (2, 3, 4):
        for v in (1, 2, 3):
            A = Amin(u, q, v)
            if A is None: continue
            x = (1 << (u + 1)) * A - 1
            n += 1
            if not wp(x, u, q, v): bad += 1
            if not ((1 << (u + 1)) - 1 <= x < (1 << (u + q + v + 2))): bad += 1
            bf = next((y for y in range(3, x + 2, 2) if wp(y, u, q, v)), None)
            if bf != x: bad += 1
chk(bad == 0, f"Theorem D: x+1 = 2^(u+1) A_min is exact, minimal and within "
              f"[2^(u+1)-1, 2^(u+q+v+2)) on {n} triples")

# Loeb
d, S, m = orbit(285175, 140)
ep = [(a, b) for (a, b, _) in episodes(S, 138, 1)]
chk(ep == [(0,15),(16,20),(21,27),(31,95),(98,99),(100,105),(108,111)],
    "Loeb: the seven occupied runs")
chk(sum(b - a for (a, b) in ep) == 98, "Loeb: O_1 = 98")
chk([changes(direction(d[a:b])) for (a, b) in ep] == [7, 1, 3, 25, 0, 3, 1],
    "Loeb: the internal direction-change counts are 7,1,3,25,0,3,1")
chk(all(d[a - 1] == 1 for (a, b) in ep if a > 0), "Loeb: d_(a-1)=1 at every re-entry")

print()
print(('REGRESSION: ALL PASS' if not fails else f'REGRESSION: {len(fails)} FAILURES'))
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
sys.exit(1 if fails else 0)
