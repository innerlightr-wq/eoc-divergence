#!/usr/bin/env python3
"""No arithmetic selection signal beyond the confinement barrier.

Companion to per_cylinder_survival.py.  That script proves the one-step law is
symbolic plus a height-truncation term; this one measures that nothing else is
present, which is the empirical half of the same statement.

The barrier state at depth N is R_N = (N, S_N).  Conditional on R_N the SYMBOLIC
one-step survival probability is exactly

    P(a_N <= K)  =  1 - 2^{-K(N,S)},      K(N,S) = max{ a : 2^{S+a} <= 3^{N+1} },

so every test below takes its expectation PER BARRIER CELL and asks whether any
arithmetic feature of the depth-N state shifts the observed rate away from it.

NO-LOOK-AHEAD RULE.  Features may use only (N, S_N, m_N, a_1..a_{N-1}, m_0).  The
label alone uses a_N.  m_N mod 2^k is EXCLUDED: a_N = v_2(3 m_N + 1) is a function of
m_N mod 2^{a_N+1}, so a 2-adic feature at that precision encodes the label.  This is
not a conservative choice, it is forced -- per_cylinder_survival.py shows a_N is a
bijective function of the cylinder index t mod 2^K and of nothing else, which is why
every non-2-adic feature below must come out null.

Exact integer arithmetic for p_N and every count; floats only for z scores and
log-losses.  z = (observed - expected)/sd with the expectation summed per cell.
"""
import math
import random
from collections import defaultdict
from fractions import Fraction


def confined_mass(nmax):
    f = {0: 1}
    P = [Fraction(1)]
    for n in range(1, nmax + 1):
        g = {}
        for S, c in f.items():
            a = 1
            while (1 << (S + a)) <= 3 ** n:
                g[S + a] = g.get(S + a, 0) + c
                a += 1
        f = g
        P.append(sum(Fraction(c, 1 << S) for S, c in f.items()))
    return P


_K = {}


def Kcap(N, S):
    if (N, S) not in _K:
        a = 0
        while (1 << (S + a + 1)) <= 3 ** (N + 1):
            a += 1
        _K[(N, S)] = a
    return _K[(N, S)]


def rows(B, nmax=160, q=1, keep=2):
    """(N, S_N, m_N, recent valuations, label, A_N) for every confined survivor"""
    M = (1 << B) - 1
    pop = [(m, m, 0, ()) for m in range(1, M + 1, 2)]
    levels = [pop]
    for n in range(1, nmax + 1):
        nxt, p3 = [], 3 ** n
        for m0, m, S, h in pop:
            x = 3 * m + q
            if x <= 0:
                continue
            a = (x & -x).bit_length() - 1
            S2 = S + a
            if (1 << S2) <= p3:
                nxt.append((m0, x >> a, S2, (h + (a,))[-keep:]))
        pop = nxt
        levels.append(pop)
        if not pop:
            break
    out = []
    for N in range(len(levels) - 1):
        if not levels[N]:
            break
        alive = {r[0] for r in levels[N + 1]}
        A = len(levels[N])
        for m0, m, S, h in levels[N]:
            out.append((N, S, m, h, 1 if m0 in alive else 0, A))
    return out, [len(s) for s in levels]


def ztable(data, feat, name, minn=200, show=6):
    acc = defaultdict(lambda: [0, 0, 0.0])
    for r in data:
        k = feat(r)
        if k is None:
            continue
        d = acc[k]
        d[0] += 1
        d[1] += r[4]
        d[2] += 1 - 2.0 ** (-Kcap(r[0], r[1]))
    worst = chi = 0.0
    dof = 0
    shown = []
    for k, (n, o, e) in sorted(acc.items(), key=lambda t: str(t[0])):
        if n < minn:
            continue
        sd = math.sqrt(max(e * (1 - e / n), 1e-9))
        z = (o - e) / sd
        worst = max(worst, abs(z))
        chi += z * z
        dof += 1
        shown.append(f"{k}:{z:+.2f}")
    print(f"      {name:<36} max|z|={worst:6.2f}  chi2={chi:8.2f}/{dof:<3}"
          f" {' '.join(shown[:show])}")


def logloss(data, tilt):
    L = 0.0
    for r in data:
        e = 1 - 2.0 ** (-Kcap(r[0], r[1]))
        p = min(max(e + tilt.get(tuple(r[3]) if len(r[3]) == 2 else None, 0.0), 1e-6),
                1 - 1e-6)
        L -= math.log(p) if r[4] else math.log(1 - p)
    return L / len(data)


