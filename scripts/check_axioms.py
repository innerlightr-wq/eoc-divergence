#!/usr/bin/env python3
"""Fail unless every `#print axioms` line reports only Lean's three standard axioms.

Usage: check_axioms.py [path/to/Axioms.lean]   (default: scripts/Axioms.lean)
"""
import re, subprocess, sys

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

target = sys.argv[1] if len(sys.argv) > 1 else "scripts/Axioms.lean"

out = subprocess.run(["lake", "env", "lean", target],
                     capture_output=True, text=True)
sys.stdout.write(out.stdout)
sys.stderr.write(out.stderr)
if out.returncode != 0:
    sys.exit(f"FAIL: {target} did not elaborate")

lines = [l for l in out.stdout.splitlines() if "depend" in l]
if not lines:
    sys.exit("FAIL: no `#print axioms` output found")

bad = False
for line in lines:
    if "does not depend on any axioms" in line:
        continue
    m = re.search(r"depends on axioms: \[(.*)\]", line)
    if not m:
        print(f"FAIL: unparsable line: {line}")
        bad = True
        continue
    used = {a.strip() for a in m.group(1).split(",") if a.strip()}
    extra = used - ALLOWED
    if extra:
        print(f"FAIL: {line}\n      disallowed: {sorted(extra)}")
        bad = True

sys.exit(1 if bad else 0)
