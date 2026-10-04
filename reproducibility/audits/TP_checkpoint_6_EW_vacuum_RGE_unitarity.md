# Ternary Polarity checkpoint 6

## TP-D electroweak vacuum, scalar unitarity, and one-loop running

**Research status:** internal technical audit  
**Theory version:** TP-D v0.1  
**Date:** 15 September 2026  
**Epistemic level:** exact tree-level results plus model-dependent one-loop results

## Executive result

The minimal kernel-sensitive model passes three limited but important tests:

1. its benchmark electroweak vacuum is the global tree-level minimum under an explicit analytic sufficient condition;
2. its complete high-energy scalar/Goldstone quartic scattering matrix satisfies tree-level partial-wave unitarity at the benchmark;
3. its 15-channel finite-energy physical-scalar matrix satisfies tree-level partial-wave unitarity from threshold to 20 TeV after including every scalar contact and exchange diagram;
4. its scalar-only one-loop quartic beta functions agree coefficient by coefficient in two independent derivations.

The first one-loop running test also produced a negative result. The weak-portal benchmark **B0** loses tree-level boundedness along the running couplings at approximately

\[
\mu_{\rm BFB}=3.57\times10^8\ {\rm GeV}.
\]

A diagnostic stronger-portal benchmark **B1** avoids that failure over the perturbative interval, but reaches the scalar-unitarity boundary near

\[
\mu_U=7.18\times10^{14}\ {\rm GeV}
\]

and the largest-coupling \(4\pi\) boundary near

\[
\mu_{4\pi}=1.35\times10^{15}\ {\rm GeV}.
\]

Therefore this checkpoint is **not** a proof of ultraviolet completion or phenomenological viability. It establishes a healthy tree-level example and a controlled one-loop interval, while exposing a high-scale trade-off between Higgs-quartic stabilization and perturbativity.

## 1. Model and conventions

The exact dual symmetry is

\[
G_{\rm TP-D}=Z_3^{(m)}\times Z_3^{(E)},
\qquad
A\sim(1,0),\quad B\sim(0,1),
\]

with Standard Model fields neutral. In the unbroken inert phase, the most general renormalizable scalar potential is

\[
\begin{aligned}
V={}&-\mu_H^2H^\dagger H+\lambda_H(H^\dagger H)^2
+m_A^2|A|^2+m_B^2|B|^2\\
&+\left(\frac{\mu_A}{3}A^3+\frac{\mu_B}{3}B^3+{\rm h.c.}\right)
+\lambda_A|A|^4+\lambda_B|B|^4\\
&+\lambda_{HA}(H^\dagger H)|A|^2
+\lambda_{HB}(H^\dagger H)|B|^2
+\lambda_{AB}|A|^2|B|^2.
\end{aligned}
\]

The phases of \(A\) and \(B\) can independently minimize their cubic terms. With

\[
H^\dagger H=\frac{h^2}{2},\qquad |A|^2=\frac{a^2}{2},\qquad |B|^2=\frac{b^2}{2},
\]

and nonnegative \(a,b,h\), the phase-minimized potential used in the audit is

\[
\begin{aligned}
V_{\min}={}&-\frac{\mu_H^2h^2}{2}+\frac{\lambda_Hh^4}{4}
+\frac{m_A^2a^2}{2}-\frac{|\mu_A|a^3}{3\sqrt2}+\frac{\lambda_Aa^4}{4}\\
&+\frac{m_B^2b^2}{2}-\frac{|\mu_B|b^3}{3\sqrt2}+\frac{\lambda_Bb^4}{4}
+\frac{\lambda_{HA}h^2a^2+\lambda_{HB}h^2b^2+\lambda_{AB}a^2b^2}{4}.
\end{aligned}
\]

All formulas use natural units, \(\hbar=c=1\). The scalar fields and cubic coefficients have mass dimension one; squared-mass parameters have dimension two; quartics are dimensionless.

## 2. Exact bounded-from-below test

Let

\[
x=H^\dagger H,\qquad y=|A|^2,\qquad z=|B|^2,
\]

so that

\[
V_4=\lambda_Hx^2+\lambda_Ay^2+\lambda_Bz^2
+\lambda_{HA}xy+\lambda_{HB}xz+\lambda_{AB}yz.
\]

This is a quadratic form on the nonnegative orthant with symmetric matrix

