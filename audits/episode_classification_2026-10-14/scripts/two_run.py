"""Step 3-4: the D_L control, and the main attempt on the class 1^u q 1^v.

MAIN CLAIM (written in ANALYSIS_PLAN.md before testing).  Let x be a state whose
maximal d=1 run has length exactly u, i.e. x+1 = 2^{u+1} A with A odd.  Then:
   after u ones-steps   x_1 + 1 = 2 * 3^u A ,
   the next valuation   q = 1 + v2(Z-1),  Z := 3^{u+1} A ,
   the next state       x_2 = M  where  Z - 1 = 2^{q-1} M,  M odd ,
   the next ones-run    v = v2(M+1) - 1 .
Hence the word begins 1^u q 1^v exactly iff
   Z == 1 - 2^{q-1}  (mod 2^{q+v})   and   Z != 1 - 2^{q-1}  (mod 2^{q+v+1}) ,
i.e. A lies in ONE residue class mod 2^{q+v}:
   A == 3^{-(u+1)} (1 - 2^{q-1})  (mod 2^{q+v}) .
So the minimum seed FACTORS:   x + 1 = 2^{u+1} * A_min(u,q,v),  A_min < 2^{q+v+1}.
If so, the answer to the primary question is NO: the two growth runs cost
(first-run 2-adic cost) x (second-run congruence cost), with no cross term.
"""
import os, sys, math, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from fractions import Fraction as F
from eoc import *
alpha = math.log2(3)
fails = []
def chk(c, m):
    print(('PASS  ' if c else 'FAIL  ') + m)
    if not c: fails.append(m)

# ---------------------------------------------------------------- D_L control
print("=" * 94)
print("CONTROL D_L = (3, 1^L, L+2) at c = 1 -- verified independently from exact arithmetic")
print("=" * 94)
print(f"{'L':>3} {'episode':>12} {'l':>4} {'w_max pred':>11} {'w_max obs':>10} "
      f"{'W_L pred':>11} {'W_L obs':>11} {'2^(L+4)|m0+3':>13} {'least r':>22} {'word ok':>8}")
badD = 0
for L in (1, 2, 3, 5, 8, 12, 16):
    d = [3] + [1] * L + [L + 2]
    r, C, SN = least_realizer(d)
    dd, S, m = orbit(r, len(d))
    word_ok = tuple(dd) == tuple(d)
    eps = episodes(S, len(d), 1)
    # predictions
    pred_w = (alpha - 1) * (L + 1) - 1
    pred_W = F(16, 3) * (1 - F(2, 3) ** L)
    z = [F(1 << S[n], 3 ** n) for n in range(len(d) + 1)]
    ep = [(a, b) for (a, b, _) in eps]
    # R_0 = 0 <= c so time zero is occupied: [0,1) is a genuine INITIAL episode
    # (Rev 8 Def. 6.1 counts from n = 0).  The prediction concerns the LATER
    # episode [2,L+2) only, so the observations below are restricted to it.
    later = [(a, b) for (a, b) in ep if a == 2]
    obs_w = max(1 - math.log2(float(z[n])) for (a, b) in later for n in range(a, b)) if later else None
    obs_W = sum(z[n] for (a, b) in later for n in range(a, b))
    div_ok = (r + 3) % (1 << (L + 4)) == 0
    ok = (word_ok and ep == [(0, 1), (2, L + 2)] and div_ok and obs_W == pred_W
          and abs(obs_w - pred_w) < 1e-9)
    badD += (not ok)
    print(f"{L:>3} {str(ep):>12} {L:>4} {pred_w:>11.6f} {obs_w:>10.6f} "
          f"{float(pred_W):>11.7f} {float(obs_W):>11.7f} {str(div_ok):>13} {r:>22} {str(word_ok):>8}")
chk(badD == 0, f"D_L: episode [2,L+2), l=L, w_max=(alpha-1)(L+1)-1, "
               f"W_L=(16/3)(1-(2/3)^L) exact, 2^(L+4)|m_0+3 ({badD} failures)")
print()
print("  CONSEQUENCE.  w_max grows LINEARLY in l = L while W_L stays below 16/3, so a")
print("  seed-independent bound  w_max <= K log2(l) + C  is FALSE for complete finite")
print("  positive-orbit episodes.  This REFUTES the (DEPTH-DURATION) lemma proposed at")
print("  the end of the previous round.  The cost appears instead in the seed:")
print("  m_0 >= 2^{L+4} - 3, i.e. log2 m_0 >= L + 4 - o(1) -- linear in the depth.")
print("  It does NOT refute the statement restricted to globally divergent orbits:")
print("  these seeds reach 1, so by Rev 8 Lemma 4.2 their drift tends to +infinity.")

