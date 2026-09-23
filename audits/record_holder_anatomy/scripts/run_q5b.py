import sys, math, glob
from q5b import load, analyse, bootstrap
from nullmodel import transfer, log2_inv_p

def series(paths, tag, shift, bound):
    tab = load(paths, tag)
    nums = transfer(max(tab)); B = math.log2(bound)
    pts, seen = [], None
    for N in sorted(tab):
        if tab[N][0] != seen:
            seen = tab[N][0]; L = log2_inv_p(N, nums) + shift
            pts.append((N, math.log2(seen) - L, B - L))
    return [(N, d, c) for N, d, c in pts if c >= d + 3.5], nums

def report(pts, label, E1):
    print(f"\n{'='*86}\n{label}\n{'='*86}")
    print(f"distinct record holders after the censoring rule: {len(pts)}")
    print("  N :", [N for N, _, _ in pts])
    print("  D :", " ".join(f"{d:+.2f}" for _, d, _ in pts))
    print(f"\nPoisson E[Delta_1] = {E1:+.3f}")
    print(f"  every value above E ?  {all(d > E1 for _, d, _ in pts)}    "
          f"min = {min(d for _, d, _ in pts):+.3f}")
    late = [d for N, d, _ in pts if N >= 180]
    if late:
        print(f"  late block (N >= 180): n = {len(late)}, mean = {sum(late)/len(late):+.3f}, "
              f"min = {min(late):+.3f}   (E = {E1:+.3f})")
    xs = [N for N, _, _ in pts]; ys = [d for _, d, _ in pts]
    out, best = analyse(xs, ys, "Delta_1")
    wins, ci, ms = bootstrap(xs, ys)
    tot = sum(wins.values()); span = max(xs) - min(xs)
    print(f"\n   block bootstrap (moving blocks L = 3, {tot} resamples):")
    for k in ("B", "A1", "A2"):
        print(f"      {k:>2} preferred in {100*wins[k]/tot:5.1f}% of resamples")
    print(f"   linear slope b: mean {ms:+.5f}, 95% CI [{ci[0]:+.5f}, {ci[1]:+.5f}]")
    print(f"   over N = {min(xs)}..{max(xs)} that is {ms*span:+.2f} bits, "
          f"CI [{ci[0]*span:+.2f}, {ci[1]*span:+.2f}]")
    return out, best, (ms, ci)

if __name__ == "__main__":
    E1 = 1 - 0.5772156649015329/math.log(2)
    A = glob.glob('/tmp/claude-1000/-home-elias/c3a43061-2697-4bee-adda-ceb1e6215d18/scratchpad/chunks/*.txt')
    pts, _ = series(A, None, 0.0, 1e12)
    report(pts, "Q5  POPULATION 'ALL'  -- 10^12 scan", E1)
    R = glob.glob('/tmp/claude-1000/-home-elias/c3a43061-2697-4bee-adda-ceb1e6215d18/scratchpad/chunks2/*.txt')
    if R:
        ptsR, _ = series(R, "R", math.log2(1.5), 2.5e11)
        report(ptsR, "Q5  POPULATION 'ROOTS'  -- chain roots, 2.5x10^11 scan, null (2/3)p_N", E1)
        ptsA2, _ = series(R, "A", 0.0, 2.5e11)
        report(ptsA2, "Q5  POPULATION 'ALL' on the SAME 2.5x10^11 range (for comparability)", E1)
