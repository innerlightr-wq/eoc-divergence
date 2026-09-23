"""Q5, tightened: the 24 distinct record holders, block-bootstrap error bars, and the
pre-registered model comparison B (linear drift) vs A1 (a + b/N) vs A2 (a + b e^{-N/c}).

All three models are fitted by least squares; A2's c by a grid search with (a,b) linear
given c.  AICc uses the EFFECTIVE sample size n_eff = n (1-rho1)/(1+rho1) from the lag-1
autocorrelation of the residuals.  The comparison is also block-bootstrapped (moving
blocks of length 3).
"""
import sys, math, random, collections, glob

def load(paths, tag=None):
    acc = collections.defaultdict(list)
    for p in paths:
        for line in open(p):
            f = line.split()
            if f[0] in ("A", "R"):
                if tag and f[0] != tag: continue
                N = int(f[1]); vals = [int(x) for x in f[3:]]
            else:
                if tag == "R": continue
                N = int(f[0]); vals = [int(x) for x in f[2:]]
            acc[N] += vals
    return {N: sorted(v)[:3] for N, v in acc.items()}

def lsq(X, y):
    """least squares for design matrix X (list of rows)."""
    p = len(X[0]); n = len(y)
    A = [[sum(X[i][a]*X[i][b] for i in range(n)) for b in range(p)] for a in range(p)]
    v = [sum(X[i][a]*y[i] for i in range(n)) for a in range(p)]
    # gaussian elimination
    M = [row[:] + [v[a]] for a, row in enumerate(A)]
    for c in range(p):
        piv = max(range(c, p), key=lambda r: abs(M[r][c])); M[c], M[piv] = M[piv], M[c]
        if abs(M[c][c]) < 1e-14: return None, float('inf')
        for r in range(p):
            if r == c: continue
            f = M[r][c]/M[c][c]
            for k in range(c, p+1): M[r][k] -= f*M[c][k]
    beta = [M[a][p]/M[a][a] for a in range(p)]
    rss = sum((y[i] - sum(beta[a]*X[i][a] for a in range(p)))**2 for i in range(n))
    return beta, rss

def fitB(xs, ys):  return lsq([[1.0, x] for x in xs], ys)
def fitA1(xs, ys): return lsq([[1.0, 1.0/x] for x in xs], ys)
def fitA2(xs, ys):
    best = (None, float('inf'), None)
    c = 5.0
    while c <= 500.0:
        b, r = lsq([[1.0, math.exp(-x/c)] for x in xs], ys)
        if r < best[1]: best = (b, r, c)
        c *= 1.05
    return best

def aicc(rss, n_eff, k):
    if n_eff - k - 1 <= 0: return float('inf')
    return n_eff*math.log(rss/len(RSS_N)) + 2*k + 2*k*(k+1)/(n_eff-k-1)

def resid(xs, ys, kind):
    if kind == 'B':  b, r = fitB(xs, ys);  pred = [b[0]+b[1]*x for x in xs]
    elif kind=='A1': b, r = fitA1(xs, ys); pred = [b[0]+b[1]/x for x in xs]
    else:            b, r, c = fitA2(xs, ys); pred = [b[0]+b[1]*math.exp(-x/c) for x in xs]
    return [y-p for y, p in zip(ys, pred)], r, b

def rho1(e):
    n = len(e); m = sum(e)/n
    num = sum((e[i]-m)*(e[i+1]-m) for i in range(n-1))
    den = sum((x-m)**2 for x in e)
    return num/den if den else 0.0

def analyse(xs, ys, label):
    global RSS_N
    RSS_N = ys
    n = len(xs)
    print(f"\n{label}:  n = {n} distinct holders, N = {min(xs)}..{max(xs)}")
    out = {}
    for kind, k in (('B', 3), ('A1', 3), ('A2', 4)):
        e, rss, b = resid(xs, ys, kind)
        r1 = rho1(e)
        n_eff = n*(1-r1)/(1+r1) if r1 > 0 else n
        a = n_eff*math.log(rss/n) + 2*k + (2*k*(k+1)/(n_eff-k-1) if n_eff-k-1 > 0 else 1e9)
        out[kind] = (a, rss, b, r1, n_eff)
        bs = ", ".join(f"{t:+.5f}" for t in (b if isinstance(b, list) else [b]))
        print(f"   {kind:>2}: rss {rss:7.3f}   rho1 {r1:+.3f}   n_eff {n_eff:5.1f}   "
              f"AICc {a:8.3f}   params [{bs}]")
    best = min(out, key=lambda k: out[k][0])
    print(f"   -> lowest AICc: {best};  "
          + ";  ".join(f"d(AICc,{k}) = {out[k][0]-out[best][0]:+.2f}" for k in out if k != best))
    return out, best

def bootstrap(xs, ys, B=20000, L=3, seed=20260923):
    rng = random.Random(seed); n = len(xs)
    wins = collections.Counter(); slopes = []
    nb = (n + L - 1)//L
    for _ in range(B):
        idx = []
        for _ in range(nb):
            s = rng.randrange(0, n - L + 1); idx += list(range(s, s+L))
        idx = sorted(idx[:n])
        bx = [xs[i] for i in idx]; by = [ys[i] for i in idx]
        try:
            best, bestv = None, float('inf')
            for kind, k in (('B',3), ('A1',3), ('A2',4)):
                e, rss, _ = resid(bx, by, kind)
                r1 = rho1(e); ne = len(bx)*(1-r1)/(1+r1) if r1 > 0 else len(bx)
                a = ne*math.log(max(rss,1e-12)/len(bx)) + 2*k + (2*k*(k+1)/(ne-k-1) if ne-k-1>0 else 1e9)
                if a < bestv: best, bestv = kind, a
            wins[best] += 1
            bb, _ = fitB(bx, by); slopes.append(bb[1])
        except Exception:
            pass
    slopes.sort()
    lo, hi = slopes[int(0.025*len(slopes))], slopes[int(0.975*len(slopes))]
    return wins, (lo, hi), sum(slopes)/len(slopes)
