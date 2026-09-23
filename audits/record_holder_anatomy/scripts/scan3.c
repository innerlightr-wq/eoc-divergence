/* Direct-count diagnostic: how many odd m in [a,b) are zero-confined for N steps?
 *
 * Output: "N count" for every N >= 1 with a nonzero count in the range.  Driver ranges
 * are chosen to split the octaves [2^j, 2^{j+1}), so cumulative counts up to 2^j are
 * exact sums of whole sub-ranges.  Same exact method as scan.c: S_k <= A[k].
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "alpha_table.h"
typedef unsigned __int128 u128;
typedef unsigned long long u64;
static u64 cnt[KMAX + 1];

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: %s a b\n", argv[0]); return 2; }
    u64 a = strtoull(argv[1], 0, 10), b = strtoull(argv[2], 0, 10);
    if (a < 3) a = 3;
    a += (3 + 4 - (a & 3)) & 3;
    memset(cnt, 0, sizeof cnt);
    const u128 GUARD = ((u128)1) << 100;
    for (u64 m = a; m < b; m += 4) {
        u128 x = m; int S = 0, k = 0;
        for (;;) {
            u128 y = 3 * x + 1; int d;
            { u64 lo = (u64)y; if (lo) d = __builtin_ctzll(lo);
              else { u64 hi = (u64)(y >> 64); d = 64 + (hi ? __builtin_ctzll(hi) : 64); } }
            S += d; k++;
            if (k > KMAX || S > A[k]) { k--; break; }
            x = y >> d;
            if (x > GUARD) { fprintf(stderr, "OVERFLOW m=%llu\n", m); return 3; }
        }
        for (int N = 1; N <= k; N++) cnt[N]++;
    }
    for (int N = 1; N <= KMAX; N++) if (cnt[N]) printf("%d %llu\n", N, cnt[N]);
    return 0;
}
