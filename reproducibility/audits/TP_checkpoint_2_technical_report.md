# Ternary Polarity Core-Survival Gate

## Scope and decision

This report tests the present TP-1 scalar-gauge core before book chapters are drafted around it. TP-1 consists of the Standard Model, a hidden compact \(U(1)_X\), a charge-three complex scalar \(S\), a charge-one complex scalar \(\chi\), and the residual \(Z_3\) left after \(\langle S\rangle\neq0\). With \(Q_X(S)=3\) and \(Q_X(\chi)=1\), this is the same local-\(Z_3\) model class studied by Ko and Tang, not a novel model class by itself.^1

Four conclusions can now be stated.

1. The full tree-level boundedness problem admits an exact reduction to a one-dimensional positivity test.
2. Every generic radial stationary branch can be enumerated algebraically through at most a cubic equation.
3. A healthy inert benchmark exists and the branch enumerator passed an independent randomized numerical validation.
4. The dual labels \((q_m,q_E)\) have no additional physics if all operators and observables depend only on \(q_P=q_m+q_E\). A genuinely distinct theory must retain the full \(Z_3\times Z_3\) selection rule or another observable action of its kernel.

The high-energy scalar unitarity matrix and the scalar-only part of the one-loop quartic RG system have also been generated reproducibly. Finite-energy unitarity, the gauge/Yukawa completion of all beta functions, loop-improved vacuum stability, and phenomenology remain open. TP-1 therefore survives this checkpoint as a consistent candidate EFT branch, not as a completed theory of nature.

> **MODEL-DEPENDENT RESULT**  
> A nonempty, explicitly checked tree-level parameter region has the required \(v\neq0\), \(f\neq0\), \(\langle\chi\rangle=0\), positive radial masses, bounded potential, and perturbative high-energy scalar amplitudes.

> **OPEN PROBLEM**  
> No unique empirical prediction of Ternary Polarity has yet been established. The strongest current route is a kernel-sensitive selection rule in a true \(Z_3\times Z_3\) realization.

## 1. Canonical scalar sector

Use natural units and write

\[
H^\dagger H=\frac{h^2}{2},\qquad
S=\frac{s}{\sqrt2}e^{i\alpha},\qquad
\chi=\frac{x}{\sqrt2}e^{i\beta},
\qquad h,s,x\ge0.
\]

The most general renormalizable potential for the stated fields and gauge charges is

\[
\begin{aligned}
V={}&-\mu_H^2H^\dagger H+\lambda_H(H^\dagger H)^2
-\mu_S^2S^\dagger S+\lambda_S(S^\dagger S)^2
+\mu_\chi^2\chi^\dagger\chi+\lambda_\chi(\chi^\dagger\chi)^2\\
&+\lambda_{HS}(H^\dagger H)(S^\dagger S)
+\lambda_{H\chi}(H^\dagger H)(\chi^\dagger\chi)
+\lambda_{S\chi}(S^\dagger S)(\chi^\dagger\chi)
+\left(\kappa S^\dagger\chi^3+\mathrm{h.c.}\right).
\end{aligned}
\]

A field redefinition makes \(\kappa\ge0\). For \(sx\neq0\), the phase minimizes at

\[
\cos(3\beta-\alpha)=-1.
\]

The phase-minimized radial potential is therefore

\[
\begin{aligned}
V(h,s,x)={}&-\frac12\mu_H^2h^2+\frac14\lambda_Hh^4
-\frac12\mu_S^2s^2+\frac14\lambda_Ss^4
+\frac12\mu_\chi^2x^2+\frac14\lambda_\chi x^4\\
&+\frac14\lambda_{HS}h^2s^2
+\frac14\lambda_{H\chi}h^2x^2
+\frac14\lambda_{S\chi}s^2x^2
-\frac12\kappa sx^3.
\end{aligned}
\]

The \(\kappa\) operator is the gauge-invariant parent of the low-energy \(Z_3\) cubic interaction. Its normalization agrees with the local-\(Z_3\) construction after the corresponding charge and field rescaling.^1 Global-\(Z_3\) singlet models contain the analogous symmetry-breaking cubic after the parent radial mode is removed.^2

## 2. Exact boundedness reduction

The quartic part satisfies

