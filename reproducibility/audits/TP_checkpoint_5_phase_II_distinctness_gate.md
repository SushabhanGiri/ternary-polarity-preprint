# Ternary Polarity Phase II — Kernel-Distinctness Audit

**Project:** *Ternary Polarity: Toward a \(Z_3\) Framework for Fundamental Physics*  
**Author:** Sushabhan Giri  
**Audit date:** 15 September 2026  
**Canonical branch tested:** TP-D  
**Scientific status:** speculative field-theory construction under audit; not an established theory of nature

## Executive verdict

\[
\boxed{\text{SUBSTANTIVE PARTIAL PASS}}
\]

The dual charge assignment

\[
A\sim(1,0),\qquad B\sim(0,1)
\]

under \(G_{\rm TP}=Z_3^{(m)}\times Z_3^{(E)}\) is physically more restrictive than assigning both fields charge one under only the projected group \(Z_3^{(P)}\). The extra restriction is not erased by a change of field basis: it is equivalently the existence of a noncentral order-three symmetry generator whose charge is conserved by the full action. It forbids a definite set of kinetic, mass, cubic, quartic, and Higgs-portal operators.

The strongest all-orders null prediction of the minimal exact model is

\[
\boxed{\mathcal M(B\rightarrow A+X_0)=0}
\]

for any final collection \(X_0\) neutral under the kernel symmetry, provided \(A\) and \(B\) are nondegenerate kernel-charge eigenstates and the full dual symmetry is exact. In particular,

\[
\boxed{\Gamma(B\rightarrow A+h)=0.}
\]

An ordinary single-\(Z_3\) theory permits the off-diagonal portal \((H^\dagger H)A^\dagger B+\mathrm{h.c.}\), so it generically permits this decay when kinematically open.

This passes the mathematical nonredundancy and radiative-protection tests. It does **not** yet pass the strong novelty or phenomenological-identifiability tests. Product discrete symmetries, symmetry-protected operator zeros, multicomponent dark sectors, and semi-annihilation are established model-building tools. A generic single-\(Z_3\) comparator can also tune its allowed off-diagonal couplings to zero. Consequently a null decay alone cannot positively identify TP-D, although observing a nonzero kernel-changing decay would falsify the exact minimal realization.

The branch therefore advances to the next research stage only as a **kernel-sensitive \(Z_3\times Z_3\) EFT**, not as a demonstrated new fundamental theory.

---

## Document A — Kernel and symmetry analysis

Define

\[
\pi:Z_3^{(m)}\times Z_3^{(E)}\longrightarrow Z_3^{(P)},\qquad
\pi(q_m,q_E)=q_m+q_E\pmod 3.
\]

Then

\[
\ker\pi=\{(0,0),(1,2),(2,1)\}\cong Z_3.
\]

The map is surjective and gives the split exact sequence

\[
0\longrightarrow Z_3\longrightarrow Z_3^2
\overset{\pi}{\longrightarrow}Z_3\longrightarrow0.
\]

A useful invertible change of charge coordinates over \(\mathbb F_3\) is

\[
p=q_m+q_E,\qquad k=q_m-q_E,
\]

because

\[
\det\begin{pmatrix}1&1\\1&-1\end{pmatrix}=-2\equiv1\pmod3.
\]

Thus the dual group can be written as \(Z_3^{(P)}\times Z_3^{(K)}\). In this basis,

\[
A:(p,k)=(1,1),\qquad B:(p,k)=(1,2).
\]

This establishes two facts that must be kept separate:

1. **Exact result:** \(A\) and \(B\) have the same projected charge but different kernel charge.
2. **Novelty limitation:** the abstract group is the standard direct product \(Z_3\times Z_3\). The names “matter-like” and “energy-like” do not add physics unless an independent construction gives those labels operational meaning.

Strictly, charges label characters while group elements act on fields. Because finite Abelian groups are isomorphic to their character groups, one may choose a self-dual pairing, but the identification is a convention. The physical statement is the existence of the extra transformation

\[
K=\operatorname{diag}(\omega,\omega^2),\qquad \omega=e^{2\pi i/3},
\]

acting on \(\Phi=(A,B)^T\). The projected generator is \(P=\omega I_2\).

