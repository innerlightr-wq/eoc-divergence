/* Least positive odd integer persisting N steps on the RARE side, for (q, r).
 *
 *   q < 4 : rare side is  S_k <= A[k]        (A[k] = floor(k log2 q) = bitlen(q^k) - 1)
 *   q > 4 : rare side is  S_k >= A[k] + 1
 *
 * A[k] is built exactly from q^k in base 2^32; orbit values are unsigned __int128
 * behind a 2^100 guard.  No floating point anywhere.
 *
 * The first letter already restricts the seed to one class mod 2^{A[1]+1} (q>4)
 * or mod 4 (q<4), and the scan steps by that modulus.
 *
 * Usage: ./scan_rare <q> <r> <start> <end>
 * Output: "N best" for every N reached in [start, end).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned __int128 u128;
typedef unsigned long long u64;
#define KMAX 900
static int A[KMAX + 1];

static void build_A(int q) {
    static unsigned w[8192]; int len = 1; w[0] = 1; A[0] = 0;
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
    if (argc != 5) { fprintf(stderr, "usage: %s <q> <r> <start> <end>\n", argv[0]); return 2; }
    int q = atoi(argv[1]); long long r = atoll(argv[2]);
    u64 start = strtoull(argv[3], 0, 10), end = strtoull(argv[4], 0, 10);
    int upper = (q > 4);
    build_A(q);
    /* first-letter class: solve q*m + r = 2^d0 (mod 2^{d0+1}) for the required d0 */
    int d0 = upper ? A[1] + 1 : 1;          /* q>4: need S_1 >= A[1]+1, minimal choice d0=A[1]+1
                                               q<4: need S_1 <= A[1] = 1, so d0 = 1 */
    u64 mod = 1ULL << (d0 + 1);
    u64 res = 0;
    for (u64 t = 1; t < mod; t += 2) {       /* find the odd residue with v2(q t + r) = d0 */
        long long y = (long long)q * (long long)t + r;
        u64 yy = (u64)((y % (long long)mod + (long long)mod) % (long long)mod);
        if (yy == (1ULL << d0)) { res = t; break; }
    }
    if (start < res) start = res;
    else { u64 off = (start - res) % mod; if (off) start += mod - off; }
    /* for q>4 the class above forces S_1 = d0 exactly only if d0 is the minimum;
       larger first letters live in sub-classes of the same modulus, so the scan
       tests the condition explicitly and the class is used only as a sieve.      */
    static u64 best[KMAX + 1];
    memset(best, 0, sizeof best);
    const u128 GUARD = ((u128)1) << 100;
    int maxN = 0;
    for (u64 m = start; m < end; m += mod) {
        u128 x = m; u64 S = 0; int k = 0;
        for (;;) {
            u128 y = (r > 0) ? (u128)q * x + (u128)r : (u128)q * x - (u128)(-r);
            if (y >= GUARD) break;
            int a = 0; while ((y & 1) == 0) { y >>= 1; a++; }
            S += a; x = y; k++;
            int ok = upper ? ((long long)S >= A[k] + 1) : ((long long)S <= A[k]);
            if (!ok) { k--; break; }
            if (k >= KMAX) break;
        }
        for (int n = 1; n <= k; n++) if (!best[n]) best[n] = m;
        if (k > maxN) maxN = k;
    }
    for (int n = 1; n <= maxN; n++) if (best[n]) printf("%d %llu\n", n, best[n]);
    return 0;
}
