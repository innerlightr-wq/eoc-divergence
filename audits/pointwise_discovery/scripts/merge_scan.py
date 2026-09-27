"""Merge the parallel depth_scan parts into H[b][n], L[n], deep list."""
import sys, os, json, glob

def merge(d):
    H, R, L, deep, guard = {}, {}, {}, [], 0
    for fn in sorted(glob.glob(os.path.join(d, "part_*.txt"))):
        for line in open(fn):
            t = line.split()
            if t[0] == "G":
                guard += int(t[1])
            elif t[0] == "R":
                b, n, c = int(t[1]), int(t[2]), int(t[3])
                R[(b, n)] = R.get((b, n), 0) + c
            elif t[0] == "H":
                b, n, c = int(t[1]), int(t[2]), int(t[3])
                H[(b, n)] = H.get((b, n), 0) + c
            elif t[0] == "L":
                n, m = int(t[1]), int(t[2])
                if n not in L or m < L[n]: L[n] = m
            elif t[0] == "D":
                deep.append((int(t[1]), int(t[2])))
    return H, R, L, sorted(deep, key=lambda x: -x[1]), guard

if __name__ == "__main__":
    d = sys.argv[1]
    H, R, L, deep, guard = merge(d)
    json.dump({"H": {f"{b},{n}": c for (b, n), c in H.items()},
               "R": {f"{b},{n}": c for (b, n), c in R.items()}, "guard": guard,
               "L": {str(n): m for n, m in L.items()},
               "deep": deep[:4000]},
              open(os.path.join(d, "merged.json"), "w"))
    lad = []
    for n in sorted(L):
        if not lad or L[n] != lad[-1][1]: lad.append((n, L[n]))
    print("ladder entries:", len(lad), " deepest:", max(L) if L else None, " guard hits:", guard)
    for n, m in lad: print(f"  N>={n:4d}  m={m}")
