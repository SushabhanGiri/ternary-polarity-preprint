# Supplementary Material

## Scope

This supplement records the equations, normalizations, numerical definitions, and validation statements required to reproduce the manuscript. It does not change the C22 scientific freeze.

# Charge and operator audit

The charge of a monomial is the sum of field charges, with conjugated fields carrying the additive inverse charge. The enumerator lists all commuting scalar monomials through engineering dimension four, groups Hermitian-conjugate pairs, and compares invariance under the projected generator \(P\) with invariance under both \(P\) and \(K\). The resulting comparator-only classes are the cross kinetic term, the bilinear \(A^\dagger B\), two mixed cubics, two modulus-weighted bilinears, \((A^\dagger B)^2\), and the off-diagonal Higgs portal. Machine output is stored in audits/dual_tp_operator_basis.json.

# Vacuum conditions

For the electroweak and two-dark-field quartic,

\[
V_4=\lambda_Hx^2+\lambda_Ay^2+\lambda_Bz^2+
\lambda_{HA}xy+\lambda_{HB}xz+\lambda_{AB}yz,
\]

exact boundedness is copositivity of the symmetric matrix defined in the main text. The implementation evaluates the full three-variable copositivity conditions, then separately checks all stationary points of the phase-minimized tree potential. The analytic positive-portal certificate is used only as a sufficient shortcut and is never described as necessary.

# Scalar partial-wave conventions

Two-particle states contain the conventional \(1/\sqrt2\) factor for identical pairs. With

\[
\mathcal M(\cos\theta)=16\pi\sum_J(2J+1)a_JP_J(\cos\theta),
\]

the projection is

\[
a_J=\frac{1}{32\pi}\int_{-1}^{1}d\cos\theta\,
P_J(\cos\theta)\mathcal M(\cos\theta),
\]

with the corresponding Wigner-\(d\) generalization for helicity amplitudes. The audit applies \(|\mathrm{Re}\,a_J|\leq1/2\) to properly normalized nonsingular physical channels.

# Sequential kinematics derivation

In the center-of-mass frame of \(X(M)S(m)\to X(M)S(m)\),

\[
u=M^2+m^2-2E_XE_S-2p^2\cos\theta.
\]

Setting the exchanged scalar on shell gives

\[
M^2-2E_XE_S-2p^2\cos\theta=0.
\]

The first and last contact with the physical angular domain occur at \(\cos\theta=-1\) and \(+1\), yielding

\[
\sqrt{s}_{\rm low}=\sqrt{2M^2+m^2},\qquad
\sqrt{s}_{\rm high}=\frac{M^2-m^2}{m}.
\]

Squaring the ordering condition shows that \(\sqrt{s}_{\rm high}>\sqrt{s}_{\rm low}\) exactly when \(M>2m\). Thus the pole interval and the physical decay \(X\to SS^\dagger\) are the same kinematic fact.

# One-loop running

The low-energy scalar quartic and dimensionful beta functions were obtained independently from the effective-potential Hessian and tensor contractions. The parent calculation evolves the Standard Model gauge and third-family Yukawa couplings, \(g_m\), \(g_E\), and all 17 CP-conserving parent scalar quartics on the protected zero-mixing slice. The numerical matching is a single step at 1 TeV. This approximation is the reason the reported high scales are model-dependent estimates rather than precision thresholds.

# Thermal system

For each complex scalar, particle and antiparticle are assumed symmetric. The equilibrium yield per charge state is evaluated with the modified Bessel function \(K_2\). The finite-width Higgs-mediated rate is inserted into the Gondolo-Gelmini integral. The coupled collision polynomials were separately tested for detailed balance, and conversion was verified to conserve total dark particle number.

The final EOS model uses ideal-gas massive thresholds and a smooth QCD parton-to-hadron interpolation. A plus-or-minus five percent variation of the thermodynamic functions yields the quoted relic envelope. This variation is a sensitivity diagnostic, not a substitute for a dedicated lattice-QCD equation of state.

# Direct detection normalization

For a complex scalar with portal \(\lambda_{HS}(H^\dagger H)|S|^2\), the per-nucleon scalar cross section used in the audit is

\[
\sigma_N^{\rm SI}=
\frac{\lambda_{HS}^2f_N^2\mu_{NS}^2m_N^2}
{4\pi m_h^4m_S^2},
\]

with \(f_N=0.30\) and \(\mu_{NS}=m_Nm_S/(m_N+m_S)\). The experiment comparison is made only after multiplying by \(\xi_i=\Omega_i/\Omega_{\rm DM}\). The two pole spectra are summed because their recoil-scale difference is below 0.5 percent.

# Validation inventory

The final suite contains 34 passing tests. It covers operator counts, analytic spectra, randomized mass and unitarity checks, copositivity and vacuum conditions, one-loop scalar projections, parent gauge coefficients, detailed balance, relic cross-checks, LZ interpolation, electroweak Goldstone identities, parent Ward contractions, cubic-rate suppression, metastability cutoff ordering, prompt parent decays, and the explicit unscored sequential interval.

# Machine-readable records

The reproducibility archive includes the JSON records for every promoted numerical statement, the Python scripts that generated them, the dependency ledger, the v0.3 theory definition, checkpoints C1-C22 where available, and a SHA-256 manifest.


\newpage


# Frozen validation dossier


\newpage

## S1 Ternary Polarity Core-Survival Gate

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



\newpage

## S2 Ternary Polarity Finite-Energy Unitarity Audit

## Result

The TP-1 benchmark passes the complete tree-level **physical-scalar** finite-energy unitarity calculation over \(250.54\ {\rm GeV}\le\sqrt{s}\le20\ {\rm TeV}\), after explicit open-channel selection and pole exclusions. It also passes the 36-channel scalar-plus-Goldstone calculation used as a gaugeless proxy for longitudinal-vector scattering.

This does not yet constitute a full gauge-theory unitarity proof. Gauge vertices, transverse-vector channels, ghosts where required by gauge fixing, and a second implementation remain outside the present calculation.

## 1. Partial-wave convention

For two-particle channels \(a=\{1,2\}\) and \(b=\{3,4\}\),

\[
a_0^{ba}=
\frac{1}{32\pi}
\sqrt{\frac{4|\mathbf p_b||\mathbf p_a|}
{2^{\delta_{12}}2^{\delta_{34}}s}}
\int_{-1}^{1}d(\cos\theta)\,
\mathcal M_{ba}(\cos\theta).
\]

The tree-level criterion is

\[
\left|\operatorname{Re}a_0^i\right|\le\frac12.
\]

A more conservative perturbative-trust diagnostic is \(|a_0^i|\le1/6\). The calculation follows the normalization and pole logic of the general SARAH scalar-unitarity treatment and its \(Z_3\) application.^1,2

## 2. Amplitude construction

The eight real scalar components are rotated to the mass basis. At the inert benchmark the tree-level squared masses are

\[
(0,0,0,0,\ 15692.7325,\ 250000,\ 250000,\ 600041.4275)\ {\rm GeV}^2.
\]

The four massive states have masses

\[
(125.2706,\ 500,\ 500,\ 774.6234)\ {\rm GeV}.
\]

For cubic tensors \(g_{ijk}\) and quartic tensors \(\lambda_{ijkl}\), every matrix element includes

\[
\mathcal M_{ab\to cd}=
-\lambda_{abcd}
-\sum_e\frac{g_{abe}g_{cde}}{s-m_e^2}
-\sum_e\frac{g_{ace}g_{bde}}{t-m_e^2}
-\sum_e\frac{g_{ade}g_{bce}}{u-m_e^2}.
\]

Both numerical Gauss–Legendre integration and analytic logarithmic integration of the \(t\)- and \(u\)-channel propagators were implemented.

## 3. Independent validation

The engine was reduced to the global-\(Z_3\) singlet model with mass \(M\), self-coupling \(\lambda\), and cubic \(\mu_3\). Its three-channel numerical eigenvalues were compared with Eqs. (3.6)–(3.7) of Hektor, Hryczuk, and Kannike:^2

\[
a_0^{(1)}=
-\frac{\sqrt{s(s-4M^2)}
\left[4\lambda(s-M^2)+9\mu_3^2\right]}
{32\pi s(s-M^2)},
\]

\[
a_0^{(2)}=
\frac{4\lambda(4M^2-s)+9\mu_3^2
\ln[(s-3M^2)/M^2]}
{16\pi\sqrt{s(s-4M^2)}}.
\]

At \(s/M^2=4.05,5,7.5,12,50\), the maximum relative discrepancy was

\[
1.23\times10^{-15}.
\]

This validates the amplitude signs, identical-state normalization, phase-space prefactor, exchange terms, and angular integration against an independent published result.

## 4. Pole policy

Tree-level amplitudes are not reliable on resonances. The scan uses the Goodsell–Staub \(s\)-channel safety condition

\[
\left|1-\frac{s}{m_e^2}\right|>C_S,
\qquad C_S=0.25.
\]

Sixteen grid points were removed by this cut. For a real \(t\)- or \(u\)-channel pole inside the angular interval, every two-particle state participating in the offending matrix element was removed before diagonalization. This is intentionally conservative and may discard more information than a block-by-block SARAH implementation.

The numerical pole cuts are safety prescriptions, not fundamental physical bounds. Earlier trilinear-unitarity work likewise emphasizes that Born amplitudes cannot be trusted on resonances.^3 A future loop-level resonance calculation would require widths and a consistent resummation scheme.

## 5. Physical-scalar scan

Ten unordered channels were constructed from the four massive scalar states. The energy grid included 260 logarithmic points plus points immediately above all six distinct two-particle thresholds:

\[
250.5413,\ 625.2706,\ 899.8940,\ 1000,\ 1274.6234,\ 1549.2468\ {\rm GeV}.
\]

After pole exclusions, 273 energy points were evaluated. The largest eigenvalue magnitude was

\[
\max_{\sqrt{s}}\max_i|a_0^i|
=0.02027154
\]

at the scan endpoint \(\sqrt{s}=20\ {\rm TeV}\). This is below both \(1/2\) and \(1/6\).

The high-energy contact limit in the same four-state basis has maximum eigenvalue magnitude \(0.02044286\), so the endpoint behavior approaches the independently generated quartic asymptote as expected.

> **MODEL-DEPENDENT RESULT**  
> The chosen benchmark has no physical-scalar perturbative-unitarity failure below \(20\ {\rm TeV}\). This does not prove that the EFT cutoff exceeds \(20\ {\rm TeV}\), because unspecified higher-dimensional operators may enter earlier.

## 6. Goldstone-equivalence scan

Following the established scalar-sector method,^1,2 the four zero modes were assigned Feynman-gauge masses:

- two charged SM Goldstones: \(80.4\ {\rm GeV}\);
- one neutral SM Goldstone: \(91.2\ {\rm GeV}\);
- one dark Goldstone: \(m_X=3g_Xf=600\ {\rm GeV}\) for \(g_X=0.20\).

All 36 unordered scalar/Goldstone channels were included. The scan began above the heaviest pair threshold and extended to \(20\ {\rm TeV}\). After partial removal of channels with angular poles, the maximum was

\[
\max_{\sqrt{s}}\max_i|a_0^i|
=0.02396323
\]

at \(20\ {\rm TeV}\). All 36 channels were retained at that energy. The value approaches the complete eight-real-scalar high-energy result \(0.02454469\).

This calculation neglects gauge vertices. It is therefore a gaugeless Goldstone-equivalence test, not a full longitudinal- and transverse-vector scattering calculation.

## 7. Cutoff interpretation

The present result establishes only that the tested renormalizable scalar interactions do not force perturbative breakdown within the scanned range. It does not determine the Wilsonian cutoff.

For the minimal hidden scalars,

\[
(16\pi^2)\beta_{g_X}=\frac{10}{3}g_X^3.
\]

The gauge-only one-loop Landau-pole estimate is

\[
\Lambda_{\rm LP}
=\mu_0\exp\!\left[\frac{8\pi^2}{(10/3)g_X^2(\mu_0)}\right].
\]

For \(g_X=0.20\), this formal scale is exponentially remote. It is not physically meaningful to extrapolate it without the complete coupled RG system, threshold matching, gravitational effects, and a UV completion.

## 8. Referee verdict

| Question | Status |
|---|---|
| Correct identical-particle normalization | Verified against published analytic eigenvalues |
| Contact plus all scalar exchanges | Completed |
| Open-channel thresholds | Completed |
| Explicit \(s\)-channel exclusion | Completed |
| Explicit \(t/u\)-pole detection | Completed |
| Physical-scalar scan | Passed for benchmark |
| Gaugeless scalar/Goldstone scan | Passed for benchmark |
| Gauge-parameter independence | Not shown |
| Full vector/scalar coupled matrix | Open |
| Independent package reproduction | Open |
| Universal TP-1 parameter-space bound | Not shown |
| EFT cutoff determination | Open |

The finite-energy gate is therefore **passed provisionally for the selected benchmark**, not closed for the theory as a whole.

## Reproducibility

- Python 3
- NumPy 2.3.5
- SciPy 1.17.0
- Gauss–Legendre orders: 48, 96, 192
- Main scan order: 96
- \(s\)-channel cut: \(C_S=0.25\)
- Physical-scalar scan: 273 evaluated energies
- Goldstone scan: 220 energies
- Upper scan energy: \(20\ {\rm TeV}\)

The implementation is contained in finite_energy_unitarity.py. The independent published-limit check is validate_finite_energy_against_hektor.py.

## Sources

