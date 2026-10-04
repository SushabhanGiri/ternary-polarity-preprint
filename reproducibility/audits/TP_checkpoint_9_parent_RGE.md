# Ternary Polarity checkpoint 9

## Parent scalar RG reconstruction and threshold-separated running

**Research status:** internal technical audit  
**Theory version:** TP-G0 matched to TP-D v0.2  
**Date:** 19 September 2026  
**Epistemic level:** exact one-loop scalar algebra plus model-dependent leading running

## Executive verdict

The general CP-conserving TP-G scalar potential has seventeen real
dimensionless couplings: five self quartics, ten modulus portals, and two
phase-sensitive quartics.  Its complete scalar-only one-loop beta functions
have been derived with exact rational arithmetic.  Representative components
were independently regenerated from the four-index quartic tensor, and the
TP-D subsystem is recovered exactly.

The factorized TP-G0 benchmark is **not an RG-invariant surface**.  Even when

\[
\lambda_{A\Phi_m}=\lambda_{B\Phi_E}=0
\]

at the matching scale, scalar and gauge loops give

\[
\begin{aligned}
16\pi^2\beta_{\lambda_{A\Phi_m}}\big|_0
 &=36\kappa_m^2+108g_m^4,\\
16\pi^2\beta_{\lambda_{B\Phi_E}}\big|_0
 &=36\kappa_E^2+108g_E^4.
\end{aligned}
\]

This invalidates extrapolation of the factorized tree-vacuum proof away from
the matching scale.  It does not immediately invalidate the benchmark: the
generated portals are positive, and a sufficient five-field boundedness
certificate survives until the Higgs quartic becomes negative.  A general
running-vacuum analysis is nevertheless required.

## 1. Exact parent scalar system

For

\[
\{H,A,B,\Phi_m,\Phi_E\},
\]

the scalar potential contains

\[
5\ \text{self quartics}+10\ \text{modulus portals}
+2\ \text{phase-sensitive quartics}=17
\]

real physical couplings after the two isolated phases of
\(\kappa_m,\kappa_E\) are removed by field redefinitions.  The scalar-only
one-loop potential was computed as

\[
16\pi^2\beta_V^{(1)}=\frac12\operatorname{Tr}\!\left[(V_4'')^2\right].
\]

Independent quartic-tensor contractions checked
\(\lambda_H,\lambda_A,\lambda_{H\Phi_m},\lambda_{A\Phi_m},
\lambda_{\Phi_m\Phi_E},\kappa_m,\kappa_E\) exactly.  The four real-component
projections of each phase-sensitive operator yield the same beta function,
which is a nontrivial covariance check.

Selected results are

\[
\begin{aligned}
16\pi^2\beta_{\lambda_A}^{\rm scalar}
={}&20\lambda_A^2+2\lambda_{HA}^2+\lambda_{AB}^2
+\lambda_{A\Phi_m}^2+\lambda_{A\Phi_E}^2+18\kappa_m^2,\\
16\pi^2\beta_{\lambda_{A\Phi_m}}^{\rm scalar}
={}&4\lambda_{A\Phi_m}^2
+8(\lambda_A+\lambda_{\Phi_m})\lambda_{A\Phi_m}
+36\kappa_m^2\\
&+2\lambda_{AB}\lambda_{B\Phi_m}
+2\lambda_{A\Phi_E}\lambda_{\Phi_m\Phi_E}
+4\lambda_{HA}\lambda_{H\Phi_m},\\
16\pi^2\beta_{\kappa_m}^{\rm scalar}
={}&\kappa_m(12\lambda_A+6\lambda_{A\Phi_m}),
\end{aligned}
\]

with the (E) sector obtained by interchange.  The complete expressions are
stored in `audits/tpd_parent_scalar_rge.json`.

## 2. New-Abelian terms

On the charge-conjugation-protected zero-mixing slice,

\[
16\pi^2\beta_{g_m}=\frac{10}{3}g_m^3,
\qquad
16\pi^2\beta_{g_E}=\frac{10}{3}g_E^3.
\]

Each coefficient follows from one charge-one and one charge-three complex
scalar:

\[
b=\frac13(1^2+3^2)=\frac{10}{3}.
\]

Examples of exact gauge contributions are

\[
\begin{aligned}
16\pi^2\beta_{\lambda_{A\Phi_m}}^{\rm gauge}
&=-60g_m^2\lambda_{A\Phi_m}+108g_m^4,\\
16\pi^2\beta_{\lambda_{\Phi_m}}^{\rm gauge}
&=-108g_m^2\lambda_{\Phi_m}+486g_m^4,\\
16\pi^2\beta_{\kappa_m}^{\rm gauge}
&=-36g_m^2\kappa_m.
\end{aligned}
\]

