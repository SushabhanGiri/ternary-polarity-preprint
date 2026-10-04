# Ternary Polarity checkpoint 10

## First phenomenology prefilter, an unintended relic, and a soft-breaking sum rule

**Research status:** internal technical audit  
**Theory versions:** exact TP-D, TP-G0, and candidate TP-Bsoft  
**Date:** 19 September 2026  
**Epistemic level:** exact tree-level selection rules and kinematics; preliminary phenomenological diagnostics

## Executive verdict

The exact kernel selection rule gives a clean but null distinction:

\[
\mathcal M(B\to A+h)=0
\]

even though the stored spectrum makes the decay kinematically open. A generic
single-
\(Z_3\) theory permits the off-diagonal Higgs portal and normally permits this
decay. This remains a valid falsification condition for exact TP-D, but a null
result alone cannot identify TP because a generic comparator may tune the
operator to zero.

A minimally **soft-broken** dual model produces a stronger tree-level sum
rule among measurable Higgs couplings and the mixing angle. This is genuine
parameter compression relative to generic projected \(Z_3\), but its algebra
is standard two-state mixing algebra and its literature novelty has not been
demonstrated.

The frozen gauge-parent benchmark TP-G0 has a more immediate problem: its
\(632\,\mathrm{GeV}\) \(E\)-radial mode has no open tree-level decay in the
chosen mass hierarchy and zero-portal slice. TP-G0 therefore contains an
unintended additional stable or long-lived relic. The benchmark is
**cosmologically incomplete and not promotable** until this state is repaired
and its lifetime and abundance are calculated.

## 1. Exact kernel-sensitive decay

The relevant charges are

\[
B\sim(0,1),\qquad A\sim(1,0),\qquad h\sim(0,0).
\]

For the benchmark,

\[
m_B=400\,\mathrm{GeV}>m_A+m_h
=305.25\,\mathrm{GeV}.
\]

The decay is therefore open kinematically but forbidden dynamically by the
two exact charge conservations. In a generic projected-
\(Z_3\) comparator,

\[
V\supset \eta_{HAB}(H^\dagger H)A^\dagger B+\mathrm{h.c.}
\]

is allowed. It gives

\[
\Gamma(B\to A+h)=
\frac{|\eta_{HAB}|^2v^2}{16\pi m_B}
\lambda^{1/2}\!\left(1,\frac{m_A^2}{m_B^2},
\frac{m_h^2}{m_B^2}\right).
\]

At the benchmark masses,

\[
\Gamma(B\to A+h)=1.93024\,|\eta_{HAB}|^2\ \mathrm{GeV}.
\]

Thus \(\eta_{HAB}=10^{-7}\) gives \(c\tau\simeq1.02\,\mathrm{cm}\), while
\(\eta_{HAB}=10^{-9}\) gives \(c\tau\simeq102\,\mathrm{m}\). These examples establish
effect size, not production reach.

## 2. Exact TP-D is a two-component dark sector

Exact \(Z_3^{(m)}\times Z_3^{(E)}\) separately stabilizes the lightest \(A\)-
and \(B\)-sector states. The following processes illustrate the distinction:

| Process | Exact TP-D | Generic projected \(Z_3\) | Reason |
|---|---|---|---|
| \(B\to A+h\) | Forbidden | Allowed | Kernel charge changes |
| \(AA\to A^\dagger h\) | Allowed | Allowed | Ordinary \(Z_3\) semi-annihilation |
| \(BB\to B^\dagger h\) | Allowed | Allowed | Ordinary \(Z_3\) semi-annihilation |
| \(BB^\dagger\leftrightarrow AA^\dagger\) | Allowed | Allowed | Both pairs are neutral |
| \(AA\to BB\) | Forbidden | Allowed by projected charge | Separate charges fail to balance |

Semi-annihilation is established \(Z_N\) dark-sector physics and is not a TP
novelty [Bel12a]. Multi-component relics and conversion processes are also
well established [Esc14]. Product residual gauge symmetries yielding
multi-component dark matter have explicit precedents [Cho21].