\[
4V_4=\lambda_Hh^4+\lambda_Ss^4+\lambda_\chi x^4
+\lambda_{HS}h^2s^2+\lambda_{H\chi}h^2x^2
+\lambda_{S\chi}s^2x^2-2\kappa sx^3.
\]

The \(x=0\) boundary is bounded strictly upward when

\[
\lambda_H>0,\qquad \lambda_S>0,\qquad
\lambda_{HS}+2\sqrt{\lambda_H\lambda_S}>0.
\]

For \(x>0\), define \(u=h/x\) and \(t=s/x\). Then

\[
\frac{4V_4}{x^4}=\lambda_Hu^4+B(t)u^2+P(t),
\]

where

\[
B(t)=\lambda_{HS}t^2+\lambda_{H\chi},
\qquad
P(t)=\lambda_St^4+\lambda_{S\chi}t^2-2\kappa t+\lambda_\chi.
\]

For fixed \(t\), set \(z=u^2\ge0\). The expression is a quadratic in \(z\), and its exact minimum is

\[
R(t)=
\begin{cases}
P(t),&B(t)\ge0,\\[3pt]
P(t)-\dfrac{B(t)^2}{4\lambda_H},&B(t)<0.
\end{cases}
\]

Consequently, apart from non-strict flat-direction boundaries, the full radial quartic is bounded from below if and only if the \(x=0\) condition holds and

\[
R(t)>0\qquad\text{for every }t\ge0.
\]

This is stronger than the earlier sufficient condition obtained by assuming all portals nonnegative and discarding positive terms. It is also practical: \(R(t)\) is piecewise quartic and can be certified by checking endpoints, switching points \(B(t)=0\), and real nonnegative stationary points in each piece.

> **DERIVED RESULT**  
> The three-field boundedness problem has been reduced exactly to a one-variable positivity problem. This is a mathematical result for TP-1's stated potential, not an experimental claim.

## 3. Complete generic stationary-branch enumeration

The radial stationarity equations are

\[
0=h\left[-\mu_H^2+\lambda_Hh^2
+\frac12\lambda_{HS}s^2+\frac12\lambda_{H\chi}x^2\right],
\]

\[
0=-\mu_S^2s+\lambda_Ss^3
+\frac12\lambda_{HS}h^2s+\frac12\lambda_{S\chi}sx^2
-\frac12\kappa x^3,
\]

\[
0=x\left[\mu_\chi^2+\lambda_\chi x^2
+\frac12\lambda_{H\chi}h^2+\frac12\lambda_{S\chi}s^2
-\frac32\kappa sx\right].
\]

For \(x=0\), the candidates are the origin, the \(H\)-only extremum, the \(S\)-only extremum, and the inert \(HS\) extremum. Define

\[
\Delta=\lambda_H\lambda_S-\frac14\lambda_{HS}^2.
\]

The inert solution is

\[
v^2=\frac{\lambda_S\mu_H^2-\frac12\lambda_{HS}\mu_S^2}{\Delta},
\qquad
f^2=\frac{\lambda_H\mu_S^2-\frac12\lambda_{HS}\mu_H^2}{\Delta},
\]

when both right-hand sides are positive. Its energy is

\[
V_{HS}=-\frac14\left(\mu_H^2v^2+\mu_S^2f^2\right).
\]

Its CP-even radial mass matrix is

\[
\mathcal M^2_{hs}=
\begin{pmatrix}
2\lambda_Hv^2&\lambda_{HS}vf\\
\lambda_{HS}vf&2\lambda_Sf^2
\end{pmatrix},
\]

while the two real components of the inert complex scalar have common mass

\[
m_\chi^2=\mu_\chi^2+\frac12\lambda_{H\chi}v^2
+\frac12\lambda_{S\chi}f^2.
\]

For \(\kappa>0\), any stationary point with \(x>0\) must also have \(s>0\). This removes an apparent branch: \(s=0,x>0\) is inconsistent because the \(s\) equation contains \(-\kappa x^3/2\).

Both remaining mixed cases reduce to the same cubic. For a branch with \(h>0\), analytically eliminate \(h\) and define Schur-complement parameters

\[
\bar\mu_S^2=\mu_S^2-\frac{\lambda_{HS}\mu_H^2}{2\lambda_H},
\qquad
\bar\mu_\chi^2=\mu_\chi^2+\frac{\lambda_{H\chi}\mu_H^2}{2\lambda_H},
\]