### Kernel pass/fail result

If the action is invariant only under \(P\), the kernel is physically unobserved. If it is invariant under both \(P\) and \(K\), amplitudes must conserve both charges. The minimal TP-D action below is invariant under \(K\); therefore the kernel acts nontrivially.

---

## Documents B and C — Exact TP-D and generic-\(Z_3\) Lagrangians

Assume that \(A\) and \(B\) are Lorentz scalars and Standard-Model gauge singlets, while all Standard-Model fields are neutral under the new discrete factors. Natural units \(\hbar=c=1\) are used. Scalar fields have mass dimension one.

### Generic projected-\(Z_3\) comparator

Let \(\Phi=(A,B)^T\), with both components transforming as \(\Phi\to\omega\Phi\). The most general renormalizable scalar Lagrangian is

\[
\mathcal L_{Z_3}^{\rm generic}
=(\partial_\mu\Phi)^\dagger Z(\partial^\mu\Phi)-V_{Z_3},
\]

where \(Z\) is a positive Hermitian \(2\times2\) kinetic matrix. It can be made the identity by an invertible field redefinition. In a canonical kinetic basis,

\[
\begin{aligned}
V_{Z_3}={}&V_H+
m_A^2|A|^2+m_B^2|B|^2
 +\left(m_{AB}^2A^\dagger B+\mathrm{h.c.}\right)\\
&+\left[\frac{\mu_A}{3}A^3+\mu_{AAB}A^2B
+\mu_{ABB}AB^2+\frac{\mu_B}{3}B^3+\mathrm{h.c.}\right]\\
&+\lambda_A|A|^4+\lambda_B|B|^4+\lambda_{AB}|A|^2|B|^2\\
&+\left[\eta_A|A|^2A^\dagger B
+\eta_B|B|^2A^\dagger B
+\frac{\eta_2}{2}(A^\dagger B)^2+\mathrm{h.c.}\right]\\
&+(H^\dagger H)\left[\lambda_{HA}|A|^2+\lambda_{HB}|B|^2
+\left(\lambda_{HAB}A^\dagger B+\mathrm{h.c.}\right)\right].
\end{aligned}
\]

Here \(V_H=-m_H^2H^\dagger H+\lambda_H(H^\dagger H)^2\). Hermiticity makes \(m_A^2,m_B^2,\lambda_A,\lambda_B,\lambda_{AB},\lambda_{HA},\lambda_{HB}\) real; the displayed phase-sensitive coefficients may be complex.

### Exact dual TP-D

Requiring the full \(Z_3^{(m)}\times Z_3^{(E)}\) gives

\[
\begin{aligned}
\mathcal L_{\rm TP-D}={}&|\partial A|^2+|\partial B|^2-V_{\rm TP-D},\\
V_{\rm TP-D}={}&V_H+m_A^2|A|^2+m_B^2|B|^2
+\left(\frac{\mu_A}{3}A^3+\frac{\mu_B}{3}B^3+\mathrm{h.c.}\right)\\
&+\lambda_A|A|^4+\lambda_B|B|^4+\lambda_{AB}|A|^2|B|^2\\
&+(H^\dagger H)(\lambda_{HA}|A|^2+\lambda_{HB}|B|^2).
\end{aligned}
\]

Nonzero \(\mu_A\) and \(\mu_B\) are important: without them, the renormalizable potential has the larger accidental symmetry \(U(1)_A\times U(1)_B\). The two cubics reduce this to the intended \(Z_3\times Z_3\).

---

## Document D — Complete distinguishing operator table

The enumerator treats Hermitian-conjugate pairs as one operator class. It finds 3 projected-\(Z_3\)-invariant quadratic, 4 cubic, and 6 quartic nonderivative classes. The six comparator-only nonderivative classes are exactly those shown below.

