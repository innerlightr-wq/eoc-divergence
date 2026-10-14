# ANALYSIS_PLAN.md — recorded before any new test

**Target.** A joint (amortized) bound on the combined duration of two or more
actual corridor episodes, not obtained by charging each episode its own
single-window allowance.

**Conventions.** Rev 8 zero-based: `m_{n+1} = (3m_n+1)/2^{d_n}`, `d_n = v2(3m_n+1)`,
`S_0 = 0`, `R_n = S_n − αn`, `α = log2 3`. Occupation `R_n ≤ c`, one-sided, no
lower boundary. `c` a nonnegative **integer**, decided by `2^{S_n} ≤ 2^c 3^n` on
integers. Time zero counts. Full forward orbit, including the fixed point at 1.

**Step 1 (preparation, not advance).** Verify exactly: `C_0=0`,
`C_{n+1}=3C_n+2^{S_n}`; `z_n = 2^{S_n}/3^n = 2^{R_n}`;
`𝓑_n = m_n z_n = m_0 + C_n/3^n = m_0 2^{E_n}`; `𝓑_{n+1}−𝓑_n = z_n/3`;
per-episode `W_i = Σ_{n∈I_i} z_n = 3(𝓑_{b_i}−𝓑_{a_i})`, `0 < η_i ≤ 1`,
`ℓ_i = (3/2^c)(𝓑_{b_i}−𝓑_{a_i})/η_i`; the block matrix
`(𝓑_b, z_b)^T = [[1,u],[0,v]](𝓑_a, z_a)^T`, `m_b = (m_a+u)/v`,
`2^s m_b = 3^t m_a + C_{[a,b)}`, composition `u_tot = u_1 + v_1 u_2`,
`v_tot = v_1 v_2`, and terminal oddness mod `2^{s+1}`.

**Step 2 (the candidate, written before testing).** Two ingredients, both
already in Rev 8, combined in a way that does **not** refresh a per-episode seed
allowance:

* *global pot (telescoping):* `Σ_{n<H} z_n = 3(𝓑_H − m_0) = 3m_0(2^{E_H}−1)`,
  so `Σ_i W_i ≤ 3m_0(2^{E_H}−1)` — **one** budget shared by all episodes;
* *per-episode toll (entry lemma, Prop. 13.1):* at a re-entry `a_i>0`,
  `c−α+1 < R_{a_i} ≤ c`, hence `z_{a_i} > 2^c·2^{1−α} = (2/3)2^c`, hence
  `W_i ≥ z_{a_i} > (2/3)2^c` **independently of `ℓ_i` and of how deep the
  episode goes**.

Candidate inequality, to be tested:
```
   P − 1  <  (9/2) · 2^{−c} · m_0 · ( 2^{E_H} − 1 ) ,     P = #episodes in [0,H).
```
and, under distinctness of `m_0..m_{H−1}`, `2^{E_H} ≤ e^{7/9} H^{1/9}` gives
`P ≤ 1 + (9/2) e^{7/9} 2^{−c} m_0 H^{1/9}`.

**Step 3 (the honest question).** Does the same pot bound `Σ_i ℓ_i`? Expected
**no**, because `ℓ_i = (3/2^c)(𝓑_{b_i}−𝓑_{a_i})/η_i` and `η_i` is not bounded
below on a **one-sided** corridor. Predicted failure mode: the entry toll is
paid once per episode and says nothing about the interior. Record the exact
residual.

**Step 4 (controls, before interpretation).** A least-realizer vs lifted
realizer in the same class; B all-ones prefixes; C the Prop. 13.2 oscillator;
D the `−1` all-ones trajectory; E the affine recurrence over positive reals
with no integer-ray constraint. Loeb benchmark `m_0=285175`, `c=1`: replicate
`15+4+6+64+1+5+3=98`, `L_1=14`, `τ_1=15` and the seven displayed runs as
**targets, not inputs**; certify no omitted return via the fixed-point drift.

**Stopping rule.** Stop if the gain reduces to reparameterization, a refreshed
per-episode seed budget, self-financing recovery, or a pointwise hypothesis of
the original strength — and then state it as an obstruction to *this* mechanism.