\[
\bar\lambda_S=\lambda_S-\frac{\lambda_{HS}^2}{4\lambda_H},
\quad
\bar\lambda_\chi=\lambda_\chi-\frac{\lambda_{H\chi}^2}{4\lambda_H},
\quad
\bar\lambda_{S\chi}=\lambda_{S\chi}
-\frac{\lambda_{HS}\lambda_{H\chi}}{2\lambda_H}.
\]

For a branch with \(h=0\), remove the bars by using the original parameters. With \(t=s/x>0\), every nondegenerate mixed stationary point obeys

\[
\begin{aligned}
0={}&\left(\frac12\mu_S^2\lambda_{S\chi}
+\mu_\chi^2\lambda_S\right)t^3
-\frac32\kappa\mu_S^2t^2\\
&+\left(\mu_S^2\lambda_\chi
+\frac12\mu_\chi^2\lambda_{S\chi}\right)t
-\frac12\kappa\mu_\chi^2,
\end{aligned}
\]

using either the barred or unbarred set as just described. Each positive real root is retained only when it gives \(x^2>0\), \(s=tx>0\), and, for the active-Higgs branch, \(h^2>0\). The Hessian and vacuum energy are then evaluated directly. Homogeneity supplies the useful stationary-point check

\[
V_{\rm stat}=\frac14\left(-\mu_H^2h^2-\mu_S^2s^2+\mu_\chi^2x^2\right).
\]

This procedure enumerates every generic radial stationary point. Measure-zero cases such as \(\kappa=0\), vanishing quartics, or singular Schur complements must be handled separately because they can introduce enhanced symmetries or continuous stationary sets.

## 4. Numerical certification

An illustrative benchmark was defined by

\[
v=246\ \mathrm{GeV},\quad f=1000\ \mathrm{GeV},\quad
m_\chi=500\ \mathrm{GeV},
\]

\[
(\lambda_H,\lambda_S,\lambda_\chi)=(0.13,0.30,0.25),
\]

\[
(\lambda_{HS},\lambda_{H\chi},\lambda_{S\chi},\kappa)
=(0.02,0.05,0.08,0.05).
\]

The mass parameters were fixed by the inert stationary conditions. The exact radial boundedness test had a positive minimum

\[
\min_{t\ge0}R(t)=0.2292548748
\quad\text{at}\quad t=0.3372682429.
\]

The inert stationary point was the lowest enumerated candidate, with

\[
V_{HS}=-7.5421601053\times10^{10}\ \mathrm{GeV}^4.
\]

The three radial Hessian eigenvalues were

\[
(1.56927\times10^4,\ 2.50000\times10^5,\ 6.00041\times10^5)\ \mathrm{GeV}^2.
\]

An independent differential-evolution search followed by bounded local minimization returned \((h,s,x)=(246.0000024,999.9999998,0)\) GeV with the same energy to the displayed accuracy.

The branch enumerator was then tested on 40 randomly generated bounded potentials using a fixed seed. The direct global optimizer and analytic enumeration agreed in all 40 cases under a relative energy tolerance of \(2\times10^{-6}\). The winning branches included the origin, \(H\)-only, \(S\)-only, inert \(HS\), mixed \(S\chi\), and fully mixed \(HS\chi\) vacua. This is a numerical cross-check, not a proof of the optimizer; the algebraic enumeration supplies the completeness argument in generic cases.

## 5. High-energy scalar unitarity

The finite-energy convention used in modern \(Z_3\) singlet analyses constructs the \(J=0\) matrix with explicit identical-particle factors and imposes

\[
\left|\operatorname{Re}a_0^i\right|\le\frac12.
\]

Exchange diagrams can make finite-energy constraints stronger than the infinite-energy quartic limit, especially when cubic interactions are important.^3 TP-1 must therefore retain a finite-energy scan in its final audit.

As a first exact layer, all eight real scalar components were included: four from \(H\), two from \(S\), and two from \(\chi\). There are 36 unordered two-particle channels. If

\[
V_4=\frac1{4!}\lambda_{abcd}\phi_a\phi_b\phi_c\phi_d,
\]

the normalized high-energy matrix is

