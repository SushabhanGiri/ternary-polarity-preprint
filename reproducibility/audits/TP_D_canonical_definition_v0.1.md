# TP-D Canonical Theory Definition Sheet — v0.1

**Freeze date:** 15 September 2026  
**Status:** surviving Phase-II EFT branch; substantive partial pass  
**Not claimed:** experimental confirmation, unique novelty, Standard-Model unification, gravity theory, or Theory of Everything

## 1. Defining question

Can two microscopic ternary charges produce observable selection rules that cannot be expressed using only the projected charge?

The answer for this model is **yes relative to a generic single \(Z_3\)**: an additional exact kernel charge forbids operators and transitions. The answer is **not yet yes relative to the full literature**: the mechanism is an instance of a conventional product discrete symmetry.

## 2. Spacetime and conventions

- Four-dimensional Minkowski spacetime.
- Metric signature \((+,-,-,-)\).
- Natural units \(\hbar=c=1\).
- Local, Lorentz-covariant, Hermitian action.
- Canonical positive scalar kinetic terms.
- Standard-Model gauge group remains \(SU(3)_C\times SU(2)_L\times U(1)_Y\).

## 3. Exact internal symmetry

\[
G_{\rm TP-D}=Z_3^{(m)}\times Z_3^{(E)}
\cong Z_3^{(P)}\times Z_3^{(K)}.
\]

Charge coordinates are related by

\[
q_P=q_m+q_E,\qquad q_K=q_m-q_E\pmod3.
\]

The projection \(\pi(q_m,q_E)=q_P\) has

\[
\ker\pi=\{(0,0),(1,2),(2,1)\}.
\]

## 4. Field content

| Field | Lorentz | \(SU(3)_C\) | \(SU(2)_L\) | \(Y\) | \((q_m,q_E)\) | \((q_P,q_K)\) | Dimension |
|---|---|---:|---:|---:|---:|---:|---:|
| \(H\) | scalar | 1 | 2 | \(+\tfrac12\) | \((0,0)\) | \((0,0)\) | 1 |
| \(A\) | complex scalar | 1 | 1 | 0 | \((1,0)\) | \((1,1)\) | 1 |
| \(B\) | complex scalar | 1 | 1 | 0 | \((0,1)\) | \((1,2)\) | 1 |

All Standard-Model fields are neutral under \(G_{\rm TP-D}\) in v0.1.

## 5. Transformations

With \(\omega=e^{2\pi i/3}\), the original generators act as

\[
g_m:(A,B)\mapsto(\omega A,B),\qquad
g_E:(A,B)\mapsto(A,\omega B).
\]

Equivalently,

\[
P=\omega I_2,\qquad K=\operatorname{diag}(\omega,\omega^2).
\]

The \(q=2\) label is a conjugate internal charge, not negative energy or negative mass.

## 6. Canonical renormalizable action

\[
S=\int d^4x\left(\mathcal L_{\rm SM}+|\partial A|^2+|\partial B|^2-V\right),
\]

where

\[
\begin{aligned}
V={}&-m_H^2H^\dagger H+\lambda_H(H^\dagger H)^2
+m_A^2|A|^2+m_B^2|B|^2\\
&+\left(\frac{\mu_A}{3}A^3+\frac{\mu_B}{3}B^3+\mathrm{h.c.}\right)
+\lambda_A|A|^4+\lambda_B|B|^4+\lambda_{AB}|A|^2|B|^2\\
&+\lambda_{HA}(H^\dagger H)|A|^2
+\lambda_{HB}(H^\dagger H)|B|^2.
\end{aligned}
\]

This is the complete renormalizable scalar action under the stated field content and symmetries. No additional zero is assumed by hand.

## 7. Independent parameter set

Excluding shared Standard-Model parameters, independent physical parameters may be chosen as

\[
\Theta_{\rm TP-D}=\{
m_A^2,m_B^2,|\mu_A|,|\mu_B|,
\lambda_A,\lambda_B,\lambda_{AB},\lambda_{HA},\lambda_{HB}
\}.
\]

Independent rephasings of \(A\) and \(B\) make \(\mu_A\) and \(\mu_B\) real. Thus v0.1 has nine new physical continuous parameters. It has no scalar-sector CP phase.

## 8. Intended vacuum branch

\[
\langle H\rangle=\frac1{\sqrt2}\binom{0}{v},\qquad
\langle A\rangle=\langle B\rangle=0.
\]

The dark discrete group is unbroken on this branch. Tree-level dark-sector boundedness requires

