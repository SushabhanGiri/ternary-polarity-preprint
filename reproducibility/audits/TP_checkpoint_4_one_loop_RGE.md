# TP-1 One-Loop Renormalization-Group Gate

## Decision

The canonical TP-1 scalar-gauge EFT now has a reproducible one-loop \(\overline{\mathrm{MS}}\) renormalization-group system for all dimensionless couplings and all three scalar quadratic parameters. The implementation includes the full \(2\times2\) Abelian gauge-coupling matrix, third-family Standard Model Yukawas, the phase-sensitive \(S^\dagger\chi^3\) operator, exact running-coupling boundedness tests, and the previously derived 36-channel high-energy scalar unitarity test.

The illustrative benchmark remains bounded from below under the one-loop evolution but reaches the coupled-channel scalar unitarity boundary at

\[
\mu_U=7.5065605933\times10^{14}\ {\rm GeV}.
\]

It reaches the looser condition \(\max_i|c_i|=4\pi\) at

\[
\mu_{4\pi}=1.4156266264\times10^{15}\ {\rm GeV}.
\]

TP-1 is therefore **not perturbatively controlled to the Planck scale for this benchmark**. This is a model-dependent negative result, not a failure of every TP-1 parameter point. A parameter scan is required before making a statement about the whole model.

> **MODEL-DEPENDENT RESULT**  
> The benchmark is a viable one-loop EFT only below approximately \(7.5\times10^{14}\) GeV under the adopted scalar-unitarity criterion. Its first failure is growth of the scalar quartics, dominated by \(\lambda_S\), rather than loss of boundedness or an Abelian Landau pole.

> **OPEN PROBLEM**  
> Two-loop running, finite one-loop threshold corrections, a loop-improved gauge-independent vacuum analysis, and a global parameter scan have not yet been completed.

## 1. Conventions and scope

The potential is

\[
\begin{aligned}
V={}&m_H^2 H^\dagger H+m_S^2 S^\dagger S+m_\chi^2\chi^\dagger\chi
+\lambda_H(H^\dagger H)^2+\lambda_S(S^\dagger S)^2+\lambda_\chi(\chi^\dagger\chi)^2\\
&+\lambda_{HS}(H^\dagger H)(S^\dagger S)
+\lambda_{H\chi}(H^\dagger H)(\chi^\dagger\chi)
+\lambda_{S\chi}(S^\dagger S)(\chi^\dagger\chi)
+\left(\kappa S^\dagger\chi^3+\mathrm{h.c.}\right).
\end{aligned}
\]

Here \(Q_X(S)=3\), \(Q_X(\chi)=1\), Standard Model fields have \(X=0\), and \(S,\chi\) have \(Y=0\). The signed quadratic parameters obey \(m_H^2=-\mu_H^2\), \(m_S^2=-\mu_S^2\), and \(m_\chi^2=\mu_\chi^2\) relative to the tree-vacuum report. The hypercharge coupling \(g_Y\) is not GUT normalized. The beta functions use

\[
\beta_c\equiv\frac{dc}{d\ln\mu}=\frac{B_c^{(1)}}{16\pi^2}.
\]

The Standard Model truncation retains \(y_t,y_b,y_\tau\), neglects first- and second-family Yukawas, and sets CKM mixing to zero. This is adequate for the present core-survival gate, but not a precision electroweak matching calculation.

