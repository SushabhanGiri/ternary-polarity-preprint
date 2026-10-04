# Ternary Polarity checkpoint 8

## Minimal gauge origin, anomaly audit, parent vacuum, and enlarged scalar unitarity

**Research status:** internal technical audit  
**Theory version:** TP-G0, a candidate parent of TP-D v0.2  
**Date:** 19 September 2026  
**Epistemic level:** explicit model construction; model-dependent benchmark; phenomenology incomplete

## Executive verdict

A minimal scalar-only gauge parent exists:

\[
U(1)_m\times U(1)_E
\longrightarrow Z_3^{(m)}\times Z_3^{(E)}.
\]

It uses two charge-three Higgs fields and reproduces the exact low-energy TP-D charges and cubic interactions. Because no chiral fermion carries either new charge, all continuous gauge, mixed-gauge, and gauge-gravitational anomaly coefficients vanish trivially.

An explicit benchmark, TP-G0, has:

- a certified global tree-level vacuum in its factorized parameter slice;
- positive gauge kinetic terms;
- two massive vectors, two radial modes, and the intended inert \(A,B\) spectrum;
- a complete 78-channel scalar/Goldstone quartic matrix satisfying high-energy tree unitarity.

This is a **conditional pass for existence of a gauge origin**, not a complete UV completion. The parent is a conventional product-Abelian residual-discrete construction, introduces many new parameters, permits three Abelian kinetic mixings, produces local cosmic strings, and has not passed full threshold RG, finite-energy vector scattering, collider, precision, or cosmological tests.

The standalone TP-D high-scale running cannot be imported into TP-G0.  The
radial modes and new vectors enter near \(0.63\) and \(0.90\,\mathrm{TeV}\),
respectively, so the beta functions change above those thresholds.  All TP-D
numbers at (10^8!-!10^{15}\,\mathrm{GeV}) remain conditional results for an
EFT in which no such low-scale parent states have appeared; they are not
predictions of TP-G0.

## 1. Frozen parent field content

\[
G_{\rm parent}=G_{\rm SM}\times U(1)_m\times U(1)_E.
\]

| Field | \(Q_m\) | \(Q_E\) | Role |
|---|---:|---:|---|
| \(\Phi_m\) | 3 | 0 | breaks \(U(1)_m\) to \(Z_3^{(m)}\) |
| \(\Phi_E\) | 0 | 3 | breaks \(U(1)_E\) to \(Z_3^{(E)}\) |
| \(A\) | 1 | 0 | low-energy \((1,0)\) state |
| \(B\) | 0 | 1 | low-energy \((0,1)\) state |

All four fields are complex Lorentz scalars and Standard-Model singlets. Standard-Model fermions and the Higgs doublet are neutral under the two new factors.

The covariant derivatives include

\[
D_\mu\Phi_m=(\partial_\mu+3ig_mX^m_\mu)\Phi_m,
\qquad
D_\mu A=(\partial_\mu+ig_mX^m_\mu)A,
\]

and the analogous \(E\) expressions.

## 2. Residual group

Let

\[
\langle\Phi_m\rangle=\frac{f_m}{\sqrt2},
\qquad
\langle\Phi_E\rangle=\frac{f_E}{\sqrt2}.
\]

Vacuum-preserving gauge transformations satisfy

\[
e^{3i\alpha_m}=e^{3i\alpha_E}=1.
\]

Therefore

\[
\alpha_m=\frac{2\pi n_m}{3},\qquad
\alpha_E=\frac{2\pi n_E}{3},
\]

with \(n_m,n_E\in\{0,1,2\}\). The surviving nine transformations form

\[
Z_3^{(m)}\times Z_3^{(E)},
\]

acting on \(A\) and \(B\) exactly as in TP-D. This is the standard residual-discrete gauge mechanism [Kra89, Ban10].

## 3. Complete renormalizable scalar operator basis

Define

\[
\mathcal S=\{\Phi_m,\Phi_E,A,B\}.
\]

The general gauge-invariant scalar potential contains:

1. one quadratic modulus for every \(S_i\in\mathcal S\);
2. one self-quartic \(|S_i|^4\) for every field;
3. all six pairwise modulus quartics \(|S_i|^2|S_j|^2\);
4. four Higgs portals \((H^\dagger H)|S_i|^2\);
5. the two phase-sensitive structures

\[
\kappa_m\Phi_m^\dagger A^3+\mathrm{h.c.},
\qquad
\kappa_E\Phi_E^\dagger B^3+\mathrm{h.c.}.
\]

No gauge-invariant scalar monomial of engineering dimension one or three exists. Exhaustive enumeration found four quadratic monomials and fourteen degree-four monomials when Hermitian-conjugate phase-sensitive terms are counted separately.

After symmetry breaking,

\[
\frac{\kappa_m f_m}{\sqrt2}A^3+\mathrm{h.c.}
=\frac{\mu_A}{3}A^3+\mathrm{h.c.},
\]

so

