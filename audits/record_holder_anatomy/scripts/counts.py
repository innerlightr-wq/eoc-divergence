"""The direct-count diagnostic: #{odd m <= 2^j : m is N-confined}  against  2^{j-1} p_N(0).

For j >= A[N]+1 the ratio is EXACTLY 1 (each class mod 2^{S+1} with S <= A[N] contributes
exactly 2^{j-S-1} elements of [0,2^j)), so the diagnostic only carries information for
j <= A[N]; that is the whole scanned range once N >= 26.
"""
import sys, glob, os, collections, math
from nullmodel import transfer
from anatomy import A

def load(dirpath):
    oct_counts = collections.defaultdict(collections.Counter)   # j -> N -> count in [2^j,2^{j+1})
    for p in glob.glob(os.path.join(dirpath, "*.txt")):
        j = int(os.path.basename(p).split("_")[0][1:])
        for line in open(p):
            a, b = line.split(); oct_counts[j][int(a)] += int(b)
    return oct_counts

if __name__ == "__main__":
    oc = load(sys.argv[1])
    jmax = max(oc) + 1
    Ns = [int(x) for x in sys.argv[2].split(",")]
    nums = transfer(max(Ns))
    cum = collections.Counter()
    print(f"observed / expected,  expected = 2^(j-1) p_N(0) = 2^(j-1-A[N]) * num_N (exact)")
    hdr = f"{'j':>4} " + " ".join(f"{('N='+str(N)):>12}" for N in Ns)
    print(hdr)
    for j in range(min(oc), jmax):
        cum.update(oc[j])
        row = f"{j+1:>4} "
        for N in Ns:
            obs = cum[N]
            e = nums[N] * 2 ** (j + 1 - 1 - A(N)) if j >= A(N) else nums[N] / 2 ** (A(N) - j)
            row += f"{(obs/e if e else float('nan')):>12.5f}" if e else f"{'-':>12}"
        print(row)
    print()
    for N in Ns:
        print(f"  N = {N:<4} A[N] = {A(N):<4} num_N = {nums[N]}   "
              f"(ratio is exactly 1 once j >= {A(N)+1})")
