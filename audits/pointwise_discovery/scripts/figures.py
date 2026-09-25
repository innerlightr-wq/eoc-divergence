"""Figures.  Palette: dataviz reference instance, light surface, slots 1-3
(#2a78d6 blue, #eb6834 orange, #1baf7a aqua), validated all-pairs.
Diverging: blue <-> red with a neutral gray midpoint."""
import os, sys, json, math, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from m3_dependence import load

SURF = "#fcfcfb"; INK = "#0b0b0b"; INK2 = "#52514e"; MUT = "#898781"
GRID = "#e1e0d9"; AXIS = "#c3c2b7"
S1, S2, S3 = "#2a78d6", "#eb6834", "#1baf7a"
DIV = LinearSegmentedColormap.from_list("bl_rd", ["#104281", "#2a78d6", "#f0efec",
                                                 "#d03b3b", "#7a1f1f"])

plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "axes.edgecolor": AXIS, "axes.labelcolor": INK2, "text.color": INK,
    "xtick.color": MUT, "ytick.color": MUT, "grid.color": GRID,
    "axes.grid": True, "grid.linewidth": 0.6, "axes.linewidth": 0.8,
    "font.size": 9, "axes.titlesize": 10, "legend.frameon": False,
    "lines.linewidth": 2.0, "axes.spines.top": False, "axes.spines.right": False,
})

def fig1_deviation_grid():
    d = json.load(open("results/m1b_bitlength.json"))["rows"]
    ns = sorted({r["n"] for r in d}); bs = sorted({r["b"] for r in d})
    Z = np.full((len(ns), len(bs)), np.nan)
    for r in d:
        if r["exp"] >= 25:
            Z[ns.index(r["n"]), bs.index(r["b"])] = r["E"] - 1
    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    im = ax.imshow(Z, aspect="auto", cmap=DIV, vmin=-0.5, vmax=0.5,
                   origin="lower", interpolation="nearest")
    ax.set_xticks(range(0, len(bs), 2)); ax.set_xticklabels(bs[::2])
    ax.set_yticks(range(len(ns))); ax.set_yticklabels(ns)
    ax.set_xlabel("seed bit length  B"); ax.set_ylabel("confinement depth  n")
    ax.set_title("Occupancy relative to the exact confined-word mass,  "
                 r"$E_B(n)-1$" "\n"
                 "complete scan of every odd $m<2^{32}$ under $3x+1$; blank = fewer "
                 "than 25 expected", loc="left", color=INK)
    ax.grid(False)
    cb = fig.colorbar(im, ax=ax, pad=0.02, fraction=0.035)
    cb.outline.set_edgecolor(AXIS); cb.ax.tick_params(color=MUT)
    cb.set_label(r"$E_B(n)-1$", color=INK2)
    # the proved vacuous boundary  n = B/alpha
    al = math.log2(3)
    xs = np.arange(len(bs))
    ys = [np.interp(bs[i] / al, ns, range(len(ns))) if bs[i]/al <= ns[-1] else np.nan
          for i in xs]
    ax.plot(xs, ys, color=INK, lw=1.4, ls="--")
    ax.text(len(bs) - 0.6, np.nanmax(np.array(ys, float)) - 0.3,
            r"$\lambda = 1/\log_2 3$" "\nbelow: exact, $E\\equiv1$",
            color=INK, ha="right", va="top", fontsize=8)
    fig.tight_layout(); fig.savefig("figures/fig1_occupancy_grid.png", dpi=200)
    plt.close(fig)

def fig2_delta_law():
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ts = np.linspace(0, 12, 200)
    ax.plot(ts, 2.0 ** -ts, color=MUT, lw=1.6, ls="--", zorder=1)
    # series are offset horizontally by +-0.12 so the three do not hide one another
    ax.text(8.5, 2.0 ** -8.0, "null  $2^{-t}$", color=INK2, fontsize=9, va="bottom")
    styles = [("3x+1", S1, "o", -0.12), ("3x-1", S2, "s", 0.0), ("5x-1", S3, "^", 0.12)]
    for name, col, mk, off in styles:
        ds = []
        for f in glob.glob(f"results/words/{name}_n*.csv"):
            ds.append(load(f)["delta"])
        d = np.concatenate(ds)
        tt = np.arange(0.5, 12.01, 0.5)
        emp = [(d > t).mean() for t in tt]
        ax.plot(tt + off, emp, color=col, marker=mk, ms=5, lw=0, zorder=3,
                mfc="none", mew=1.4, label=f"{name}  (K={len(d):,})")
    ax.set_yscale("log"); ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$P(\delta > t)$")
    ax.set_title("The realizer deficit obeys the uniform-class null exactly\n"
                 r"$\delta(w)=S_n+1-\log_2 r(w)$, words sampled from the exact dyadic law",
                 loc="left", color=INK)
    ax.legend(loc="upper right", labelcolor=INK2)
    fig.tight_layout(); fig.savefig("figures/fig2_delta_law.png", dpi=200)
    plt.close(fig)

