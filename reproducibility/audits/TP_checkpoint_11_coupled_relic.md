# Ternary Polarity checkpoint 11

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
