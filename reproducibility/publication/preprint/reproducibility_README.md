# Reproducibility record

## Frozen scope

This package reproduces the final C1–C22 Ternary Polarity audit. The frozen theory is TP-D v0.3 and the frozen phenomenological point is the C22 Higgs-pole benchmark. The regression suite reports 34/34 PASS. Reproduction means rerunning the recorded deterministic scripts against the frozen inputs; it does not authorize a new parameter scan or a change of physical assumptions.

## Benchmark definition

The benchmark has

`mA=62.00 GeV`, `mB=62.20 GeV`, `lambda_HA=5.539381702448959e-4`, `lambda_HB=4.917087212953458e-4`, `mu_A=mu_B=1 GeV`, `lambda_A=lambda_B=0.10`, and `lambda_AB=1e-5`.

The final leading thermal result is `Omega_A h2=0.0592356`, `Omega_B h2=0.0596303`, and `Omega_total h2=0.118866`. The final nearly-degenerate abundance-weighted direct-detection ratio is `R_combined=0.2395`. The first scalar partial-wave boundary is `5.285e17 GeV`; the leading Higgs-direction metastability envelope gives `S4=885.8` and `ln P < -337`.

## Environment recorded for publication build

- Python 3.12.14
- NumPy 2.3.5
- SciPy 1.17.0
- Matplotlib 3.10.8
- python-docx 1.2.0
- Pandoc 3.1.3
- XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023/Debian)

Earlier numerical checkpoints contain their own code paths, inputs, tolerances, and outputs. These publication-build versions are recorded for document and figure regeneration and should not be misread as historical versions for every completed calculation.

## Layout

- `main.md`: journal manuscript source.
- `supplementary_material.md`: consolidated technical supplement.
- `figures/`: deterministic PNG and PDF figures.
- `make_figures.py`: figure generator using frozen JSON records.
- `audits/`: checkpoint reports, numerical records, and final regression.
- `code/`: audit and regression programs.

## Minimal reproduction sequence

1. Retain the repository directory structure.
2. Run `python publication/preprint/make_figures.py` to regenerate the four manuscript figures.
3. Run `python publication/preprint/assemble_supplement.py` to reconstruct the consolidated supplement from the frozen checkpoint record.
4. Run the existing final regression entry point documented in the C22 checkpoint. Confirm 34/34 PASS without changing tolerances.
5. Compare the generated manifest hashes with `FREEZE_MANIFEST_SHA256.txt` after the publication freeze.

## Interpretation constraints

The physical on-shell `XS -> XS` sequential interval is intentionally UNSCORED. It is not to be regularized into a finite partial wave. The direct-detection result uses abundance-rescaled published LZ limits and a nearly-degenerate summed-rate approximation, not a detector-level two-component likelihood. The relic density is a leading-order numerical result near a narrow Higgs pole. The vacuum lifetime is a leading one-loop/leading-log Higgs-direction estimate, not a gauge-controlled multi-field bounce.

## Data and code availability

The frozen source package is archived on Zenodo:

- DOI: https://doi.org/10.5281/zenodo.23090199
- Author ORCID: https://orcid.org/0009-0006-1579-5477
- Reproducibility correspondence: sushabhangiri2025@gmail.com

