# TP checkpoint 14 — electroweak gauge finite-energy audit

**Classification:** verified model-dependent low-energy TP-D result.  
**Candidate:** the checkpoint-13 Higgs-pole point.  
**Scope boundary:** this closes the Standard-Model electroweak-vector layer, not the separate TP-G parent-vector layer.

## Structural result

The dark fields (A) and (B) are electroweak singlets and have zero vacuum expectation values. Therefore:

- pure-SM vector scattering is unchanged at tree level;
- there is no dark-scalar/vector mixing;
- the only new tree-level physical-vector channels are
  (SS^dagger\leftrightarrow h^*\leftrightarrow W^+W^-,ZZ), for (S=A,B).

For either vector (V=W,Z), the relevant amplitudes are

\[
\mathcal M_{LL}=\lambda_{HS}\frac{s-2M_V^2}{s-m_h^2},\qquad
\mathcal M_{TT}=-2\lambda_{HS}\frac{M_V^2}{s-m_h^2},
\]

with (mathcal M_{LT}=0). The scalar-potential Goldstone amplitude is

\[
\mathcal M_G=-\lambda_{HS}\frac{s}{s-m_h^2},
\]

so the tree-level equivalence identity is exact:

\[
\frac{\mathcal M_{LL}}{-\mathcal M_G}=1-\frac{2M_V^2}{s}.
\]

No pole prescription is required in this vector scan because the first physical (WW) threshold is above the (125.25\) GeV Higgs pole.

## Numerical result

The normalized channel block

\[
\{AA^dagger,BB^dagger\}
\longleftrightarrow
\{W_{LL},W_{++},W_{--},Z_{LL},Z_{++},Z_{--}\}
\]

was scanned from the first open (WW) threshold to (20\) TeV using 800 logarithmic energy points. Normalized identical-(ZZ) states carry the required (1/\sqrt2).

The maximum portal-induced singular value is

\[
\max_s\sigma_{\rm portal}(a_0)=1.80469\times10^{-5}
\]

at the upper scan endpoint. This is more than four orders of magnitude below the tree-unitarity boundary (1/2). The largest individual matrix element is (1.10200\times10^{-5}).

At (20\) TeV, the longitudinal/Goldstone deviations from their asymptotic equality are (3.23\times10^{-5}) for (W) and (4.16\times10^{-5}) for (Z); the implemented analytic identity is reproduced to machine precision.

## Verdict and remaining boundary

The Higgs-pole candidate **passes the complete new tree-level electroweak-vector finite-energy contribution**. Together with the existing scalar/Goldstone calculations, no low-energy TP-D gauge-unitarity obstruction remains.

This does not certify the TP-G parent. The following remain open there:

1. finite-energy scattering with the (U(1)_m\) and (U(1)_E) longitudinal and transverse vectors;
2. radial/vector and charged-dark-scalar exchange diagrams;
3. nonzero Abelian kinetic mixing away from the protected zero-mixing slice;
4. a point-specific match of the pole candidate to the parent thresholds.

Reproduction: `code/tpd_electroweak_gauge_unitarity.py`; data: `audits/tpd_electroweak_gauge_unitarity.json`.