\[
Q=\begin{pmatrix}
\lambda_H&\lambda_{HA}/2&\lambda_{HB}/2\\
\lambda_{HA}/2&\lambda_A&\lambda_{AB}/2\\
\lambda_{HB}/2&\lambda_{AB}/2&\lambda_B
\end{pmatrix}.
\]

For a real symmetric \(3\times3\) matrix, the exact copositivity conditions can be written as

\[
\lambda_H,\lambda_A,\lambda_B\ge0,
\]

\[
\bar q_{ij}=q_{ij}+\sqrt{q_{ii}q_{jj}}\ge0,
\]

and

\[
\sqrt{q_{11}q_{22}q_{33}}
+q_{12}\sqrt{q_{33}}+q_{13}\sqrt{q_{22}}+q_{23}\sqrt{q_{11}}
+\sqrt{2\bar q_{12}\bar q_{13}\bar q_{23}}\ge0.
\]

The implementation follows the copositivity formulation reviewed by [Kannike](https://arxiv.org/abs/1205.3781). For B0 the smallest pairwise margin is \(0.17086235\), the final three-field margin is \(0.24509872\), and all exact conditions pass.

## 3. Analytic proof of the benchmark global minimum

The benchmark uses

\[
v=246.22\ {\rm GeV},\quad m_h=125.25\ {\rm GeV},\quad
M_A=180\ {\rm GeV},\quad M_B=400\ {\rm GeV},
\]

\[
\lambda_A=0.20,\quad\lambda_B=0.25,\quad\lambda_{AB}=0.10,
\quad\lambda_{HA}=0.020,\quad\lambda_{HB}=0.030,
\]

\[
|\mu_A|=60\ {\rm GeV},\qquad |\mu_B|=90\ {\rm GeV}.
\]

The Lagrangian masses are fixed by

\[
m_A^2=M_A^2-\frac{\lambda_{HA}v^2}{2},\qquad
m_B^2=M_B^2-\frac{\lambda_{HB}v^2}{2}.
\]

For either dark radial field \(r\),

\[
U(r)=\frac{m^2r^2}{2}-\frac{|\mu|r^3}{3\sqrt2}+\frac{\lambda r^4}{4}
=r^2\left(\frac{m^2}{2}-\frac{|\mu|r}{3\sqrt2}+\frac{\lambda r^2}{4}\right).
\]

The expression in parentheses is nonnegative for every \(r\ge0\) if

\[
|\mu|^2\le9\lambda m^2.
\]

Because all three portal quartics are nonnegative at B0, and both dark inequalities hold, every dark-field contribution relative to \(a=b=0\) is nonnegative. It follows directly that

\[
V_{\min}(h,a,b)\ge -\frac{\mu_H^2h^2}{2}+\frac{\lambda_Hh^4}{4},
\]

whose global minimum is \((h,a,b)=(v,0,0)\). This is an analytic sufficient proof, not only a numerical scan.

At this point the radial Hessian eigenvalues are

\[
(m_h^2,M_A^2,M_B^2)=(15687.5625,32400,160000)\ {\rm GeV}^2.
\]

A 300-start stationary-point search found only the electroweak minimum and the unstable origin within the stated search region. Differential evolution reproduced the electroweak vacuum energy to \(5.8\times10^{-6}\ {\rm GeV}^4\). These numerical results check, but do not replace, the analytic proof.

## 4. Complete high-energy scalar/Goldstone unitarity matrix

Writing the Higgs doublet as four real fields and each complex singlet as two real fields gives eight real scalar components and 36 normalized two-particle channels. The code constructs the full quartic tensor and diagonalizes the corresponding \(36\times36\) scattering matrix.

Its spectrum reduces exactly to

- \(2\lambda_H\), multiplicity 9;
- \(2\lambda_A\), multiplicity 2;
- \(2\lambda_B\), multiplicity 2;
- \(\lambda_{HA}\), multiplicity 8;
- \(\lambda_{HB}\), multiplicity 8;
- \(\lambda_{AB}\), multiplicity 4;
- three eigenvalues of

\[
S=\begin{pmatrix}
6\lambda_H&\sqrt2\lambda_{HA}&\sqrt2\lambda_{HB}\\
\sqrt2\lambda_{HA}&4\lambda_A&\lambda_{AB}\\
\sqrt2\lambda_{HB}&\lambda_{AB}&4\lambda_B
\end{pmatrix}.
\]

With \(a_0=-\Lambda/(16\pi)\), the tree criterion \(|\operatorname{Re}a_0|\le1/2\) becomes \(|\Lambda|\le8\pi\). B0 has

\[
\max|\Lambda|=1.05056,
\qquad
\max|a_0|=0.02090,
\]

and passes comfortably. A 250-point random comparison between direct tensor diagonalization and the analytic spectrum found a maximum absolute eigenvalue discrepancy of \(8.0\times10^{-15}\).

This result is restricted to the high-energy quartic limit. Finite-energy scalar exchange is added below; a gauge-complete analysis must additionally establish Goldstone/longitudinal-vector consistency, include transverse gauge states where relevant, and declare its pole treatment. The methodological need for finite-energy testing is discussed by [Goodsell and Staub](https://arxiv.org/abs/1805.07306).

### 4.1 Finite-energy physical-scalar result

The physical external states at B0 are

\[
h,\ A_1,\ A_2,\ B_1,\ B_2
\]

with masses \((125.25,180,180,400,400)\ {\rm GeV}\). Their 15 unordered two-particle channels were scanned from the lightest threshold, \(250.5025\ {\rm GeV}\), to \(20\ {\rm TeV}\). The matrix includes the quartic contact term and every scalar \(s\)-, \(t\)-, and \(u\)-channel exchange:

\[
\mathcal M_{ab\to cd}=-\lambda_{abcd}
-\sum_e\frac{g_{abe}g_{cde}}{s-m_e^2}
-\sum_e\frac{g_{ace}g_{bde}}{t-m_e^2}
-\sum_e\frac{g_{ade}g_{bce}}{u-m_e^2}.
\]

The scan used the same partial-wave normalization as the high-energy audit. No sampled point required an \(s\)-channel or angular-pole exclusion for the physical-scalar channels of B0. The maximum was

\[
\max_{\sqrt s,i}|a_0^i|=0.0207110
\]

at \(20\ {\rm TeV}\), approaching the physical-subspace high-energy value \(0.0207374\). Analytic logarithmic angular integration agreed with independent 192-point Gauss–Legendre integration at representative energies; the largest absolute matrix difference was \(2.8\times10^{-9}\).

> **MODEL-DEPENDENT RESULT**  
> B0 passes the complete finite-energy **physical-scalar** tree-level test over the scanned interval. This is not yet the complete electroweak/gauge-sector unitarity result because external Goldstones and vectors and gauge-exchange diagrams have not been included.

## 5. Independently regenerated scalar one-loop RGEs

The scalar-only beta functions were derived in two independent ways:

1. contraction of the fully symmetric four-index quartic tensor;
2. extraction from \(\tfrac12\operatorname{Tr}[(V_4'')^2]\).

The two results agree exactly as rational polynomials. With \(\beta_\lambda=d\lambda/d\ln\mu\),

\[
\begin{aligned}
16\pi^2\beta_{\lambda_H}&=24\lambda_H^2+\lambda_{HA}^2+\lambda_{HB}^2,\\
16\pi^2\beta_{\lambda_A}&=20\lambda_A^2+2\lambda_{HA}^2+\lambda_{AB}^2,\\
16\pi^2\beta_{\lambda_B}&=20\lambda_B^2+2\lambda_{HB}^2+\lambda_{AB}^2,\\
16\pi^2\beta_{\lambda_{HA}}&=12\lambda_H\lambda_{HA}+8\lambda_A\lambda_{HA}
+4\lambda_{HA}^2+2\lambda_{AB}\lambda_{HB},\\
16\pi^2\beta_{\lambda_{HB}}&=12\lambda_H\lambda_{HB}+8\lambda_B\lambda_{HB}
+4\lambda_{HB}^2+2\lambda_{AB}\lambda_{HA},\\
16\pi^2\beta_{\lambda_{AB}}&=8\lambda_A\lambda_{AB}+8\lambda_B\lambda_{AB}
+4\lambda_{AB}^2+4\lambda_{HA}\lambda_{HB}.
\end{aligned}
\]

The coefficients reproduce the decoupled \(O(4)\) and \(O(2)\) limits. Standard Model gauge and third-family Yukawa terms were then added in the one-loop running code. Dimensionful masses and cubic coefficients are not yet included.

## 6. Named running benchmarks

### B0 — weak portals

\[
(\lambda_{HA},\lambda_{HB})=(0.020,0.030)
\]

at \(\mu_0=173\ {\rm GeV}\). This is the same quartic point used in the tree-level vacuum and high-energy unitarity audits. The one-loop system gives

\[
\mu_{\rm BFB}=3.5739\times10^8\ {\rm GeV},\quad
\mu_U=2.1109\times10^{15}\ {\rm GeV},\quad
\mu_{4\pi}=3.9611\times10^{15}\ {\rm GeV}.
\]

The first failure is the running Higgs quartic becoming negative. B0 therefore fails the chosen **absolute tree-level BFB-at-every-scale criterion**. This does not by itself prove an unacceptable vacuum lifetime; a metastability calculation using the RG-improved effective potential would be required for that different question.

### B1 — diagnostic stabilizing portals

\[
(\lambda_{HA},\lambda_{HB})=(0.18,0.18),
\]

with the other dimensionless initial values unchanged. No BFB failure occurs before perturbation theory fails. The minimum copositivity margin is \(0.004086\), while

\[
\mu_U=7.1790\times10^{14}\ {\rm GeV},\qquad
\mu_{4\pi}=1.3534\times10^{15}\ {\rm GeV}.
\]

The estimates are stable under 3000, 6000, and 9000 logarithmic sample points. The ODE solver eventually stops after the theory has already crossed both declared perturbative boundaries; its later blow-up is not used as a physical prediction.

B1 is a theoretical diagnostic, **not yet a phenomenologically accepted benchmark**. In particular, changing the portals requires recomputing the dimensionful mass parameters if the same pole-mass targets are desired, and Higgs-portal direct-detection and invisible-width constraints must be imposed before claiming viability.

## 7. Referee attack

### What has actually been shown

- The B0 scalar potential is bounded from below at the input scale.
- The B0 inert electroweak point is the global tree-level minimum under explicit sufficient inequalities.
- The full high-energy scalar/Goldstone quartic matrix is unitary at B0.
- The full finite-energy physical-scalar matrix is unitary for B0 from threshold to 20 TeV.
- Two independent scalar-only one-loop derivations agree exactly.
- Weak portals do not stabilize the running Higgs quartic in the one-loop approximation used.
- Stronger portals can postpone BFB failure beyond the perturbative domain, but they make the theory reach strong coupling earlier.

### What has not been shown

- a complete finite-energy gauge-independent scalar/Goldstone/vector bound;
- two-loop or threshold-matched running;
- the running of masses and cubic coefficients;
- tunnelling lifetime or metastability;
- collider, relic-density, direct-detection, or cosmological viability of B0 or B1;
- ultraviolet completion;
- any new experimentally confirmed prediction.

### Failure conditions

This benchmark branch fails if a complete calculation finds a deeper vacuum with unacceptable lifetime, a finite-energy unitarity violation below its intended cutoff, exclusion by portal/dark-sector data throughout the theoretically allowed region, or radiative generation of an operator forbidden by the claimed exact symmetry.

## 8. Status and next gate

| Test | Status | Reason |
|---|---|---|
| Tree-level boundedness | Achieved for B0 | Exact copositivity conditions pass |
| Global inert electroweak vacuum | Achieved for B0 | Analytic sufficient proof plus numerical checks |
| High-energy scalar unitarity | Achieved for B0 | Complete 36-channel quartic matrix |
| Scalar one-loop RGE derivation | Achieved | Two exact methods agree |
| One-loop absolute stability | Failed for B0; provisional for B1 | B0 loses BFB; B1 reaches perturbative boundary first |
| Finite-energy physical-scalar unitarity | Provisional pass for B0 | All scalar contacts and exchanges included to 20 TeV |
| Finite-energy gauge-sector unitarity | Open | Goldstone/vector channels and gauge diagrams incomplete |
| Full quantum consistency | Partial | Two-loop, thresholds, and dimensionful RGEs absent |
| Phenomenology | Open | No global experimental constraint analysis yet |
| TP-specific prediction | Open | The symmetry-protected null transition remains the current lead |

The next defensible step is the gauge-complete finite-energy scattering audit followed by a deliberately minimal phenomenology benchmark. Grand-unification claims remain quarantined.

## Reproducible files

- `code/tpd_ew_vacuum.py`
- `code/tpd_high_energy_unitarity.py`
- `code/tpd_finite_energy_unitarity.py`
- `code/tpd_scalar_rge.py`
- `code/tpd_quartic_rge_running.py`
- `code/test_tpd_phase3.py`
- `audits/tpd_ew_vacuum.json`
- `audits/tpd_high_energy_unitarity.json`
- `audits/tpd_finite_energy_unitarity.json`
- `audits/tpd_scalar_rge.json`
- `audits/tpd_quartic_rge_running.json`
- `audits/tpd_quartic_rge_B1.json`
- `audits/tpd_rge_convergence_B1.json`