\[
\mu_A=\frac{3\kappa_m f_m}{\sqrt2},
\qquad
\mu_B=\frac{3\kappa_E f_E}{\sqrt2}.
\]

The low-energy cubic is therefore matched rather than inserted by hand.

## 4. Gauge kinetic mixing correction

The most general Abelian kinetic sector includes

\[
-\frac14F_Y^2-\frac14F_m^2-\frac14F_E^2
-\frac{\epsilon_{Ym}}2F_YF_m
-\frac{\epsilon_{YE}}2F_YF_E
-\frac{\epsilon_{mE}}2F_mF_E.
\]

Omitting the two hypercharge mixings would be inconsistent with the most-general-action rule. Kinetic mixing is a standard allowed interaction between Abelian factors [Hol86].

In the frozen scalar-only charge assignment,

\[
\operatorname{Tr}(YQ_m)=\operatorname{Tr}(YQ_E)
=\operatorname{Tr}(Q_mQ_E)=0,
\]

because no field carries both relevant charges. Thus zero mixing has no one-loop matter source. It is not enforced by the gauge group itself. The TP-G0 zero-mixing slice additionally imposes independent charge-conjugation automorphisms \(C_m\) and \(C_E\), under which \(X^m_\mu\) or \(X^E_\mu\) changes sign and the corresponding charged scalars are conjugated. With real scalar couplings, these symmetries protect all new-sector kinetic mixings from perturbative generation.

Without those extra automorphisms, all three \(\epsilon\)'s are independent parameters and must be constrained experimentally.

## 5. Gauge spectrum

When hypercharge mixing vanishes, the unmixed masses are

\[
M_m^2=9g_m^2f_m^2,
\qquad
M_E^2=9g_E^2f_E^2.
\]

For nonzero \(\epsilon_{mE}=\epsilon\), canonical normalization gives

\[
M_\pm^2=
\frac{M_m^2+M_E^2\pm
\sqrt{(M_m^2-M_E^2)^2+4\epsilon^2M_m^2M_E^2}}
{2(1-\epsilon^2)}.
\]

The kinetic matrix requires \(|\epsilon|<1\) on this two-factor slice. A 500-point numerical generalized-eigenvalue check reproduced the analytic formula to maximum relative error \(8.3\times10^{-14}\).

The phases of \(\Phi_m\) and \(\Phi_E\) are eaten. Two physical radial modes remain.

## 6. Anomaly audit

Gauge anomalies receive contributions from chiral fermions, not scalars. TP-G0 contains no fermion charged under either new \(U(1)\), while all Standard-Model chiral fermions are neutral. Consequently,

\[
[U(1)_m]^3=[U(1)_E]^3=0,
\]

all mixed Abelian coefficients vanish, all mixed Standard-Model coefficients vanish, and both gravitational-\(U(1)\) coefficients vanish.

The continuous parent is therefore anomaly-free in this restricted field content, and its residual discrete subgroup inherits a consistent gauge origin. This result does **not** survive automatically if chiral portal matter or Standard-Model charges are added; every such extension requires a new audit [Iba91].

## 7. TP-G0 benchmark

Choose

\[
f_m=f_E=1\,\mathrm{TeV},qquad
g_m=g_E=0.30,qquad
\lambda_{\Phi_m}=\lambda_{\Phi_E}=0.20,
\]

with the B0 low-energy quartics and masses. Set the other modulus portals and all kinetic mixings to zero on the charge-conjugation-symmetric slice. Cubic matching fixes

\[
\kappa_m=0.0282843,qquad
\kappa_E=0.0424264.
\]

The tree spectrum is

\[
m_{\rho_m}=m_{\rho_E}=632.46\,\mathrm{GeV},
\qquad
M_m=M_E=900\,\mathrm{GeV},
\]

plus \(M_A=180\,\mathrm{GeV}\), \(M_B=400\,\mathrm{GeV}\), and the Standard-Model-like Higgs.

### Parent BFB and global vacuum

For either \((\Phi,A)\) sector with vanishing modulus portal, the phase-minimized quartic along \(t=|\Phi|/|A|\) is proportional to

\[
f_4(t)=\lambda_\Phi t^4+\lambda_A-2|\kappa|t.
\]

Its minimum occurs at

\[
t_*=\left(\frac{|\kappa|}{2\lambda_\Phi}\right)^{1/3},
\]

with margin

\[
f_4(t_*)=\lambda_A-\frac32|\kappa|t_*.
\]

The TP-G0 margins are \(0.18246\) and \(0.21988\), respectively.

Interior stationary points with dark radial value \(a>0\) reduce to positive roots of

\[
4\lambda_\Phi M(x)
\left[4M(x)^2-9\kappa^2f^2x\right]
-27\kappa^4x^3=0,
\]

where \(x=a^2\) and \(M(x)=m_A^2+\lambda_Ax\). Both benchmark polynomials have no positive real root. Boundary directions and infinity are positive, so each factorized sector has its global minimum at \((|\Phi|,|A|)=(f/\sqrt2,0)\) in complex-field notation. Nonnegative \(H\)-\(A\), \(H\)-\(B\), and \(A\)-\(B\) portals complete the benchmark global-vacuum certificate.

