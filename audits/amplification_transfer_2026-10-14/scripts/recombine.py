"""Exact test of the recombination transformation Phi at a branch node.

For every branch node (P, e<e') of the depth-N 0-confined tree, take every
0-confined word P||e'||t' in the e'-subtree and ask whether the recombined word
P||e||t' is still 0-confined.  Counts survivors exactly, integer arithmetic.

Also reports, for the reverse direction (onto the LARGER digit e'), the
confinement budget defect actually needed, i.e. the least c for which
P||e'||t is c-confined when P||e||t was 0-confined.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mass import sN


def confwords(N):
    """All 0-confined words of length N, as tuples.  2^{S_j} <= 3^j."""
    out = []
    def rec(w, S, j):
        if j == N:
            out.append(tuple(w)); return
        p3 = 3 ** (j + 1)
        d = 1
        while (1 << (S + d)) <= p3:
            w.append(d); rec(w, S + d, j + 1); w.pop()
            d += 1
    rec([], 0, 0)
    return out


def defect(w):
    """Least c >= 0 with 2^{S_j} <= 2^c 3^j for all j (0 iff 0-confined)."""
    S = 0; c = 0
    for j, d in enumerate(w, start=1):
        S += d
        p3 = 3 ** j
        need = 0
        while (1 << S) > (1 << need) * p3:
            need += 1
        c = max(c, need)
    return c


print(f"{'N':>3} {'#conf words':>12} {'#nodes':>8} {'down-shifts tried':>18}"
      f" {'survive':>8} {'rate':>7} | {'up-shifts tried':>16} {'survive':>8} {'rate':>7}"
      f" {'max defect':>11}")
for N in range(3, 13):
    W_ = confwords(N)
    S = set(W_)
    # index by prefix
    nodes = {}
    for w in W_:
        for j in range(0, N):
            nodes.setdefault(w[:j], set()).add(w[j])
    ndown = sdown = nup = sup_ = 0
    maxdef = 0
    nnode = 0
    for P, digits in nodes.items():
        ds = sorted(digits)
        if len(ds) < 2:
            continue
        nnode += 1
        j = len(P)
        for a in range(len(ds)):
            for b in range(a + 1, len(ds)):
                e, ep = ds[a], ds[b]
                # suffixes available under each child
                suf_e  = [w[j+1:] for w in W_ if w[:j] == P and w[j] == e]
                suf_ep = [w[j+1:] for w in W_ if w[:j] == P and w[j] == ep]
                # DOWN-shift: move e'-subtree suffixes onto the smaller digit e
                for t in suf_ep:
                    ndown += 1
                    cand = P + (e,) + t
                    if cand in S:
                        sdown += 1
                # UP-shift: move e-subtree suffixes onto the larger digit e'
                for t in suf_e:
                    nup += 1
                    cand = P + (ep,) + t
                    if cand in S:
                        sup_ += 1
                    else:
                        maxdef = max(maxdef, defect(cand))
    rd = sdown / ndown if ndown else float('nan')
    ru = sup_ / nup if nup else float('nan')
    print(f"{N:>3} {len(W_):>12} {nnode:>8} {ndown:>18} {sdown:>8} {rd:>7.4f} |"
          f" {nup:>16} {sup_:>8} {ru:>7.4f} {maxdef:>11}")

print()
print("Phi is a PARTIAL map into the confined set.  Key questions:")
print("  * is the image ever larger than the domain?  (it cannot be: Theorem 3)")
print("  * does the survivor RATE stay bounded away from 0 uniformly in N?")
print()
# explicit smallest example for the writeup
N = 4
W_ = confwords(N)
print(f"N=4: the {len(W_)} 0-confined words: {W_}")
root = {}
for w in W_:
    root.setdefault(w[0], []).append(w[1:])
print(f"  root children: { {k: len(v) for k, v in root.items()} }")
for e in sorted(root):
    for ep in sorted(root):
        if ep <= e: continue
        surv = [t for t in root[ep] if (e,) + t in set(W_)]
        print(f"  down-shift e'={ep} -> e={e}: {len(surv)}/{len(root[ep])} survive"
              f"   (failures: {[t for t in root[ep] if (e,)+t not in set(W_)]})")
