# TP checkpoint 12 — direct-detection gate

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