| Operator class | Dimension | Generic \(Z_3^{(P)}\) | Exact TP-D | Consequence if present |
|---|---:|:---:|:---:|---|
| \(\partial A^\dagger\partial B+\mathrm{h.c.}\) | 4 | allowed | forbidden | kinetic flavour mixing |
| \(A^\dagger B+\mathrm{h.c.}\) | 2 | allowed | forbidden | mass mixing and oscillation |
| \(A^2B+\mathrm{h.c.}\) | 3 | allowed | forbidden | conversion/decay vertices |
| \(AB^2+\mathrm{h.c.}\) | 3 | allowed | forbidden | conversion/decay vertices |
| \(|A|^2A^\dagger B+\mathrm{h.c.}\) | 4 | allowed | forbidden | flavour-changing scattering |
| \(|B|^2A^\dagger B+\mathrm{h.c.}\) | 4 | allowed | forbidden | flavour-changing scattering |
| \((A^\dagger B)^2+\mathrm{h.c.}\) | 4 | allowed | forbidden | pair conversion |
| \((H^\dagger H)A^\dagger B+\mathrm{h.c.}\) | 4 | allowed | forbidden | Higgs-mediated transition/decay |

The common nonderivative classes are

\[
|A|^2,\ |B|^2,\ A^3+\mathrm{h.c.},\ B^3+\mathrm{h.c.},\
|A|^4,\ |B|^4,\ |A|^2|B|^2.
\]

The Standard-Model Higgs adds the common portals \((H^\dagger H)|A|^2\) and \((H^\dagger H)|B|^2\). No renormalizable linear singlet portal is allowed because \(A\) and \(B\) have nonzero projected charge.

The enumeration is exhaustive for nonderivative monomials in two commuting complex singlets through dimension four. Gauge-field and Standard-Model-only operators are common to both theories and cancel from the comparator.

Therefore

\[
\Delta\mathcal L
=\mathcal L_{Z_3}^{\rm generic}-\mathcal L_{\rm TP-D}
\]

is precisely the set of cross terms in the table, modulo field-basis normalization.

---

## Document E — Spectrum and mixing analysis

In the generic comparator, the quadratic matrix is

\[
M^2=\begin{pmatrix}
m_A^2&m_{AB}^2\\
m_{AB}^{2*}&m_B^2
\end{pmatrix}.
\]

After one relative rephasing makes \(m_{AB}^2\) real and nonnegative,

\[
m_\pm^2=\frac{m_A^2+m_B^2}{2}
\pm\frac12\sqrt{(m_B^2-m_A^2)^2+4|m_{AB}^2|^2},
\]

and

\[
\tan2\theta=\frac{2|m_{AB}^2|}{m_B^2-m_A^2}.
\]

For \(|m_{AB}^2|\ll|m_B^2-m_A^2|\),

\[
\theta\simeq\frac{|m_{AB}^2|}{m_B^2-m_A^2}.
\]

Exact TP-D enforces

\[
m_{AB}^2=0,\qquad \theta=0.
\]

The numerical diagonalization test agreed with the analytic eigenvalues to \(1.2\times10^{-10}\ \mathrm{GeV}^2\) for the stored test point; 100 randomized regression points passed.

### Oscillation statement

For coherent relativistic propagation in a broken model,

\[
P(A\to B;L)=\sin^2(2\theta)
\sin^2\!\left(\frac{\Delta m^2L}{4E}\right).
\]

In exact TP-D, \(P(A\to B;L)=0\). This is meaningful only if production and detection define the interaction basis and coherence is maintained. It must not be advertised as a generic prediction before an experimental realization is specified.

---

## Basis-invariance audit

The statement “the off-diagonal entry vanishes” is basis dependent. The physically invariant statement is that there exists a noncentral unitary matrix \(K\), with

\[
K^3=I,\qquad K\not\propto I,
\]

that leaves **every** coupling tensor invariant. For the quadratic tensor,

\[
K^\dagger M^2K=M^2.
\]

Under a basis transformation \(\Phi\to U\Phi\),

\[
M^2\to UM^2U^\dagger,\qquad K\to UKU^\dagger,
\]

so the existence of the symmetry is unchanged. One diagnostic is

\[
I_M(K)=\operatorname{Tr}\!\left[
(K^\dagger M^2K-M^2)^\dagger(K^\dagger M^2K-M^2)
\right].
\]

Exact invariance requires \(I_M=0\), together with analogous zero residuals for the cubic, quartic, and portal tensors.

