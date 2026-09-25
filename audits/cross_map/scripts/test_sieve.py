#!/usr/bin/env python3
"""Regression test for the first-step sieve of `scan_rare.c`.

The bug this guards against (found 2026-09-25):  for q > 4 the rare-side
condition at n = 1 is  S_1 >= A[1] + 1 =: d0,  a LOWER bound, so every first
letter d >= d0 is admissible.  The union of those classes is

        v2(q m + r) >= d0    <=>    m == -r q^{-1}   (mod 2^{d0}) ,

ONE class modulo 2^{d0}.  The previous version sieved modulo 2^{d0+1} to the
single class with v2(q m + r) = d0 exactly, and so never visited the seeds with
v2(q m + r) > d0.  For (q, r) = (5, -1) those are m == 13 (mod 16), and they are
where r_min(2) = 13 lives.

For q < 4 the same condition reads S_1 <= A[1] = 1, which with S_1 >= 1 forces
v2(q m + r) = 1 exactly; there the old sieve was already right, which is why the
3x+1 ladder is unaffected.

Three levels of check, all exact:
  T1  the algebra: the admissible first-step set IS the stated class, verified by
      exhaustion over a full period, and the old rule is shown to miss it.
  T2  no loss: the sieved C scanner reproduces, for every map, the ladder that an
      unsieved pure-Python orbit scan produces.
  T3  the corrected values, pinned as literals.

Standard library only.  Exit status 0 iff every check passes.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ladder_ref import Afloor, v2, ladder_scan, jumps          # noqa: E402

SCAN = os.path.join(HERE, "scan_rare")
MAPS = [(5, 1), (5, -1), (7, 1), (7, -1)]          # q > 4: the corrected cases
CONTROL = [(3, 1), (3, -1)]                        # q < 4: must be unchanged

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not cond:
        fails.append(name)


def sieve_new(q, r):
    """The patched rule: (modulus, residue)."""
    A = Afloor(q, 2)
    if q > 4:
        d0 = A[1] + 1
        mod, target = 1 << d0, 0
    else:
        mod, target = 4, 2
    for t in range(1, mod, 2):
        if (q * t + r) % mod == target:
            return mod, t
    raise AssertionError("no admissible first-step class")


def sieve_old(q, r):
    """The rule as it stood before the correction."""
    A = Afloor(q, 2)
    d0 = A[1] + 1 if q > 4 else 1
    mod = 1 << (d0 + 1)
    for t in range(1, mod, 2):
        if (q * t + r) % mod == (1 << d0):
            return mod, t
    raise AssertionError("no class")


def admissible_first(q, r, period):
    """Every odd residue mod `period` admissible at step 1, by brute force."""
    A = Afloor(q, 2)
    upper = q > 4
    out = set()
    for m in range(1, period, 2):
        a = v2(q * m + r)
        if (a >= A[1] + 1) if upper else (a <= A[1]):
            out.add(m)
    return out


def run_c(q, r, cap):
    out = subprocess.run([SCAN, str(q), str(r), "1", str(cap)],
                         capture_output=True, text=True, check=True)
    best = {}
    for line in out.stdout.split("\n"):
        if not line.strip():
            continue
        n, m = map(int, line.split())
        if n not in best or m < best[n]:
            best[n] = m
    assert "guard_hits 0" in out.stderr, "guard fired: depths are lower bounds"
    return best


# ------------------------------------------------------------------ T1 -------
print("T1  the first-step sieve, by exhaustion over a full period")
for q, r in MAPS + CONTROL:
    mod, res = sieve_new(q, r)
    period = mod << 6
    want = admissible_first(q, r, period)
    got = set(range(res, period, mod))
    check(f"T1a q={q} r={r:+d}: patched sieve = the admissible set exactly",
          got == want, f"(class {res} mod {mod}; {len(want)} residues mod {period})")
    omod, ores = sieve_old(q, r)
    ogot = set(range(ores, period, omod))
    missed = want - ogot
    if q > 4:
        check(f"T1b q={q} r={r:+d}: OLD sieve misses a nonempty admissible set",
              len(missed) > 0 and ogot < want,
              f"(old class {ores} mod {omod}; misses {min(missed)} mod {omod})")
    else:
        check(f"T1b q={q} r={r:+d}: OLD sieve was already exact (q < 4)",
              ogot == want, f"(class {ores} mod {omod})")

# ------------------------------------------------------------------ T2 -------
print()
print("T2  no loss: sieved C scanner == unsieved pure-Python orbit scan")
CAP = 1 << 17
have_c = os.path.exists(SCAN)
if not have_c:
    check("T2 scan_rare binary present", False, "(build it: gcc -O3 -o scan_rare scan_rare.c)")
else:
    for q, r in MAPS + CONTROL:
        py = jumps(ladder_scan(q, r, CAP))
        c = jumps(run_c(q, r, CAP))
        check(f"T2 q={q} r={r:+d}: ladders agree to cap 2^17",
              py == c, f"({len(py)} holders, maxN={py[-1][0] if py else 0})")

# ------------------------------------------------------------------ T3 -------
print()
print("T3  the corrected values, pinned")
EXPECT = {
    (5, -1): [(1, 5), (2, 13), (13, 21), (16, 45), (22, 77), (25, 269)],
    (7, -1): [(1, 7), (3, 55), (4, 63), (5, 183)],
    (5, 1): [(1, 3)],
    (7, 1): [(1, 1)],
    (3, 1): [(1, 3), (2, 7), (4, 27), (37, 703)],
    (3, -1): [(1, 1)],
}
for (q, r), want in EXPECT.items():
    got = jumps(ladder_scan(q, r, 1 << 17))[:len(want)]
    check(f"T3 q={q} r={r:+d}: ladder starts {want}", got == want, f"(got {got})")
check("T3 r_min(2) for 5x-1 is 13, NOT the 21 of the sieved scan",
      jumps(ladder_scan(5, -1, 1 << 17))[1] == (2, 13))

print()
print("FAILURES:", fails if fails else "none")
sys.exit(1 if fails else 0)
