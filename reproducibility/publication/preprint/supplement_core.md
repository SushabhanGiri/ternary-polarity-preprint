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
