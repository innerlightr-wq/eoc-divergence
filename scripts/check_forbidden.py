#!/usr/bin/env python3
"""Fail if any Lean source uses a forbidden construct outside comments."""
import pathlib, re, sys

BANNED = ["sorry", "admit", "axiom", "opaque", "native_decide", "implemented_by"]

def strip_comments(text: str) -> str:
    text = re.sub(r"/-.*?-/", " ", text, flags=re.S)      # block and doc comments
    return re.sub(r"--[^\n]*", " ", text)                  # line comments

bad = False
for path in sorted(pathlib.Path(".").rglob("*.lean")):
    if ".lake" in path.parts:
        continue
    for i, line in enumerate(strip_comments(path.read_text()).splitlines(), 1):
        for tok in BANNED:
            if re.search(rf"\b{re.escape(tok)}\b", line):
                print(f"FAIL: {path}:{i}: forbidden `{tok}`: {line.strip()}")
                bad = True

print("no forbidden constructs found" if not bad else "")
sys.exit(1 if bad else 0)