# ------------------------------------------------- main attempt: 1^u q 1^v
print()
print("=" * 94)
print("MAIN ATTEMPT: the class 1^u q 1^v -- does the factorisation hold?")
print("=" * 94)

def Amin(u, q, v):
    """least positive A in the predicted class, with the exactness condition."""
    Mod = 1 << (q + v)
    tgt = (1 - (1 << (q - 1))) % Mod
    a = (pow(pow(3, u + 1, Mod), -1, Mod) * tgt) % Mod
    if a == 0: a = Mod
    for cand in (a, a + Mod):                     # exactness kills at most one
        Z = pow(3, u + 1) * cand
        if v2(Z - 1) != q - 1: continue
        M = (Z - 1) >> (q - 1)
        if v2(M + 1) == v + 1: return cand
    return None

def word_prefix(x, u, q, v):
    """does the orbit of x begin with 1^u, q, 1^v, with BOTH ones-runs MAXIMAL?

    Maximality matters: without the trailing d >= 2 test, a seed whose second
    ones-run is LONGER than v also passes, and the brute-force minimum then
    undercuts the predicted A_min.  (That is exactly what an earlier version of
    this test did: it reported 28 spurious failures, e.g. x = 27 for
    (u,q,v) = (1,2,1), whose second run actually has v = 4.)"""
    d, S, m = orbit(x, u + 1 + v + 2)
    if tuple(d[:u]) != (1,) * u: return False
    if d[u] != q: return False                       # forces the first run maximal
    if tuple(d[u+1:u+1+v]) != (1,) * v: return False
    return d[u+1+v] >= 2                             # forces the second run maximal

print(f"{'u':>3} {'q':>3} {'v':>3} {'A_min':>12} {'x=2^(u+1)A_min-1':>22} "
      f"{'word ok':>8} {'brute-force min x':>20} {'equal':>6} {'2^(u+1)-1 <= x':>15}")
badM = 0; tested = 0
for u in (1, 2, 3, 5, 8):
    for q in (2, 3, 4):
        for v in (1, 2, 3, 5):
            A = Amin(u, q, v)
            if A is None:
                print(f"{u:>3} {q:>3} {v:>3} {'none':>12}   (exactness unsatisfiable)")
                continue
            x = (1 << (u + 1)) * A - 1
            ok = word_prefix(x, u, q, v)
            # brute force the true minimum over odd x, bounded by the predicted value
            bf = None
            for y in range(3, min(x + 2, 1 << 22), 2):
                if word_prefix(y, u, q, v): bf = y; break
            eq = (bf == x)
            lo = (1 << (u + 1)) - 1 <= x
            tested += 1
            if not (ok and eq and lo): badM += 1
            print(f"{u:>3} {q:>3} {v:>3} {A:>12} {x:>22} {str(ok):>8} "
                  f"{str(bf):>20} {str(eq):>6} {str(lo):>15}")
chk(badM == 0, f"factorisation x+1 = 2^(u+1) A_min is EXACT and minimal on "
               f"{tested} (u,q,v) triples ({badM} failures)")
print()
print("  So the realising set of 1^u q 1^v is  { x : x+1 = 2^{u+1} A,  A odd,")
print("  A == 3^{-(u+1)}(1-2^{q-1}) mod 2^{q+v} }, and")
print("        2^{u+1} - 1  <=  r(1^u q 1^v)  <  2^{u+q+v+2} .")
print("  The two run costs MULTIPLY and there is no cross term: the first run")
print("  contributes the factor 2^{u+1} and the second contributes a residue class")
print("  mod 2^{q+v}.  ANSWER TO THE PRIMARY QUESTION: NO extra joint cost.")
print()
print("  When is the lower bound 2^{u+1}-1 attained?  Exactly when A_min = 1, i.e.")
print("  3^{u+1} == 1 - 2^{q-1} mod 2^{q+v}, i.e. when x = 2^{u+1}-1 is itself the")
print("  realiser -- the Mersenne/all-ones-prefix seeds, for which q and v are")
print("  DETERMINED by u:")
print(f"  {'u':>3} {'x=2^(u+1)-1':>14} {'q':>3} {'v':>3} {'v2(3^(u+1)-1)':>14} {'A_min(u,q,v)':>13}")
for u in (1, 2, 3, 4, 5, 7, 8, 11, 15):
    x = (1 << (u + 1)) - 1
    d, S, m = orbit(x, u + 2 + 40)
    q = d[u]
    vv = 0
    while d[u + 1 + vv] == 1: vv += 1
    print(f"  {u:>3} {x:>14} {q:>3} {vv:>3} {v2(3**(u+1)-1):>14} {str(Amin(u,q,vv)):>13}")
print()
print(('ALL PASS' if not fails else f'{len(fails)} FAILURES'))
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
sys.exit(1 if fails else 0)
