# Ternary Polarity TP-D v0.3 — Zenodo reproducibility freeze

## Purpose

This archive is the reproducibility record associated with the manuscript
**“Kernel Sensitive Z3 x Z3 Two Component Scalar Dark Matter Near the Higgs Resonance”**
by **Sushabhan Giri**. It preserves the TP-D v0.3 scientific freeze, the C22 benchmark
audit trail, numerical records, Python verification programs, manuscript source, figures,
and clean manuscript/supplement PDFs.

The scientific status preserved by this archive is deliberately narrow: the result is a
**conditionally viable numerical benchmark within a conventional Z3 x Z3 scalar effective
field theory**. The archive does not claim experimental confirmation, a new fundamental
theory, broad novelty, unification, quantum gravity, a generation-counting mechanism, or
a unique nonzero observable relation.

## Persistent identifiers and contact

- Zenodo DOI: https://doi.org/10.5281/zenodo.23090199
- Creator: Sushabhan Giri
- ORCID: https://orcid.org/0009-0006-1579-5477
- Correspondence: sushabhangiri2025@gmail.com

## Frozen benchmark

- mA = 62.00 GeV
- mB = 62.20 GeV
- lambda_HA = 5.539381702448959e-4
- lambda_HB = 4.917087212953458e-4
- mu_A = mu_B = 1 GeV
- lambda_A = lambda_B = 0.10
- lambda_AB = 1e-5
- Omega_A h^2 = 0.0592356
- Omega_B h^2 = 0.0596303
- Omega_total h^2 = 0.118866
- combined nearly-degenerate abundance-weighted direct-detection ratio R = 0.2395
- first scalar partial-wave boundary = 5.285e17 GeV
- leading Higgs-direction metastability estimate S4 = 885.8, with ln P < -337

## Archive layout

- `paper/`
  - clean manuscript PDF
  - manuscript supplement PDF
- `publication/preprint/`
  - manuscript sources (`main.md`, `main.tex`)
  - consolidated supplement sources
  - bibliography
  - four deterministic figures in PNG/PDF form
  - figure and supplement assembly scripts
  - original reproducibility README
- `publication/PREPRINT_v1.0_FREEZE.md`
  - preprint freeze statement
- `publication/STAGE_1_C22_CLAIM_FREEZE.md`
  - claim-freeze record
- `publication/FINAL_PUBLICATION_READINESS_REPORT.md`
  - publication readiness record
- `audits/`
  - checkpoint reports and machine-readable numerical records
- `code/`
  - audit, regression, freeze-out, unitarity, RGE, phenomenology, and validation programs
- `MANIFEST_SHA256.txt`
  - SHA-256 integrity manifest for the contents of this archive
- `VALIDATION_REPORT.txt`
  - validation executed when this Zenodo package was assembled

## Reproduction

The archive is a scientific freeze, not an instruction to rescan parameter space or change
physical assumptions. Preserve the directory layout.

Suggested minimum sequence from the archive root:

1. `python publication/preprint/make_figures.py`
2. `python publication/preprint/assemble_supplement.py`
3. `python code/test_dual_tp.py`
4. `python code/test_tpd_phase3.py`
5. `python code/tpd_final_regression.py`

The manuscript's physical on-shell `XS -> XS` sequential interval is intentionally unscored;
it is not to be regularized into an artificial finite partial wave. Direct detection is based
on abundance-rescaled published LZ limits with the stated nearly-degenerate summed-rate
approximation. Relic density is a leading-order numerical calculation near a narrow Higgs
pole. The metastability result is a leading one-loop/leading-log Higgs-direction estimate,
not a gauge-controlled multi-field bounce calculation.

## Recorded publication-build environment

The accompanying frozen documentation records:

- Python 3.12.14
- NumPy 2.3.5
- SciPy 1.17.0
- Matplotlib 3.10.8
- python-docx 1.2.0
- Pandoc 3.1.3
- XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023/Debian)

Historical checkpoints may have been generated with earlier code paths or environments;
the versions above describe the publication build rather than every historical calculation.

## Versioning

- Scientific theory freeze: **TP-D v0.3**
- Reproducibility package: **Zenodo archival package v1.0**
- Manuscript: **Preprint v1.0 CLEAN**

A later Zenodo record version should be created rather than overwriting the scientific
meaning of this freeze if substantive data, equations, benchmark values, or scripts change.
