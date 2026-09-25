/* Least positive odd integer persisting N steps on the RARE side, for (q, r).
 *
 *   q < 4 : rare side is  S_k <= A[k]        (A[k] = floor(k log2 q) = bitlen(q^k) - 1)
 *   q > 4 : rare side is  S_k >= A[k] + 1
 *
 * A[k] is built exactly from q^k in base 2^32; orbit values are unsigned __int128
 * behind a 2^100 guard.  No floating point anywhere.
 *
 * FIRST-STEP SIEVE.  The n = 1 condition confines the seed to a residue class,
 * and the scan steps by that class's modulus.  The two sides differ, and the
 * difference is the whole of the correction of 2026-09-25:
 *
 *   q < 4 :  S_1 <= A[1] = 1 together with S_1 >= 1 forces  v2(qm+r) = 1 EXACTLY,
 *            so the seeds form one class modulo 4:   m == (2 - r) q^{-1} (mod 4).
 *
 *   q > 4 :  S_1 >= A[1] + 1 =: d0 is a LOWER bound.  Every d >= d0 is admissible,
 *            and the union of those classes is exactly  v2(qm+r) >= d0, i.e.
 *
 *                 m == -r q^{-1}   (mod 2^{d0}) ,
 *
 *            ONE class modulo 2^{d0} -- not modulo 2^{d0+1}.  The earlier version
 *            of this file took the modulus 2^{d0+1} and the single class with
 *            v2(qm+r) = d0 exactly, which for (q,r) = (5,-1) scans m == 5 (mod 16)
 *            and never visits m == 13 (mod 16) -- the seeds with v2(5m-1) >= 4.
 *            Those are admissible: r_min(2) = 13, not 21.  See REPORT.md, Item 3.
 *
 * The guard is counted and reported on stderr, so a truncated (hence merely
 * lower-bound) depth can never pass unnoticed; stdout carries only "N m" lines.
 *
 * Usage: ./scan_rare <q> <r> <start> <end>
 * Output (stdout): "N best" for every N reached in [start, end).
 * Output (stderr): "guard_hits <count>".
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

/* (q*t + r) reduced into [0, M) */
static u64 res_mod(int q, long long r, u64 t, u64 M) {
    long long y = (long long)q * (long long)t + r;
    long long m = (long long)M;
    return (u64)(((y % m) + m) % m);
}

int main(int argc, char **argv) {
    if (argc != 5) { fprintf(stderr, "usage: %s <q> <r> <start> <end>\n", argv[0]); return 2; }
    int q = atoi(argv[1]); long long r = atoll(argv[2]);
    u64 start = strtoull(argv[3], 0, 10), end = strtoull(argv[4], 0, 10);
    int upper = (q > 4);
    build_A(q);

    /* first-step sieve; see the header comment for the derivation of each case */
    int d0 = upper ? A[1] + 1 : 1;
    u64 mod = upper ? (1ULL << d0)       /* v2(qm+r) >= d0 : one class mod 2^{d0} */
                    : 4ULL;              /* v2(qm+r) == 1  : one class mod 4      */
    u64 target = upper ? 0ULL : 2ULL;    /* required value of (qm+r) mod `mod`    */
    u64 res = 0; int found = 0;
    for (u64 t = 1; t < mod; t += 2) {
        if (res_mod(q, r, t, mod) == target) { res = t; found = 1; break; }
    }
    if (!found) { fprintf(stderr, "no admissible first-step class\n"); return 3; }
    if (start < res) start = res;
    else { u64 off = (start - res) % mod; if (off) start += mod - off; }

    static u64 best[KMAX + 1];
    memset(best, 0, sizeof best);
    const u128 GUARD = ((u128)1) << 100;
    unsigned long long guard_hits = 0;
    int maxN = 0;
    for (u64 m = start; m < end; m += mod) {
        u128 x = m; u64 S = 0; int k = 0;
        for (;;) {
            u128 y = (r > 0) ? (u128)q * x + (u128)r : (u128)q * x - (u128)(-r);
            if (y >= GUARD) { guard_hits++; break; }   /* k is then a lower bound */
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
    fprintf(stderr, "guard_hits %llu\n", guard_hits);
    return 0;
}
