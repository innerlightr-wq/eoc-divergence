"""Exact convergents of alpha = log2(3) by Stern-Brocot descent.
Only comparison used: 2^p < 3^q  <=>  p < bit_length(3^q).  Exact, no floats."""
from functools import lru_cache

@lru_cache(maxsize=None)
def bl3(q):
    return (3 ** q).bit_length()

def lt_alpha(q, p):
    """p/q < alpha  <=>  2^p < 3^q."""
    return p < bl3(q)

def convergents(maxq):
    """All convergents (q,p) of alpha with q <= maxq, in order."""
    qlo, plo = 1, 1      # 1/1 < alpha
    qhi, phi = 1, 2      # 2/1 > alpha
    conv = [(1, 1), (1, 2)]
    side = 'lo'
    while True:
        if side == 'lo':
            # largest k >= 1 with (plo + k*phi)/(qlo + k*qhi) < alpha
            k = 1
            while lt_alpha(qlo + 2*k*qhi, plo + 2*k*phi) and qlo + 2*k*qhi <= 2*maxq:
                k *= 2
            lo_, hi_ = k, 2*k
            while lo_ < hi_:
                mid = (lo_ + hi_ + 1)//2
                if lt_alpha(qlo + mid*qhi, plo + mid*phi):
                    lo_ = mid
                else:
                    hi_ = mid - 1
            k = lo_
            qlo, plo = qlo + k*qhi, plo + k*phi
            conv.append((qlo, plo))
            side = 'hi'
        else:
            k = 1
            while (not lt_alpha(qhi + 2*k*qlo, phi + 2*k*plo)) and qhi + 2*k*qlo <= 2*maxq:
                k *= 2
            lo_, hi_ = k, 2*k
            while lo_ < hi_:
                mid = (lo_ + hi_ + 1)//2
                if not lt_alpha(qhi + mid*qlo, phi + mid*plo):
                    lo_ = mid
                else:
                    hi_ = mid - 1
            k = lo_
            qhi, phi = qhi + k*qlo, phi + k*plo
            conv.append((qhi, phi))
            side = 'lo'
        if conv[-1][0] > maxq:
            conv.pop()
            return conv

if __name__ == "__main__":
    import sys, time
    t0 = time.time()
    cv = convergents(int(sys.argv[1]) if len(sys.argv) > 1 else 200000)
    print(f"{time.time()-t0:.1f}s")
    for n, (q, p) in enumerate(cv):
        print(f"  n={n:2d}  (q,p) = ({q:8d}, {p:8d})   {'upper' if not lt_alpha(q,p) else 'lower'}")
