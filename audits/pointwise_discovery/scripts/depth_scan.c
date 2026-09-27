/* Rare-side confinement depth of every odd seed in a range, for (q, r).
 *
 * Adapted from eoc-divergence/audits/cross_map/scripts/scan_rare.c (Apache-2.0),
 * which is used unmodified in its own repository; this copy adds the per-bitlength
 * depth histogram and the deep-seed list.  No floating point anywhere.
 *
 *   q < 4 : rare side is  S_k <= A[k]        (A[k] = bitlen(q^k) - 1)
 *   q > 4 : rare side is  S_k >= A[k] + 1
 *
 * Usage: ./depth_scan <q> <r> <start> <end> <deep_threshold> <depth_cap>
 * Output:
 *   H <bitlen> <n> <count>      #{odd m in range, bitlen(m)=bitlen, N(m) >= n}
 *   L <n> <m>                   least m in range with N(m) >= n
 *   D <m> <N>                   every m with N(m) >= deep_threshold
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned __int128 u128;
typedef unsigned long long u64;
#define KMAX 1200
#define BMAX 70
static int A[KMAX + 1];

static void build_A(int q) {
    static unsigned w[16384]; int len = 1; w[0] = 1; A[0] = 0;
    for (int k = 1; k <= KMAX; k++) {
        unsigned long long carry = 0;
        for (int i = 0; i < len; i++) {
            unsigned long long t = (unsigned long long)w[i] * q + carry;
            w[i] = (unsigned)(t & 0xffffffffu); carry = t >> 32;
        }
        while (carry) { w[len++] = (unsigned)(carry & 0xffffffffu); carry >>= 32; }
        int top = len - 1; while (top > 0 && w[top] == 0) top--;
        int bits = top * 32; unsigned v = w[top]; while (v) { bits++; v >>= 1; }
        A[k] = bits - 1;
    }
}

static int bitlen64(u64 x) { int b = 0; while (x) { b++; x >>= 1; } return b; }

static long long H[BMAX + 1][KMAX + 2];
static long long HR[BMAX + 1][KMAX + 2];   /* chain roots: m % 3 != 2 */
static long long guard_hits = 0;
static u64 L[KMAX + 2];

int main(int argc, char **argv) {
    if (argc != 7) { fprintf(stderr, "usage: %s q r start end deep ncap\n", argv[0]); return 2; }
    int q = atoi(argv[1]); long long r = atoll(argv[2]);
    u64 start = strtoull(argv[3], 0, 10), end = strtoull(argv[4], 0, 10);
    int deep = atoi(argv[5]);
    int ncap = atoi(argv[6]); if (ncap > KMAX) ncap = KMAX;
    int upper = (q > 4);
    build_A(q);
    memset(H, 0, sizeof H); memset(HR, 0, sizeof HR); memset(L, 0, sizeof L);
    const u128 GUARD = ((u128)1) << 118;
    if (start % 2 == 0) start++;
    for (u64 m = start; m < end; m += 2) {
        u128 x = m; u64 S = 0; int k = 0;
        for (;;) {
            u128 y = (r > 0) ? (u128)q * x + (u128)r : (u128)q * x - (u128)(-r);
            if (y >= GUARD) { guard_hits++; break; }  /* overflow guard: k is then a lower bound */
            int a = 0; while ((y & 1) == 0) { y >>= 1; a++; }
            S += a; x = y; k++;
            int ok = upper ? ((long long)S >= A[k] + 1) : ((long long)S <= A[k]);
            if (!ok) { k--; break; }
            if (k >= ncap) break;
        }
        int b = bitlen64(m);
        int root = (m % 3 != 2);
        if (b <= BMAX) for (int n = 0; n <= k; n++) { H[b][n]++; if (root) HR[b][n]++; }
        for (int n = 1; n <= k; n++) if (!L[n]) L[n] = m;
        if (k >= deep) printf("D %llu %d\n", m, k);
    }
    for (int b = 1; b <= BMAX; b++)
        for (int n = 0; n <= KMAX; n++) {
            if (H[b][n]) printf("H %d %d %lld\n", b, n, H[b][n]);
            if (HR[b][n]) printf("R %d %d %lld\n", b, n, HR[b][n]);
        }
    printf("G %lld\n", guard_hits);
    for (int n = 1; n <= KMAX; n++) if (L[n]) printf("L %d %llu\n", n, L[n]);
    return 0;
}