## 3. Direct-detection prefilter

For

\[
V\supset\lambda_{Hi}(H^\dagger H)|i|^2,
\]

the tree-level per-nucleon spin-independent cross section is

\[
\sigma_i^{\rm SI}=
\frac{\lambda_{Hi}^2 f_N^2\mu_{Ni}^2m_N^2}
{4\pi m_h^4m_i^2}.
\]

Using \(f_N=0.30\), the stored point gives

\[
\sigma_A^{\rm SI}=1.07\times10^{-46}\,\mathrm{cm}^2,
\qquad
\sigma_B^{\rm SI}=4.92\times10^{-47}\,\mathrm{cm}^2.
\]

For two components the experimental comparison is not \(\sigma_i\) alone but
approximately

\[
\xi_i\sigma_i^{\rm SI},\qquad
\xi_i=\frac{\Omega_i}{\Omega_{\rm DM}}.
\]

The LZ 4.2 tonne-year analysis reports no WIMP excess and a strongest
spin-independent 90% limit of \(2.2\times10^{-48}\,\mathrm{cm}^2\) at
\(40\,\mathrm{GeV}\) [LZ25]. Its mass-dependent likelihood or limit must be
evaluated at \(180\) and \(400\,\mathrm{GeV}\). Because the coupled TP relic
fractions have not yet been calculated, this checkpoint does **not** label B0
excluded or viable. It establishes that direct detection is already a severe
constraint and that relic fractions are mandatory, not optional.

## 4. TP-G0 parent-state decay audit

The frozen parent spectrum contains

\[
m_{\rho_E}=632.46\,\mathrm{GeV},\quad
m_B=400\,\mathrm{GeV},\quad
M_{X_E}=900\,\mathrm{GeV}.
\]

Consequently,

\[
m_{\rho_E}<2m_B,\qquad
m_{\rho_E}<3m_B,\qquad
m_{\rho_E}<2M_{X_E}.
\]

The benchmark also set \(\lambda_{B\Phi_E}\),
\(\lambda_{H\Phi_E}\), and cross-parent portals to zero at matching. Hence no
two- or three-body tree decay is open for \(\rho_E\). By contrast,
\(\rho_m\to AAA\) is open because \(632.46>3\times180\,\mathrm{GeV}\), and
both new vectors can decay to their charge-one scalar pairs.

This is a serious model issue:

- if \(\rho_E\) is exactly stable, the model has at least three relic species;
- if it decays only through induced loops, its lifetime must be calculated and
  confronted with BBN, CMB, and diffuse-energy-injection limits;
- if an allowed portal is turned on to make it decay, the vacuum, mixing,
  direct detection, and parameter count must be re-audited.

Minimal repair branches include:

1. change the hierarchy so \(m_{\rho_E}>2m_B\) and use a nonzero allowed
   modulus portal;
2. introduce a controlled Higgs-parent portal and calculate scalar mixing;
3. retain the long-lived state and solve the full three-component cosmology.

No repair is promoted yet because each changes the phenomenology and model
complexity.

## 5. Candidate TP-Bsoft sum rule

Consider only a dimension-two soft breaking,

\[
V_{\rm soft}=\delta^2A^\dagger B+\mathrm{h.c.},
\]

which breaks the product symmetry to the projected diagonal \(Z_3\). Keep the
dimension-four hard-breaking portal
\(\eta_{HAB}(H^\dagger H)A^\dagger B\) equal to zero. For a CP-conserving
two-state system,

\[
\tan2\theta=\frac{2\delta^2}{M_B^2-M_A^2}.
\]

Let \(G_h\) be the physical Higgs-coupling matrix after the same rotation. A
generic projected-\(Z_3\) theory obeys the identity

\[
2G_{12}\cos2\theta-(G_{22}-G_{11})\sin2\theta
=2v\eta_{HAB}.
\]