A mass matrix by itself is insufficient: one can diagonalize any Hermitian matrix and invent a diagonal order-three matrix in that basis. The nontrivial test is whether the **same** \(K\) leaves all interaction tensors invariant. TP-D passes this simultaneous-tensor test by construction. The generic comparator does not pass it for generic coefficients.

The matrix element between nondegenerate charge eigenstates,

\[
\langle A;X_0|S|B\rangle,
\]

is an observable. If \([S,K]=0\) and \(X_0\) is kernel neutral, its initial and final kernel phases differ, forcing the amplitude to zero. That is the basis-independent content of the selection rule.

---

## Parameter-count audit

Shared Standard-Model parameters are omitted.

### Generic projected \(Z_3\)

After canonicalizing the kinetic term:

- Hermitian mass matrix: 4 real parameters;
- complex symmetric cubic rank-three tensor in two flavours: 8;
- Hermitian quartic tensor on \(\operatorname{Sym}^2(\mathbb C^2)\): 9;
- Hermitian Higgs-portal matrix: 4.

This gives 25 real coefficients. A common \(U(2)\) field-basis transformation removes four redundancies, leaving

\[
N_{\rm phys}^{Z_3}=21
\]

for a generic point with no accidental stabilizer.

### Exact TP-D

The exact dual potential has 2 real masses, 2 complex cubics, 3 real dark quartics, and 2 real diagonal Higgs portals: 11 real coefficients. Two independent field rephasings remove the two cubic phases, leaving

\[
N_{\rm phys}^{\rm TP-D}=9.
\]

Thus this realization removes twelve physical continuous parameters relative to the most general projected comparator:

\[
\Delta N_{\rm phys}=12.
\]

This is real parameter compression, but most of it consists of symmetry-protected zeros. No nonzero numerical sum rule has yet been derived.

---

## Document F — Vacuum and stability audit

The exact dark quartic is

\[
V_4=\lambda_A|A|^4+\lambda_B|B|^4+\lambda_{AB}|A|^2|B|^2.
\]

Its exact tree-level bounded-from-below conditions are

\[
\lambda_A>0,\qquad \lambda_B>0,\qquad
\lambda_{AB}>-2\sqrt{\lambda_A\lambda_B},
\]

with non-strict boundary variants requiring separate flat-direction analysis.

For one field, after minimizing its phase,

\[
V_i(r)=m_i^2r^2-\frac{2|\mu_i|}{3}r^3+\lambda_i r^4.
\]

The origin is no higher than every nonzero stationary point when

\[
|\mu_i|^2\le 9\lambda_i m_i^2.
\]

Therefore the following are simple sufficient conditions for the two-field origin to be the global minimum:

\[
\lambda_{AB}\ge0,\qquad
|\mu_A|^2\le9\lambda_A m_A^2,\qquad
|\mu_B|^2\le9\lambda_B m_B^2,
\]

in addition to positive masses and self-quartics. They are sufficient, not necessary. A negative portal requires a full mixed stationary-point analysis.

The stored benchmark

\[
(m_A,m_B,|\mu_A|,|\mu_B|)=(180,400,60,90)\ \mathrm{GeV},
\]

\[
(\lambda_A,\lambda_B,\lambda_{AB})=(0.20,0.25,0.10)
\]

passes these sufficient conditions. A deterministic 200,000-point log-radial numerical search with seed 20260915 found no negative value after phase minimization. This numerical scan corroborates the analytic sufficient proof; it is not the proof itself.

Higgs-portal terms shift the physical masses after electroweak symmetry breaking:

\[
M_A^2=m_A^2+\frac12\lambda_{HA}v^2,\qquad
M_B^2=m_B^2+\frac12\lambda_{HB}v^2.
\]

The full electroweak-plus-dark global-vacuum audit remains to be performed for a final phenomenology benchmark.

---

## Document G — High-energy unitarity audit

Writing

\[
A=(a_1+ia_2)/\sqrt2,\qquad B=(b_1+ib_2)/\sqrt2,
\]

the normalized ten-channel real-scalar quartic scattering matrix has eigenvalues

\[
2\lambda_A\quad(\times2),\qquad
2\lambda_B\quad(\times2),\qquad
\lambda_{AB}\quad(\times4),
\]

