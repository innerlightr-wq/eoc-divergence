"""Task 5 controls: the Liouville template must NOT fire on a rational point.
Exact integer arithmetic (no modular reduction) for the M_n table."""
from cf import convergents, lt_alpha

def carry_block_exact(q, p):
    A = 0
    for j in range(q):
        A = 3 * A + (1 << ((j * p) // q))
    return A

def v2(z):
    return None if z == 0 else (abs(z) & -abs(z)).bit_length() - 1

if __name__ == "__main__":
    cv = convergents(30000)
    NMAX = 9
    C = {}; D = {}; X = {}
    for n in range(2, NMAX + 1):
        q, p = cv[n]
        C[n] = carry_block_exact(q, p)
        D[n] = 3 ** q - (1 << p)
    print("exact block data")
    print(f"{'n':>3} {'q_n':>7} {'p_n':>7} {'side':>6} {'law l_n':>9} {'C_n (bits)':>11} {'|delta_n| (bits)':>17}")
    for n in range(2, NMAX + 1):
        q, p = cv[n]
        up = not lt_alpha(q, p)
        law = (p - 1) if up else (p + cv[n+1][1] - 1)
        print(f"{n:3d} {q:7d} {p:7d} {'upper' if up else 'lower':>6} {law:9d} "
              f"{C[n].bit_length():11d} {abs(D[n]).bit_length():17d}")
    print(f"\nsanity: x_2 = -C_2/delta_2 = {-C[2]}/{D[2]} = {-C[2]//D[2]}   (the (1,2)^inf point)")

    for m in (2, 4, 6):
        q, p = cv[m]
        print(f"\n--- CONTROL: rational point  -x_{m} = C_{m}/delta_{m}  (shell ({q},{p})) ---")
        print(f"{'n':>3} {'v2(M_n)':>8} {'log2|M_n|':>10} {'q_n*log2(3)':>12} {'2^v2 <= |M_n| ?':>16}")
        for n in range(2, NMAX + 1):
            if n == m: continue
            Mn = C[m] * D[n] - D[m] * C[n]
            vv = v2(Mn)
            qn = cv[n][0]
            print(f"{n:3d} {str(vv):>8} {Mn.bit_length():10d} {int(qn*1.5849625007):12d} "
                  f"{str(2**vv <= abs(Mn)):>16}")

    print("\n--- v2(x_n + 5) directly (x_2 = -5) ---")
    for n in range(2, NMAX + 1):
        Mn = C[2] * D[n] - D[2] * C[n]
        print(f"  n={n}: v2 = {v2(Mn)}")
