# Ternary Polarity Finite-Energy Unitarity Audit

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
