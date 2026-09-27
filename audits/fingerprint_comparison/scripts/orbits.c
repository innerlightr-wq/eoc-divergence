/* Integer-orbit fingerprints for the three accelerated maps.
 *
 *   A: x -> (3x+1)/2^v2(3x+1)   B: x -> (3x-1)/2^v2(3x-1)   C: x -> (5x+1)/2^v2(5x+1)
 *
 * Exact arithmetic throughout (unsigned __int128, guard at 2^100); floating point
 * appears only in reported averages, never in a decision.
 *
 * Two modes, deliberately separated so that no statistic is conditioned on an
 * event correlated with the quantity being measured (see the selection mirage of
 * "Two Normalization Nulls"):
 *
 *   capture : iterate each odd x < X until it meets a known cycle element, or the
 *             step budget runs out, or the value passes 2^100.  Reports capture
 *             fractions, stopping times, maximum excursion.
 *   letters : iterate each odd x < X for EXACTLY D steps, with no early stop and no
 *             conditioning of any kind -- orbits that have reached a cycle keep
 *             emitting that cycle's letters.  Reports P(a_k = j) at each depth k.
 *
 * Cycle tables (conjecturally complete; an orbit that stays under the guard for
 * the whole budget without meeting one is reported as UNCAPTURED-BOUNDED, which
 * would signal an unlisted cycle):
 *   A: {1}    B: {1}, {5,7}, {17,25,37,55,41,61,91}    C: {1,3}, {13,33,83}, {17,43,27}
 *
 * Usage: ./orbits <A|B|C> <capture|letters> <X> <budget-or-depth>
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef unsigned __int128 u128;
typedef unsigned long long u64;

#define CMAX 128
static int cyc[CMAX];
#define DMAX 512
#define AMAX 48
static u64 letter[DMAX][AMAX + 2];
static u64 alive[DMAX];

static int q; static long long r; static int ncyc;

static void setmap(char M) {
    memset(cyc, 0, sizeof cyc);
    if (M == 'A') { q = 3; r = 1;  cyc[1] = 1; ncyc = 1; }
    else if (M == 'B') { q = 3; r = -1; cyc[1] = 1; cyc[5] = cyc[7] = 2;
        cyc[17] = cyc[25] = cyc[37] = cyc[55] = cyc[41] = cyc[61] = cyc[91] = 3; ncyc = 3; }
    else { q = 5; r = 1; cyc[1] = cyc[3] = 1; cyc[13] = cyc[33] = cyc[83] = 2;
        cyc[17] = cyc[43] = cyc[27] = 3; ncyc = 3; }
}

int main(int argc, char **argv) {
    if (argc != 5) { fprintf(stderr, "usage: %s <A|B|C> <capture|letters> <X> <budget>\n", argv[0]); return 2; }
    char M = argv[1][0];
    int lettersmode = (argv[2][0] == 'l');
    u64 X = strtoull(argv[3], 0, 10);
    int BUD = atoi(argv[4]);
    if (BUD > DMAX && lettersmode) BUD = DMAX;
    setmap(M);
    const u128 GUARD = ((u128)1) << 100;
    u64 n = 0;

    if (lettersmode) {
        memset(letter, 0, sizeof letter); memset(alive, 0, sizeof alive);
        for (u64 x = 1; x < X; x += 2) {
            u128 m = x; n++;
            for (int k = 0; k < BUD; k++) {
                u128 y = (r > 0) ? (u128)q * m + 1 : (u128)q * m - 1;
                if (y >= GUARD) break;                 /* only C reaches this */
                int a = 0; while ((y & 1) == 0) { y >>= 1; a++; }
                letter[k][a > AMAX ? AMAX + 1 : a]++; alive[k]++;
                m = y;
            }
        }
        printf("map %c  LETTERS  X=%llu  odd seeds=%llu  depth=%d  (no conditioning)\n", M, X, n, BUD);
        printf("  depth   alive        P(a=1)      P(a=2)      P(a=3)      P(a=4)      mean a\n");
        int depths[] = {0, 1, 2, 4, 9, 19, 29, 39, 59, 79, 119, 199, 299, 399, 499, -1};
        for (int i = 0; depths[i] >= 0; i++) {
            int k = depths[i]; if (k >= BUD) break;
            double tot = (double)alive[k]; if (tot == 0) continue;
            double mean = 0; for (int a = 1; a <= AMAX + 1; a++) mean += a * letter[k][a] / tot;
            printf("  %5d  %10llu  %.8f  %.8f  %.8f  %.8f  %.6f\n", k + 1, alive[k],
                   letter[k][1]/tot, letter[k][2]/tot, letter[k][3]/tot, letter[k][4]/tot, mean);
        }
        /* pooled over the first 10 depths, where absorption is negligible */
        u64 pool[AMAX + 2]; memset(pool, 0, sizeof pool); u64 pt = 0;
        for (int k = 0; k < 10 && k < BUD; k++) { for (int a = 0; a <= AMAX + 1; a++) pool[a] += letter[k][a]; pt += alive[k]; }
        double tv = 0, mean = 0;
        for (int a = 1; a <= AMAX; a++) { tv += fabs(pool[a]/(double)pt - pow(2.0,-a)); mean += a*pool[a]/(double)pt; }
        printf("  pooled depths 1-10: n=%llu  total-variation distance to geometric(1/2) = %.3e  mean a = %.9f\n",
               pt, tv/2, mean);
        return 0;
    }

    u64 cap[8]; memset(cap, 0, sizeof cap);
    u64 capby[64]; memset(capby, 0, sizeof capby);   /* captured within k steps */
    u64 escaped = 0, unc = 0;
    double steps_sum = 0, steps_sq = 0, S_sum = 0, exc_sum = 0, exc_sq = 0, excn_sum = 0;
    double esc_steps = 0; u64 steps_max = 0;
    for (u64 x = 1; x < X; x += 2) {
        u128 m = x, mx = x; int k = 0, fate = 0; u64 S = 0;
        if (x < CMAX && cyc[x]) fate = cyc[x];
        while (!fate) {
            if (k >= BUD) { fate = -2; break; }
            u128 y = (r > 0) ? (u128)q * m + 1 : (u128)q * m - 1;
            if (y >= GUARD) { fate = -1; break; }
            int a = 0; while ((y & 1) == 0) { y >>= 1; a++; }
            S += a; m = y; k++;
            if (m > mx) mx = m;
            if (m < CMAX && cyc[(int)m]) fate = cyc[(int)m];
        }
        n++;
        if (fate > 0) {
            for (int j = (k < 63 ? k : 63); j < 64; j++) capby[j]++;
            cap[fate]++; steps_sum += k; steps_sq += (double)k*k; if ((u64)k > steps_max) steps_max = k;
            S_sum += S;
            double lx = log2((double)x), e = log2((double)mx) - lx;
            exc_sum += e; exc_sq += e*e; if (x > 1) excn_sum += e / lx;
        } else if (fate == -1) { escaped++; esc_steps += k; }
        else unc++;
    }
    printf("map %c  CAPTURE  q=%d r=%+lld  X=%llu  odd seeds=%llu  budget=%d\n", M, q, r, X, n, BUD);
    double capt = 0; for (int i = 1; i <= ncyc; i++) capt += cap[i];
    for (int i = 1; i <= ncyc; i++)
        printf("  cycle %d captured  : %14llu   frac %.9f\n", i, cap[i], cap[i]/(double)n);
    printf("  escaped past 2^100: %14llu   frac %.9f   mean steps to escape %.4f\n",
           escaped, escaped/(double)n, escaped ? esc_steps/escaped : 0.0);
    printf("  uncaptured bounded: %14llu   frac %.9f   (nonzero => unlisted cycle)\n", unc, unc/(double)n);
    printf("  captured within k steps:");
    for (int j = 9; j < 64; j += 10) printf("  k=%2d: %.6f", j + 1, capby[j]/(double)n);
    printf("\n");
    if (capt > 0) {
        double ms = steps_sum/capt;
        printf("  steps to capture  : mean %.6f  sd %.6f  max %llu\n", ms, sqrt(steps_sq/capt - ms*ms), steps_max);
        printf("  mean S/steps      : %.6f   (Haar 2)\n", S_sum/steps_sum);
        double me = exc_sum/capt;
        printf("  log2(max/x)       : mean %.6f  sd %.6f ;  /log2(x) mean %.6f\n",
               me, sqrt(exc_sq/capt - me*me), excn_sum/capt);
    }
    return 0;
}