1. M. D. Goodsell and F. Staub, “[Unitarity constraints on general scalar couplings with SARAH](https://doi.org/10.1140/epjc/s10052-018-6127-z),” *European Physical Journal C* 78, 649 (2018).
2. A. Hektor, A. Hryczuk, and K. Kannike, “[Improved bounds on \(Z_3\) singlet dark matter](https://doi.org/10.1007/JHEP03(2019)204),” *Journal of High Energy Physics* 2019, 204 (2019).
3. A. Schuessler and D. Zeppenfeld, “[Unitarity constraints on MSSM trilinear couplings](https://arxiv.org/abs/0710.5175),” arXiv:0710.5175 (2007).


\newpage

## S3 Ternary Polarity Phase II — Kernel-Distinctness Audit

**Project:** *Ternary Polarity: Toward a \(Z_3\) Framework for Fundamental Physics*  
**Author:** Sushabhan Giri  
**Audit date:** 15 September 2026  
**Canonical branch tested:** TP-D  
**Scientific status:** speculative field-theory construction under audit; not an established theory of nature

## Executive verdict

\[
\boxed{\text{SUBSTANTIVE PARTIAL PASS}}
\]

The dual charge assignment

\[
A\sim(1,0),\qquad B\sim(0,1)
\]

under \(G_{\rm TP}=Z_3^{(m)}\times Z_3^{(E)}\) is physically more restrictive than assigning both fields charge one under only the projected group \(Z_3^{(P)}\). The extra restriction is not erased by a change of field basis: it is equivalently the existence of a noncentral order-three symmetry generator whose charge is conserved by the full action. It forbids a definite set of kinetic, mass, cubic, quartic, and Higgs-portal operators.

The strongest all-orders null prediction of the minimal exact model is

\[
\boxed{\mathcal M(B\rightarrow A+X_0)=0}
\]

for any final collection \(X_0\) neutral under the kernel symmetry, provided \(A\) and \(B\) are nondegenerate kernel-charge eigenstates and the full dual symmetry is exact. In particular,

\[
\boxed{\Gamma(B\rightarrow A+h)=0.}
\]

An ordinary single-\(Z_3\) theory permits the off-diagonal portal \((H^\dagger H)A^\dagger B+\mathrm{h.c.}\), so it generically permits this decay when kinematically open.

This passes the mathematical nonredundancy and radiative-protection tests. It does **not** yet pass the strong novelty or phenomenological-identifiability tests. Product discrete symmetries, symmetry-protected operator zeros, multicomponent dark sectors, and semi-annihilation are established model-building tools. A generic single-\(Z_3\) comparator can also tune its allowed off-diagonal couplings to zero. Consequently a null decay alone cannot positively identify TP-D, although observing a nonzero kernel-changing decay would falsify the exact minimal realization.

The branch therefore advances to the next research stage only as a **kernel-sensitive \(Z_3\times Z_3\) EFT**, not as a demonstrated new fundamental theory.

---

## Document A — Kernel and symmetry analysis

Define

\[
\pi:Z_3^{(m)}\times Z_3^{(E)}\longrightarrow Z_3^{(P)},\qquad
\pi(q_m,q_E)=q_m+q_E\pmod 3.
\]

Then

\[
\ker\pi=\{(0,0),(1,2),(2,1)\}\cong Z_3.
\]

The map is surjective and gives the split exact sequence

\[
0\longrightarrow Z_3\longrightarrow Z_3^2
\overset{\pi}{\longrightarrow}Z_3\longrightarrow0.
\]

A useful invertible change of charge coordinates over \(\mathbb F_3\) is

\[
p=q_m+q_E,\qquad k=q_m-q_E,
\]

because

\[
\det\begin{pmatrix}1&1\\1&-1\end{pmatrix}=-2\equiv1\pmod3.
\]

Thus the dual group can be written as \(Z_3^{(P)}\times Z_3^{(K)}\). In this basis,

\[
A:(p,k)=(1,1),\qquad B:(p,k)=(1,2).
\]

This establishes two facts that must be kept separate:

1. **Exact result:** \(A\) and \(B\) have the same projected charge but different kernel charge.
2. **Novelty limitation:** the abstract group is the standard direct product \(Z_3\times Z_3\). The names “matter-like” and “energy-like” do not add physics unless an independent construction gives those labels operational meaning.

Strictly, charges label characters while group elements act on fields. Because finite Abelian groups are isomorphic to their character groups, one may choose a self-dual pairing, but the identification is a convention. The physical statement is the existence of the extra transformation

\[
K=\operatorname{diag}(\omega,\omega^2),\qquad \omega=e^{2\pi i/3},
\]

acting on \(\Phi=(A,B)^T\). The projected generator is \(P=\omega I_2\).

### Kernel pass/fail result

If the action is invariant only under \(P\), the kernel is physically unobserved. If it is invariant under both \(P\) and \(K\), amplitudes must conserve both charges. The minimal TP-D action below is invariant under \(K\); therefore the kernel acts nontrivially.

---

## Documents B and C — Exact TP-D and generic-\(Z_3\) Lagrangians

Assume that \(A\) and \(B\) are Lorentz scalars and Standard-Model gauge singlets, while all Standard-Model fields are neutral under the new discrete factors. Natural units \(\hbar=c=1\) are used. Scalar fields have mass dimension one.

### Generic projected-\(Z_3\) comparator

Let \(\Phi=(A,B)^T\), with both components transforming as \(\Phi\to\omega\Phi\). The most general renormalizable scalar Lagrangian is

\[
\mathcal L_{Z_3}^{\rm generic}
=(\partial_\mu\Phi)^\dagger Z(\partial^\mu\Phi)-V_{Z_3},
\]

where \(Z\) is a positive Hermitian \(2\times2\) kinetic matrix. It can be made the identity by an invertible field redefinition. In a canonical kinetic basis,

\[
\begin{aligned}
V_{Z_3}={}&V_H+
m_A^2|A|^2+m_B^2|B|^2
 +\left(m_{AB}^2A^\dagger B+\mathrm{h.c.}\right)\\
&+\left[\frac{\mu_A}{3}A^3+\mu_{AAB}A^2B
+\mu_{ABB}AB^2+\frac{\mu_B}{3}B^3+\mathrm{h.c.}\right]\\
&+\lambda_A|A|^4+\lambda_B|B|^4+\lambda_{AB}|A|^2|B|^2\\
&+\left[\eta_A|A|^2A^\dagger B
+\eta_B|B|^2A^\dagger B
+\frac{\eta_2}{2}(A^\dagger B)^2+\mathrm{h.c.}\right]\\
&+(H^\dagger H)\left[\lambda_{HA}|A|^2+\lambda_{HB}|B|^2
+\left(\lambda_{HAB}A^\dagger B+\mathrm{h.c.}\right)\right].
\end{aligned}
\]

Here \(V_H=-m_H^2H^\dagger H+\lambda_H(H^\dagger H)^2\). Hermiticity makes \(m_A^2,m_B^2,\lambda_A,\lambda_B,\lambda_{AB},\lambda_{HA},\lambda_{HB}\) real; the displayed phase-sensitive coefficients may be complex.

### Exact dual TP-D

Requiring the full \(Z_3^{(m)}\times Z_3^{(E)}\) gives

\[
\begin{aligned}
\mathcal L_{\rm TP-D}={}&|\partial A|^2+|\partial B|^2-V_{\rm TP-D},\\
V_{\rm TP-D}={}&V_H+m_A^2|A|^2+m_B^2|B|^2
+\left(\frac{\mu_A}{3}A^3+\frac{\mu_B}{3}B^3+\mathrm{h.c.}\right)\\
&+\lambda_A|A|^4+\lambda_B|B|^4+\lambda_{AB}|A|^2|B|^2\\
&+(H^\dagger H)(\lambda_{HA}|A|^2+\lambda_{HB}|B|^2).
\end{aligned}
\]

Nonzero \(\mu_A\) and \(\mu_B\) are important: without them, the renormalizable potential has the larger accidental symmetry \(U(1)_A\times U(1)_B\). The two cubics reduce this to the intended \(Z_3\times Z_3\).

---

## Document D — Complete distinguishing operator table

The enumerator treats Hermitian-conjugate pairs as one operator class. It finds 3 projected-\(Z_3\)-invariant quadratic, 4 cubic, and 6 quartic nonderivative classes. The six comparator-only nonderivative classes are exactly those shown below.

| Operator class | Dimension | Generic \(Z_3^{(P)}\) | Exact TP-D | Consequence if present |
|---|---:|:---:|:---:|---|
| \(\partial A^\dagger\partial B+\mathrm{h.c.}\) | 4 | allowed | forbidden | kinetic flavour mixing |
| \(A^\dagger B+\mathrm{h.c.}\) | 2 | allowed | forbidden | mass mixing and oscillation |
| \(A^2B+\mathrm{h.c.}\) | 3 | allowed | forbidden | conversion/decay vertices |
| \(AB^2+\mathrm{h.c.}\) | 3 | allowed | forbidden | conversion/decay vertices |
| \(|A|^2A^\dagger B+\mathrm{h.c.}\) | 4 | allowed | forbidden | flavour-changing scattering |
| \(|B|^2A^\dagger B+\mathrm{h.c.}\) | 4 | allowed | forbidden | flavour-changing scattering |
| \((A^\dagger B)^2+\mathrm{h.c.}\) | 4 | allowed | forbidden | pair conversion |
| \((H^\dagger H)A^\dagger B+\mathrm{h.c.}\) | 4 | allowed | forbidden | Higgs-mediated transition/decay |

The common nonderivative classes are

\[
|A|^2,\ |B|^2,\ A^3+\mathrm{h.c.},\ B^3+\mathrm{h.c.},\
|A|^4,\ |B|^4,\ |A|^2|B|^2.
\]

The Standard-Model Higgs adds the common portals \((H^\dagger H)|A|^2\) and \((H^\dagger H)|B|^2\). No renormalizable linear singlet portal is allowed because \(A\) and \(B\) have nonzero projected charge.

The enumeration is exhaustive for nonderivative monomials in two commuting complex singlets through dimension four. Gauge-field and Standard-Model-only operators are common to both theories and cancel from the comparator.

Therefore

\[
\Delta\mathcal L
=\mathcal L_{Z_3}^{\rm generic}-\mathcal L_{\rm TP-D}
\]

is precisely the set of cross terms in the table, modulo field-basis normalization.

---

## Document E — Spectrum and mixing analysis

In the generic comparator, the quadratic matrix is

\[
M^2=\begin{pmatrix}
m_A^2&m_{AB}^2\\
m_{AB}^{2*}&m_B^2
\end{pmatrix}.
\]

After one relative rephasing makes \(m_{AB}^2\) real and nonnegative,

\[
m_\pm^2=\frac{m_A^2+m_B^2}{2}
\pm\frac12\sqrt{(m_B^2-m_A^2)^2+4|m_{AB}^2|^2},
\]

and

\[
\tan2\theta=\frac{2|m_{AB}^2|}{m_B^2-m_A^2}.
\]

For \(|m_{AB}^2|\ll|m_B^2-m_A^2|\),

\[
\theta\simeq\frac{|m_{AB}^2|}{m_B^2-m_A^2}.
\]

Exact TP-D enforces

\[
m_{AB}^2=0,\qquad \theta=0.
\]

The numerical diagonalization test agreed with the analytic eigenvalues to \(1.2\times10^{-10}\ \mathrm{GeV}^2\) for the stored test point; 100 randomized regression points passed.

### Oscillation statement

For coherent relativistic propagation in a broken model,

\[
P(A\to B;L)=\sin^2(2\theta)
\sin^2\!\left(\frac{\Delta m^2L}{4E}\right).
\]

In exact TP-D, \(P(A\to B;L)=0\). This is meaningful only if production and detection define the interaction basis and coherence is maintained. It must not be advertised as a generic prediction before an experimental realization is specified.

---

## Basis-invariance audit

The statement “the off-diagonal entry vanishes” is basis dependent. The physically invariant statement is that there exists a noncentral unitary matrix \(K\), with

\[
K^3=I,\qquad K\not\propto I,
\]

that leaves **every** coupling tensor invariant. For the quadratic tensor,

\[
K^\dagger M^2K=M^2.
\]

Under a basis transformation \(\Phi\to U\Phi\),

\[
M^2\to UM^2U^\dagger,\qquad K\to UKU^\dagger,
\]

so the existence of the symmetry is unchanged. One diagnostic is

\[
I_M(K)=\operatorname{Tr}\!\left[
(K^\dagger M^2K-M^2)^\dagger(K^\dagger M^2K-M^2)
\right].
\]

Exact invariance requires \(I_M=0\), together with analogous zero residuals for the cubic, quartic, and portal tensors.

A mass matrix by itself is insufficient: one can diagonalize any Hermitian matrix and invent a diagonal order-three matrix in that basis. The nontrivial test is whether the **same** \(K\) leaves all interaction tensors invariant. TP-D passes this simultaneous-tensor test by construction. The generic comparator does not pass it for generic coefficients.

The matrix element between nondegenerate charge eigenstates,

\[
\langle A;X_0|S|B\rangle,
\]

is an observable. If \([S,K]=0\) and \(X_0\) is kernel neutral, its initial and final kernel phases differ, forcing the amplitude to zero. That is the basis-independent content of the selection rule.

---

## Parameter-count audit

Shared Standard-Model parameters are omitted.

### Generic projected \(Z_3\)

After canonicalizing the kinetic term:

- Hermitian mass matrix: 4 real parameters;
- complex symmetric cubic rank-three tensor in two flavours: 8;
- Hermitian quartic tensor on \(\operatorname{Sym}^2(\mathbb C^2)\): 9;
- Hermitian Higgs-portal matrix: 4.

This gives 25 real coefficients. A common \(U(2)\) field-basis transformation removes four redundancies, leaving

\[
N_{\rm phys}^{Z_3}=21
\]

for a generic point with no accidental stabilizer.

### Exact TP-D

The exact dual potential has 2 real masses, 2 complex cubics, 3 real dark quartics, and 2 real diagonal Higgs portals: 11 real coefficients. Two independent field rephasings remove the two cubic phases, leaving

\[
N_{\rm phys}^{\rm TP-D}=9.
\]

Thus this realization removes twelve physical continuous parameters relative to the most general projected comparator:

\[
\Delta N_{\rm phys}=12.
\]

This is real parameter compression, but most of it consists of symmetry-protected zeros. No nonzero numerical sum rule has yet been derived.

---

## Document F — Vacuum and stability audit

The exact dark quartic is

\[
V_4=\lambda_A|A|^4+\lambda_B|B|^4+\lambda_{AB}|A|^2|B|^2.
\]

Its exact tree-level bounded-from-below conditions are

\[
\lambda_A>0,\qquad \lambda_B>0,\qquad
\lambda_{AB}>-2\sqrt{\lambda_A\lambda_B},
\]

with non-strict boundary variants requiring separate flat-direction analysis.

For one field, after minimizing its phase,

\[
V_i(r)=m_i^2r^2-\frac{2|\mu_i|}{3}r^3+\lambda_i r^4.
\]

The origin is no higher than every nonzero stationary point when

\[
|\mu_i|^2\le 9\lambda_i m_i^2.
\]

Therefore the following are simple sufficient conditions for the two-field origin to be the global minimum:

\[
\lambda_{AB}\ge0,\qquad
|\mu_A|^2\le9\lambda_A m_A^2,\qquad
|\mu_B|^2\le9\lambda_B m_B^2,
\]

in addition to positive masses and self-quartics. They are sufficient, not necessary. A negative portal requires a full mixed stationary-point analysis.

The stored benchmark

\[
(m_A,m_B,|\mu_A|,|\mu_B|)=(180,400,60,90)\ \mathrm{GeV},
\]

\[
(\lambda_A,\lambda_B,\lambda_{AB})=(0.20,0.25,0.10)
\]

passes these sufficient conditions. A deterministic 200,000-point log-radial numerical search with seed 20260915 found no negative value after phase minimization. This numerical scan corroborates the analytic sufficient proof; it is not the proof itself.

Higgs-portal terms shift the physical masses after electroweak symmetry breaking:

\[
M_A^2=m_A^2+\frac12\lambda_{HA}v^2,\qquad
M_B^2=m_B^2+\frac12\lambda_{HB}v^2.
\]

The full electroweak-plus-dark global-vacuum audit remains to be performed for a final phenomenology benchmark.

---

## Document G — High-energy unitarity audit

Writing

\[
A=(a_1+ia_2)/\sqrt2,\qquad B=(b_1+ib_2)/\sqrt2,
\]

the normalized ten-channel real-scalar quartic scattering matrix has eigenvalues

\[
2\lambda_A\quad(\times2),\qquad
2\lambda_B\quad(\times2),\qquad
\lambda_{AB}\quad(\times4),
\]

and

\[
2(\lambda_A+\lambda_B)
\pm\sqrt{4(\lambda_A-\lambda_B)^2+\lambda_{AB}^2}.
\]

With the convention \(a_0=-\Lambda/(16\pi)\), tree-level perturbative unitarity requires every eigenvalue \(\Lambda\) to satisfy

\[
|\Lambda|\le8\pi.
\]

For the stored benchmark the spectral radius is 1.041421356, far below \(8\pi\). The analytic spectrum was verified against the directly constructed \(10\times10\) tensor matrix at 100 randomized coupling points with relative and absolute tolerances \(10^{-12}\).

**Scope limitation:** this is the high-energy dark-scalar quartic limit. A final benchmark still requires Higgs/Goldstone channels and finite-energy exchange diagrams with pole excision. Thus the complete finite-energy unitarity item is open.

---

## Document H — Radiative-stability audit

Every exact-TP-D vertex has total vector charge \((0,0)\). Charge adds at internal contractions, so every perturbative diagram with external legs of nonzero total vector charge vanishes. Equivalently, a symmetry-preserving regulator and subtraction scheme produce a renormalized effective action satisfying

\[
\Gamma[\omega A,B]=\Gamma[A,B],\qquad
\Gamma[A,\omega B]=\Gamma[A,B].
\]

Consequently no counterterm proportional to

\[
A^\dagger B,\quad A^2B,\quad AB^2,
\quad |A|^2A^\dagger B,\quad |B|^2A^\dagger B,
\quad(A^\dagger B)^2,
\quad(H^\dagger H)A^\dagger B
\]

can be generated while the full symmetry is exact. In particular,

\[
\left.\beta_{m_{AB}^2}\right|_{\text{all kernel-breaking spurions}=0}=0.
\]

This conclusion holds to all perturbative orders. The scalar-only model has no chiral gauge anomaly. A parent gauge completion containing chiral fermions would require a separate continuous and residual-discrete anomaly audit.

### Controlled breaking TP-B

Introduce a scalar spurion/field

\[
\Sigma\sim(1,2),\qquad q_P(\Sigma)=0.
\]

A vacuum expectation value \(\langle\Sigma\rangle=w/\sqrt2\) preserves the diagonal projected subgroup but breaks the kernel symmetry. The renormalizable term

\[
\mu_\Sigma\Sigma A^\dagger B+\mathrm{h.c.}
\]

generates

\[
m_{AB}^2=\frac{\mu_\Sigma w}{\sqrt2}.
\]

Similarly, \(\Sigma A^2B\) and \(\Sigma^\dagger AB^2\) generate mixed cubics linearly in \(w\). Off-diagonal kinetic, quartic, and Higgs-portal terms arise through dimension-five operators and scale as \(w/\Lambda\) in the minimal EFT. Hence

\[
\theta\sim\frac{\mu_\Sigma w}{\sqrt2\,(m_B^2-m_A^2)},
\qquad
\Gamma_{K\text{-violating}}\propto w^2
\]

at leading order, provided no lower-order breaking source exists. The coefficients remain independent Wilson coefficients; symmetry alone does not give a numerical sum rule among them.

---

## Document I — Minimal falsification benchmark

Take the illustrative masses

\[
M_A=180\ \mathrm{GeV},\qquad M_B=400\ \mathrm{GeV},\qquad
m_h=125.25\ \mathrm{GeV},
\]

so \(B\to A+h\) is kinematically open. In the generic comparator, after electroweak symmetry breaking,

\[
(H^\dagger H)A^\dagger B+\mathrm{h.c.}
\supset \lambda_{HAB}v\,hA^\dagger B+\mathrm{h.c.}
\]

and

\[
\Gamma(B\to Ah)=
\frac{|\lambda_{HAB}v|^2}{16\pi M_B}
\lambda^{1/2}\!\left(1,\frac{M_A^2}{M_B^2},\frac{m_h^2}{M_B^2}\right).
\]

For the purely illustrative comparator value \(\lambda_{HAB}=0.01\), the stored calculation gives

\[
\Gamma_{Z_3}(B\to Ah)=1.93024\times10^{-4}\ \mathrm{GeV},
\]

whereas exact TP-D gives zero.

This number is not a TP prediction; \(\lambda_{HAB}=0.01\) was chosen only to display an effect size. The robust prediction is the exact zero.

### Falsification card

Under the assumptions that:

1. the observed states are the two nondegenerate TP-D charge eigenstates;
2. the visible final state is kernel neutral;
3. no explicit or spontaneous kernel breaking occurs;
4. the tested decay is kinematically allowed;

then

> **Any statistically significant nonzero \(B\to A+h\) amplitude falsifies exact minimal TP-D.**

A null result does not prove TP-D because the generic comparator may set \(\lambda_{HAB}=0\) accidentally. Positive model identification would require observing both species and enough independent allowed and forbidden channels to infer the extra conserved charge.

---

## Document J — Preliminary novelty matrix

| Feature | Generic single \(Z_3\) | Established enlarged discrete models | TP-D result | Novelty status |
|---|---|---|---|---|
| residual charge-one fields | yes | yes | yes | known |
| cubic \(Z_3\) self-interactions | yes | yes | \(A^3,B^3\) | known |
| semi-annihilation | yes | yes | allowed within each sector | known |
| multiple stable species | possible | established | natural if each is lightest in its vector-charge sector | known mechanism |
| extra conserved kernel charge | no | yes for product groups | yes | known group mechanism |
| forbidden \(A^\dagger B\) | not generic | common when charges differ under extra factor | yes | known selection-rule consequence |
| all-orders null \(B\to A+X_0\) | not generic | standard consequence of an exact extra charge | yes | known mechanism, TP-specific labeling |
| \(q_P=q_m+q_E\) projection | optional relabeling | homomorphisms are standard | central organizing map | known mathematics; combination-specific |
| nonzero numerical sum rule | none required | model dependent | none found | absent |
| unique experimental signature | no | model dependent | not yet demonstrated | open |

Relevant prior work already establishes the nearby physics:

- G. Bélanger, K. Kannike, A. Pukhov, and M. Raidal, [“Impact of semi-annihilations on dark matter phenomenology—an example of \(Z_N\)-symmetric scalar dark matter”](https://arxiv.org/abs/1202.2962), develops discrete-charge operator selection, semi-annihilation, and enlarged-symmetry multicomponent sectors.
- P. Ko and Y. Tang, [“Self-interacting scalar dark matter with local \(Z_3\) symmetry”](https://arxiv.org/abs/1402.6449), realizes local \(Z_3\) as a remnant of a broken dark \(U(1)\).
- C. E. Yaguna and Ó. Zapata, [“Multi-component scalar dark matter from a \(Z_N\) symmetry: a systematic analysis”](https://arxiv.org/abs/1911.05515), shows that multiple stable scalar species and nontrivial conversion patterns already arise in established discrete-symmetry models.
- D. Borah, E. Ma, and D. Nanda, [“Dark \(SU(2)\to Z_3\times Z_2\) Gauge Symmetry”](https://arxiv.org/abs/2212.11847), is a concrete example of product residual discrete symmetry used to organize multiple dark states.

Therefore the present construction has **not** passed a claim of demonstrable literature novelty. Its defensible contribution at this checkpoint is a precise TP-specific formulation and comparator audit, not discovery of product-discrete dark matter.

---

## Document K — Gate report

### 1. Executive verdict

\[
\boxed{\text{SUBSTANTIVE PARTIAL PASS}}
\]

### 2. What survived

- The projection has a nontrivial three-element kernel.
- The minimal two-field representation makes the kernel act nontrivially.
- The complete renormalizable operator basis differs from the generic projected-\(Z_3\) basis.
- The distinction is expressible as a basis-invariant symmetry of all coupling tensors.
- Kernel-changing amplitudes vanish to all perturbative orders in the exact model.
- A healthy inert tree-level benchmark exists under explicit sufficient conditions.
- The dark-scalar high-energy unitarity matrix is perturbative at that benchmark.
- Exact TP-D removes twelve physical continuous parameters relative to the generic comparator under the stated counting assumptions.

### 3. What failed or remains incomplete

- No unique nonzero numerical relation or sum rule has been found.
- A null transition is not positive evidence because generic \(Z_3\) can tune the corresponding coupling to zero.
- The core group and its selection-rule mechanism are already known mathematics and model-building technology.
- Full electroweak-plus-dark vacuum analysis is unfinished.
- Full finite-energy scalar/Higgs/Goldstone/gauge unitarity is unfinished.
- The complete one-loop RGE system for TP-D has not yet been independently regenerated, although the forbidden-operator surface is protected exactly by symmetry.
- No relic-density, collider-production, detector-background, or global-likelihood analysis has yet established practical accessibility.
- A gauge-origin and anomaly-free completion has not yet been constructed.

### 4. What is genuinely new

No element is yet demonstrably new after literature comparison. The potentially original contribution is the **specific interpretation and systematic use of the projection/kernel pair as the defining TP architecture**, together with a future overconstrained observable pattern. That claim remains “known ingredients, newly combined” until a broader search and a distinctive prediction succeed.

### 5. What is known physics

Finite Abelian product groups, residual discrete symmetries, multicomponent stable sectors, cubic \(Z_3\) interactions, semi-annihilation, symmetry-protected coupling zeros, and forbidden-transition null tests are known.

### 6. First distinctive prediction

For exact minimal TP-D,

\[
\boxed{\mathcal M(B\to A+X_0)=0}
\]

whenever \(X_0\) is kernel neutral. This differs from the generic single-\(Z_3\) theory, which allows the amplitude.

### 7. Experimental falsification condition

Observation of any kernel-changing transition, such as \(B\to A+h\), excludes exact TP-D under the explicit four assumptions in the falsification card.

### 8. Remaining blockers, ranked

1. **Critical:** find an identifiable pattern or nonzero relation that generic \(Z_3\) cannot imitate by tuning.
2. **Critical:** establish production and detection channels for both charge eigenstates.
3. **High:** complete current-data phenomenology and coupled relic-density analysis.
4. **High:** finish electroweak vacuum and finite-energy unitarity audits.
5. **High:** independently derive the full TP-D one-loop RGEs.
6. **Medium:** construct and audit a minimal residual-gauge completion.
7. **Medium:** complete a systematic prior-art search for the exact operator basis and signature.

### 9. Confidence assessment

| Domain | Confidence | Reason |
|---|---|---|
| finite-group and operator algebra | high | exhaustive enumeration plus analytic charge proof |
| mass and basis analysis | high | exact formulas and randomized numerical cross-checks |
| tree-level dark vacuum | medium-high | exact BFB and sufficient global-origin proof; not full Higgs system |
| high-energy dark-scalar unitarity | high within stated scope | direct tensor construction and randomized spectral test |
| all-orders selection-rule protection | high | exact finite symmetry and scalar-only anomaly status |
| phenomenology | low-medium | one illustrative decay; no production/global constraint study |
| novelty | low | nearby mechanisms are established; exact combination not exhaustively searched |
| experimental accessibility | low-medium | possible in principle, no detector-level analysis |

### 10. Recommendation

\[
\boxed{\text{Continue TP-D conditionally; do not promote it beyond a }Z_3\times Z_3\text{ EFT.}}
\]

The immediate next objective is not gravity or grand unification. It is to construct a minimal visible/dark portal with more measured quantities than free parameters and search for a correlated set of kernel-conserving and kernel-violating rates. If no such overconstrained pattern exists, TP-D remains a valid conventional product-discrete EFT rather than a new theoretical framework.

---

## Reproducibility record

- Operator enumerator: `code/dual_tp_operator_enumerator.py`
- Machine-readable operator basis: `audits/dual_tp_operator_basis.json`
- Vacuum, spectrum, unitarity, and decay validator: `code/dual_tp_validation.py`
- Machine-readable numerical output: `audits/dual_tp_validation.json`
- Regression tests: `code/test_dual_tp.py`
- Test result: 5/5 passed on 15 September 2026.

The numerical vacuum scan used NumPy 2.3.5, 200,000 samples, seed 20260915, and log-uniform radial sampling. The analytic inequalities, not the scan, establish the stated sufficient vacuum result.


\newpage

## S4 Ternary Polarity checkpoint 6

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


\newpage

## S5 Ternary Polarity checkpoint 7

## Dimensionful one-loop RGEs, portal trade-off, and preliminary metastability

**Research status:** internal technical audit  
**Theory version:** TP-D v0.1, with v0.2 update recommended  
**Date:** 19 September 2026  
**Epistemic level:** exact scalar one-loop derivations; model-dependent running; leading-only metastability diagnostic

## Executive verdict

The dimensionful scalar one-loop system has been derived twice and agrees exactly. The dual \(Z_3\times Z_3\) cubic structure is preserved: no forbidden mixed mass or mixed cubic is generated when the symmetry is exact.

The running analysis exposes a real tension:

- weak Higgs portals leave the Higgs quartic negative above approximately \(3.57\times10^8\,\mathrm{GeV}\);
- stronger equal portals can keep all quartics bounded, but their mass-weighted contributions drive the running Higgs quadratic parameter through zero around \(2.31\times10^8\,\mathrm{GeV}\);
- an asymmetric portal concentrated on the lighter species substantially improves this trade-off, reaching approximately \(1.46\times10^{15}\,\mathrm{GeV}\) before the simple inert-vacuum certificate fails;
- the best scanned asymmetric point is near-critical and therefore not robust against omitted higher-order and threshold corrections.

The leading quartic-bounce estimate suggests that B0 is long-lived inside the declared perturbative interval. This is **not** a precision lifetime calculation because the most negative quartic occurs at the cutoff, not at a controlled stationary bounce scale.

## 1. Dimensionful normalization

The canonical potential contains

\[
V\supset -\mu_H^2 H^\dagger H+m_A^2|A|^2+m_B^2|B|^2
+\left(\frac{\mu_A}{3}A^3+\frac{\mu_B}{3}B^3+\mathrm{h.c.}\right).
\]

Independent rephasings choose the cubic terms to be negative along the phase-minimized positive radial directions. For

\[
A=\frac{A_1+iA_2}{\sqrt2},
\]

the convention used by the tensor calculation is

\[
V_A^{(3)}=-\frac{k_A}{3}A_1^3+k_AA_1A_2^2,
\qquad k_A=\frac{|\mu_A|}{\sqrt2},
\]

and similarly for \(B\). This differs from the common literature convention \(\mu_3(S^3+S^{\dagger3})/2\); the conversion is \(\mu_3=2\mu_A/3\). The distinction is purely normalization and must be retained when importing published bounds [Bel12, Hek19].

## 2. Independent derivations

The complete eight-real-scalar potential was evaluated in two ways.

### Method A — one-loop effective-potential divergence

The scalar contribution to the one-loop beta-potential numerator was extracted from

\[
\frac12\operatorname{Tr}\!\left[(V'')^2\right].
\]

Coefficients of quadratic, cubic, and quartic field monomials were projected onto the canonical parameters.

### Method B — general tensor contractions

For

\[
V=\frac12m^2_{ab}\phi_a\phi_b+rac1{3!}h_{abc}\phi_a\phi_b\phi_c
+\frac1{4!}\lambda_{abcd}\phi_a\phi_b\phi_c\phi_d,
\]

the pure-scalar one-loop relations are

\[
(16\pi^2)\beta_{m^2_{ab}}
=\lambda_{abef}m^2_{ef}+h_{aef}h_{bef},
\]

\[
(16\pi^2)\beta_{h_{abc}}
=\lambda_{abef}h_{cef}+\lambda_{acef}h_{bef}+\lambda_{bcef}h_{aef}.
\]

These agree with the general formulas of Luo, Wang, and Xiao, including the permutation normalization [Luo02b]. The two in-project implementations agree coefficient by coefficient using exact rational arithmetic.

## 3. Scalar-only dimensionful beta functions

With \(\beta_x=dx/d\ln\mu\), the exact scalar contributions are

\[
\begin{aligned}
16\pi^2\beta_{\mu_H^2}^{\rm scalar}
={}&12\lambda_H\mu_H^2-2\lambda_{HA}m_A^2-2\lambda_{HB}m_B^2,\\
16\pi^2\beta_{m_A^2}^{\rm scalar}
={}&8\lambda_A m_A^2+2\lambda_{AB}m_B^2-4\lambda_{HA}\mu_H^2+4|\mu_A|^2,\\
16\pi^2\beta_{m_B^2}^{\rm scalar}
={}&8\lambda_B m_B^2+2\lambda_{AB}m_A^2-4\lambda_{HB}\mu_H^2+4|\mu_B|^2,\\
16\pi^2\beta_{\mu_A}^{\rm scalar}
={}&12\lambda_A\mu_A,\\
16\pi^2\beta_{\mu_B}^{\rm scalar}
={}&12\lambda_B\mu_B.
\end{aligned}
\]

The Standard Model gauge and third-family Yukawa contribution added to the first equation is

\[
\mu_H^2\left[2(3y_t^2+3y_b^2+y_\tau^2)-\frac92g_2^2-\frac32g_1^2\right].
\]

The scalar quartic beta functions remain those independently verified in checkpoint 6.

### Symmetry preservation

The alternative \(A_1A_2^2\) and \(B_1B_2^2\) tensor projections yield the same cubic beta functions as the \(A_1^3\) and \(B_1^3\) projections. Thus the exact \(Z_3\) cubic tensors retain their required ratios. Because every retained vertex is neutral under both discrete factors, mixed bilinears and mixed cubics remain absent to all perturbative orders.

## 4. Running certificates

The one-loop integration now stops at the first \(4\pi\) dimensionless-coupling boundary instead of continuing into numerical blow-up. It monitors:

- exact three-field copositivity;
- \(\mu_H^2>0\), \(m_A^2>0\), and \(m_B^2>0\);
- nonnegative portal quartics for the analytic sufficient proof;
- \(9\lambda_A m_A^2-|\mu_A|^2\ge0\);
- \(9\lambda_B m_B^2-|\mu_B|^2\ge0\);
- the complete high-energy scalar-unitarity eigenvalue.

These running inequalities are diagnostics constructed from the RG-improved tree potential. At finite perturbative order they are not themselves scale-independent observables.

### B0 — weak portals

\[
(\lambda_{HA},\lambda_{HB})=(0.020,0.030).
\]

The interpolated first BFB failure is

\[
\mu_{\rm BFB}=3.5707\times10^8\,\mathrm{GeV}.
\]

All mass and cubic sufficient-condition margins remain positive up to the later perturbative boundaries. Therefore the first B0 failure is specifically the negative Higgs quartic, not a dark tachyon or cubic-induced dark minimum.

### B1 — equal stabilizing portals

\[
(\lambda_{HA},\lambda_{HB})=(0.18,0.18).
\]

The quartic potential remains copositive over the scanned perturbative interval, but

\[
\mu_H^2(\mu)=0
\quad\text{at}\quad
\mu\simeq2.3054\times10^8\,\mathrm{GeV}.
\]

This does not prove vacuum decay. It means the simple all-scale analytic certificate derived for a negative Higgs quadratic term no longer applies. The result also quantifies a hierarchy/naturalness tension: the same portal terms that raise \(\beta_{\lambda_H}\) contribute negatively to \(\beta_{\mu_H^2}\), weighted by \(m_A^2\) and \(m_B^2\).

### B2 — asymmetric diagnostic branch

The beta function of the Higgs quartic depends on

\[
\lambda_{HA}^2+\lambda_{HB}^2,
\]

whereas the portal contribution to the Higgs quadratic beta function is weighted approximately by

\[
\lambda_{HA}m_A^2+\lambda_{HB}m_B^2.
\]

At fixed stabilizing quartic norm, concentrating the portal on the lighter state reduces the mass-weighted correction. The diagnostic point

\[
(\lambda_{HA},\lambda_{HB})=(0.2385,0)
\]

has no BFB failure before its perturbative boundary and retains the sufficient inert certificate until

\[
\mu\simeq1.4624\times10^{15}\,\mathrm{GeV}.
\]

Its scalar-unitarity and \(4\pi\) boundaries are approximately

\[
\mu_U=2.1555\times10^{15}\,\mathrm{GeV},
\qquad
\mu_{4\pi}=4.0470\times10^{15}\,\mathrm{GeV}.
\]

However, its minimum BFB margin is only

\[
3.3\times10^{-6}.
\]

The point is therefore near-critical and highly sensitive to threshold matching, two-loop terms, and input uncertainties. B2 is not promoted to a phenomenological benchmark.

## 5. Sparse portal scan

For equal portals between \(0.02\) and \(0.22\), increasing the portal first postpones the Higgs-quartic zero, then makes the Higgs quadratic sign change the earlier failure. At the fixed masses and self-couplings used here, the largest reach occurs near the crossover rather than at the largest portal.

An asymmetric scan confirms that the lighter-state portal performs substantially better. This is a model-building result, but not a universal theorem: changing dark masses, self-couplings, cubic terms, or adding threshold matching changes the optimum.

## 6. Leading metastability diagnostic

For a negative quartic potential, the leading Fubini action is

\[
S_4\simeq\frac{8\pi^2}{3|\lambda_H(\mu)|},
\]

with a rough expected-event exponent

\[
\ln N_{\rm decay}\sim4\ln(T_U\mu)-S_4.
\]

This approximation and its limitations are standard in electroweak-vacuum analyses [Isi01, Esp20].

For B0, restricting the calculation to the interval below the first scalar-unitarity boundary gives

\[
\lambda_{H,\min}=-0.027390,
\qquad
S_4\simeq960.9,
\qquad
\log_{10}N_{\rm decay}\sim-188.7.
\]

This leading diagnostic is compatible with a very long-lived vacuum. It is not a controlled lifetime prediction because:

1. the minimum occurs at the declared cutoff endpoint;
2. \(\beta_{\lambda_H}\ne0\) there, so the calculation has not selected a stationary bounce scale;
3. two-loop running, threshold matching, fluctuation determinants, gauge-consistent effective couplings, gravity, higher-dimensional operators, and multi-field bounces are absent.

B1 and B2 keep \(\lambda_H\ge0\) inside their declared perturbative intervals, so this particular negative-quartic bounce is absent there. That does not replace a complete multi-field vacuum analysis.

## 7. Referee attack and classification

| Question | Result | Classification |
|---|---|---|
| Scalar mass RGEs | Two exact methods agree | Derived |
| Scalar cubic RGEs | Two exact methods agree | Derived |
| Preservation of each \(Z_3\) cubic tensor | Verified | Derived |
| B0 absolute BFB at all scales | Fails near \(3.57\times10^8\) GeV | Negative model result |
| B0 lifetime | Leading diagnostic appears safe | Provisional; UV sensitive |
| B1 quartic stability | Passes to perturbative boundary | Model-dependent |
| B1 inert-vacuum certificate | Fails via \(\mu_H^2=0\) | Certificate failure, not proven decay |
| B2 improved scale reach | Reaches \(1.46\times10^{15}\) GeV | Near-critical diagnostic |
| Threshold-matched running | Not done | Open |
| Two-loop uncertainty | Not done | Open |
| Full Coleman–Weinberg/multi-field bounce | Not done | Open |
| Gauge-origin contributions | Undefined until TP-G is specified | Blocked by model choice |

## 8. Consequences for the theory programme

1. TP-D remains a consistent low-energy scalar EFT branch.
2. B0 should be described as metastability-compatible at leading order, not absolutely stable to high scales.
3. B1 should not be advertised as a clean solution to vacuum stability; it trades the quartic problem for a quadratic-parameter problem.
4. B2 demonstrates a repair mechanism through asymmetric portals but is too close to criticality to be trusted without higher-order work.
5. None of these results produces a TP-specific observable or proves novelty beyond known product-discrete scalar models.
6. A gauge-complete unitarity/anomaly audit cannot begin until the parent gauge field content and chiral charge assignments are frozen.

## 9. Reproducibility

- `code/tpd_dimensionful_rge.py`
- `code/tpd_full_rge_running.py`
- `code/tpd_portal_tradeoff_scan.py`
- `code/tpd_metastability_diagnostic.py`
- `code/test_tpd_phase3.py`
- `audits/tpd_dimensionful_rge.json`
- `audits/tpd_full_rge_B0.json`
- `audits/tpd_full_rge_B1.json`
- `audits/tpd_full_rge_B2.json`
- `audits/tpd_full_rge_convergence.json`
- `audits/tpd_portal_tradeoff_scan.json`
- `audits/tpd_metastability_diagnostic.json`

Thirteen automated regression tests pass at this checkpoint.

## Literature keys

- [Luo02b] M. Luo, H. Wang, and Y. Xiao, *Physical Review D* **67**, 065019 (2003), DOI 10.1103/PhysRevD.67.065019.
- [Bel12] G. Bélanger et al., *JCAP* **2013**(01), 022, DOI 10.1088/1475-7516/2013/01/022.
- [Hek19] A. Hektor, A. Hryczuk, and K. Kannike, *JHEP* **03** (2019) 204, DOI 10.1007/JHEP03(2019)204.
- [Isi01] G. Isidori, G. Ridolfi, and A. Strumia, *Nuclear Physics B* **609**, 387–409 (2001), DOI 10.1016/S0550-3213(01)00302-9.
- [Esp20] J. R. Espinosa, *JCAP* **2020**(06), 052, DOI 10.1088/1475-7516/2020/06/052.


\newpage

## S6 Ternary Polarity checkpoint 8

## Minimal gauge origin, anomaly audit, parent vacuum, and enlarged scalar unitarity

**Research status:** internal technical audit  
**Theory version:** TP-G0, a candidate parent of TP-D v0.2  
**Date:** 19 September 2026  
**Epistemic level:** explicit model construction; model-dependent benchmark; phenomenology incomplete

## Executive verdict

A minimal scalar-only gauge parent exists:

\[
U(1)_m\times U(1)_E
\longrightarrow Z_3^{(m)}\times Z_3^{(E)}.
\]

It uses two charge-three Higgs fields and reproduces the exact low-energy TP-D charges and cubic interactions. Because no chiral fermion carries either new charge, all continuous gauge, mixed-gauge, and gauge-gravitational anomaly coefficients vanish trivially.

An explicit benchmark, TP-G0, has:

- a certified global tree-level vacuum in its factorized parameter slice;
- positive gauge kinetic terms;
- two massive vectors, two radial modes, and the intended inert \(A,B\) spectrum;
- a complete 78-channel scalar/Goldstone quartic matrix satisfying high-energy tree unitarity.

This is a **conditional pass for existence of a gauge origin**, not a complete UV completion. The parent is a conventional product-Abelian residual-discrete construction, introduces many new parameters, permits three Abelian kinetic mixings, produces local cosmic strings, and has not passed full threshold RG, finite-energy vector scattering, collider, precision, or cosmological tests.

The standalone TP-D high-scale running cannot be imported into TP-G0.  The
radial modes and new vectors enter near \(0.63\) and \(0.90\,\mathrm{TeV}\),
respectively, so the beta functions change above those thresholds.  All TP-D
numbers at (10^8!-!10^{15}\,\mathrm{GeV}) remain conditional results for an
EFT in which no such low-scale parent states have appeared; they are not
predictions of TP-G0.

## 1. Frozen parent field content

\[
G_{\rm parent}=G_{\rm SM}\times U(1)_m\times U(1)_E.
\]

| Field | \(Q_m\) | \(Q_E\) | Role |
|---|---:|---:|---|
| \(\Phi_m\) | 3 | 0 | breaks \(U(1)_m\) to \(Z_3^{(m)}\) |
| \(\Phi_E\) | 0 | 3 | breaks \(U(1)_E\) to \(Z_3^{(E)}\) |
| \(A\) | 1 | 0 | low-energy \((1,0)\) state |
| \(B\) | 0 | 1 | low-energy \((0,1)\) state |

All four fields are complex Lorentz scalars and Standard-Model singlets. Standard-Model fermions and the Higgs doublet are neutral under the two new factors.

The covariant derivatives include

\[
D_\mu\Phi_m=(\partial_\mu+3ig_mX^m_\mu)\Phi_m,
\qquad
D_\mu A=(\partial_\mu+ig_mX^m_\mu)A,
\]

and the analogous \(E\) expressions.

## 2. Residual group

Let

\[
\langle\Phi_m\rangle=\frac{f_m}{\sqrt2},
\qquad
\langle\Phi_E\rangle=\frac{f_E}{\sqrt2}.
\]

Vacuum-preserving gauge transformations satisfy

\[
e^{3i\alpha_m}=e^{3i\alpha_E}=1.
\]

Therefore

\[
\alpha_m=\frac{2\pi n_m}{3},\qquad
\alpha_E=\frac{2\pi n_E}{3},
\]

with \(n_m,n_E\in\{0,1,2\}\). The surviving nine transformations form

\[
Z_3^{(m)}\times Z_3^{(E)},
\]

acting on \(A\) and \(B\) exactly as in TP-D. This is the standard residual-discrete gauge mechanism [Kra89, Ban10].

## 3. Complete renormalizable scalar operator basis

Define

\[
\mathcal S=\{\Phi_m,\Phi_E,A,B\}.
\]

The general gauge-invariant scalar potential contains:

1. one quadratic modulus for every \(S_i\in\mathcal S\);
2. one self-quartic \(|S_i|^4\) for every field;
3. all six pairwise modulus quartics \(|S_i|^2|S_j|^2\);
4. four Higgs portals \((H^\dagger H)|S_i|^2\);
5. the two phase-sensitive structures

\[
\kappa_m\Phi_m^\dagger A^3+\mathrm{h.c.},
\qquad
\kappa_E\Phi_E^\dagger B^3+\mathrm{h.c.}.
\]

No gauge-invariant scalar monomial of engineering dimension one or three exists. Exhaustive enumeration found four quadratic monomials and fourteen degree-four monomials when Hermitian-conjugate phase-sensitive terms are counted separately.

After symmetry breaking,

\[
\frac{\kappa_m f_m}{\sqrt2}A^3+\mathrm{h.c.}
=\frac{\mu_A}{3}A^3+\mathrm{h.c.},
\]

so

\[
\mu_A=\frac{3\kappa_m f_m}{\sqrt2},
\qquad
\mu_B=\frac{3\kappa_E f_E}{\sqrt2}.
\]

The low-energy cubic is therefore matched rather than inserted by hand.

## 4. Gauge kinetic mixing correction

The most general Abelian kinetic sector includes

\[
-\frac14F_Y^2-\frac14F_m^2-\frac14F_E^2
-\frac{\epsilon_{Ym}}2F_YF_m
-\frac{\epsilon_{YE}}2F_YF_E
-\frac{\epsilon_{mE}}2F_mF_E.
\]

Omitting the two hypercharge mixings would be inconsistent with the most-general-action rule. Kinetic mixing is a standard allowed interaction between Abelian factors [Hol86].

In the frozen scalar-only charge assignment,

\[
\operatorname{Tr}(YQ_m)=\operatorname{Tr}(YQ_E)
=\operatorname{Tr}(Q_mQ_E)=0,
\]

because no field carries both relevant charges. Thus zero mixing has no one-loop matter source. It is not enforced by the gauge group itself. The TP-G0 zero-mixing slice additionally imposes independent charge-conjugation automorphisms \(C_m\) and \(C_E\), under which \(X^m_\mu\) or \(X^E_\mu\) changes sign and the corresponding charged scalars are conjugated. With real scalar couplings, these symmetries protect all new-sector kinetic mixings from perturbative generation.

Without those extra automorphisms, all three \(\epsilon\)'s are independent parameters and must be constrained experimentally.

## 5. Gauge spectrum

When hypercharge mixing vanishes, the unmixed masses are

\[
M_m^2=9g_m^2f_m^2,
\qquad
M_E^2=9g_E^2f_E^2.
\]

For nonzero \(\epsilon_{mE}=\epsilon\), canonical normalization gives

\[
M_\pm^2=
\frac{M_m^2+M_E^2\pm
\sqrt{(M_m^2-M_E^2)^2+4\epsilon^2M_m^2M_E^2}}
{2(1-\epsilon^2)}.
\]

The kinetic matrix requires \(|\epsilon|<1\) on this two-factor slice. A 500-point numerical generalized-eigenvalue check reproduced the analytic formula to maximum relative error \(8.3\times10^{-14}\).

The phases of \(\Phi_m\) and \(\Phi_E\) are eaten. Two physical radial modes remain.

## 6. Anomaly audit

Gauge anomalies receive contributions from chiral fermions, not scalars. TP-G0 contains no fermion charged under either new \(U(1)\), while all Standard-Model chiral fermions are neutral. Consequently,

\[
[U(1)_m]^3=[U(1)_E]^3=0,
\]

all mixed Abelian coefficients vanish, all mixed Standard-Model coefficients vanish, and both gravitational-\(U(1)\) coefficients vanish.

The continuous parent is therefore anomaly-free in this restricted field content, and its residual discrete subgroup inherits a consistent gauge origin. This result does **not** survive automatically if chiral portal matter or Standard-Model charges are added; every such extension requires a new audit [Iba91].

## 7. TP-G0 benchmark

Choose

\[
f_m=f_E=1\,\mathrm{TeV},qquad
g_m=g_E=0.30,qquad
\lambda_{\Phi_m}=\lambda_{\Phi_E}=0.20,
\]

with the B0 low-energy quartics and masses. Set the other modulus portals and all kinetic mixings to zero on the charge-conjugation-symmetric slice. Cubic matching fixes

\[
\kappa_m=0.0282843,qquad
\kappa_E=0.0424264.
\]

The tree spectrum is

\[
m_{\rho_m}=m_{\rho_E}=632.46\,\mathrm{GeV},
\qquad
M_m=M_E=900\,\mathrm{GeV},
\]

plus \(M_A=180\,\mathrm{GeV}\), \(M_B=400\,\mathrm{GeV}\), and the Standard-Model-like Higgs.

### Parent BFB and global vacuum

For either \((\Phi,A)\) sector with vanishing modulus portal, the phase-minimized quartic along \(t=|\Phi|/|A|\) is proportional to

\[
f_4(t)=\lambda_\Phi t^4+\lambda_A-2|\kappa|t.
\]

Its minimum occurs at

\[
t_*=\left(\frac{|\kappa|}{2\lambda_\Phi}\right)^{1/3},
\]

with margin

\[
f_4(t_*)=\lambda_A-\frac32|\kappa|t_*.
\]

The TP-G0 margins are \(0.18246\) and \(0.21988\), respectively.

Interior stationary points with dark radial value \(a>0\) reduce to positive roots of

\[
4\lambda_\Phi M(x)
\left[4M(x)^2-9\kappa^2f^2x\right]
-27\kappa^4x^3=0,
\]

where \(x=a^2\) and \(M(x)=m_A^2+\lambda_Ax\). Both benchmark polynomials have no positive real root. Boundary directions and infinity are positive, so each factorized sector has its global minimum at \((|\Phi|,|A|)=(f/\sqrt2,0)\) in complex-field notation. Nonnegative \(H\)-\(A\), \(H\)-\(B\), and \(A\)-\(B\) portals complete the benchmark global-vacuum certificate.

The proof applies to this factorized parameter slice. The zero modulus portals are not claimed to form a closed RG surface.

## 8. Enlarged high-energy scalar matrix

The parent contains twelve real scalar components and 78 normalized two-particle channels. The complete scalar-potential quartic tensor includes the phase-sensitive \(\kappa_m\Phi_m^\dagger A^3\) and \(\kappa_E\Phi_E^\dagger B^3\) interactions.

For TP-G0,

\[
\max|\Lambda|=1.05056,
\qquad
\max|a_0|=0.0209001,
\]

well below \(|\operatorname{Re}a_0|\le1/2\). The 36-channel \(H+A+B\) principal submatrix reproduces the independent low-energy generator exactly.

This is a scalar/Goldstone quartic result. Gauge exchanges, transverse vectors, finite-energy diagrams, and nonzero kinetic mixing remain outside it.

## 9. Topological defects

Each breaking \(U(1)\to Z_3\) has vacuum manifold \(U(1)/Z_3\) with

\[
\pi_1(U(1)/Z_3)=\mathbb Z,
\]

so local cosmic strings are expected. Their flux is quantized in units proportional to \(2\pi/(3g)\). For \(f=1\,\mathrm{TeV}\), a tension estimate \(\mu_{\rm string}\sim2\pi f^2\) gives a gravitational strength of order

\[
G\mu_{\rm string}\sim4\times10^{-32}
\]

using the reduced Planck-mass convention. This is cosmologically negligible as a gravitational source, though the particle-emission history has not been calculated.

There are no physical domain walls while the residual discrete gauge group remains unbroken. A later \(A\) or \(B\) vacuum expectation value would require a new string-wall analysis.

## 10. Occam and novelty audit

TP-G0 solves one problem: it realizes the exact product \(Z_3\) as a residual gauge symmetry and removes the need to postulate an exact global discrete symmetry. Its cost is substantial:

- two gauge couplings;
- two breaking scales;
- two radial self-couplings and multiple modulus portals;
- two matching couplings \(\kappa_m,\kappa_E\);
- up to three Abelian kinetic mixings;
- two new vectors and two new radial modes;
- local cosmic strings.

The construction is not novel by itself. Residual discrete gauge symmetries, Abelian kinetic mixing, and product-discrete dark sectors are established structures. Any TP novelty must come from a restricted relation or observable not already present in generic versions of these models.

## 11. Gate status

| Requirement | Status |
|---|---|
| Explicit parent gauge group and charges | Achieved |
| Derivation of residual \(Z_3\times Z_3\) | Achieved |
| Complete renormalizable scalar operator enumeration | Achieved |
| Continuous anomaly cancellation | Achieved trivially for scalar-only matter |
| Discrete gauge consistency | Inherited conditionally from parent |
| General kinetic mixing included | Achieved |
| Positive-kinetic benchmark | Achieved on protected zero-mixing slice |
| Global tree vacuum | Achieved for TP-G0 factorized slice |
| High-energy scalar/Goldstone unitarity | Achieved for TP-G0 |
| Full gauge-sector finite-energy unitarity | Open |
| Parent one-/two-loop RGEs and threshold matching | Open |
| Collider and precision viability | Open |
| Cosmic-string particle/cosmology analysis | Open |
| Parameter reduction or unique prediction | Failed to emerge at this stage |

The correct verdict is **conditional pass as a minimal anomaly-free gauge origin**, not UV completion and not unification.

In particular, the B0/B1/B2 ultraviolet scales quoted in checkpoint 7 must
not be combined with TP-G0 until matching at the (
ho_m,
ho_E,X_m,X_E)
thresholds and the parent RG system have been calculated.

## 12. Reproducibility

- `code/tpd_gauge_origin_audit.py`
- `code/tpd_gauge_vacuum.py`
- `code/tpd_gauge_high_energy_unitarity.py`
- `audits/tpd_gauge_origin_audit.json`
- `audits/tpd_gauge_vacuum.json`
- `audits/tpd_gauge_high_energy_unitarity.json`

Seventeen automated regression tests pass after integrating this checkpoint.

## Literature keys

- [Kra89] L. M. Krauss and F. Wilczek, *Physical Review Letters* **62**, 1221–1223 (1989), DOI 10.1103/PhysRevLett.62.1221.
- [Ban10] T. Banks and N. Seiberg, *Physical Review D* **83**, 084019 (2011), DOI 10.1103/PhysRevD.83.084019.
- [Hol86] B. Holdom, *Physics Letters B* **166**, 196–198 (1986), DOI 10.1016/0370-2693(86)91377-8.
- [Iba91] L. Ibáñez and G. Ross, *Physics Letters B* **260**, 291–295 (1991), DOI 10.1016/0370-2693(91)91614-2.


\newpage

## S7 Ternary Polarity checkpoint 9

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


\newpage

## S8 Ternary Polarity checkpoint 11

## Coupled TP-D freeze-out equations and rejection of B0 as a thermal-relic benchmark

**Research status:** internal technical audit  
**Theory version:** exact TP-D  
**Date:** 19 September 2026  
**Epistemic level:** exact collision structure; leading tree-level numerical diagnostic

## Executive verdict

The two-component collision system has been written in a convention that
tracks one yield per charge state and explicitly includes annihilation,
semi-annihilation, and \(B\bar B\leftrightarrow A\bar A\) conversion. It
passes detailed-balance and dark-particle-number conservation tests.

Using tree-level threshold cross sections, fixed \(g_*=g_{*s}=90\), and the
stored B0 parameters gives

\[
\Omega_Ah^2=1.248,\qquad
\Omega_Bh^2=0.572,\qquad
\boxed{\Omega_{\rm TP}h^2=1.820}.
\]

The reference cosmological value is \(\Omega_ch^2=0.120\pm0.001\) in base
\(\Lambda\)CDM [Pla20]. B0 therefore overcloses the Universe by a factor of
about \(15\) in this leading calculation. The discrepancy remains large under
deliberately favourable rate rescalings. B0 is consequently **rejected as a
standard thermal-relic benchmark**. This is a benchmark failure, not a
falsification of the TP-D symmetry or of every TP-D parameter point.

## 1. Yield convention and exact collision structure

Assume a symmetric plasma,

\[
Y_A=Y_{\bar A},\qquad Y_B=Y_{\bar B},
\]

where each \(Y_i=n_i/s\) is the yield of one charge state. The total late-time
energy density contains an explicit factor of two for particle plus
antiparticle.

With \(x=m_A/T\), the equations are

\[
\frac{dY_A}{dx}=-\frac{s}{Hx}\left[
\langle\sigma v\rangle_{A\bar A\to {\rm SM}}(Y_A^2-Y_{A,{\rm eq}}^2)
+\frac12\langle\sigma v\rangle_{AA\to\bar Ah}
(Y_A^2-Y_AY_{A,{\rm eq}})-C_{B\to A}
\right],
\]

\[
\frac{dY_B}{dx}=-\frac{s}{Hx}\left[
\langle\sigma v\rangle_{B\bar B\to {\rm SM}}(Y_B^2-Y_{B,{\rm eq}}^2)
+\frac12\langle\sigma v\rangle_{BB\to\bar Bh}
(Y_B^2-Y_BY_{B,{\rm eq}})+C_{B\to A}
\right],
\]

where

\[
C_{B\to A}=\langle\sigma v\rangle_{B\bar B\to A\bar A}
\left[Y_B^2-
\left(\frac{Y_{B,{\rm eq}}}{Y_{A,{\rm eq}}}\right)^2Y_A^2\right].
\]

The factor \(1/2\) in each semi-annihilation term agrees with the standard
\(Z_3\) collision equation [Bel12, Bel13]. Detailed balance makes every
collision polynomial vanish at equilibrium. Conversion enters with opposite
signs, so it cancels from the equation for \(Y_A+Y_B\): it redistributes dark
particle number but does not itself reduce it. These properties are exact for
the stated processes and convention.

## 2. Tree-level threshold rates

For the B0 parameters,

\[
m_A=180\,\mathrm{GeV},\quad m_B=400\,\mathrm{GeV},\quad
\lambda_{HA}=0.020,\quad\lambda_{HB}=0.030,\quad\lambda_{AB}=0.10,
\]

\[
\mu_A=60\,\mathrm{GeV},\qquad\mu_B=90\,\mathrm{GeV},
\]

the threshold calculation gives:

| Process class | \(\langle\sigma v\rangle\) [\(\mathrm{GeV}^{-2}\)] | \(\langle\sigma v\rangle\) [\(\mathrm{cm^3\,s^{-1}}\)] |
|---|---:|---:|
| \(A\bar A\to\mathrm{SM}\), including \(hh\) | \(2.60\times10^{-10}\) | \(3.03\times10^{-27}\) |
| \(AA\to\bar Ah\) | \(8.45\times10^{-11}\) | \(9.86\times10^{-28}\) |
| \(B\bar B\to\mathrm{SM}\), including \(hh\) | \(1.25\times10^{-10}\) | \(1.46\times10^{-27}\) |
| \(BB\to\bar Bh\) | \(3.32\times10^{-12}\) | \(3.88\times10^{-29}\) |
| \(B\bar B\to A\bar A\) | \(5.55\times10^{-10}\) | \(6.48\times10^{-27}\) |

The Higgs-mediated Standard-Model rate is computed using the tree-level
off-shell Higgs width. The \(hh\) final state includes the contact,
\(s\)-channel, and dark-scalar exchange diagrams. The semi-annihilation rate
uses the cubic and Higgs-portal vertices in the canonical potential. All rates
are evaluated at threshold rather than thermally averaged.

## 3. Numerical method

The system is integrated with an implicit Radau method in \(\ln x\):

- \(x\in[1,10^4]\);
- relative tolerance \(2\times10^{-8}\);
- absolute tolerance \(10^{-15}\);
- constant \(g_*=g_{*s}=90\);
- equilibrium densities use the exact Bessel function \(K_2(m_i/T)\).

An independent implementation evolves total particle-plus-antiparticle yields
with a BDF solver and separately reconstructed number-counting factors. It gives
\(\Omega_{\rm TP}h^2=1.82015\), differing from the primary result by
\(2.6\times10^{-5}\) fractionally. This validates the yield convention and
ODE normalization; it does not independently validate the matrix elements.

The late yields are

\[
Y_A=1.2646\times10^{-11},\qquad
Y_B=2.6065\times10^{-12}
\]

per charge state. The conversion process substantially reduces the heavy
component, but it transfers population into \(A\); it cannot compensate for
insufficient number-changing rates.

## 4. Robustness diagnostics

| Diagnostic | \(\Omega_{\rm TP}h^2\) |
|---|---:|
| Nominal | 1.820 |
| \(g_*=80\) | 1.936 |
| \(g_*=100\) | 1.722 |
| Stop at \(x=10^3\) | 1.847 |
| Stop at \(x=10^5\) | 1.817 |
| Remove conversion | 4.056 |
| Remove semi-annihilation | 2.002 |
| Multiply all number-changing rates by 2 | 1.139 |
| Multiply all number-changing rates by 10 | 0.364 |

The simple global-vacuum certificate permits approximately

\[
|\mu_A|<239\,\mathrm{GeV},\qquad |\mu_B|<598\,\mathrm{GeV}
\]

at the stored masses and quartics. Raising both cubics to \(99\%\) of those
bounds still gives

\[
\Omega_{\rm TP}h^2\simeq0.980.
\]

Thus the fixed B0 masses, portals, and quartics cannot be rescued merely by
increasing the cubic couplings while remaining inside this certificate.

## 5. What is exact and what is provisional

### Exact within the frozen reaction set

- the charge selection rules;
- the form of the collision polynomials;
- the \(1/2\) semi-annihilation number-counting factor;
- detailed balance;
- cancellation of conversion in total dark-particle number;
- the conclusion that conversion alone cannot cure overproduction.

### Leading/model-dependent

- all numerical cross sections;
- the use of threshold rather than thermal averages;
- constant \(g_*\) and \(g_{*s}\);
- tree-level Standard-Model widths;
- neglect of thermal masses, kinetic decoupling, and higher-order corrections;
- the assumption of a standard radiation-dominated thermal history.

An independent matrix-element implementation and proper thermal averaging are
still required before a precision viable benchmark can be certified. They are
not expected to bridge the factor-15 nominal discrepancy; the explicit
factor-ten stress test is included to make that inference transparent.

## 6. Consequences for the research programme

1. B0 remains useful as a vacuum/RGE/unitarity regression point, but it must no
   longer be called a viable dark-matter benchmark.
2. Direct-detection fraction rescaling cannot rescue an overclosing thermal
   point. The direct-detection likelihood should be applied only after a new
   point reproduces the observed total abundance or is explicitly treated as a
   subcomponent under a different production history.
3. The next TP-D task is a constrained scan over masses, portals, cubics,
   quartics, and conversion strength with vacuum and unitarity cuts applied
   before relic and LZ cuts.
4. The frozen TP-G0 parent is still separately blocked by its unintended
   \(\rho_E\) relic.

## 7. Failure statement

Under a standard radiation-dominated thermal history and the canonical B0
parameters, B0 fails if its thermally averaged and independently regenerated
relic abundance remains above the measured dark-matter density. The present
leading result exceeds it by enough that B0 is rejected now for benchmark use;
an independent implementation is retained as a verification requirement, not
as a reason to continue advertising the point as viable.

## 8. Reproducibility

- `code/tpd_coupled_relic.py`
- `audits/tpd_coupled_relic.json`
- `code/tpd_coupled_relic_crosscheck.py`
- `audits/tpd_coupled_relic_crosscheck.json`
- `code/test_tpd_phase3.py`

Twenty-seven automated regression tests pass after this checkpoint.

## Verified literature keys

- [Bel12] G. Bélanger, K. Kannike, A. Pukhov, and M. Raidal, *JCAP* **04**
  (2012) 010, DOI 10.1088/1475-7516/2012/04/010, arXiv:1202.2962.
- [Bel13] G. Bélanger, K. Kannike, A. Pukhov, and M. Raidal, *JCAP* **01**
  (2013) 022, DOI 10.1088/1475-7516/2013/01/022, arXiv:1211.1014.
- [Esc14] S. Esch, M. Klasen, and C. E. Yaguna, *JHEP* **09** (2014) 108,
  DOI 10.1007/JHEP09(2014)108, arXiv:1406.0617.
- [Pla20] N. Aghanim et al. (Planck Collaboration), *Astronomy &
  Astrophysics* **641** (2020) A6, DOI 10.1051/0004-6361/201833910,
  arXiv:1807.06209.


\newpage

## S9 TP checkpoint 12 — direct-detection gate

**Authoritative continuation state:** 2026-09-19  
**Gate verdict:** all four relic-compatible points from the 160-point leading-order scan are robustly excluded by LZ under the stated standard SI/local-density assumptions. This rejects the four points, not all TP-D parameter space.

## Experimental input

- Source: J. Aalbers et al. (LZ Collaboration), *Dark Matter Search Results from 4.2 Tonne-Years of Exposure of the LUX-ZEPLIN (LZ) Experiment*, Phys. Rev. Lett. **135**, 011802 (2025), [arXiv:2410.17036v3](https://arxiv.org/abs/2410.17036), version dated 2025-07-01.
- Curve: combined WS2024+WS2022, 4.2 tonne-years / 280 live days, spin-independent WIMP–nucleon power-constrained 90% C.L. upper limit.
- Data route: programmatic log–log interpolation of the solid-black vector path embedded in Figure 5. HEPData record 155182 remained blocked and was not retried.
- Cross-check: interpolation gives \(2.18\times10^{-48}\,\mathrm{cm^2}\) at 40 GeV versus \(2.2\times10^{-48}\,\mathrm{cm^2}\) stated in the paper.

## Preserved parameter vectors

All masses and cubics are in GeV; bare mass parameters are in GeV\(^2\).

- **P151:** `mA=287.3881512, mB=451.8144615, mu_A=552.4374723, mu_B=278.8235522, lambda_HA=0.09848361249, lambda_HB=0.2467728786, lambda_AB=0.01424436406, lambda_A=0.5697719149, lambda_B=0.2161664158, cubic_fraction_A=0.8646424330, cubic_fraction_B=0.4507755869, bare_mA2=79606.70000, bare_mB2=196656.09251`.
- **P82:** `mA=172.0264639, mB=351.5807483, mu_A=205.2434277, mu_B=483.6417227, lambda_HA=0.1040147876, lambda_HB=0.004932664608, lambda_AB=0.2436293520, lambda_A=0.2373680250, lambda_B=0.5665194537, cubic_fraction_A=0.8635839963, cubic_fraction_B=0.6095829745, bare_mA2=26440.19303, bare_mB2=123459.50295`.
- **P141:** `mA=141.5633314, mB=414.3938204, mu_A=53.73663092, mu_B=762.7198088, lambda_HA=0.1467871706, lambda_HB=0.1275889494, lambda_AB=0.007965433064, lambda_A=0.1138031249, lambda_B=0.4495388445, cubic_fraction_A=0.4252444761, cubic_fraction_B=0.9255360701, bare_mA2=15590.74292, bare_mB2=167854.74376`.
- **P10:** `mA=321.2231638, mB=343.4716475, mu_A=550.7208237, mu_B=983.4851594, lambda_HA=0.08403040257, lambda_HB=0.2326296108, lambda_AB=0.005419119393, lambda_A=0.4386327313, lambda_B=0.9848090620, cubic_fraction_A=0.8737365383, cubic_fraction_B=0.9918891067, bare_mA2=100637.17928, bare_mB2=110921.27034`.

## Component results

\[
\xi_i=\frac{\Omega_i h^2}{0.1200},\qquad
\sigma^{\rm eff}_{iN}=\xi_i\sigma^{\rm SI}_{iN},\qquad
R_i=\frac{\sigma^{\rm eff}_{iN}}{\sigma_{\rm LZ}(m_i)}.
\]

| Point | Component | \(m_i\) (GeV) | \(\Omega_i h^2\) | \(\xi_i\) | raw \(\sigma_i^{\rm SI}\) (cm²) | effective \(\xi_i\sigma_i\) (cm²) | LZ limit (cm²) | \(R_i\) | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P151 | A | 287.388 | 0.0565070 | 0.470892 | 1.025e-45 | 4.825e-46 | 9.011e-48 | 53.55 | excluded |
| P151 | B | 451.814 | 0.0634679 | 0.528899 | 2.609e-45 | 1.380e-45 | 1.375e-47 | 100.38 | excluded |
| P82 | A | 172.026 | 0.0271190 | 0.225992 | 3.176e-45 | 7.178e-46 | 5.291e-48 | 135.64 | excluded |
| P82 | B | 351.581 | 0.1004482 | 0.837068 | 1.720e-48 | 1.439e-48 | 1.072e-47 | 0.134 | not individually excluded |
| P141 | A | 141.563 | 0.0181996 | 0.151663 | 9.319e-45 | 1.413e-45 | 4.532e-48 | 311.85 | excluded |
| P141 | B | 414.394 | 0.1119164 | 0.932637 | 8.288e-46 | 7.730e-46 | 1.260e-47 | 61.34 | excluded |
| P10 | A | 321.223 | 0.1240571 | 1.033809 | 5.975e-46 | 6.177e-46 | 9.918e-48 | 62.28 | excluded; also individually overabundant in the leading relic approximation |
| P10 | B | 343.472 | 0.0116976 | 0.097480 | 4.007e-45 | 3.906e-46 | 1.051e-47 | 37.17 | excluded |

Point verdicts: **P151 excluded; P82 excluded by A; P141 excluded; P10 excluded.** The smallest excluding ratio is 37.17.

## Interpretation audit

- **Abundance rescaling:** each predicted component abundance is divided by the observed 0.1200, not by the point’s own model total.
- **Local density:** assumes \(\rho_i/\rho_{\rm DM}=\Omega_i/\Omega_{\rm DM}\). A large departure requires an astrophysical model absent here.
- **Mediator and interference:** minimal TP-D has one diagonal SM-Higgs exchange amplitude per component. There is no second amplitude or adjustable sign, hence no tree-level blind spot. Higgs–radial or kinetic-mixing amplitudes belong to a modified TP-G benchmark and cannot be invoked retroactively.
- **Isospin and normalization:** Higgs exchange is approximately isospin conserving, with \(f_N=0.30\), and
  \[
  \sigma_{iN}^{\rm SI}=\frac{\lambda_{Hi}^{2}f_N^2\mu_{iN}^2m_N^2}{4\pi m_h^4m_i^2}.
  \]
  Reasonable hadronic uncertainty cannot remove a minimum factor-37 excess.
- **Momentum dependence:** \(m_h\gg q_{\rm xenon}\), so the contact, momentum-independent SI mapping is valid.
- **Confidence convention:** LZ’s power-constrained 90% C.L. upper limit is applied.
- **Halo convention:** the comparison inherits LZ’s standard WIMP halo assumptions. The result is conditional on those assumptions, but the margins are not marginal.
- **Multicomponent likelihood:** a component that independently exceeds the rescaled single-component limit is sufficient for conservative exclusion because the other component adds a nonnegative event rate. A combined likelihood is needed only when every component is individually below its limit.

## Analytic reason and next reduced search

The failed points obtain freeze-out depletion using Higgs portals large enough to produce xenon rates 37–312 times above LZ. Away from poles and thresholds, both Higgs-mediated annihilation and direct detection scale as \(\lambda_{Hi}^2\); simply lowering a portal raises the relic abundance and does not generically lower \(\xi_i\sigma_i\). Conversion \(B\bar B\leftrightarrow A\bar A\) conserves total dark-particle number and is not an independent depletion mechanism.

The next justified reduced directions are:

1. \(m_i\simeq m_h/2\), requiring finite-width thermal averaging before any resonance scan.
2. Semi-annihilation dominance with a near-maximal vacuum-safe cubic and a small Higgs portal, with exact vacuum and finite-energy unitarity filters.
3. Only after TP-G repair: secluded annihilation into lighter dark vectors/radials.
4. Only as a costed modified model: Higgs–radial interference blind spots.

No new broad random scan is authorized by this result.

## Claim update

- **Strengthened, verified model-dependent result:** all four previously “relic compatible” random-scan points are excluded under the standard SI/local-density mapping.
- **Invalidated claim:** these four points cannot be called viable numerical benchmarks.
- **Preserved exact result:** TP-D’s kernel selection rules and forbidden \(B\to A+h\) amplitude are unaffected.
- **Open:** whether any resonance, semi-annihilation-dominated, or repaired secluded TP-G region is simultaneously relic-, direct-detection-, vacuum-, unitarity-, and RG-consistent.

## Exact unresolved dependency order

1. Implement finite-width thermal averaging and run the smallest Higgs-pole scan.
2. Bound the semi-annihilation escape direction analytically and with a minimal targeted grid.
3. Decide whether any TP-D point survives all phenomenology gates.
4. Continue gauge/Goldstone/transverse-vector finite-energy unitarity.
5. Complete parent gauge/scalar/kinetic-mixing RG matching, anomalies, perturbativity, and EFT cutoff.
6. Complete loop-improved vacuum/metastability and applicable cosmology.
7. Finish novelty, parameter-reducing observable, hostile-referee, and final equation/claim regression audits.

Machine-readable results: `audits/tpd_direct_detection_gate.json`. Reproduction code: `code/tpd_direct_detection_gate.py`. Regression status: **29/29 tests pass**.


\newpage

## S10 TP checkpoint 15 — point-matched TP-G finite-energy gauge gate

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


\newpage

## S11 TP checkpoint 16 — Higgs-pole thermal and experimental certification

**Completion-protocol checkpoint:** C15  
**Verdict:** **CONDITIONAL PHENOMENOLOGICAL PASS**

## Frozen parameter vector

| Parameter | Value |
|---|---:|
| $m_A,m_B$ | $62.0,62.2$ GeV |
| $\lambda_{HA},\lambda_{HB}$ | $5.5393817\times10^{-4},4.9170872\times10^{-4}$ |
| $\mu_A,\mu_B$ | $1,1$ GeV |
| $\lambda_A,\lambda_B,\lambda_{AB}$ | $0.1,0.1,10^{-5}$ |

## Thermal certification

The coupled Boltzmann system was recomputed with direct finite-width Gondolo–Gelmini thermal averages, the off-pole continuum, temperature-dependent $g_\rho(T)$ and $g_s(T)$, and the $d\ln g_s/d\ln T$ correction. Scaled Bessel functions remove the former large-$x$ numerical underflow.

| Quantity | Result |
|---|---:|
| $\Omega_Ah^2$ | $0.0592356$ |
| $\Omega_Bh^2$ | $0.0596303$ |
| $\Omega_{\rm tot}h^2$ | $0.118866$ |
| $\xi_A,\xi_B$ within the predicted abundance | $0.498340,0.501660$ |
| 110-to-150-point rate-table shift | $5.29\times10^{-5}$ |
| $g_\rho,g_s$ at $T=3.1$ GeV | $84.5747,84.1187$ |
| EOS $\pm5\%$ envelope for $\Omega_{\rm tot}h^2$ | $0.11593$–$0.12205$ |

The nominal result is $0.945\%$ below the reference $0.120$. This is a viable numerical benchmark at the present leading-order precision, not a precision relic prediction.

## Refined direct detection and collider checks

Fractions below use $\Omega_{\rm DM}h^2=0.1200$, as required for abundance-weighted comparison.

| Component | $\xi_i$ | raw $\sigma^{\rm SI}_{iN}$ [cm$^2$] | effective [cm$^2$] | LZ limit [cm$^2$] | $R_i$ |
|---|---:|---:|---:|---:|---:|
| $A$ | $0.493630$ | $6.8030\times10^{-49}$ | $3.3582\times10^{-49}$ | $2.5060\times10^{-48}$ | $0.13401$ |
| $B$ | $0.496919$ | $5.3265\times10^{-49}$ | $2.6468\times10^{-49}$ | $2.5087\times10^{-48}$ | $0.10551$ |

The masses differ by only $0.2$ GeV: their xenon recoil-scale proxy differs by $0.43\%$, so at exclusion-level precision the spectra are indistinguishable and the rate ratios add to $R_{\rm combined}=0.23952<1$.

The predicted invisible-Higgs branching fraction is $1.6881\times10^{-4}$, versus the ATLAS observed 95% C.L. bound $0.107$. In minimal TP-D there is no Higgs mixing because both dark scalars have zero vevs. In the protected TP-G slice, kinetic mixing and Higgs–parent-radial portals vanish at matching; switching either on requires a separate collider analysis.

## Classification and limitation

The point survives the current relic, direct-detection, and collider gate at leading order. Dominant limitations are the approximate QCD equation of state, higher-order energy-dependent virtual-Higgs width, and use of the published LZ exclusion curve rather than a two-component detector likelihood. None is numerically close to reversing the present factor-$4.17$ rate margin.

Reproduction: `code/tpd_pole_thermal_certification.py`; results: `audits/tpd_pole_thermal_certification.json`.


\newpage

## S12 TP checkpoint 17 — cubic processes and point-matched metastability

**Completion-protocol checkpoint:** C16  
**Verdict:** **CONDITIONAL PASS**

## Cubic-process gate

For both $m_A=62.0$ GeV and $m_B=62.2$ GeV, the zero-temperature semi-annihilation channel $SS\to S^\dagger h$ is exactly closed because $m_S<m_h$.

A deliberately conservative five-point amplitude envelope,

$$
|\mathcal M_{3\to2}|\le 100\frac{|\mu_S\lambda_S|}{m_S^2},
$$

gives at $x=20$

$$
\max_S\frac{n_{S,\rm eq}^2\langle\sigma v^2\rangle}{H}
=2.19\times10^{-9}.
$$

Thus cubic-induced $3\to2$ reactions cannot change the certified freeze-out result at relevant accuracy; no enlarged Boltzmann system is justified.

## Point-matched one-loop running

The parent running was repeated with the actual pole-point low-energy quartics and portals, and with

$$
g_m=g_E=0.30,\quad \lambda_{\Phi_m}=\lambda_{\Phi_E}=0.20,
\quad \kappa_m=\kappa_E=4.71405\times10^{-4}
$$

at the 1 TeV matching scale.

| Diagnostic | Scale/result |
|---|---:|
| First failure of the sufficient BFB certificate | $3.36215\times10^8$ GeV |
| High-energy scalar-unitarity boundary | $5.28504\times10^{17}$ GeV |
| First $4\pi$ coupling boundary | $1.03367\times10^{18}$ GeV |
| $\lambda_H$ at scalar-unitarity cutoff | $-0.0297107$ |

The instability is the familiar Higgs-direction loss of absolute stability, not a cubic-driven dark direction.

## Metastability envelope

Using the leading-log quartic bounce envelope,

$$
S_4\simeq\frac{8\pi^2}{3|\lambda_H|}=885.8,
$$

and the conservative four-volume prefactor capped at the first scalar partial-wave unitarity boundary, $5.285\times10^{17}$ GeV, gives $\ln P_{\rm decay}<-337$. The electroweak vacuum is therefore cosmologically long-lived in this approximation. No bounce claim is extrapolated into the interval between the scalar-unitarity and $4\pi$ boundaries.

This is not a full multi-field loop-improved bounce calculation. Finite threshold corrections, dimensionful running in the parent theory, two-loop evolution, gauge dependence of the effective potential, and a numerical multi-field bounce remain open precision tasks. Accordingly, the scientifically valid result is a **conditional metastability pass**, not an absolute-stability claim.

Reproduction: `code/tpd_cubic_metastability.py`; results: `audits/tpd_cubic_metastability.json`.


\newpage

## S13 TP checkpoint 18 — point-specific parent cosmology

**Completion-protocol checkpoint:** C17  
**Verdict:** **PASS at leading order**

## Extra parent states

At the matched pole point, $f_m=f_E=1$ TeV, $g_m=g_E=0.30$, $M_X=900$ GeV, and $m_\rho=632.456$ GeV. Unlike the already rejected B0 benchmark, both parent sectors have open prompt decays.

| Sector | Decay | Width [GeV] | Lifetime [s] | $\Gamma/H(T=M)$ |
|---|---|---:|---:|---:|
| $m$ vector | $X_m\to AA^\dagger$ | $0.521926$ | $1.26\times10^{-24}$ | $4.59\times10^{11}$ |
| $E$ vector | $X_E\to BB^\dagger$ | $0.521828$ | $1.26\times10^{-24}$ | $4.59\times10^{11}$ |
| $m$ radial | $\rho_m\to AAA+\mathrm{c.c.}$ | $3.9212\times10^{-8}$ | $1.68\times10^{-17}$ | $6.98\times10^4$ |
| $E$ radial | $\rho_E\to BBB+\mathrm{c.c.}$ | $3.9144\times10^{-8}$ | $1.68\times10^{-17}$ | $6.97\times10^4$ |

The radial widths use the exact massive three-body phase-space integral. From $\kappa\Phi^\dagger S^3+\mathrm{h.c.}$ and $\mu=3\kappa f/\sqrt2$, each charge-channel amplitude is $|\mathcal M|=2\mu/f=0.002$. These lifetimes exclude late entropy injection and BBN disruption by many orders of magnitude.

## Late-time stable-state checks

The zero-velocity Higgs-mediated annihilation rates are $1.47\times10^{-28}$ and $2.49\times10^{-28}\,\mathrm{cm^3s^{-1}}$. Including the squared component fractions and conservatively setting the deposition efficiency to one gives

$$
p_{\rm ann}=1.56\times10^{-30}\ {
m cm^3s^{-1}GeV^{-1}},
$$

or $0.00489$ of the Planck 2018 95% C.L. limit $3.2\times10^{-28}\,\mathrm{cm^3s^{-1}GeV^{-1}}$.

A deliberately loose low-velocity self-scattering amplitude envelope gives $\sigma/m<4.6\times10^{-12}\,\mathrm{cm^2g^{-1}}$ for either component. This is phenomenologically negligible.

Both parent Goldstones are eaten. The broken gauge factors produce local strings, not domain walls; their TeV-scale tension estimate is only $G\mu\sim1.1\times10^{-30}$. Thus there is no dark-radiation or relevant defect constraint in this matched slice.

## Classification

**Verified model-dependent result:** the pole benchmark has no unintended long-lived parent state and passes the applicable leading-order BBN, late-entropy, CMB-injection, self-interaction, dark-radiation, and defect checks. A nonstandard cosmological history was neither assumed nor needed.

Reproduction: `code/tpd_parent_extra_state_cosmology.py`; results: `audits/tpd_parent_extra_state_cosmology.json`.


\newpage

## S14 TP checkpoint 19 — adversarial novelty and prior-art gate

**Completion-protocol checkpoint:** C18  
**Verdict:** **FAIL for broad novelty; narrow formulation claim remains unproven**

## Closest established mechanisms

The comparison was deliberately limited to primary papers that decide the gate:

| Claimed ingredient | Prior-art result | Consequence for TP-D |
|---|---|---|
| $Z_N$ scalar semi-annihilation and cross-sector reactions | Bélanger et al., arXiv:1202.2962 | established |
| local $U(1)\to Z_3$ with a charge-three dark Higgs, vector, and radial | Ko and Tang, arXiv:1402.6449 | TP-G mechanism established |
| several stable scalar species under discrete symmetry | Yaguna and Zapata, arXiv:1911.05515 | multicomponent stabilization established |
| product residual discrete gauge symmetry organizing dark states | Borah, Ma, and Nanda, arXiv:2212.11847 | product-remnant mechanism established |

A targeted search for the exact two-singlet $Z_3\times Z_3$ operator basis and the particular projection/kernel language did not produce a closer indexed match. Absence from a targeted search is not evidence of novelty and is not promoted to a claim.

## Adversarial claim classification

| Statement | Classification |
|---|---|
| The kernel forbids the enumerated cross operators | exact mathematical/model result |
| The forbidden surface is radiatively protected | exact symmetry result |
| TP-D removes 12 physical continuous coefficients relative to the stated generic projected-$Z_3$ comparator | verified model-dependent result |
| $B\to A+X_0$ vanishes in exact TP-D | exact selection rule |
| Product discrete dark matter, semi-annihilation, or residual local $Z_3$ is new | excluded/failed claim |
| The names “matter-like” and “energy-like” encode new physics | unsupported conjecture |
| The projection/kernel organization is itself literature-new | unresolved; not demonstrated |
| TP-D is a new fundamental theory rather than a conventional product-discrete EFT | excluded/failed claim at current evidence |

## Gate result

The defensible scientific contribution is a fully audited, kernel-sensitive $Z_3\times Z_3$ EFT with a viable pole benchmark and explicit null selection rules. It is not a demonstrated novel symmetry mechanism. Any publication claim must use “specific construction/audit” or “known ingredients combined,” not “new class of dark matter symmetry,” unless a substantially more exhaustive professional literature review establishes otherwise.

Primary comparison set: arXiv:1202.2962, 1402.6449, 1911.05515, and 2212.11847. Search checked 19 September 2026.


\newpage

## S15 TP checkpoint 20 — parameter reduction and falsifiability

**Completion-protocol checkpoint:** C19  
**Verdict:** **WEAK PASS for exact null relations; FAIL for a unique nonzero TP-D relation**

## Exact minimal TP-D

The complete operator audit removes twelve physical continuous coefficients relative to the generic two-field projected-$Z_3$ comparator. This produces a correlated family of parameter-free observable nulls,

$$
\mathcal M(B\to A+X_0)=0,
$$

and analogous kernel-changing scattering amplitudes, whenever $X_0$ is kernel neutral and the exact symmetry is unbroken. These are genuinely parameter-reducing and falsifiable: one verified nonzero kernel-changing amplitude rejects exact minimal TP-D.

This satisfies the minimal “at least one falsifiable relation” criterion, but only weakly. A generic comparator can tune the same amplitudes to zero, so a null observation cannot positively identify TP-D. Identification would require both charge eigenstates, measured nonzero diagonal interactions, and several independently open but absent kernel-changing channels.

## Controlled soft extension

If the only breaking is a dimension-two $A^\dagger B$ mass term while the hard off-diagonal Higgs portal remains zero, the mass-basis Higgs couplings obey

$$
2G_{12}\cos2\theta=(G_{22}-G_{11})\sin2\theta.
$$

The generic projected-$Z_3$ theory instead has

$$
2G_{12}\cos2\theta-(G_{22}-G_{11})\sin2\theta=2v\eta_{HAB}.
$$

The identity is basis-covariant once another interaction—such as the parent gauge current—operationally identifies the charge basis. It was checked at 1000 random points to an absolute residual below $6.9\times10^{-13}$ GeV.

This is a real parameter-reducing nonzero sum rule, but it belongs to TP-Bsoft, not the exact viable TP-D pole benchmark, and its two-state alignment algebra is standard. It therefore cannot be used to rescue a strong TP-D novelty claim.

## Final classification

- **Exact result:** TP-D has parameter-free kernel-changing null amplitudes.
- **Falsifiability:** PASS—nonzero kernel-changing transitions falsify the exact model.
- **Positive identifiability:** unresolved and experimentally difficult.
- **Unique nonzero TP-D sum rule:** absent.
- **Soft-extension relation:** verified model-dependent result, not established novelty.

Reproduction: `code/tpd_soft_breaking_sum_rule.py`; results: `audits/tpd_soft_breaking_sum_rule.json`.


\newpage

## S16 TP checkpoint 21 — hostile-referee audit

**Completion-protocol checkpoint:** C20  
**Verdict:** **CONDITIONAL SURVIVAL AS A CONVENTIONAL EFT BENCHMARK**

## Referee decision

No fatal algebraic contradiction, stable-state perturbative-unitarity violation, anomaly, relic-density failure, direct-detection exclusion, or applicable cosmological exclusion was found for the Higgs-pole point. The benchmark survives, but several stronger interpretations fail.

## Findings by severity

### Corrected during review

The first metastability envelope had used the later $4\pi$ coupling boundary as its prefactor scale although high-energy scalar partial-wave unitarity is lost earlier. The calculation is now capped at $5.285\times10^{17}$ GeV, the first scalar-unitarity boundary. The corrected values are $S_4=885.8$ and $\ln P<-337$; the qualitative conditional metastability verdict is unchanged.

### Major limitations

1. The relic result is a leading-order numerical benchmark near a narrow Higgs pole. Its $0.95\%$ target offset is inside the tested EOS envelope, but precision thermal-QCD input and higher-order virtual-Higgs treatment are absent.
2. Direct detection uses abundance-rescaled published LZ limits and a justified nearly-degenerate rate sum, not a detector-level two-component likelihood. The combined ratio $0.2395$ leaves a sufficient present margin but is not a global fit.
3. Parent RG evolution uses a common 1 TeV step threshold. Finite matching, two-loop running, and parent dimensionful beta functions are not complete. The declared leading perturbative EFT ceiling is therefore $\Lambda_{\rm EFT}\lesssim5.3\times10^{17}$ GeV, not a UV-completion scale.
4. The parent vector is unstable. The physical $XS$ sequential interval is correctly unscored; an unconditional full-S-matrix statement would require stable asymptotic states or a consistent unstable-particle inclusive scheme.
5. Vacuum longevity is supported by a one-loop leading-log Higgs-direction envelope, not a gauge-controlled numerical multi-field bounce.
6. Zero kinetic mixing is an extra charge-conjugation-protected slice. It is not forced by $U(1)_m\times U(1)_E$ alone.
7. The exact selection rule is formally falsifiable but experimentally inaccessible in the frozen pole point without an additional production/tagging structure. It is not positive evidence for TP-D.

### Claims rejected

- broad symmetry or dark-matter-mechanism novelty;
- a unique nonzero TP-D observable relation;
- absolute stability to the Planck scale;
- an unconditional PASS assigned to the $XS$ pole interval;
- explanations of generations, gravity, constants, quantum gravity, or unification.

## Surviving scientific statement

TP-D has one conditionally viable two-component scalar Higgs-pole benchmark with exact kernel selection rules. Its scalar, electroweak-vector, controlled parent-gauge, leading one-loop RG/metastability, collider-prefilter, direct-detection, and necessary cosmology checks are mutually consistent within explicitly recorded approximations. It remains a conventional product-discrete EFT, not a demonstrated fundamental theory.

## Exact unresolved work

- finite one-loop matching at the split parent thresholds and two-loop uncertainty;
- parent dimensionful RG evolution and a gauge-controlled multi-field bounce;
- detector-level two-component xenon likelihood if precision exclusion is required;
- stable-state inclusive treatment if an unconditional parent-vector S-matrix claim is desired;
- a concrete production/tagging setup for the kernel nulls;
- professional exhaustive prior-art review if any narrow novelty claim is pursued.


\newpage

## S17 TP checkpoint 22 — final equation and claim regression

**Completion-protocol checkpoint:** C21  
**Verdict:** **PASS WITH EXPLICIT CONDITIONALS**

## Automated result

All 34 unit/regression tests pass. The cross-artifact freeze regression passes all 13 checks, including:

- preservation and exclusion status of the four original relic-compatible scan points;
- exact preservation of the P0 parameter vector;
- finite-width thermal abundance and numerical convergence;
- separate and combined abundance-weighted direct-detection ratios;
- electroweak and parent gauge blocks;
- explicit unscored treatment of both physical $XS$ sequential-pole intervals;
- absence of any stable-state genuine unitarity violation;
- correct ordering of BFB, scalar-unitarity, and $4\pi$ boundaries;
- metastability evaluation capped at the scalar-unitarity boundary;
- prompt parent-state decays and conservative CMB safety;
- claim-ledger continuity through M21.

Machine record: `audits/tpd_final_regression.json`.

## Authoritative continuation state

The promoted state is `TP_D_canonical_definition_v0.3.md`. P0 is a **conditionally viable numerical benchmark** of a conventional $Z_3\times Z_3$ scalar EFT. The parent gauge result is conditional only because unstable-vector external states do not define a conventional asymptotic S-matrix across the physical sequential interval; that interval is not a perturbative-unitarity failure.

The original four scan points remain excluded. Broad novelty and a unique nonzero TP-D sum rule remain failed claims. Absolute stability, experimental confirmation, generation counting, gravity, fundamental constants, quantum gravity, and unification are not claimed.

## Exact unresolved tasks

1. finite one-loop matching at the split $0.63/0.90$ TeV thresholds;
2. two-loop uncertainty and parent dimensionful running;
3. gauge-controlled numerical multi-field bounce;
4. detector-level two-component xenon likelihood only if precision exclusion is needed;
5. stable-state inclusive calculation only if an unconditional parent-vector S-matrix claim is pursued;
6. production/tagging construction for experimentally actionable kernel nulls;
7. exhaustive professional prior-art review only if a narrow novelty claim is pursued.

No additional broad scan is scientifically justified before one of these precision objectives is explicitly selected.

