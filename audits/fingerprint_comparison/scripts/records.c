/* O4 -- record holders of the one-sided sector, for all three maps.
 *
 *   LOWER side (A, B): least odd m > 0 with S_k <= A[k] for 1 <= k <= N   (confined)
 *   UPPER side (C)   : least odd m > 0 with S_k >= A[k]+1 for 1 <= k <= N (anti-confined)
 *
 * A[k] = floor(k log2 q) is supplied exactly as a precomputed table (bit lengths of q^k).
 * Orbit values in unsigned __int128 with a 2^100 guard.  No floating point.
 *
 * Usage: ./records <A|B|C> <X>      prints "N  r_min(N)" for each N reached.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned __int128 u128;
typedef unsigned long long u64;
#define KMAX 600

static int A[KMAX + 1];

static void build_A(int q) {
    /* A[k] = bitlength(q^k) - 1, exact, via big-integer doubling in base 2^32 */
    static unsigned w[4096]; int len = 1; w[0] = 1; A[0] = 0;
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

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: %s <A|B|C> <X>\n", argv[0]); return 2; }
    char M = argv[1][0];
    u64 X = strtoull(argv[2], 0, 10);
    int q; long long r; int upper;
    if (M == 'A') { q = 3; r = 1; upper = 0; }
    else if (M == 'B') { q = 3; r = -1; upper = 0; }
    else { q = 5; r = 1; upper = 1; }
    build_A(q);
    const u128 GUARD = ((u128)1) << 100;
    u64 best[KMAX + 1]; memset(best, 0, sizeof best);
    int maxN = 0;
    for (u64 m = 1; m < X; m += 2) {
        u128 x = m; u64 S = 0; int k = 0;
        for (;;) {
            u128 y = (r > 0) ? (u128)q * x + 1 : (u128)q * x - 1;
            if (y >= GUARD) break;
            int a = 0; while ((y & 1) == 0) { y >>= 1; a++; }
            S += a; x = y; k++;
            int ok = upper ? ((long long)S >= A[k] + 1) : ((long long)S <= A[k]);
            if (!ok) { k--; break; }
            if (k >= KMAX) break;
        }
        for (int n = 1; n <= k; n++) if (!best[n]) best[n] = m;
        if (k > maxN) { maxN = k; }
    }
    printf("map %c  %s side  X=%llu\n", M, upper ? "UPPER (anti-confined)" : "LOWER (confined)", X);
    for (int n = 1; n <= maxN; n++)
        if (best[n]) printf("  N=%3d  r_min=%llu\n", n, best[n]);
    return 0;
}
