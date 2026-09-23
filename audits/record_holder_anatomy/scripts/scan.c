/* Exact record-holder scan for the accelerated 3x+1 map.
 *
 *   T(m) = (3m+1) / 2^{v2(3m+1)}   on odd m,   S_k = sum of the first k valuations.
 *   m is zero-confined for N steps iff  2^{S_k} <= 3^k  for 1 <= k <= N,
 *   equivalently  S_k <= A[k]  with A[k] = floor(k log2 3)  (alpha_table.h, exact).
 *
 * Only m = 3 (mod 4) can be 1-confined: S_1 = v2(3m+1) and 2^{S_1} <= 3 forces S_1 = 1,
 * i.e. 3m+1 = 2 (mod 4), i.e. m = 3 (mod 4).  The scan therefore steps by 4.
 *
 * Arithmetic is exact: orbit values are carried in unsigned __int128 and an overflow
 * guard aborts (loudly) if any orbit value exceeds 2^100.  No floating point anywhere.
 *
 * Usage:  ./scan <start> <end>          scans odd m in [start, end) with m = 3 (mod 4)
 * Output: "N c m1 m2 m3"  -- for each depth N reached, the c<=3 smallest m in this range
 *         that are zero-confined for N steps.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "alpha_table.h"

typedef unsigned __int128 u128;
typedef unsigned long long u64;

static u64 best[KMAX + 1][3];
static int cnt[KMAX + 1];

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: %s start end\n", argv[0]); return 2; }
    u64 start = strtoull(argv[1], 0, 10), end = strtoull(argv[2], 0, 10);
    if (start < 3) start = 3;
    start += (3 + 4 - (start & 3)) & 3;           /* first m >= start with m = 3 (mod 4) */
    memset(cnt, 0, sizeof cnt);
    const u128 GUARD = ((u128)1) << 100;
    int maxdepth = 0;

    for (u64 m = start; m < end; m += 4) {
        u128 x = m;
        int S = 0, k = 0;
        for (;;) {
            u128 y = 3 * x + 1;
            int d = 0;
            { u64 lo = (u64)y; if (lo) d = __builtin_ctzll(lo);
              else { d = 64; u64 hi = (u64)(y >> 64); d += hi ? __builtin_ctzll(hi) : 64; } }
            S += d; k++;
            if (k > KMAX || S > A[k]) { k--; break; }
            x = y >> d;
            if (x > GUARD) { fprintf(stderr, "OVERFLOW GUARD at m=%llu k=%d\n", m, k); return 3; }
        }
        if (k > maxdepth) maxdepth = k;
        for (int N = 1; N <= k; N++)
            if (cnt[N] < 3) best[N][cnt[N]++] = m;
    }
    for (int N = 1; N <= maxdepth; N++) {
        if (!cnt[N]) continue;
        printf("%d %d", N, cnt[N]);
        for (int i = 0; i < cnt[N]; i++) printf(" %llu", best[N][i]);
        printf("\n");
    }
    return 0;
}
