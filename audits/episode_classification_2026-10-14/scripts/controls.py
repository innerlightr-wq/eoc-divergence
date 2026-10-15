"""Step 5: the Loeb classifier and the pre-specified controls."""
import os, sys, math, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from fractions import Fraction as F
from eoc import *
alpha = math.log2(3)
fails = []
def chk(c, m):
    print(('PASS  ' if c else 'FAIL  ') + m); 
    if not c: fails.append(m)

print("=" * 96)
print("THE CLASSIFIER ON THE LOEB BENCHMARK  m_0 = 285175, c = 1")
print("=" * 96)
m0, c = 285175, 1
H = 138                                  # certified: m_138 = 1 and R rises thereafter
d, S, m = orbit(m0, H + 40)
eps = episodes(S, H, c)
chk([(a, b) for (a, b, _) in eps] == [(0,15),(16,20),(21,27),(31,95),(98,99),(100,105),(108,111)],
    "the seven occupied runs replicate")
chk(sum(b - a for (a, b, _) in eps) == 98, "O_1 = 98")
print()
print(f"{'i':>2} {'[a,b)':>12} {'l':>4} {'block D_I = (d_a..d_(b-1))':>46} "
      f"{'direction word':>18} {'k':>3} {'runs (sym,len)':>26} {'F_k class':>9}")
for i, (a, b, trunc) in enumerate(eps):
    D = d[a:b]                           # boundary-inclusive: includes the exit transition
    sym = direction(D); k = changes(sym)
    Ds = str(tuple(D)) if len(D) <= 10 else str(tuple(D[:5]))[:-1] + ", ...]".replace('[','')
    Ds = str(tuple(D)) if len(D) <= 10 else f"({D[0]},{D[1]},...,{D[-2]},{D[-1]}) len {len(D)}"
    print(f"{i:>2} {f'[{a},{b})':>12} {b-a:>4} {Ds:>46} "
          f"{''.join(map(str,sym)) if len(sym)<=18 else ''.join(map(str,sym[:8]))+'...':>18} "
          f"{k:>3} {str(runs(sym)) if len(runs(sym))<=5 else str(runs(sym)[:3])+'...':>26} F_{k}")
print()
print("  Note the boundary convention at work: D_I includes d_{b-1}, the outgoing")
print("  transition, so the LAST symbol of every complete episode's direction word is")
print("  the one that carries R above c.  The entry transition d_{a-1} is excluded and")
print("  stored separately: d_{a-1} = 1 at every re-entry (Rev 8 Prop. 13.1).")
pre = [d[a-1] for (a, b, _) in eps if a > 0]
chk(all(x == 1 for x in pre), f"d_(a-1) = 1 at all {len(pre)} re-entries: {pre}")

print()
print("=" * 96)
print("CONTROLS")
print("=" * 96)
print("A. least realizer vs larger lifts of the SAME word.")
print("   The word, direction runs, k, episode structure and W are class invariants;")
print("   the absolute seed is not.  So a bound on the LEAST realizer is not obtained")
print("   by making some realizer large, and vice versa.")
dL = [3] + [1]*8 + [10]
r, C, SN = least_realizer(dL)
print(f"   word {tuple(dL)}: least r = {r}, class r mod 2^{SN+1} = {r} mod {1<<(SN+1)}")
print(f"   {'lift':>14} {'word reproduced':>16} {'k':>3} {'episodes (c=1)':>20}")
bad = 0
for t in range(4):
    x = r + t * (1 << (SN + 1))
    dd, SS, mm = orbit(x, len(dL))
    ok = tuple(dd) == tuple(dL)
    bad += (not ok)
    print(f"   {x:>14} {str(ok):>16} {changes(direction(dd)):>3} "
          f"{str([(a,b) for (a,b,_) in episodes(SS,len(dL),1)]):>20}")
chk(bad == 0, "every lift in the class reproduces the word, k and the episodes")

print()
print("B. long all-ones (Mersenne) prefixes: the ones-run is maximal at length u =")
print("   v2(m_0+1)-1, and q is then DETERMINED, so (u,q,v) is not free here.")
print(f"   {'u':>3} {'m_0':>12} {'max ones-run':>13} {'v2(m0+1)-1':>11} {'then q':>7}")
bad = 0
for u in (3, 7, 11, 15, 19):
    x = (1 << (u + 1)) - 1
    dd, SS, mm = orbit(x, u + 3)
    lead = 0
    while dd[lead] == 1: lead += 1
    bad += (lead != v2(x + 1) - 1 or lead != u)
    print(f"   {u:>3} {x:>12} {lead:>13} {v2(x+1)-1:>11} {dd[u]:>7}")
chk(bad == 0, "Mersenne: maximal ones-run = v2(m_0+1)-1 = u")

print()
print("C. the Prop. 13.2 oscillator: short episodes, k small INSIDE each episode but")
print("   the episode COUNT unbounded -- a per-episode bound on k bounds nothing global.")
def osc(c, N):
    S = [0]; dd = []
    for n in range(N):
        x = 2 if (1 << S[n]) <= (1 << c) * 3 ** n else 1
        dd.append(x); S.append(S[n] + x)
    return dd, S
for cc in (0, 1):
    dd, SS = osc(cc, 200)
    ee = episodes(SS, 200, cc)
    ks = [changes(direction(dd[a:b])) for (a, b, _) in ee]
    print(f"   c={cc}: {len(ee)} episodes, max internal k = {max(ks)}, "
          f"global k over [0,200) = {changes(direction(dd))}")
print("   => internal k <= 1 while the global change count grows linearly in N.")

print()
print("D. eventual fixed-point tail.  At m = 1, d = 2 and R rises by 2-alpha per step,")
print("   so after arrival the orbit leaves every corridor and never returns.")
d1, S1, m1 = orbit(1, 12)
print(f"   orbit of 1: m = {m1[:6]}, d = {d1[:6]}, R_n - R_0 = "
      f"{[round(S1[n]-alpha*n,4) for n in range(6)]}")
chk(all(x == 2 for x in d1), "at m=1 every valuation is 2")

print()
print("E. prescribed word over positive reals, no integer ray.  Fix the word of 285175")
print("   and run x -> (3x+1)/2^{d_n} from several real x_0 > 0.")
for x0 in (F(285175), F(1, 7), F(10 ** 9)):
    x = x0
    for n in range(40): x = (3 * x + 1) / (1 << d[n])
    print(f"   x_0 = {float(x0):>14.6g}  ->  x_40 = {float(x):>16.6g}   "
          f"(integer orbit m_40 = {m[40]})")
print("   The R-profile, the episodes, k and the run structure are PRESCRIBED by the")
print("   word, so they are identical for every real x_0 > 0.  Everything that")
print("   distinguishes seeds -- the 2^{u+1} | x+1 condition of Lemma A, the residue")
print("   class of Theorem D -- comes from INTEGRALITY alone.  A positive-real")
print("   trajectory has no minimum-seed cost at all.")
print()
print(('ALL PASS' if not fails else f'{len(fails)} FAILURES'))
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
sys.exit(1 if fails else 0)