\[
L_{(ij)(kl)}=
\frac{\lambda_{ijkl}}
{\sqrt{2^{\delta_{ij}}2^{\delta_{kl}}}},
\qquad
a_0=-\frac{L}{16\pi}.
\]

Thus every eigenvalue \(L_i\) must satisfy \(|L_i|\le8\pi\). For the benchmark above, the spectral radius was \(1.2337507508\), giving

\[
\max_i|a_0^i|=0.0245447.
\]

The benchmark therefore passes the scalar-quartic high-energy test by a wide margin. One-coupling-at-a-time checks reproduce the expected \(O(4)\) eigenvalue \(6\lambda_H\) and \(O(2)\) eigenvalues \(4\lambda_S\) and \(4\lambda_\chi\), providing a normalization check.

> **PARTIAL RESULT**  
> The complete 36-channel high-energy scalar quartic matrix has been generated and checked. This does not yet replace the required finite-energy calculation with scalar exchange, gauge/Goldstone channels, pole excision, and an explicit energy range.

## 6. One-loop RGE checkpoint

For real scalars in the convention above, the scalar-only one-loop tensor equation is

\[
(16\pi^2)\beta_{abcd}=
\lambda_{abef}\lambda_{efcd}
+\lambda_{acef}\lambda_{efbd}
+\lambda_{adef}\lambda_{efbc}.
\]

An exact-arithmetic tensor generator gives

\[
(16\pi^2)\beta_{\lambda_H}^{\rm scalar}
=24\lambda_H^2+\lambda_{HS}^2+\lambda_{H\chi}^2,
\]

\[
(16\pi^2)\beta_{\lambda_S}^{\rm scalar}
=20\lambda_S^2+2\lambda_{HS}^2+\lambda_{S\chi}^2,
\]

\[
(16\pi^2)\beta_{\lambda_\chi}^{\rm scalar}
=20\lambda_\chi^2+2\lambda_{H\chi}^2+\lambda_{S\chi}^2+18\kappa^2,
\]

\[
\begin{aligned}
(16\pi^2)\beta_{\lambda_{HS}}^{\rm scalar}={}&
12\lambda_H\lambda_{HS}+8\lambda_S\lambda_{HS}
+4\lambda_{HS}^2+2\lambda_{H\chi}\lambda_{S\chi},\\
(16\pi^2)\beta_{\lambda_{H\chi}}^{\rm scalar}={}&
12\lambda_H\lambda_{H\chi}+8\lambda_\chi\lambda_{H\chi}
+4\lambda_{H\chi}^2+2\lambda_{HS}\lambda_{S\chi},\\
(16\pi^2)\beta_{\lambda_{S\chi}}^{\rm scalar}={}&
8\lambda_S\lambda_{S\chi}+8\lambda_\chi\lambda_{S\chi}
+4\lambda_{S\chi}^2+4\lambda_{HS}\lambda_{H\chi}
+36\kappa^2,\\
(16\pi^2)\beta_\kappa^{\rm scalar}={}&
\kappa(12\lambda_\chi+6\lambda_{S\chi}).
\end{aligned}
\]

The generator reproduces independently known \(O(4)\) and \(O(2)\) scalar coefficients. These equations remain a checkpoint until a second implementation verifies every mixed and \(\kappa\)-dependent coefficient.

For the minimal hidden field content, the one-loop Abelian gauge coefficient is fixed by the two complex scalars:

\[
(16\pi^2)\beta_{g_X}=\frac{10}{3}g_X^3,
\]

because \(\frac13(3^2+1^2)=10/3\). A general multiple-\(U(1)\) treatment must use a gauge-coupling matrix rather than treating kinetic mixing as an afterthought.^4,5 If no field carries both hypercharge and \(X\) charge, the inhomogeneous one-loop source proportional to \(\sum_iY_iQ_{X,i}\) vanishes. A nonzero UV threshold or added bi-charged matter can nevertheless generate kinetic mixing, so \(\epsilon=0\) is a model boundary condition, not a consequence of residual \(Z_3\) alone.

The complete one-loop system still requires Standard Model gauge and Yukawa terms, \(U(1)_X\) gauge terms in every scalar beta function, masses, scalar anomalous dimensions, threshold matching at \(f\), and optional nonminimal gravitational couplings. No RG-stability scale is claimed in this report.

