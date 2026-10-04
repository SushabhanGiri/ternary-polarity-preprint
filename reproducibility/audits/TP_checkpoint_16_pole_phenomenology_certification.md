# TP checkpoint 16 — Higgs-pole thermal and experimental certification

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
