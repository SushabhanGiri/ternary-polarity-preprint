# Ternary Polarity checkpoint 7

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