## 7. The dual-charge distinctness theorem

Let

\[
G=Z_3\times Z_3,\qquad
\pi(a,b)=a+b\pmod3,\qquad
K=\ker\pi=\{(0,0),(1,2),(2,1)\}.
\]

Suppose every field transformation, allowed operator, Hamiltonian term, state label, and observable depends on \((a,b)\) only through \(\pi(a,b)\). Then the action of \(K\) is physically trivial and the representation factors through

\[
G/K\simeq Z_3.
\]

Any two assignments in the same fibre of \(\pi\) are operationally indistinguishable. The theory is therefore equivalent, with respect to all specified observables, to an ordinary \(Z_3\) theory plus redundant labels or unresolved multiplicity.

> **DERIVED RESULT**  
> The fibre cardinality of three does not by itself create three physical states, three generations, or new selection rules. Physical distinctness requires a kernel-sensitive operation or observable.

| Structure | Operator condition | Physical content |
|---|---|---|
| Quotient-only \(H_0\) | \(\sum_i(a_i+b_i)=0\pmod3\) | Ordinary \(Z_3\) |
| Full dual symmetry \(H_1\) | \(\sum_i a_i=0\) and \(\sum_i b_i=0\pmod3\) | Strictly stronger selection rules |

Take two complex scalars

\[
A\sim(1,0),\qquad B\sim(0,1).
\]

Both have quotient charge \(q_P=1\). Under quotient-only \(Z_3\), the bilinear \(A^\dagger B\) is neutral and allowed. Under the full product symmetry it carries \((2,1)\neq(0,0)\) and is forbidden. The cubic operators \(A^2B\) and \(AB^2\) are likewise quotient-neutral but forbidden by \(Z_3\times Z_3\).

The lowest-dimension difference is therefore already dimension two:

\[
A^\dagger B:\quad H_0\ \text{allows},\qquad H_1\ \text{forbids}.
\]

With a neutral scalar mediator \(R\), \(RA^\dagger B\) supplies a dimension-three decay or conversion vertex in \(H_0\) but remains forbidden in \(H_1\). Hence an exact full symmetry predicts

\[
\Gamma(A\to B+R)=0
\]

whenever that decay would rely on this operator and no symmetry-breaking spurion is present. Observation of such mixing or conversion would falsify the exact \(H_1\) assignment. Non-observation would not by itself establish Ternary Polarity, because an ordinary model can set the same coupling to zero for another reason.

A minimal anomaly-free parent uses only scalars beyond the SM:

\[
U(1)_m\times U(1)_E
\xrightarrow{\langle S_m\rangle,\langle S_E\rangle}
Z_3^{(m)}\times Z_3^{(E)},
\]

with \(S_m\sim(3,0)\), \(S_E\sim(0,3)\), \(A\sim(1,0)\), and \(B\sim(0,1)\). Because no new chiral fermions are required, gauge anomalies are absent in this minimal scalar realization. Its two string species give a kernel-sensitive holonomy matrix:

| Probe | \(m\)-string phase | \(E\)-string phase |
|---|---:|---:|
| \(A\sim(1,0)\) | \(\omega\) | \(1\) |
| \(B\sim(0,1)\) | \(1\) | \(\omega\) |

This is distinct in principle from a single residual \(Z_3\), whose probes of equal quotient charge have the same discrete holonomy. Discrete gauge symmetries and their Aharonov–Bohm observables are established structures, so the novelty could only lie in a constrained physical identification and its consequences, not in the existence of such holonomies.^6

The cost is significant: a second gauge factor, gauge boson, breaking scalar, portals, kinetic-mixing parameters, and defect sector are introduced. The words “mass” and “energy” do not acquire physical meaning from the group labels. Until observables link \(q_m\) and \(q_E\) to independently measured mass- and energy-related quantities, they should be described technically as two internal ternary charges.

## 8. Hostile-referee assessment