and

\[
2(\lambda_A+\lambda_B)
\pm\sqrt{4(\lambda_A-\lambda_B)^2+\lambda_{AB}^2}.
\]

With the convention \(a_0=-\Lambda/(16\pi)\), tree-level perturbative unitarity requires every eigenvalue \(\Lambda\) to satisfy

\[
|\Lambda|\le8\pi.
\]

For the stored benchmark the spectral radius is 1.041421356, far below \(8\pi\). The analytic spectrum was verified against the directly constructed \(10\times10\) tensor matrix at 100 randomized coupling points with relative and absolute tolerances \(10^{-12}\).

**Scope limitation:** this is the high-energy dark-scalar quartic limit. A final benchmark still requires Higgs/Goldstone channels and finite-energy exchange diagrams with pole excision. Thus the complete finite-energy unitarity item is open.

---

## Document H — Radiative-stability audit

Every exact-TP-D vertex has total vector charge \((0,0)\). Charge adds at internal contractions, so every perturbative diagram with external legs of nonzero total vector charge vanishes. Equivalently, a symmetry-preserving regulator and subtraction scheme produce a renormalized effective action satisfying

\[
\Gamma[\omega A,B]=\Gamma[A,B],\qquad
\Gamma[A,\omega B]=\Gamma[A,B].
\]

Consequently no counterterm proportional to

\[
A^\dagger B,\quad A^2B,\quad AB^2,
\quad |A|^2A^\dagger B,\quad |B|^2A^\dagger B,
\quad(A^\dagger B)^2,
\quad(H^\dagger H)A^\dagger B
\]

can be generated while the full symmetry is exact. In particular,

\[
\left.\beta_{m_{AB}^2}\right|_{\text{all kernel-breaking spurions}=0}=0.
\]

This conclusion holds to all perturbative orders. The scalar-only model has no chiral gauge anomaly. A parent gauge completion containing chiral fermions would require a separate continuous and residual-discrete anomaly audit.

### Controlled breaking TP-B

Introduce a scalar spurion/field

\[
\Sigma\sim(1,2),\qquad q_P(\Sigma)=0.
\]

A vacuum expectation value \(\langle\Sigma\rangle=w/\sqrt2\) preserves the diagonal projected subgroup but breaks the kernel symmetry. The renormalizable term

\[
\mu_\Sigma\Sigma A^\dagger B+\mathrm{h.c.}
\]

generates

\[
m_{AB}^2=\frac{\mu_\Sigma w}{\sqrt2}.
\]

Similarly, \(\Sigma A^2B\) and \(\Sigma^\dagger AB^2\) generate mixed cubics linearly in \(w\). Off-diagonal kinetic, quartic, and Higgs-portal terms arise through dimension-five operators and scale as \(w/\Lambda\) in the minimal EFT. Hence

\[
\theta\sim\frac{\mu_\Sigma w}{\sqrt2\,(m_B^2-m_A^2)},
\qquad
\Gamma_{K\text{-violating}}\propto w^2
\]

at leading order, provided no lower-order breaking source exists. The coefficients remain independent Wilson coefficients; symmetry alone does not give a numerical sum rule among them.

---

## Document I — Minimal falsification benchmark

Take the illustrative masses

\[
M_A=180\ \mathrm{GeV},\qquad M_B=400\ \mathrm{GeV},\qquad
m_h=125.25\ \mathrm{GeV},
\]

so \(B\to A+h\) is kinematically open. In the generic comparator, after electroweak symmetry breaking,

\[
(H^\dagger H)A^\dagger B+\mathrm{h.c.}
\supset \lambda_{HAB}v\,hA^\dagger B+\mathrm{h.c.}
\]

and

\[
\Gamma(B\to Ah)=
\frac{|\lambda_{HAB}v|^2}{16\pi M_B}
\lambda^{1/2}\!\left(1,\frac{M_A^2}{M_B^2},\frac{m_h^2}{M_B^2}\right).
\]

For the purely illustrative comparator value \(\lambda_{HAB}=0.01\), the stored calculation gives

