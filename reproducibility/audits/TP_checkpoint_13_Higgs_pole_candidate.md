# TP checkpoint 13 — minimal Higgs-pole candidate

**Classification:** viable leading-order candidate, not yet a certified benchmark.  
**Dependency:** checkpoint 12 remains the authoritative rejection of the four random-scan points.

## Fixed candidate

\[
m_A=62.00\ \mathrm{GeV},\qquad m_B=62.20\ \mathrm{GeV},
\]

\[
\lambda_{HA}=5.53938\times10^{-4},\qquad
\lambda_{HB}=4.91709\times10^{-4}.
\]

The remaining fixed scalar parameters are

`mu_A=mu_B=1 GeV, lambda_A=lambda_B=0.10, lambda_AB=1e-5, bare_mA2=3827.20895 GeV^2, bare_mB2=3853.93525 GeV^2`.

## Verified leading results

- A narrow-width Gondolo–Gelmini thermal average gives
  \[
  \Omega_Ah^2=0.05999998,\qquad
  \Omega_Bh^2=0.06000000,
  \]
  hence \(\Omega_{\rm tot}h^2=0.11999998\).
- Direct finite-width Breit–Wigner integration agrees with the narrow-width rate to 0.09–0.14% at \(x=15,20,25\).
- Abundance-weighted LZ ratios are \(R_A=0.1357\) and \(R_B=0.1062\). Because the masses and recoil spectra are nearly identical, the summed-rate screening proxy is
  \[
  R_{\rm combined}\simeq0.2419<1.
  \]
- Varying constant \(g_*=g_{*s}\) from 70 to 90 changes that proxy only from 0.260 to 0.227.
- The full coupled two-component solve with \(\lambda_{AB}=10^{-5}\) returns \(\Omega_{\rm tot}h^2=0.12000005\); its conversion rate is \(2.06\times10^{-17}\,\mathrm{GeV^{-2}}\) and is numerically negligible.
- The combined Higgs invisible branching fraction predicted at tree level is \(1.69\times10^{-4}\).
- Exact tree-level three-field copositivity passes.
- The sufficient inert electroweak global-minimum certificate passes.
- The high-energy scalar/Goldstone quartic unitarity radius is 0.7763, well below \(8\pi\).
- The complete physical-scalar finite-energy scan through 20 TeV, with contact and \(s,t,u\) exchange terms, gives \(\max|a_0|=0.00832\). Its scope still excludes external gauge states.
- Point-specific one-loop \(\overline{\mathrm{MS}}\) running first loses the absolute-BFB certificate at \(3.36\times10^8\) GeV through the SM-like Higgs quartic. No scalar-unitarity or \(4\pi\) boundary occurs before the \(2.435\times10^{18}\) GeV integration endpoint. This defines the present conservative EFT cutoff; it is not a tunnelling/metastability calculation.

## Scientific interpretation

The Higgs resonance genuinely breaks the off-resonance relic/direct-detection tension: freeze-out samples the narrow \(s\)-channel pole, whereas xenon scattering probes the zero-momentum Higgs propagator. The required portals fall to \(O(5\times10^{-4})\), so the model can reproduce the leading relic target without producing an excessive xenon rate.

This is a **verified model-dependent screening result**, not proof of a phenomenologically viable TP-D region. It does establish that checkpoint 12 does not exclude the full TP-D EFT.

## Remaining certification tasks

1. Replace constant \(g_*\) with a temperature-dependent equation-of-state table and include the off-pole continuum in the relic solve.
2. Apply a current Higgs-invisible likelihood rather than a scale comparison.
3. Perform a proper two-component LZ spectral likelihood/recast; the summed-rate proxy is justified for screening because the masses differ by only 0.2 GeV.
4. Calculate loop-improved metastability and threshold/two-loop uncertainty around the one-loop \(3.36\times10^8\) GeV absolute-stability cutoff.
5. Complete external-Goldstone/transverse-vector finite-energy unitarity in the parent completion.
6. Test whether nonzero cubics induce relevant higher-order number-changing processes; the stored 1 GeV cubics make them plausibly negligible but not yet calculated.

Reproduction: `code/tpd_higgs_pole_diagnostic.py`; results: `audits/tpd_higgs_pole_diagnostic.json`. Regression status after this addition: **30/30 tests pass**.