print(__doc__)
print("=" * 78)
print("FEATURE SWEEP, WITH THE 3x-1 CONTROL AND SHUFFLE CONTROLS")
print("=" * 78)
for label, qq in (("3x+1", 1), ("3x-1 CONTROL", -1)):
    for B in (16, 20):
        data, _ = rows(B, q=qq)
        obs = sum(r[4] for r in data)
        exp = sum(1 - 2.0 ** (-Kcap(r[0], r[1])) for r in data)
        print(f"  --- {label}, M = 2^{B}-1 ---  rows={len(data):,}  observed={obs:,}"
              f"  expected={exp:,.1f}  GLOBAL z={(obs - exp) / math.sqrt(exp):+.3f}")
        for qm in (3, 5, 7, 9, 11, 13):
            ztable(data, lambda r, qm=qm: r[2] % qm, f"m_N mod {qm}")
        ztable(data, lambda r: r[3][-1] if r[3] else None, "previous valuation a_{N-1}")
        ztable(data, lambda r: tuple(r[3]) if len(r[3]) == 2 else None,
               "(a_{N-2}, a_{N-1})", minn=400, show=5)
        ztable(data, lambda r, B=B: min(9, r[2].bit_length() * 10 // (B + 2)),
               "height decile of m_N")
        sh = [r[4] for r in data]
        random.Random(7).shuffle(sh)
        ztable([r[:4] + (sh[i],) + r[5:] for i, r in enumerate(data)],
               lambda r: r[2] % 7, "CONTROL shuffled labels, mod 7")
        hs = [r[3] for r in data]
        random.Random(9).shuffle(hs)
        ztable([r[:3] + (hs[i],) + r[4:] for i, r in enumerate(data)],
               lambda r: r[3][-1] if r[3] else None, "CONTROL shuffled histories")
        print()

print("=" * 78)
print("HELD-OUT HEIGHTS: the one marginal in-sample feature ANTI-TRANSFERS")
print("=" * 78)
train = []
for B in (12, 14, 16):
    d, _ = rows(B)
    train += d
num, den = defaultdict(float), defaultdict(int)
for r in train:
    k = tuple(r[3]) if len(r[3]) == 2 else None
    if k is None:
        continue
    num[k] += r[4] - (1 - 2.0 ** (-Kcap(r[0], r[1])))
    den[k] += 1
tilt = {k: num[k] / den[k] for k in num if den[k] >= 400}
print(f"  trained on M = 2^12-1, 2^14-1, 2^16-1: rows={len(train):,},"
      f" tilt classes={len(tilt)}, largest |tilt|={max(abs(v) for v in tilt.values()):.4f}")
print(f"  {'test M':>10} {'rows':>12} {'log-loss base':>14} {'log-loss+tilt':>14}"
      f" {'improvement':>13} {'global z':>9}")
for B in (18, 20):
    d, _ = rows(B)
    lb, lt = logloss(d, {}), logloss(d, tilt)
    o = sum(r[4] for r in d)
    e = sum(1 - 2.0 ** (-Kcap(r[0], r[1])) for r in d)
    print(f"  2^{B}-1 {len(d):>14,} {lb:>14.6f} {lt:>14.6f} {lb - lt:>+13.2e}"
          f" {(o - e) / math.sqrt(e):>+9.3f}")
    for nm, lo, hi in (("large A>=100", 100, 1 << 62), ("intermediate 10<=A<100", 10, 100),
                       ("endgame 1<=A<10", 1, 10)):
        sub = [r for r in d if lo <= r[5] < hi]
        if len(sub) < 50:
            print(f"        {nm:<24} rows={len(sub):>9,}   (too few to report)")
            continue
        o = sum(r[4] for r in sub)
        e = sum(1 - 2.0 ** (-Kcap(r[0], r[1])) for r in sub)
        print(f"        {nm:<24} rows={len(sub):>9,}   improvement="
              f"{logloss(sub, {}) - logloss(sub, tilt):+.2e}   z={(o - e) / math.sqrt(e):+.2f}")
print("  A NEGATIVE improvement means the fitted tilt makes held-out prediction WORSE.")

print()
print("=" * 78)
print("WHERE THE DRIFT LIVES:  g = g_comp + g_arith")
print("=" * 78)
print("  h_int = A_{N+1}/A_N,  h_sym = p_{N+1}/p_N,  h_bar = E_nu[1 - 2^{-K}] with nu the")
print("  barrier-state distribution of the INTEGER survivors.  Then")
print("      g = log2(h_int/h_sym) = log2(h_bar/h_sym) + log2(h_int/h_bar) = g_comp + g_arith,")
print("  g_comp being pure composition (nu versus Haar mu) and g_arith the residue.")
print()
P = confined_mass(160)
for B in (16, 20):
    M = (1 << B) - 1
    OM = (M + 1) // 2
    data, A = rows(B)
    nu = defaultdict(lambda: defaultdict(int))
    for r in data:
        nu[r[0]][r[1]] += 1
    cg = ca = 0.0
    print(f"  --- M = 2^{B}-1 ---")
    print(f"   {'N':>4} {'A_N':>10} {'log2 Q_N':>10} {'sum g_comp':>11} {'sum g_arith':>12}")
    for N in range(len(A) - 1):
        if A[N] == 0 or A[N + 1] == 0:
            break
        hint = A[N + 1] / A[N]
        hsym = float(P[N + 1] / P[N])
        hbar = sum(c * (1 - 2.0 ** (-Kcap(N, s))) for s, c in nu[N].items()) / A[N]
        cg += math.log2(hbar / hsym)
        ca += math.log2(hint / hbar)
        if N % 8 == 0 or A[N + 1] < 8:
            lq = math.log2(A[N + 1] / (OM * float(P[N + 1])))
            print(f"   {N+1:>4} {A[N+1]:>10,} {lq:>+10.4f} {cg:>+11.4f} {ca:>+12.4f}")
    print()
print("  The systematic drift is carried by g_comp.  Since nu(S) = A_{N,M}(S)/A_{N,M},")
print("  the measure nu IS the placement datum: it is not computable from symbolic")
print("  depth-<=N data.  g_arith stays small until the survivor count is O(1), where it")
print("  is dominated by discreteness (a single survivor forces h_int in {0,1}).")