\[
\Gamma_{Z_3}(B\to Ah)=1.93024\times10^{-4}\ \mathrm{GeV},
\]

whereas exact TP-D gives zero.

This number is not a TP prediction; \(\lambda_{HAB}=0.01\) was chosen only to display an effect size. The robust prediction is the exact zero.

### Falsification card

Under the assumptions that:

1. the observed states are the two nondegenerate TP-D charge eigenstates;
2. the visible final state is kernel neutral;
3. no explicit or spontaneous kernel breaking occurs;
4. the tested decay is kinematically allowed;

then

> **Any statistically significant nonzero \(B\to A+h\) amplitude falsifies exact minimal TP-D.**

A null result does not prove TP-D because the generic comparator may set \(\lambda_{HAB}=0\) accidentally. Positive model identification would require observing both species and enough independent allowed and forbidden channels to infer the extra conserved charge.

---

## Document J — Preliminary novelty matrix

| Feature | Generic single \(Z_3\) | Established enlarged discrete models | TP-D result | Novelty status |
|---|---|---|---|---|
| residual charge-one fields | yes | yes | yes | known |
| cubic \(Z_3\) self-interactions | yes | yes | \(A^3,B^3\) | known |
| semi-annihilation | yes | yes | allowed within each sector | known |
| multiple stable species | possible | established | natural if each is lightest in its vector-charge sector | known mechanism |
| extra conserved kernel charge | no | yes for product groups | yes | known group mechanism |
| forbidden \(A^\dagger B\) | not generic | common when charges differ under extra factor | yes | known selection-rule consequence |
| all-orders null \(B\to A+X_0\) | not generic | standard consequence of an exact extra charge | yes | known mechanism, TP-specific labeling |
| \(q_P=q_m+q_E\) projection | optional relabeling | homomorphisms are standard | central organizing map | known mathematics; combination-specific |
| nonzero numerical sum rule | none required | model dependent | none found | absent |
| unique experimental signature | no | model dependent | not yet demonstrated | open |

Relevant prior work already establishes the nearby physics:

