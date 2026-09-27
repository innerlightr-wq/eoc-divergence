# Draft section for the paper — **not inserted; awaiting approval**

Intended as a new §9 ("All Sturmian words"), replacing Remark 8.9 and open
problem (1). LaTeX below uses the paper's existing macros (`\Ph`, `\lab`, `\vt`).

```latex
\section{All Sturmian words}\label{sec:allwords}

Section~\ref{sec:allslopes} settles every irrational slope at intercept $0$.
The restriction to intercept $0$ was forced: the ones of $1c_{\gamma,\rho}$ are
no longer at $\lfloor j\alpha_\gamma\rfloor$, and the two exact identities behind
Lemma~\ref{lem:floor} lose their right-hand sides. This section removes the
restriction by a different route, which uses no depth law at all. Instead of
comparing $s$ with the periodic words attached to the convergents, we compare it
with the periodic word attached to an \emph{initial square} of $s$ itself.

\begin{theorem}\label{thm:allwords}
Let $\gamma\in(0,1)$ be irrational and $\rho\in[0,1)$, and let $s$ be either
mechanical word of slope $\gamma$ and intercept $\rho$. Then $\Ph(s)\notin\Q$.
More precisely, if $\Ph(s)=u/v$ in lowest terms with $H=\max(|u|,v)$, then every
half-length $\ell$ of an initial square of $s$ satisfies
\[
  c(\gamma)\,\ell \;\le\; \log_2 H + \log_2(2+3\ell) + \log_2 3,
  \qquad c(\gamma)=2-\max(1,\gamma\log_2 3)\;\ge\;2-\log_2 3 .
\]
\end{theorem}

The proof needs two facts from the combinatorics of Sturmian words, both
\lab{cited}, and nothing else beyond Proposition~\ref{prop:iso} and
Proposition~\ref{prop:periodic}.

\begin{theorem}[Allouche--Davison--Queff\'elec--Zamboni]\label{thm:squares}
Every Sturmian sequence begins in infinitely many squares; consequently its
initial critical exponent is at least $2$.
\end{theorem}
\lab{cited} \cite{ADQZ2001}; see also \cite{DamanikKillipLenz2000} and the
account in \cite[\S1]{BertheHoltonZamboni2006}, where the exact value of the
initial critical exponent is computed from the Ostrowski expansion of the
intercept. Since a word has at most one prefix of each length, the half-lengths
of the initial squares are unbounded. The exponent $2$ cannot be improved in
general: \cite[Thm.~1.1]{BertheHoltonZamboni2006} characterises the slopes
admitting a Sturmian sequence of initial critical exponent exactly $2$. It is
enough here, because $2>\max(1,\gamma\log_2 3)$ for every $\gamma\in(0,1)$.

\begin{theorem}[Berth\'e--Holton--Zamboni]\label{thm:roots}
If a Sturmian sequence begins in $w^{r}$ with $r\ge2$, $|w|\ge2$ and $w$
primitive, then $w$ is a cyclic permutation of a standard word; in particular
$w^{\infty}$ is balanced.
\end{theorem}
\lab{cited} \cite[Prop.~3.2]{BertheHoltonZamboni2006}: $w$ is a cyclic
permutation of $\tau_{i_1}\circ\cdots\circ\tau_{i_m}(01)$, where
$\tau_0:0\mapsto0,\,1\mapsto01$ and $\tau_1:0\mapsto10,\,1\mapsto1$; applying
these to the standard pair $(0,1)$ yields standard pairs, and the concatenation
of a standard pair is a standard word. If $w$ is not primitive, $w=v^{t}$ and $s$
begins in $v^{2t}$, so primitivity costs nothing.

\begin{lemma}\label{lem:conjheight}
Let $W$ be a cyclic permutation of a standard word, $|W|=\ell$, with $k$ ones.
Then $0<c_W\le 3\,\ell\max(2^{\ell},3^{k})$.
\end{lemma}

\begin{proof}
By Theorem~\ref{thm:roots}, $W^{\infty}$ is balanced, so
$|k_{i+1}(W)-(i+1)k/\ell|<1$ and hence $k-k_{i+1}(W)<k(\ell-1-i)/\ell+1$. With
$\rho=3^{k/\ell}$,
\[
 3^{\,k-k_{i+1}(W)}2^{\,i}\;<\;3\,\rho^{\,\ell-1-i}2^{\,i}
 \;\le\;3\max\bigl(\rho^{\,\ell-1},2^{\,\ell-1}\bigr)\;\le\;3\max(3^{k},2^{\ell}),
\]
the middle step because $i\mapsto\rho^{\ell-1-i}2^{i}$ is monotone and so attains
its maximum on $0\le i\le\ell-1$ at an endpoint. The sum \eqref{eq:cw} has at
most $\ell$ terms. Positivity is clear.
\end{proof}

This is the estimate sketched in Remark~\ref{rem:notmech}; the hypothesis that
$W^{\infty}$ be balanced cannot be dropped, by the family $W=0^{a}1^{a}$ there.

\begin{proof}[Proof of Theorem~\ref{thm:allwords}]
Suppose $\Ph(s)=u/v$ in lowest terms and put $H=\max(|u|,v)$. As $\Ph(s)\in\Zt$,
$v$ is odd. Let $WW$ be an initial square of $s$ with $W$ primitive, $|W|=\ell$,
$k$ ones, and set $\delta=2^{\ell}-3^{k}$, odd since $\ell\ge1$. Put
\[
   M \;=\; u\delta - v\,c_W \;\in\;\Z .
\]
If $M=0$ then $\Ph(s)=c_W/\delta=\Ph(W^{\infty})$ by
Proposition~\ref{prop:periodic}, and $\Ph$ is a bijection, so $s=W^{\infty}$,
contradicting the aperiodicity of $s$. Hence $M\ne0$.

Both $s$ and $W^{\infty}$ begin with $WW$, so $\mathrm{lcp}(s,W^{\infty})\ge2\ell$.
Since $\Ph(s)-\Ph(W^{\infty})=M/(v\delta)$ with $v$ and $\delta$ odd,
Proposition~\ref{prop:iso} gives
$\vt(M)=\mathrm{lcp}(s,W^{\infty})\ge2\ell$, whence $|M|\ge2^{2\ell}$.

In the other direction, Lemma~\ref{lem:conjheight} gives
$|M|\le H\bigl(|\delta|+|c_W|\bigr)\le H(2+3\ell)\max(2^{\ell},3^{k})$, so
\[
   2\ell \;\le\; \log_2 H+\log_2(2+3\ell)+\max\bigl(\ell,\,k\log_2 3\bigr).
\]
$W$ is a factor of a Sturmian word of slope $\gamma$, so $|k-\gamma\ell|\le1$ and
$\max(\ell,k\log_2 3)\le\max(1,\gamma\log_2 3)\,\ell+\log_2 3$. Rearranging gives
the displayed inequality. By Theorem~\ref{thm:squares} there are such $\ell$
arbitrarily large, while $c(\gamma)\ge2-\log_2 3>0$; the inequality fails for
large $\ell$.
\end{proof}

\begin{corollary}\label{cor:subshift}
For every irrational $\gamma\in(0,1)$, $\Ph(X_\gamma)\cap\Q=\emptyset$, where
$X_\gamma$ is the Sturmian subshift of slope $\gamma$.
\end{corollary}
\lab{proved (paper)}. $X_\gamma$ consists of the mechanical words of slope
$\gamma$ at all intercepts, so this is Theorem~\ref{thm:allwords} restated.
Theorem~\ref{thm:main} and Theorem~\ref{thm:allslopes} are the cases
$\rho=0$; Corollary~\ref{cor:shifts} is the case $\rho\in\{\,j\gamma\,\}$.

\begin{remark}
The depth law of Section~\ref{sec:allslopes} is not used. The two arguments are
independent and their strengths differ: the depth law gives, at intercept $0$,
the sharper height floor of Corollary~\ref{cor:heightfloor}, of order
$2^{q_n+q_{n+1}-1}$, because it exploits the continued fraction of $\gamma$;
Theorem~\ref{thm:allwords} gives, at every intercept, a floor of order
$2^{c(\gamma)\ell}$ where $\ell$ runs over the initial-square half-lengths. At
intercept $0$ those half-lengths are the convergent and semiconvergent
denominators, and the first bound is stronger.
\end{remark}
```

