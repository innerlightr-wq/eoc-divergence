"""M1 -- the square-poorness profile, with the per-block ceiling of the Phase-1
correction.

For an integer m whose parity word begins with a repetition of block W
(|W| = l, k ones, agreement length R, exponent e = R/l):

    Phi(word) = m,   delta_W = 2^l - 3^k,   c_W as in paper eq. (4.1),
    M = m * delta_W - c_W ,
    v2(M) = R                      EXACTLY   (isometry, paper Prop. 2.2)
    |M| <= |m| * (|delta_W| + c_W)
  =>  R <= log2|m| + log2(|delta_W| + c_W)
  =>  l * (e - max(1, theta_W)) <= log2|m| + O(log l),   theta_W = (k/l) log2 3,

the last step using the BALANCED height bound c_W <= 3l*max(2^l,3^k); it is valid
only for balanced W.  At e = 2 this is the brief's ceiling
l <= (log2 m + O(log l)) / (2 - theta_W), computed per block from that block's own
theta_W.  A balanced block with negative slack is a bug or a counterexample.

Every test is an exact integer test; floats appear only in printed columns.
"""
from fractions import Fraction
from anatomy import (acc_orbit, parity_word, rep_profile, discrepancy,
                     c_of, delta_of, v2)

def repetitions(m, horizon=None, need_square=True):
    """Every initial repetition of the parity word of the integer m."""
    bits = abs(m).bit_length()
    L = horizon or max(128, 6 * bits + 48)
    w = parity_word(m, L)
    out = []
    for p, R in sorted(rep_profile(w).items()):
        if need_square and R < 2 * p:
            continue
        if R <= p:
            continue
        u = w[:p]; k = sum(u)
        c = c_of(u); d = delta_of(u)
        M = m * d - c
        per = (R >= L)                          # periodic to the horizon: M should be 0
        disc = discrepancy(u)
        row = dict(l=p, k=k, R=R, exp=Fraction(R, p), disc=disc, balanced=disc < 1,
                   periodic=per, M=M, v2M=v2(M), horizon=L)
        if M == 0:
            row.update(slack=None, Q=None, ok=per)
        else:
            rhs_int = abs(m) * (abs(d) + c)
            # exact agreement check: v2(M) must equal R
            row['isometry_ok'] = (v2(M) == R) or per
            row['upper_ok'] = abs(M) <= rhs_int
            row['slack'] = rhs_int.bit_length() - R
            # Q = l*(e - max(1,theta_W)), exactly, via  l*e = R  and  l*theta_W = k*log2 3,
            # compared against log2|m| by the integer test  2^R <= |m|*(|delta|+c).
            row['Q_num'] = R - max(p, (3 ** k).bit_length() - 1)    # l*e - max(l, k log2 3)
            row['ok'] = row['isometry_ok'] and row['upper_ok'] and row['slack'] >= 0
        out.append(row)
    return out

def profile(m, cap=4000, maxsteps=None):
    """M1 across the confined run of m: at every step k, the longest initial square
    and the worst slack; any balanced violation is collected."""
    dep, rows = acc_orbit(m, cap)
    n = min(dep, maxsteps) if maxsteps else dep
    best_l = best_R = 0; worst = None; viol = []; nsq = 0; bestQ = None; bestQat = None
    for k in range(min(n, len(rows))):
        mk = rows[k][0]
        for r in repetitions(mk):
            nsq += 1
            best_l = max(best_l, r['l']); best_R = max(best_R, r['R'])
            if r['slack'] is not None:
                worst = r['slack'] if worst is None else min(worst, r['slack'])
                q = r['Q_num']
                if bestQ is None or q > bestQ:
                    bestQ, bestQat = q, (k, mk, r['l'], r['k'], str(r['exp']))
                if r['balanced'] and r['slack'] < 0:
                    viol.append((k, mk, dict(r)))
            if not r['ok'] and not r['periodic']:
                viol.append((k, mk, dict(r)))
    return dict(depth=dep, longest_square_half=best_l, longest_rep=best_R,
                n_reps=nsq, worst_slack=worst, Qmax=bestQ, Qat=bestQat,
                log2m=abs(m).bit_length() - 1, violations=viol)
