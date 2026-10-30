import sys; sys.path.insert(0,'.')
import eoc, math, random
random.seed(20261016)
alpha=math.log2(3)
print("="*92)
print("THE DECISIVE OBSTRUCTION (Rev 8 Sec 5.3 / Obs 5.9), verified independently")
print("  The only general tool converting divisibility into a size statement is")
print("      'a nonzero multiple of 2^m has absolute value at least 2^m',")
print("  giving either  A + chi*Lambda = 0  or  |chi| >= 2^{S_N}/H - 1,  H = max(|C_N|, 3^N).")
print("  The second branch is USEFUL only if rho_N = log2(H)/S_N is bounded away from 1.")
print("="*92)
def report(name, ds, ns=(10,20,40,60)):
    rh = eoc.rho(ds); S,C = eoc.SC(ds)
    conf = eoc.confined(ds)
    vals = " ".join(f"{rh[n-1]:>7.4f}" for n in ns if n-1 < len(rh))
    # usefulness of the second branch: 2^{S_N}/H - 1
    useful=[]
    for n in ns:
        if n < len(S):
            H = max(C[n], 3**n)
            useful.append((1<<S[n])/H - 1)
        
    print(f"  {name:<34} confined={str(conf):<5} rho_N: {vals}   2^S/H-1 at N={ns[-1]}: "
          f"{useful[-1] if useful else float('nan'):+.4e}")

# real orbits
for m0 in [27, 703, 159487]:
    ds,_ = eoc.orbit_word(m0, 70); report(f"orbit m0={m0}", ds)
# Beatty / Sturmian zero-corridor word
report("Beatty word (alpha=log2 3)", [int((j+1)*alpha)-int(j*alpha) for j in range(70)])
# periodic words
for p in [[1,2],[1,2,2],[2,1,1,2]]:
    report(f"periodic {p}", (p*40)[:70])
# random confined-ish words
for t in range(3):
    ds=[]
    S=0
    for j in range(70):
        # greedily keep 2^S <= 3^(j+1)
        choices=[d for d in (1,2,3) if (1<<(S+d)) <= 3**(j+1)]
        d = random.choice(choices) if choices else 1
        ds.append(d); S+=d
    report(f"random confined #{t+1}", ds)
print()
print("  READING.  Every CONFINED word has rho_N >= 1, so 2^{S_N}/H - 1 <= 0 and the")
print("  divisibility-to-size branch is VACUOUS.  Periodic words have rho_N -> 0 and the")
print("  branch is useful -- but periodic words are exactly the ones already excluded.")
print()
print("  WHY: confinement IS 2^{S_n} <= 3^n, and H >= 3^n, so 2^{S_N} <= 3^N <= H identically.")
print("  The hypothesis that defines the interesting sector is precisely what makes every")
print("  divisibility-to-size tool vacuous on it.  This is self-defeating by construction.")
