# TP checkpoint 17 — cubic processes and point-matched metastability

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