\[
\lambda_A>0,\quad\lambda_B>0,\quad
\lambda_{AB}>-2\sqrt{\lambda_A\lambda_B}.
\]

A useful sufficient global-inert condition is

\[
\lambda_{AB}\ge0,\quad
|\mu_A|^2\le9\lambda_A m_A^2,\quad
|\mu_B|^2\le9\lambda_B m_B^2,
\]

with positive quadratic masses. The full Higgs-plus-dark global-vacuum conditions are not frozen yet.

After electroweak symmetry breaking,

\[
M_A^2=m_A^2+\frac12\lambda_{HA}v^2,\qquad
M_B^2=m_B^2+\frac12\lambda_{HB}v^2.
\]

## 9. Exact conservation laws

Every allowed amplitude obeys

\[
\sum_i q_{m,i}=0,\qquad \sum_i q_{E,i}=0\pmod3,
\]

or equivalently conserves both \(q_P\) and \(q_K\). Projected conservation alone is necessary but not sufficient.

## 10. Exact renormalizable exclusions

The following classes are forbidden by \(q_K\) although allowed by projected \(Z_3^{(P)}\):

\[
\partial A^\dagger\partial B,\quad A^\dagger B,\quad
A^2B,\quad AB^2,
\]

\[
|A|^2A^\dagger B,\quad |B|^2A^\dagger B,\quad
(A^\dagger B)^2,\quad(H^\dagger H)A^\dagger B,
\]

plus Hermitian conjugates. Exact symmetry prevents their perturbative regeneration.

## 11. Physical spectrum and stability

On the inert branch, \(A\) and \(B\) are unmixed complex mass eigenstates. The lightest state carrying each independent vector charge is stable. With no additional charged fields, both \(A\) and \(B\) are stable against decay into Standard-Model particles or into each other plus kernel-neutral states.

This is a two-component dark-sector possibility, not yet a successful dark-matter model. Relic abundance and experimental constraints remain open.

## 12. First falsifiable selection rule

For any collection \(X_0\) neutral under \(Z_3^{(K)}\),

\[
\boxed{\mathcal M(B\to A+X_0)=0}
\]

to all perturbative orders in exact TP-D. The special case \(X_0=h\) supplies the first benchmark null test.

Observation of a nonzero amplitude falsifies v0.1 if the states and exact-symmetry assumptions are independently established. A null result does not prove v0.1.

## 13. Controlled broken branch

TP-B adds a neutral-under-\(P\) breaking field

\[
\Sigma\sim(1,2),\qquad \langle\Sigma\rangle=w/\sqrt2.
\]

Its vacuum leaves \(Z_3^{(P)}\) but breaks \(Z_3^{(K)}\). The term

\[
\mu_\Sigma\Sigma A^\dagger B+\mathrm{h.c.}
\]

gives \(m_{AB}^2=\mu_\Sigma w/\sqrt2\). TP-B is a separate theory version and must not be used silently to rescue a failed exact-TP-D prediction.

## 14. Claim classification

| Claim | Status |
|---|---|
| \(\ker\pi\cong Z_3\) | exact mathematical result |
| TP-D operator basis | exact under frozen field/symmetry assumptions |
| absence of kernel-changing amplitudes | exact model-dependent result |
| two stable species on inert branch | model-dependent result |
| viable dark matter | open |
| unique phenomenological prediction | open |
| novel symmetry mechanism | not demonstrated; mechanism is known |
| matter/energy ontology of \(q_m,q_E\) | conjectural labels only |
| explanation of three generations | not derived |
| gravity or unification | outside v0.1 |

## 15. Failure conditions

TP-D v0.1 fails if any of the following occurs:

1. no electroweak-plus-dark global inert vacuum exists in the required parameter region;
2. perturbative unitarity fails below the intended validity scale;
3. RG evolution destroys stability before the stated cutoff;
4. the required two-component abundance conflicts with cosmology;
5. an experimentally identified kernel-changing transition is nonzero;
6. all accessible signatures remain statistically indistinguishable from a generic tuned \(Z_3\);
7. a claimed novelty is fully equivalent to prior art without a new prediction.

## 16. Frozen boundaries and next permitted work

The following are permitted next:

- full dimension-six operator basis;
- complete electroweak-plus-dark vacuum enumeration;
- independent one-loop TP-D RGEs;
- finite-energy coupled-channel unitarity;
- two-component Boltzmann system;
- collider/direct-detection identifiability study;
- minimal residual-gauge completion.

Gravity, flavour, cosmology beyond necessary relic/defect checks, and unification are not part of the frozen core and cannot be promoted until the preceding tests survive.

