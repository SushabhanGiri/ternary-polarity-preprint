# Ternary Polarity TP-D

**Kernel-Sensitive Z₃ × Z₃ Two-Component Scalar Dark Matter Near the Higgs Resonance**

By **Sushabhan Giri** · [ORCID](https://orcid.org/0009-0006-1579-5477)

This repository preserves the preprint and reproducibility package archived in [Zenodo record 23090199](https://zenodo.org/records/23090199), DOI [10.5281/zenodo.23090199](https://doi.org/10.5281/zenodo.23090199).

Scientific freeze: **TP-D v0.3**. Reproducibility package: **1.0**.

## Read the preprint

- [Main preprint PDF](zenodo/TP_Preprint_v1.0_CLEAN.pdf)
- [Published supplement PDF](zenodo/TP_Preprint_Supplement_v1.0.pdf)
- [Zenodo record guide](zenodo/TERNARY_POLARITY_ZENODO_README.md)
- [Archived validation report](zenodo/VALIDATION_REPORT.txt)

## Repository layout

- `reproducibility/`: the extracted authoritative archive, with its internal directory structure and file contents preserved. It includes Python programs, audit records, numerical outputs, manuscript sources, figures, and its integrity manifest.
- `zenodo/`: all seven original deposit files, including the compressed archive and public-file checksums.
- `CITATION.cff`: the original citation metadata for the Zenodo package.

The separately deposited supplement and the supplement inside the archive are different files. Both are preserved at their respective original paths.

## Reproduce the archived checks

See [the archive README](reproducibility/README.md) for its recorded environment, scientific scope, and reproduction procedure.

From the `reproducibility` directory, the archived validation entry points are:

```sh
python code/test_dual_tp.py
python code/test_tpd_phase3.py
python code/tpd_final_regression.py
```

The original manuscript sources and deterministic figure scripts are under `reproducibility/publication/preprint/`.

## Citation and license

Please cite the [Zenodo release](https://doi.org/10.5281/zenodo.23090199), using the supplied `CITATION.cff` metadata.

The Zenodo record specifies **Creative Commons Attribution 4.0 International**, copyright © 2026 Sushabhan Giri. See [LICENSE.md](LICENSE.md).
