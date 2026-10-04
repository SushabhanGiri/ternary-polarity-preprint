# TP checkpoint 18 — point-specific parent cosmology

**Completion-protocol checkpoint:** C17  
**Verdict:** **PASS at leading order**

## Extra parent states

At the matched pole point, $f_m=f_E=1$ TeV, $g_m=g_E=0.30$, $M_X=900$ GeV, and $m_\rho=632.456$ GeV. Unlike the already rejected B0 benchmark, both parent sectors have open prompt decays.

| Sector | Decay | Width [GeV] | Lifetime [s] | $\Gamma/H(T=M)$ |
|---|---|---:|---:|---:|
| $m$ vector | $X_m\to AA^\dagger$ | $0.521926$ | $1.26\times10^{-24}$ | $4.59\times10^{11}$ |
| $E$ vector | $X_E\to BB^\dagger$ | $0.521828$ | $1.26\times10^{-24}$ | $4.59\times10^{11}$ |
| $m$ radial | $\rho_m\to AAA+\mathrm{c.c.}$ | $3.9212\times10^{-8}$ | $1.68\times10^{-17}$ | $6.98\times10^4$ |
| $E$ radial | $\rho_E\to BBB+\mathrm{c.c.}$ | $3.9144\times10^{-8}$ | $1.68\times10^{-17}$ | $6.97\times10^4$ |

The radial widths use the exact massive three-body phase-space integral. From $\kappa\Phi^\dagger S^3+\mathrm{h.c.}$ and $\mu=3\kappa f/\sqrt2$, each charge-channel amplitude is $|\mathcal M|=2\mu/f=0.002$. These lifetimes exclude late entropy injection and BBN disruption by many orders of magnitude.

## Late-time stable-state checks

The zero-velocity Higgs-mediated annihilation rates are $1.47\times10^{-28}$ and $2.49\times10^{-28}\,\mathrm{cm^3s^{-1}}$. Including the squared component fractions and conservatively setting the deposition efficiency to one gives

$$
p_{\rm ann}=1.56\times10^{-30}\ {m cm^3s^{-1}GeV^{-1}},
$$

or $0.00489$ of the Planck 2018 95% C.L. limit $3.2\times10^{-28}\,\mathrm{cm^3s^{-1}GeV^{-1}}$.

A deliberately loose low-velocity self-scattering amplitude envelope gives $\sigma/m<4.6\times10^{-12}\,\mathrm{cm^2g^{-1}}$ for either component. This is phenomenologically negligible.

Both parent Goldstones are eaten. The broken gauge factors produce local strings, not domain walls; their TeV-scale tension estimate is only $G\mu\sim1.1\times10^{-30}$. Thus there is no dark-radiation or relevant defect constraint in this matched slice.

## Classification

**Verified model-dependent result:** the pole benchmark has no unintended long-lived parent state and passes the applicable leading-order BBN, late-entropy, CMB-injection, self-interaction, dark-radiation, and defect checks. A nonstandard cosmological history was neither assumed nor needed.

Reproduction: `code/tpd_parent_extra_state_cosmology.py`; results: `audits/tpd_parent_extra_state_cosmology.json`.
