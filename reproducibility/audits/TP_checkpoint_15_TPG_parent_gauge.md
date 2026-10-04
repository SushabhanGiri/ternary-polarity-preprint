# TP checkpoint 15 — point-matched TP-G finite-energy gauge gate

**Completion-protocol checkpoint:** C14  
**Verdict:** **CONDITIONAL PASS**  
**Scope:** frozen Higgs-pole point matched to the charge-conjugation-protected zero-kinetic-mixing TP-G parent, through $20$ TeV.

## Point-specific matching

For each $m/E$ Abelian sector,

$$
f=1\ {\rm TeV},\quad g=0.30,\quad Q_\Phi=3,\quad M_X=900\ {\rm GeV},
$$

$$
\lambda_\Phi=0.20,\quad m_\rho=632.456\ {\rm GeV},\quad \lambda_{S\Phi}=0.
$$

The dark masses are $62.0$ and $62.2$ GeV, with $\lambda_S=0.10$ and

$$
\kappa=\frac{\sqrt2\,\mu_S}{3f}=4.71405\times10^{-4}
$$

for $\mu_S=1$ GeV. The two sectors factorize in the gauge calculation; the tiny $A$–$B$ and Higgs portals remain in the already-tested scalar block.

## Methods

- Physical massive-vector helicity amplitudes were constructed for longitudinal and transverse states.
- The normalized neutral $J=0$ basis was $\{X_LX_L/\sqrt2,\rho\rho/\sqrt2,SS^\dagger\}$.
- The mixed charged block $XS\leftrightarrow\rho S$ was projected for $J=0,1,2,3,4$.
- Other pure-vector and charged helicity entries were bounded for every $J$ using $|d^J_{mm'}|\le1$.
- Identical-state factors, thresholds, radial/vector exchange, contact diagrams, and angular convergence were included.
- The physical $J=1$ vector resonance was width-resummed using $X\to SS^\dagger$.
- Scalar-QED Ward contractions and fixed-angle longitudinal/Goldstone equivalence were checked.

## Controlled results

| Diagnostic | Result |
|---|---:|
| Largest neutral longitudinal $J=0$ eigenvalue magnitude | $0.190989$ |
| Strongest non-LLLL pure-vector all-$J$ entry bound | $0.031975$ |
| Largest charged-block eigenvalue in the clean regions, $J=0\ldots4$ | $0.0613163$ |
| Strongest charged all-$J$ entry bound in the clean regions | $0.0613017$ |
| Scalar-QED Ward relative residual | $<8.5\times10^{-16}$ |
| Compton Ward relative residual | $<3.0\times10^{-16}$ |
| Longitudinal/Goldstone mismatch at 20 TeV, fixed angle | $0.28\%$–$0.82\%$ |
| $X_m\to AA^\dagger$ width | $0.52193$ GeV |
| $X_E\to BB^\dagger$ width | $0.52183$ GeV |
| $\kappa/(16\pi)$ amplitude scale | $9.38\times10^{-6}$ |

The 80/160/320-node values of the most forward-sensitive normalized $X_LX_L\to\rho\rho$ wave at 20 TeV are $-0.179808572$, $-0.179808667$, and $-0.179808667$. The largest controlled eigenvalue therefore also satisfies the stronger comfort criterion $|a_J|<1/4$.

## Resonance and exact sequential-pole diagnosis

At $\sqrt{s}=M_X$, the width-resummed elastic $SS^\dagger$ $J=1$ wave has

$$
a_1\simeq-4.16\times10^{-4}+i,
$$

and lies on the elastic Argand circle to $1.8\times10^{-7}$. This is a physical resonance, not a tree-unitarity violation.

For $X(M)+S(m)\to X(M)+S(m)$, the exact exchanged-scalar condition is

$$
u-m^2=M^2-2E_XE_S-2p^2\cos\theta=0.
$$

Its angular solution first enters and finally leaves the physical interval at

$$
\sqrt{s}_{\rm low}=\sqrt{2M^2+m^2},\qquad
\sqrt{s}_{\rm high}=\frac{M^2-m^2}{m}.
$$

The ordering $\sqrt{s}_{\rm high}>\sqrt{s}_{\rm low}$ holds if and only if $M>2m$, exactly the decay condition $X\to SS^\dagger$. Numerically the contaminated intervals are:

- $1.2743$–$13.0025$ TeV in the $m$ sector;
- $1.2743$–$12.9603$ TeV in the $E$ sector.

Thus $X$ is unstable and is not a conventional asymptotic external state. This interval is assigned neither PASS nor FAIL and is not numerically regularized. The ordinary two-body waves in the clean regions below and above it remain below $1/2$; high-energy helicity cancellations are included in the all-$J$ bounds.

## Verdict

**CONDITIONAL PASS.** No properly normalized, nonsingular stable-state channel shows a genuine perturbative-unitarity or Ward-identity failure through $20$ TeV. The largest controlled formal gauge eigenvalue is $0.191<1/2$. The $XS$ interval is unscored. An unconditional parent full-S-matrix PASS would require an inclusive calculation using stable asymptotic states or a consistently defined unstable-particle scheme.

Nonzero Abelian kinetic mixing is outside this protected benchmark and is not a loophole needed to save it.

Reproduction: `code/tpd_parent_gauge_finite_energy.py`; results: `audits/tpd_parent_gauge_finite_energy.json`.