## Bibliography entries to add

```bibtex
@article{ADQZ2001,
  author  = {Allouche, Jean-Paul and Davison, J. Peter and Queff\'elec, Michel
             and Zamboni, Luca Q.},
  title   = {Transcendence of {S}turmian or morphic continued fractions},
  journal = {Journal of Number Theory}, volume = {91}, year = {2001}, pages = {39--66}
}
@article{BertheHoltonZamboni2006,
  author  = {Berth\'e, Val\'erie and Holton, Charles and Zamboni, Luca Q.},
  title   = {Initial powers of {S}turmian sequences},
  journal = {Acta Arithmetica}, volume = {122}, number = {4}, year = {2006}, pages = {315--347}
}
@article{DamanikKillipLenz2000,
  author  = {Damanik, David and Killip, Rowan and Lenz, Daniel},
  title   = {Uniform spectral properties of one-dimensional quasicrystals, {III}.
             $\alpha$-continuity},
  journal = {Communications in Mathematical Physics}, volume = {212}, year = {2000}, pages = {191--204}
}
```

## Edits implied elsewhere in the paper

1. **Remark 8.9** ("The intercept is not generalised") — **delete**, or reduce to
   a pointer saying the depth law is still intercept-0 only while the
   irrationality conclusion is not.
2. **§10 open problem (1)** ("General intercepts") — **resolved**. Replace with
   the sharper question that survives: *is there a depth law at general
   intercept?* — i.e. the quantitative statement, now that the qualitative one is
   proved. The Ostrowski route (BHZ's own formula for `ice`) is the natural attack.
3. **Abstract and §1** — the scope sentence changes from "one explicit word …
   together with its shifts and the two variants" to "every Sturmian word".
4. **§8 title** — "All irrational slopes" becomes a subsection of "All Sturmian
   words", or the two sections are ordered depth-law-first, squares-second.
5. **Credit paragraph** — add that I1 and I2 are cited (ADQZ 2001; BHZ 2006
   Prop. 3.2) and that only the height bound and the Liouville comparison are the
   author's, exactly as for §8.