The analogous (E)-sector formulas follow by exchange.  There is no one-loop
inhomogeneous kinetic-mixing source because no active field is bi-charged.
The imposed \(C_m\times C_E\) automorphism protects the zero-mixing slice to
all perturbative orders.

## 3. Threshold separation

The TP-D running of checkpoints 6 and 7 is a standalone-EFT calculation.  It
cannot be used above the TP-G0 radial and vector masses.  For the benchmark,

\[
m_{\rho_m}=m_{\rho_E}=632.46\ \mathrm{GeV},\qquad
M_m=M_E=900\ \mathrm{GeV}.
\]

The present leading calculation uses a common step matching scale of
\(1\,\mathrm{TeV}\).  It evolves TP-D from (173\,\mathrm{GeV}) to that scale,
turns on the parent fields, and then runs all 17 scalar couplings together
with the SM and new gauge couplings.  It neglects finite matching corrections
and the physical splitting between the four thresholds.

## 4. TP-G0 running result

At \(1\,\mathrm{TeV}\), the running values inherited from the low theory
include

\[
\lambda_H=0.09899,\quad
\lambda_A=0.20943,\quad
\lambda_B=0.26485,
\]

\[
\lambda_{HA}=0.02142,\quad
\lambda_{HB}=0.03224,\quad
\lambda_{AB}=0.10470.
\]

The parent inputs are (g_m=g_E=0.30),
\(\lambda_{\Phi_m}=\lambda_{\Phi_E}=0.20),
\(\kappa_m=0.028284\), and \(\kappa_E=0.042426\).

The leading one-loop trajectory gives:

| Diagnostic | Scale |
|---|---:|
| Sufficient parent BFB certificate first fails | \(3.56\times10^8\,\mathrm{GeV}\) |
| High-energy scalar/Goldstone unitarity boundary | \(3.33\times10^{16}\,\mathrm{GeV}\) |
| First (4\pi) dimensionless-coupling boundary | \(6.28\times10^{16}\,\mathrm{GeV}\) |

The BFB failure is the Higgs direction, as in the standalone B0 branch.  The
new Abelian gauge couplings do not become large first.

At \(10\,\mathrm{TeV}\), radiatively generated portals include

\[
\lambda_{A\Phi_m}=0.01311,\qquad
\lambda_{B\Phi_E}=0.01368,
\]

\[
\lambda_{A\Phi_E}=2.14\times10^{-5},\qquad
\lambda_{B\Phi_m}=2.05\times10^{-5},
\]

and small Higgs-parent portals are generated at the next linked order.  Thus
the general operator basis becomes dynamically relevant even when many
couplings are zero at matching.

## 5. What has and has not been shown

### Derived

- The complete scalar-only one-loop beta system for all 17 parent quartics.
- Exact scalar and gauge sources that destroy the factorized zero-portal
  surface.
- Exact one-loop Abelian coefficients on the protected zero-mixing slice.
- A leading step-matched parent trajectory and its scalar perturbative
  boundaries.

### Model-dependent

- The numerical (3.56\times10^8\), (3.33\times10^{16}\), and
  (6.28\times10^{16}\,\mathrm{GeV}) scales.
- The portal values quoted at (10\,\mathrm{TeV}).

### Not shown

- Dimensionful parent running and a global running-vacuum proof.
- Finite one-loop threshold matching at each physical mass.
- Two-loop stability of the quoted scales.
- Full finite-energy vector/scalar unitarity.
- Collider, precision, relic-density, or direct-detection viability.
- A nonzero TP-specific prediction.

## 6. Referee classification

| Finding | Classification | Consequence |
|---|---|---|
| Standalone TP-D high-scale flow was being juxtaposed with a TeV parent | Repairable dependency error | The two flows are now explicitly separated |
| Factorized parent portal zeros run | Model-dependent but mandatory correction | Replace the factorized proof by a general parent vacuum audit above matching |
| Generated portals are positive in TP-G0 | Conditional survival | No immediate high-field instability from those portals |
| Higgs quartic becomes negative | Model-dependent warning | Metastability/UV sensitivity remains; no absolute-stability claim |
| Scalar perturbativity eventually fails | EFT cutoff | No extrapolation beyond the first controlled boundary |

## 7. Reproducibility

- `code/tpd_parent_scalar_rge.py`
- `code/tpd_parent_gauge_rge.py`
- `code/tpd_parent_rge_running.py`
- `audits/tpd_parent_scalar_rge.json`
- `audits/tpd_parent_gauge_rge.json`
- `audits/tpd_parent_rge_running.json`

Twenty automated regression tests pass after this checkpoint.

## Literature basis

The tensor normalization follows the general one-loop renormalization-group
formulas of Luo, Wang, and Xiao [Luo02b].  Residual gauge symmetry and Abelian
kinetic-mixing context are as cited in checkpoint 8 [Kra89, Hol86].  These
references support the methods and known mechanisms; they do not establish
TP-G0 phenomenology or novelty.