The proof applies to this factorized parameter slice. The zero modulus portals are not claimed to form a closed RG surface.

## 8. Enlarged high-energy scalar matrix

The parent contains twelve real scalar components and 78 normalized two-particle channels. The complete scalar-potential quartic tensor includes the phase-sensitive \(\kappa_m\Phi_m^\dagger A^3\) and \(\kappa_E\Phi_E^\dagger B^3\) interactions.

For TP-G0,

\[
\max|\Lambda|=1.05056,
\qquad
\max|a_0|=0.0209001,
\]

well below \(|\operatorname{Re}a_0|\le1/2\). The 36-channel \(H+A+B\) principal submatrix reproduces the independent low-energy generator exactly.

This is a scalar/Goldstone quartic result. Gauge exchanges, transverse vectors, finite-energy diagrams, and nonzero kinetic mixing remain outside it.

## 9. Topological defects

Each breaking \(U(1)\to Z_3\) has vacuum manifold \(U(1)/Z_3\) with

\[
\pi_1(U(1)/Z_3)=\mathbb Z,
\]

so local cosmic strings are expected. Their flux is quantized in units proportional to \(2\pi/(3g)\). For \(f=1\,\mathrm{TeV}\), a tension estimate \(\mu_{\rm string}\sim2\pi f^2\) gives a gravitational strength of order

\[
G\mu_{\rm string}\sim4\times10^{-32}
\]

using the reduced Planck-mass convention. This is cosmologically negligible as a gravitational source, though the particle-emission history has not been calculated.

There are no physical domain walls while the residual discrete gauge group remains unbroken. A later \(A\) or \(B\) vacuum expectation value would require a new string-wall analysis.

## 10. Occam and novelty audit

TP-G0 solves one problem: it realizes the exact product \(Z_3\) as a residual gauge symmetry and removes the need to postulate an exact global discrete symmetry. Its cost is substantial:

- two gauge couplings;
- two breaking scales;
- two radial self-couplings and multiple modulus portals;
- two matching couplings \(\kappa_m,\kappa_E\);
- up to three Abelian kinetic mixings;
- two new vectors and two new radial modes;
- local cosmic strings.

The construction is not novel by itself. Residual discrete gauge symmetries, Abelian kinetic mixing, and product-discrete dark sectors are established structures. Any TP novelty must come from a restricted relation or observable not already present in generic versions of these models.

## 11. Gate status

| Requirement | Status |
|---|---|
| Explicit parent gauge group and charges | Achieved |
| Derivation of residual \(Z_3\times Z_3\) | Achieved |
| Complete renormalizable scalar operator enumeration | Achieved |
| Continuous anomaly cancellation | Achieved trivially for scalar-only matter |
| Discrete gauge consistency | Inherited conditionally from parent |
| General kinetic mixing included | Achieved |
| Positive-kinetic benchmark | Achieved on protected zero-mixing slice |
| Global tree vacuum | Achieved for TP-G0 factorized slice |
| High-energy scalar/Goldstone unitarity | Achieved for TP-G0 |
| Full gauge-sector finite-energy unitarity | Open |
| Parent one-/two-loop RGEs and threshold matching | Open |
| Collider and precision viability | Open |
| Cosmic-string particle/cosmology analysis | Open |
| Parameter reduction or unique prediction | Failed to emerge at this stage |

The correct verdict is **conditional pass as a minimal anomaly-free gauge origin**, not UV completion and not unification.

In particular, the B0/B1/B2 ultraviolet scales quoted in checkpoint 7 must
not be combined with TP-G0 until matching at the (ho_m,ho_E,X_m,X_E)
thresholds and the parent RG system have been calculated.

## 12. Reproducibility

- `code/tpd_gauge_origin_audit.py`
- `code/tpd_gauge_vacuum.py`
- `code/tpd_gauge_high_energy_unitarity.py`
- `audits/tpd_gauge_origin_audit.json`
- `audits/tpd_gauge_vacuum.json`
- `audits/tpd_gauge_high_energy_unitarity.json`

Seventeen automated regression tests pass after integrating this checkpoint.

## Literature keys

- [Kra89] L. M. Krauss and F. Wilczek, *Physical Review Letters* **62**, 1221–1223 (1989), DOI 10.1103/PhysRevLett.62.1221.
- [Ban10] T. Banks and N. Seiberg, *Physical Review D* **83**, 084019 (2011), DOI 10.1103/PhysRevD.83.084019.
- [Hol86] B. Holdom, *Physics Letters B* **166**, 196–198 (1986), DOI 10.1016/0370-2693(86)91377-8.
- [Iba91] L. Ibáñez and G. Ross, *Physics Letters B* **260**, 291–295 (1991), DOI 10.1016/0370-2693(91)91614-2.