def fig3_reach():
    from pmass import p_series
    from eoc import Map
    mp = Map(3, 1)
    ps, _ = p_series(mp, 320)
    d = json.load(open("results/scan_A32/merged.json"))
    L = {int(k): v for k, v in d["L"].items()}
    ns = sorted(L)
    fig, ax = plt.subplots(figsize=(7.0, 4.6))
    nn = np.arange(2, 321)
    ax.plot(nn, [mp.A(n) + 1 for n in nn], color=MUT, lw=1.6, ls="--", zorder=1)
    ax.plot(nn, [-math.log2(float(ps[n])) for n in nn], color=S2, lw=2.0, zorder=3)
    ax.plot(ns, [math.log2(L[n]) for n in ns], color=S1, lw=2.0, zorder=4)
    # reach of a K-word sample
    reach = []
    for f in sorted(glob.glob("results/words/3x+1_n*.csv"),
                    key=lambda s: int(s.split("_n")[1][:-4])):
        n = int(f.split("_n")[1][:-4]); c = load(f)
        reach.append((n, (c["S"] + 1 - c["delta"]).min()))
    ax.plot([r[0] for r in reach], [r[1] for r in reach], color=S3, lw=0,
            marker="^", ms=6, zorder=5)
    ax.fill_between(nn, [-math.log2(float(ps[n])) for n in nn],
                    [mp.A(n) + 1 for n in nn], color="#f0efec", zorder=0)
    ax.text(262, 105, "out of reach of any sample:\n"
            "$\\approx 2^{(\\alpha-I_0)n}$ words would be needed",
            color=INK2, fontsize=8.5, ha="center")
    ax.text(318, mp.A(318) + 3, "class modulus  $S_n+1$", color=INK2,
            fontsize=8.5, ha="right", va="bottom")
    ax.text(196, 292, "smallest realizer in a $2\\times10^4$-word sample",
            color=S3, fontsize=8.5, ha="right", va="bottom")
    ax.text(318, 44, "exact word mass  $\\log_2(1/p_n)$", color=S2,
            fontsize=8.5, ha="right", va="bottom")
    ax.text(318, 6, "frontier  $\\log_2 r_{\\min}(n)$, complete scan to $2^{32}$",
            color=S1, fontsize=8.5, ha="right", va="top")
    ax.set_xlabel("depth  $n$"); ax.set_ylabel("bits")
    ax.set_title("Why sampling cannot reach the frontier\n"
                 "the open problem lives at a deficit linear in $n$; a sample of "
                 "$K$ words reaches $\\delta\\approx\\log_2 K$",
                 loc="left", color=INK)
    fig.tight_layout(); fig.savefig("figures/fig3_reach.png", dpi=200)
    plt.close(fig)



def fig4_controls():
    """The control contrast: exact letter law vs the confined-integer cohort."""
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import numpy as np
    from eoc import Map, word_of
    from m4d_strata import cohort
    from m7_exact_letter_law import exact_letter_law
    n = 140
    panels = [("$3x+1$", Map(3, 1), "results/scan_A36", True, S1),
              ("$5x-1$", Map(5, -1), "results/scan_E32deep", False, S2)]
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.9), sharey=True)
    for ax, (lab, mp, scan, rootf, col) in zip(axes, panels):
        law = exact_letter_law(mp, n, list(range(n)), dmax=12)
        P = [float(sum(law[k][d] for k in range(n)) / n) for d in range(1, 7)]
        ms = cohort(scan, n)
        if rootf: ms = [m for m in ms if m % 3 != 2]
        W = np.array([word_of(mp, m, n) for m in ms], dtype=np.int16)
        O = [float((W == d).sum()) / W.size for d in range(1, 7)]
        x = np.arange(1, 7)
        ax.bar(x - 0.19, P, 0.34, color="#c3c2b7", label="exact ensemble law")
        ax.bar(x + 0.19, O, 0.34, color=col, label="confined integers")
        ax.set_yscale("log"); ax.set_xticks(x)
        ax.set_xlabel("letter  $a_k$")
        ax.set_title(lab + ("  — rare side is growth" if rootf else
                            "  — rare side is shrinking"), loc="left", color=INK)
        ax.legend(labelcolor=INK2, fontsize=8)
        for xi, p, o in zip(x, P, O):
            if abs(o - p) / p > 0.03:
                ax.text(xi, max(p, o) * 1.35, f"{100*(o-p)/p:+.0f}%",
                        ha="center", fontsize=7.5, color=col)
    axes[0].set_ylabel("frequency")
    fig.suptitle("The archimedean size leaves a fingerprint on $5x-1$ and none on "
                 "$3x+1$\n"
                 "depth 140; complete enumeration of the confined integers below "
                 "$2^{36}$ / $2^{32}$", ha="left", x=0.02, y=0.995, va="top", color=INK, fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig("figures/fig4_control_contrast.png", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs("figures", exist_ok=True)
    fig1_deviation_grid(); print("fig1")
    fig2_delta_law(); print("fig2")
    fig3_reach(); print("fig3")
    fig4_controls(); print("fig4")