| Test | Status | Reason |
|---|---|---|
| Lorentz-covariant local action | Achieved | Standard gauge-scalar EFT |
| Healthy tree-level kinetic terms | Achieved | Canonical signs |
| Complete renormalizable scalar potential | Achieved | All allowed operators retained |
| Exact tree-level boundedness test | Achieved | One-variable reduction |
| Generic tree-level branch enumeration | Achieved | Cubic reduction plus boundaries |
| Example global inert vacuum | Achieved | Algebraic and numerical agreement |
| High-energy scalar unitarity | Achieved for benchmark | 36-channel quartic matrix |
| Finite-energy unitarity | Open | Exchange and gauge channels pending |
| Complete one-loop RG | Partial | Scalar-only tensor and \(g_X\) beta derived |
| Loop-improved global vacuum | Open | Scheme and counterterms not frozen |
| Distinctness from ordinary \(Z_3\) | Failed for TP-1 | Present dynamics use only one residual charge |
| Distinct dual-charge model | Partial | Exact selection-rule candidate, no fitted benchmark |
| Unique empirical prediction | Open | Null conversion rule is conditional |
| Three-generation explanation | Not achieved | Fibre multiplicity is not a mechanism |
| Gravity-scale prediction | Not achieved | Matching relation still contains free inputs |

The decisive scientific conclusion is narrow but useful: TP-1 is a viable local-\(Z_3\) EFT candidate in an established model class. Its current Ternary Polarity identity resides in interpretation, not an empirical distinction. TP-1D, the full dual-charge extension, supplies genuinely stronger selection rules but pays a substantial complexity cost and has not yet demonstrated parameter compression.

## 9. Next mandatory calculations

1. Generate the full finite-energy \(2\to2\) scalar/Goldstone matrix, excise pole regions consistently, and scan the relevant center-of-mass energy range.
2. Independently regenerate the complete one-loop RGEs with a second implementation, including all gauge, Yukawa, kinetic-mixing, mass, and threshold terms.
3. Turn the \(A^\dagger B\) selection-rule difference into a minimal production-and-decay benchmark with fewer free parameters than measured channels.
4. Compare the dual model against an ordinary \(Z_3\) two-species model using explicit parameter counts and likelihood-independent falsification criteria.
5. Only after these steps, select the canonical branch for dependency-safe manuscript drafting.

## Reproducibility record

The checkpoint uses Python 3 with NumPy 2.3.5 and SciPy 1.17.0. The random seed is 20260915. The included scripts are:

- vacuum_audit.py: exact branch reduction, benchmark evaluation, and direct global minimization;
- test_vacuum_enumerator.py: 40-case randomized cross-check;
- scalar_rge_generator.py: exact-arithmetic real-scalar tensor contraction;
- unitarity_matrix.py: 36-channel high-energy scalar matrix.

Machine-readable outputs record the benchmark, stationary points, optimizer residuals, random-validation result, RGE coefficients, and unitarity spectrum. The calculations use natural units; dimensionful scalar inputs are in GeV or GeV\(^2\).

## Sources

1. P. Ko and Y. Tang, “[Self-interacting scalar dark matter with local \(Z_3\) symmetry](https://doi.org/10.1088/1475-7516/2014/05/047),” *Journal of Cosmology and Astroparticle Physics* 2014(05), 047 (2014).
2. G. Bélanger, K. Kannike, A. Pukhov, and M. Raidal, “[\(Z_3\) Scalar Singlet Dark Matter](https://doi.org/10.1088/1475-7516/2013/01/022),” *Journal of Cosmology and Astroparticle Physics* 2013(01), 022 (2013).
3. A. Hektor, A. Hryczuk, and K. Kannike, “[Improved bounds on \(Z_3\) singlet dark matter](https://doi.org/10.1007/JHEP03(2019)204),” *Journal of High Energy Physics* 2019, 204 (2019).
4. R. M. Fonseca, M. Malinský, and F. Staub, “[Renormalization group equations and matching in a general quantum field theory with kinetic mixing](https://doi.org/10.1016/j.physletb.2013.09.042),” *Physics Letters B* 726, 882–886 (2013).
5. M. Luo and Y. Xiao, “[Renormalization group equations in gauge theories with multiple \(U(1)\) groups](https://doi.org/10.1016/S0370-2693(03)00076-5),” *Physics Letters B* 555, 279–286 (2003).
6. L. M. Krauss and F. Wilczek, “[Discrete gauge symmetry in continuum theories](https://doi.org/10.1103/PhysRevLett.62.1221),” *Physical Review Letters* 62, 1221–1223 (1989).

