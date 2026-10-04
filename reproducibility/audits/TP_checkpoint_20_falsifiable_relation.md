# TP checkpoint 20 — parameter reduction and falsifiability

**Completion-protocol checkpoint:** C19  
**Verdict:** **WEAK PASS for exact null relations; FAIL for a unique nonzero TP-D relation**

## Exact minimal TP-D

The complete operator audit removes twelve physical continuous coefficients relative to the generic two-field projected-$Z_3$ comparator. This produces a correlated family of parameter-free observable nulls,

$$
\mathcal M(B\to A+X_0)=0,
$$

and analogous kernel-changing scattering amplitudes, whenever $X_0$ is kernel neutral and the exact symmetry is unbroken. These are genuinely parameter-reducing and falsifiable: one verified nonzero kernel-changing amplitude rejects exact minimal TP-D.

This satisfies the minimal “at least one falsifiable relation” criterion, but only weakly. A generic comparator can tune the same amplitudes to zero, so a null observation cannot positively identify TP-D. Identification would require both charge eigenstates, measured nonzero diagonal interactions, and several independently open but absent kernel-changing channels.

## Controlled soft extension

If the only breaking is a dimension-two $A^\dagger B$ mass term while the hard off-diagonal Higgs portal remains zero, the mass-basis Higgs couplings obey

$$
2G_{12}\cos2\theta=(G_{22}-G_{11})\sin2\theta.
$$

The generic projected-$Z_3$ theory instead has

$$
2G_{12}\cos2\theta-(G_{22}-G_{11})\sin2\theta=2v\eta_{HAB}.
$$

The identity is basis-covariant once another interaction—such as the parent gauge current—operationally identifies the charge basis. It was checked at 1000 random points to an absolute residual below $6.9\times10^{-13}$ GeV.

This is a real parameter-reducing nonzero sum rule, but it belongs to TP-Bsoft, not the exact viable TP-D pole benchmark, and its two-state alignment algebra is standard. It therefore cannot be used to rescue a strong TP-D novelty claim.

## Final classification

- **Exact result:** TP-D has parameter-free kernel-changing null amplitudes.
- **Falsifiability:** PASS—nonzero kernel-changing transitions falsify the exact model.
- **Positive identifiability:** unresolved and experimentally difficult.
- **Unique nonzero TP-D sum rule:** absent.
- **Soft-extension relation:** verified model-dependent result, not established novelty.

Reproduction: `code/tpd_soft_breaking_sum_rule.py`; results: `audits/tpd_soft_breaking_sum_rule.json`.