The general tensor normalization and scalar-mass formula follow Luo, Wang, and Xiao's corrected general-gauge-theory compilation ([DOI](https://doi.org/10.1103/PhysRevD.67.065019)). The multiple-Abelian formulation follows Fonseca, Malinský, and Staub ([DOI](https://doi.org/10.1016/j.physletb.2013.09.042)). The Standard Model Higgs terms were checked against Chetyrkin and Zoller's convention-explicit calculation ([DOI](https://doi.org/10.1007/JHEP04(2013)091)); their \(\mu^2d/d\mu^2\) coefficients were converted to \(d/d\ln\mu\). PyR@TE 2 supplies an additional implementation-level comparison for general RGEs with kinetic mixing ([DOI](https://doi.org/10.1016/j.cpc.2016.12.003)).

## 2. Abelian gauge matrix and kinetic mixing

Write the Abelian part of the covariant derivative as \(Q^TGA_\mu\), with charge vector \(Q=(Y,X)^T\). Define

\[
W_i=G^TQ_i,
\qquad
B_Q=\begin{pmatrix}41/6&0\\0&10/3\end{pmatrix}.
\]

The lower-right coefficient is

\[
b_X=\frac13\left[Q_X(S)^2+Q_X(\chi)^2\right]=\frac{10}{3},
\]

because both new fields are complex scalars. The matrix RGE is

\[
(16\pi^2)\beta_G=G\left(G^TB_QG\right).
\]

The charge-trace source \(\sum_iY_iX_i\) vanishes field by field in the minimal EFT. Hence diagonal \(G\) is an invariant one-loop trajectory. This does **not** prove that kinetic mixing vanishes in a UV completion: bi-charged heavy thresholds can generate a nonzero matching value, after which the full matrix equation must be used.

For nonzero mixing, define \(u_Y=G^T(1,0)^T\), \(u_X=G^T(0,1)^T\), and

\[
W_H=\frac12u_Y,\qquad W_S=3u_X,\qquad W_\chi=u_X.
\]

The code evaluates all Abelian scalar terms through the invariants \(C_i=W_i\cdot W_i\) and \(D_{ij}=W_i\cdot W_j\). For example,

\[
\begin{aligned}
(16\pi^2)\beta_{\lambda_i}\big|_{U(1)}&=-12C_i\lambda_i+6C_i^2,\\
(16\pi^2)\beta_{\lambda_{ij}}\big|_{U(1)}&=-6(C_i+C_j)\lambda_{ij}+12D_{ij}^2,\\
(16\pi^2)\beta_\kappa\big|_{U(1)}&=-3(C_S+3C_\chi)\kappa.
\end{aligned}
\]

## 3. Explicit beta functions on the zero-mixing trajectory

Set \(G=\mathrm{diag}(g_Y,g_X)\) and define

\[
T=3y_t^2+3y_b^2+y_\tau^2,
\qquad
Y_4=3y_t^4+3y_b^4+y_\tau^4.
\]

The gauge and Yukawa equations are

\[
\begin{aligned}
B_{g_Y}^{(1)}&=\frac{41}{6}g_Y^3,&
B_{g_2}^{(1)}&=-\frac{19}{6}g_2^3,&
B_{g_3}^{(1)}&=-7g_3^3,&
B_{g_X}^{(1)}&=\frac{10}{3}g_X^3,\\
B_{y_t}^{(1)}&=y_t\!\left[\frac32(y_t^2-y_b^2)+T-\frac{17}{12}g_Y^2-\frac94g_2^2-8g_3^2\right],\\
B_{y_b}^{(1)}&=y_b\!\left[\frac32(y_b^2-y_t^2)+T-\frac{5}{12}g_Y^2-\frac94g_2^2-8g_3^2\right],\\
B_{y_\tau}^{(1)}&=y_\tau\!\left[\frac32y_\tau^2+T-\frac{15}{4}g_Y^2-\frac94g_2^2\right].
\end{aligned}
\]

The seven scalar-coupling equations are

\[
\begin{aligned}
B_{\lambda_H}^{(1)}={}&24\lambda_H^2+\lambda_{HS}^2+\lambda_{H\chi}^2
+4T\lambda_H-2Y_4-(9g_2^2+3g_Y^2)\lambda_H\\
&+\frac98g_2^4+\frac34g_2^2g_Y^2+\frac38g_Y^4,\\
B_{\lambda_S}^{(1)}={}&20\lambda_S^2+2\lambda_{HS}^2+\lambda_{S\chi}^2
-108g_X^2\lambda_S+486g_X^4,\\
B_{\lambda_\chi}^{(1)}={}&20\lambda_\chi^2+2\lambda_{H\chi}^2+\lambda_{S\chi}^2+18\kappa^2
-12g_X^2\lambda_\chi+6g_X^4,\\
B_{\lambda_{HS}}^{(1)}={}&12\lambda_H\lambda_{HS}+8\lambda_S\lambda_{HS}+4\lambda_{HS}^2
+2\lambda_{H\chi}\lambda_{S\chi}\\
&+2T\lambda_{HS}-\left(\frac92g_2^2+\frac32g_Y^2+54g_X^2\right)\lambda_{HS},\\
B_{\lambda_{H\chi}}^{(1)}={}&12\lambda_H\lambda_{H\chi}+8\lambda_\chi\lambda_{H\chi}+4\lambda_{H\chi}^2
+2\lambda_{HS}\lambda_{S\chi}\\
&+2T\lambda_{H\chi}-\left(\frac92g_2^2+\frac32g_Y^2+6g_X^2\right)\lambda_{H\chi},\\
B_{\lambda_{S\chi}}^{(1)}={}&8\lambda_S\lambda_{S\chi}+8\lambda_\chi\lambda_{S\chi}+4\lambda_{S\chi}^2
+4\lambda_{HS}\lambda_{H\chi}+36\kappa^2\\
&-60g_X^2\lambda_{S\chi}+108g_X^4,\\
B_\kappa^{(1)}={}&\kappa\left(12\lambda_\chi+6\lambda_{S\chi}-36g_X^2\right).
\end{aligned}
\]

The pure \(g_X^4\) contribution to \(\beta_\kappa\) vanishes. The independent real-generator projection gives \(486\), \(6\), and \(108\) for the pure-gauge terms in \(B_{\lambda_S}^{(1)}\), \(B_{\lambda_\chi}^{(1)}\), and \(B_{\lambda_{S\chi}}^{(1)}\), respectively. These are particularly normalization-sensitive coefficients.

### Literature discrepancy found during the audit

Ko and Tang's original local-\(Z_3\) paper uses charges \(Q(\phi_X)=1\), \(Q(X)=1/3\) ([DOI](https://doi.org/10.1088/1475-7516/2014/05/047)). With \(\widehat g_X=3g_X\), its printed self-quartic gauge terms map exactly to the present results:

\[
6\widehat g_X^4-12\lambda_\phi\widehat g_X^2
\longrightarrow486g_X^4-108\lambda_Sg_X^2,
\]

\[
\frac{2}{27}\widehat g_X^4-\frac43\lambda_X\widehat g_X^2
\longrightarrow6g_X^4-12\lambda_\chi g_X^2.
\]

However, the same appendix's printed \(\lambda_3\) and mixed-quartic equations do not agree with the general tensor formula: the \(\lambda_3\) scalar coefficients are too small, the \(\lambda_3\) gauge anomalous-dimension term is absent, the mixed pure-gauge term is absent, and one mixed gauge term appears to multiply \(\lambda_{HX}\) rather than \(\lambda_{\phi X}\). These differences cannot all be removed by charge rescaling or a common beta-function convention. A second derivation from the one-loop scalar effective-potential divergence, \((16\pi^2)\beta_V=\tfrac12\mathrm{Tr}[(V_4'')^2]\), reproduces every coefficient in the present scalar equations exactly. The present equations therefore retain the independently duplicated general result, while recording the published appendix as a likely incomplete or typographically corrupted cross-check rather than silently copying it.

The signed scalar-mass equations are

\[
\begin{aligned}
B_{m_H^2}^{(1)}={}&m_H^2\left(12\lambda_H+2T-\frac92g_2^2-\frac32g_Y^2\right)
+2\lambda_{HS}m_S^2+2\lambda_{H\chi}m_\chi^2,\\
B_{m_S^2}^{(1)}={}&m_S^2(8\lambda_S-54g_X^2)
+4\lambda_{HS}m_H^2+2\lambda_{S\chi}m_\chi^2,\\
B_{m_\chi^2}^{(1)}={}&m_\chi^2(8\lambda_\chi-6g_X^2)
+4\lambda_{H\chi}m_H^2+2\lambda_{S\chi}m_S^2.
\end{aligned}
\]

There is no one-loop \(\kappa\) term in these quadratic beta functions because a diagonal mass insertion cannot contract the odd \(S\chi^3\) field content into a two-point scalar diagram in the unbroken theory.

## 4. Threshold matching at the broken-\(U(1)_X\) scale

With \(S=(f+s)/\sqrt2\), the leading radial mass is

\[
m_s^2=2\lambda_Sf^2.
\]

Eliminating the heavy radial field at tree level and zero external momentum gives

\[
\lambda_H^{<}=\lambda_H-\frac{\lambda_{HS}^2}{4\lambda_S},\qquad
\lambda_\chi^{<}=\lambda_\chi-\frac{\lambda_{S\chi}^2}{4\lambda_S},
\]

\[
\lambda_{H\chi}^{<}=\lambda_{H\chi}-\frac{\lambda_{HS}\lambda_{S\chi}}{2\lambda_S},
\qquad
\mu_3=\frac{\kappa f}{\sqrt2}
\]

when the low-energy potential contains \(\mu_3(\chi^3+\mathrm{h.c.})\). The same elimination also generates higher-dimensional operators. One-loop finite matching terms are not included in this checkpoint.

The cubic relation \(\mu_3=\kappa f/\sqrt2\) agrees with the explicit local-to-global \(Z_3\) matching in Ko and Tang.

For the benchmark at \(f=1\) TeV,

\[
(\lambda_H^{<},\lambda_\chi^{<},\lambda_{H\chi}^{<})
=(0.1296667,\,0.2446667,\,0.0473333),
\]

\[
m_s=774.60\ {\rm GeV},\qquad \mu_3=35.36\ {\rm GeV}.
\]

## 5. Numerical benchmark and failure scale

The run starts at \(\mu_0=1\) TeV with the scalar parameters from the tree-vacuum benchmark and illustrative rounded gauge/Yukawa inputs

\[
(g_Y,g_2,g_3,g_X)=(0.36,0.64,1.05,0.10),
\]

\[
(y_t,y_b,y_\tau)=(0.85,0.015,0.010).
\]

The calculation uses DOP853 in \(\ln\mu\), nominal tolerances \(\mathrm{rtol}=2\times10^{-10}\), \(\mathrm{atol}=10^{-12}\), and maximum step \(0.05\). At each sampled scale it applies:

1. the exact one-variable BFB reduction;
2. \(\max|c_i|<4\pi\) for dimensionless couplings;
3. the 36-channel scalar condition \(\rho(L)\le8\pi\).

At the refined unitarity boundary,

\[
\lambda_S=6.27095,\quad
\lambda_\chi=2.10848,\quad
\lambda_{S\chi}=0.89576,\quad
\kappa=0.20524,
\]

and \(\rho(L)=8\pi\) by construction. The minimum BFB value before failure is the initial value \(0.2292548748\); it does not cross zero. The off-diagonal Abelian entries remain zero to machine precision along the benchmark trajectory.

Three numerical resolutions give

\[
\mu_U=(7.5065605933026,\ 7.5065605933222,\ 7.5065605933222)\times10^{14}\ {\rm GeV},
\]

with a maximum relative spread \(2.61\times10^{-12}\). This confirms numerical convergence of the reported boundary within the one-loop system; it does not estimate missing two-loop uncertainty.

## 6. Independent checks

| Check | Result |
|---|---:|
| Scalar-only quartic tensor versus implemented scalar terms | exact; maximum residual \(0\) |
| Independent \(\tfrac12\mathrm{Tr}[(V_4'')^2]\) scalar derivation | exact agreement for all seven couplings |
| \(O(4)\) Higgs self-coupling limit | \(24\lambda_H^2\), passed |
| \(O(2)\) complex-scalar self limits | \(20\lambda^2\), passed |
| Abelian real-generator projection | all four hidden-sector equations passed exactly |
| Scalar mass-tensor contraction | all three equations passed exactly |
| Published local-\(Z_3\) diagonal self-gauge terms after charge rescaling | exact agreement |
| Published local-\(Z_3\) phase-sensitive/mixed equations | discrepancy recorded; general tensor result retained |
| Algebraic BFB versus independent numerical minimization | 30/30 classifications; maximum value difference \(3.41\times10^{-13}\) |
| RGE numerical convergence | relative boundary spread \(2.61\times10^{-12}\) |
| Zero-mixing invariant trajectory | off-diagonal numerical residual \(0\) |

The convergence test also found and eliminated an order-dependent software defect: repeated calls to the symbolic potential builder had accumulated duplicate coefficients. The builder is now explicitly idempotent, and all dependent outputs were regenerated. Recording this correction is part of the reproducibility audit.

## 7. What has and has not been shown

### Shown

- The minimal TP-1 field content admits a closed one-loop RGE system.
- Zero kinetic mixing is stable at one loop **if imposed at matching** for this field content.
- The normalization-sensitive hidden-sector gauge coefficients pass an independent tensor derivation.
- The illustrative benchmark is BFB throughout its perturbative trajectory.
- The benchmark loses scalar partial-wave control near \(7.5\times10^{14}\) GeV.

### Not shown

- That every phenomenologically viable TP-1 point fails below the Planck scale.
- That the one-loop scale is reliable to the displayed numerical precision once two-loop theoretical uncertainty is included.
- That UV threshold corrections set kinetic mixing to zero.
- That the loop-corrected vacuum is absolutely stable in a gauge-independent sense.
- That the benchmark satisfies relic-density, direct-detection, collider, fifth-force, or cosmological constraints.
- That any RGE relation is unique to Ternary Polarity rather than the established local-\(Z_3\) model class.

## 8. Failure condition and next gate

This benchmark is ruled out as a perturbative UV trajectory above \(\mu_U\) unless new degrees of freedom or threshold effects modify its running before that scale. The immediate next tasks are:

1. scan the low-energy parameter space for trajectories remaining BFB and unitary to specified target scales;
2. add precision matching and two-loop running for surviving points;
3. construct a genuinely kernel-sensitive \(Z_3\times Z_3\) benchmark and test whether it creates any parameter relation absent from an ordinary local-\(Z_3\) model.

The third task remains the central novelty gate.
