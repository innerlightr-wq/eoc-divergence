"""Fast, closed-form version of the pre-registered Q5 model comparison.

Every model is  y = a + b*z  for a transform z of N, so the least-squares fit is
closed form and O(n).  A2's c is a grid search over 40 geometric points in [5, 500].
"""
import math, random, collections

def fit(z, y):
    n = len(y); mz = sum(z)/n; my = sum(y)/n
    szz = sum((t-mz)**2 for t in z)
    if szz < 1e-15: return (my, 0.0), sum((t-my)**2 for t in y)
    b = sum((z[i]-mz)*(y[i]-my) for i in range(n))/szz
    a = my - b*mz
    rss = sum((y[i]-a-b*z[i])**2 for i in range(n))
    return (a, b), rss

CGRID = [5.0*(1.1**k) for k in range(49)]      # 5 .. ~500

def fit_model(xs, ys, kind):
    if kind == 'B':   return fit(list(xs), ys) + (None,)
    if kind == 'A1':  return fit([1.0/x for x in xs], ys) + (None,)
    best = (None, float('inf'), None)
    for c in CGRID:
        p, r = fit([math.exp(-x/c) for x in xs], ys)
        if r < best[1]: best = (p, r, c)
    return best

def resid(xs, ys, kind):
    p, r, c = fit_model(xs, ys, kind)
    if kind == 'B':   pred = [p[0]+p[1]*x for x in xs]
    elif kind == 'A1':pred = [p[0]+p[1]/x for x in xs]
    else:             pred = [p[0]+p[1]*math.exp(-x/c) for x in xs]
    return [y-q for y, q in zip(ys, pred)], r, p, c

def rho1(e):
    n = len(e); m = sum(e)/n
    den = sum((t-m)**2 for t in e)
    if den < 1e-15: return 0.0
    return sum((e[i]-m)*(e[i+1]-m) for i in range(n-1))/den

def aicc_of(xs, ys, kind):
    k = 4 if kind == 'A2' else 3
    e, rss, p, c = resid(xs, ys, kind)
    n = len(ys); r = rho1(e)
    ne = n*(1-r)/(1+r) if r > 0 else float(n)
    if ne - k - 1 <= 0: return float('inf'), rss, p, c, r, ne
    a = ne*math.log(max(rss, 1e-12)/n) + 2*k + 2*k*(k+1)/(ne-k-1)
    return a, rss, p, c, r, ne

def compare(xs, ys):
    out = {}
    for kind in ('B', 'A1', 'A2'):
        out[kind] = aicc_of(xs, ys, kind)
    best = min(out, key=lambda k: out[k][0])
    return out, best

def bootstrap(xs, ys, B=5000, L=3, seed=20260923):
    rng = random.Random(seed); n = len(xs); nb = (n+L-1)//L
    wins = collections.Counter(); slopes = []
    for _ in range(B):
        idx = []
        for _ in range(nb):
            s = rng.randrange(0, max(1, n-L+1)); idx += list(range(s, min(s+L, n)))
        idx = sorted(idx[:n])
        bx = [xs[i] for i in idx]; by = [ys[i] for i in idx]
        try:
            _, best = compare(bx, by); wins[best] += 1
            p, _ = fit(list(bx), by); slopes.append(p[1])
        except Exception: pass
    slopes.sort()
    return wins, (slopes[int(0.025*len(slopes))], slopes[int(0.975*len(slopes))]), sum(slopes)/len(slopes)