Minimal soft TP sets the right-hand side to zero and therefore predicts

\[
\boxed{
2G_{12}\cos2\theta=(G_{22}-G_{11})\sin2\theta
}.
\]

This is an overconstrained tree-level relation. One thousand randomized matrix
tests reproduced the generic identity to maximum absolute error
\(6.8\times10^{-13}\,\mathrm{GeV}\).

The relation is technically preferable to an arbitrary zero because a
dimension-two soft breaking does not create an inhomogeneous beta function
for a dimension-four hard-breaking coupling in a mass-independent
renormalization scheme. Physical on-shell amplitudes still receive loop
corrections, so the eventual experimental relation must include them.

### Essential observability caveat

The angle \(\theta\) is not separately physical if the Higgs portal is the only
interaction that labels \(A\) and \(B\). A second interaction must identify the
charge basis. The distinct \(U(1)_m\) and \(U(1)_E\) gauge currents in TP-G can
do this in principle. Without access to those currents, the sum rule can be a
basis parametrization rather than an observable test.

### Novelty status

The equation is standard simultaneous-rotation/alignment algebra. The
potentially distinctive claim is narrower: a dual-charge theory plus purely
soft reduction to diagonal \(Z_3\) motivates and protects this restricted
coupling surface. A focused literature search has not yet established that
this exact mechanism-plus-observable package is new. It must therefore remain
**potentially distinctive, not demonstrably novel**.

## 6. Gate update

| Requirement | Status after this checkpoint |
|---|---|
| Exact kernel-sensitive observable | Achieved as a null amplitude |
| Nonzero parameter relation | Achieved conditionally in TP-Bsoft at tree level |
| Basis-invariant observability | Conditional on measuring a charge-basis interaction |
| Radiative protection | Achieved for absence of hard breaking in the soft MS-bar model; on-shell loop corrections open |
| Existing-data viability | Open; relic fractions absent |
| TP-G0 cosmological viability | Failed for frozen benchmark pending repair of \(\rho_E\) |
| Literature novelty | Not demonstrated |
| Phase-II strong pass | Not yet achieved |

## 7. How these models can fail

- Exact TP-D fails if a verified kernel-changing transition such as
  \(B\to A+h\) occurs under the frozen field and charge assumptions.
- TP-Bsoft fails if measured \(G_{ij}\) and \(\theta\), after calculated loop
  corrections, violate the boxed relation while hard breaking is excluded by
  the assumed model.
- B0 fails as a dark-matter benchmark if no coupled relic solution makes both
  abundance and fraction-rescaled direct-detection rates acceptable.
- Frozen TP-G0 fails cosmologically if \(\rho_E\) is overproduced or decays too
  late and no minimal viable repair exists.

## 8. Reproducibility

- `code/tpd_phenomenology_prefilter.py`
- `code/tpd_soft_breaking_sum_rule.py`
- `audits/tpd_phenomenology_prefilter.json`
- `audits/tpd_soft_breaking_sum_rule.json`

Twenty-three automated regression tests pass after this checkpoint.

## Verified literature keys

- [Bel12a] G. Bélanger, K. Kannike, A. Pukhov, and M. Raidal, *JCAP* **04**
  (2012) 010, DOI 10.1088/1475-7516/2012/04/010, arXiv:1202.2962.
- [Esc14] S. Esch, M. Klasen, and C. E. Yaguna, *JHEP* **09** (2014) 108,
  DOI 10.1007/JHEP09(2014)108, arXiv:1406.0617.
- [Cho21] S.-M. Choi, J. Kim, P. Ko, and J. Li, *JHEP* **09** (2021) 028,
  DOI 10.1007/JHEP09(2021)028, arXiv:2103.05956.
- [LZ25] J. Aalbers et al. (LZ Collaboration), *Physical Review Letters*
  **135**, 011802 (2025), DOI 10.1103/4dyc-z8zf, arXiv:2410.17036.