- G. Bélanger, K. Kannike, A. Pukhov, and M. Raidal, [“Impact of semi-annihilations on dark matter phenomenology—an example of \(Z_N\)-symmetric scalar dark matter”](https://arxiv.org/abs/1202.2962), develops discrete-charge operator selection, semi-annihilation, and enlarged-symmetry multicomponent sectors.
- P. Ko and Y. Tang, [“Self-interacting scalar dark matter with local \(Z_3\) symmetry”](https://arxiv.org/abs/1402.6449), realizes local \(Z_3\) as a remnant of a broken dark \(U(1)\).
- C. E. Yaguna and Ó. Zapata, [“Multi-component scalar dark matter from a \(Z_N\) symmetry: a systematic analysis”](https://arxiv.org/abs/1911.05515), shows that multiple stable scalar species and nontrivial conversion patterns already arise in established discrete-symmetry models.
- D. Borah, E. Ma, and D. Nanda, [“Dark \(SU(2)\to Z_3\times Z_2\) Gauge Symmetry”](https://arxiv.org/abs/2212.11847), is a concrete example of product residual discrete symmetry used to organize multiple dark states.

Therefore the present construction has **not** passed a claim of demonstrable literature novelty. Its defensible contribution at this checkpoint is a precise TP-specific formulation and comparator audit, not discovery of product-discrete dark matter.

---

## Document K — Gate report

### 1. Executive verdict

\[
\boxed{\text{SUBSTANTIVE PARTIAL PASS}}
\]

### 2. What survived

- The projection has a nontrivial three-element kernel.
- The minimal two-field representation makes the kernel act nontrivially.
- The complete renormalizable operator basis differs from the generic projected-\(Z_3\) basis.
- The distinction is expressible as a basis-invariant symmetry of all coupling tensors.
- Kernel-changing amplitudes vanish to all perturbative orders in the exact model.
- A healthy inert tree-level benchmark exists under explicit sufficient conditions.
- The dark-scalar high-energy unitarity matrix is perturbative at that benchmark.
- Exact TP-D removes twelve physical continuous parameters relative to the generic comparator under the stated counting assumptions.

### 3. What failed or remains incomplete

- No unique nonzero numerical relation or sum rule has been found.
- A null transition is not positive evidence because generic \(Z_3\) can tune the corresponding coupling to zero.
- The core group and its selection-rule mechanism are already known mathematics and model-building technology.
- Full electroweak-plus-dark vacuum analysis is unfinished.
- Full finite-energy scalar/Higgs/Goldstone/gauge unitarity is unfinished.
- The complete one-loop RGE system for TP-D has not yet been independently regenerated, although the forbidden-operator surface is protected exactly by symmetry.
- No relic-density, collider-production, detector-background, or global-likelihood analysis has yet established practical accessibility.
- A gauge-origin and anomaly-free completion has not yet been constructed.

### 4. What is genuinely new

No element is yet demonstrably new after literature comparison. The potentially original contribution is the **specific interpretation and systematic use of the projection/kernel pair as the defining TP architecture**, together with a future overconstrained observable pattern. That claim remains “known ingredients, newly combined” until a broader search and a distinctive prediction succeed.

### 5. What is known physics

Finite Abelian product groups, residual discrete symmetries, multicomponent stable sectors, cubic \(Z_3\) interactions, semi-annihilation, symmetry-protected coupling zeros, and forbidden-transition null tests are known.

### 6. First distinctive prediction

For exact minimal TP-D,

\[
\boxed{\mathcal M(B\to A+X_0)=0}
\]

whenever \(X_0\) is kernel neutral. This differs from the generic single-\(Z_3\) theory, which allows the amplitude.

### 7. Experimental falsification condition

Observation of any kernel-changing transition, such as \(B\to A+h\), excludes exact TP-D under the explicit four assumptions in the falsification card.

### 8. Remaining blockers, ranked

1. **Critical:** find an identifiable pattern or nonzero relation that generic \(Z_3\) cannot imitate by tuning.
2. **Critical:** establish production and detection channels for both charge eigenstates.
3. **High:** complete current-data phenomenology and coupled relic-density analysis.
4. **High:** finish electroweak vacuum and finite-energy unitarity audits.
5. **High:** independently derive the full TP-D one-loop RGEs.
6. **Medium:** construct and audit a minimal residual-gauge completion.
7. **Medium:** complete a systematic prior-art search for the exact operator basis and signature.

### 9. Confidence assessment

| Domain | Confidence | Reason |
|---|---|---|
| finite-group and operator algebra | high | exhaustive enumeration plus analytic charge proof |
| mass and basis analysis | high | exact formulas and randomized numerical cross-checks |
| tree-level dark vacuum | medium-high | exact BFB and sufficient global-origin proof; not full Higgs system |
| high-energy dark-scalar unitarity | high within stated scope | direct tensor construction and randomized spectral test |
| all-orders selection-rule protection | high | exact finite symmetry and scalar-only anomaly status |
| phenomenology | low-medium | one illustrative decay; no production/global constraint study |
| novelty | low | nearby mechanisms are established; exact combination not exhaustively searched |
| experimental accessibility | low-medium | possible in principle, no detector-level analysis |

### 10. Recommendation

\[
\boxed{\text{Continue TP-D conditionally; do not promote it beyond a }Z_3\times Z_3\text{ EFT.}}
\]

The immediate next objective is not gravity or grand unification. It is to construct a minimal visible/dark portal with more measured quantities than free parameters and search for a correlated set of kernel-conserving and kernel-violating rates. If no such overconstrained pattern exists, TP-D remains a valid conventional product-discrete EFT rather than a new theoretical framework.

---

## Reproducibility record

- Operator enumerator: `code/dual_tp_operator_enumerator.py`
- Machine-readable operator basis: `audits/dual_tp_operator_basis.json`
- Vacuum, spectrum, unitarity, and decay validator: `code/dual_tp_validation.py`
- Machine-readable numerical output: `audits/dual_tp_validation.json`
- Regression tests: `code/test_dual_tp.py`
- Test result: 5/5 passed on 15 September 2026.

The numerical vacuum scan used NumPy 2.3.5, 200,000 samples, seed 20260915, and log-uniform radial sampling. The analytic inequalities, not the scan, establish the stated sufficient vacuum result.
