import sys, math, glob
from q5b import load
from q5fit import compare, bootstrap, resid
from nullmodel import transfer, log2_inv_p

E1 = 1 - 0.5772156649015329/math.log(2)
CH  = '/tmp/claude-1000/-home-elias/c3a43061-2697-4bee-adda-ceb1e6215d18/scratchpad/chunks/*.txt'
CH2 = '/tmp/claude-1000/-home-elias/c3a43061-2697-4bee-adda-ceb1e6215d18/scratchpad/chunks2/*.txt'

def series(paths, tag, shift, bound):
    tab = load(paths, tag); nums = transfer(max(tab)); B = math.log2(bound)
    pts, seen = [], None
    for N in sorted(tab):
        if tab[N][0] != seen:
            seen = tab[N][0]; L = log2_inv_p(N, nums) + shift
            pts.append((N, math.log2(seen) - L, B - L))
    kept = [(N, d, c) for N, d, c in pts if c >= d + 3.5]
    return kept, len(pts) - len(kept)

def report(pts, dropped, label):
    print("\n" + "=" * 90); print(label); print("=" * 90)
    xs = [N for N, _, _ in pts]; ys = [d for _, d, _ in pts]
    print(f"distinct record holders: {len(pts)}"
          + (f"  ({dropped} dropped by the censoring rule)" if dropped else ""))
    print("  N :", xs)
    print("  D :", " ".join(f"{d:+.2f}" for d in ys))
    print(f"  Poisson E = {E1:+.3f};  every value above E ? {all(d > E1 for d in ys)};"
          f"  min {min(ys):+.3f}  mean {sum(ys)/len(ys):+.3f}")
    late = [d for N, d, _ in pts if N >= 180]
    if late:
        print(f"  late block N >= 180: n={len(late)} mean {sum(late)/len(late):+.3f} "
              f"min {min(late):+.3f}")
    out, best = compare(xs, ys)
    print(f"\n  {'model':>6} {'rss':>8} {'rho1':>7} {'n_eff':>7} {'AICc':>9} {'dAICc':>8}  params")
    for k in ('B', 'A1', 'A2'):
        a, rss, p, c, r, ne = out[k]
        ps = f"a={p[0]:+.3f} b={p[1]:+.5f}" + (f" c={c:.1f}" if c else "")
        print(f"  {k:>6} {rss:>8.3f} {r:>7.3f} {ne:>7.2f} {a:>9.3f} "
              f"{a-out[best][0]:>8.2f}  {ps}")
    print(f"  -> lowest AICc: {best}")
    wins, ci, ms = bootstrap(xs, ys)
    tot = sum(wins.values()); span = max(xs) - min(xs)
    print(f"\n  block bootstrap (L=3, {tot} resamples): "
          + ", ".join(f"{k} {100*wins[k]/tot:.1f}%" for k in ('B', 'A1', 'A2')))
    print(f"  linear slope b: mean {ms:+.5f}, 95% CI [{ci[0]:+.5f}, {ci[1]:+.5f}]")
    print(f"     over N = {min(xs)}..{max(xs)}: {ms*span:+.2f} bits, "
          f"CI [{ci[0]*span:+.2f}, {ci[1]*span:+.2f}]"
          + ("   (CI excludes 0)" if ci[0]*ci[1] > 0 else "   (CI includes 0)"))

if __name__ == "__main__":
    p, d = series(glob.glob(CH), None, 0.0, 1e12)
    report(p, d, "Q5  ALL  -- every N-confined odd integer, 10^12 scan")
    R = glob.glob(CH2)
    if R:
        p, d = series(R, "R", math.log2(1.5), 2.5e11)
        report(p, d, "Q5  ROOTS  -- chain roots only (m != 2 mod 3), null (2/3)p_N, 2.5e11 scan")
        p, d = series(R, "A", 0.0, 2.5e11)
        report(p, d, "Q5  ALL on the SAME 2.5e11 range (control for the range difference)")
