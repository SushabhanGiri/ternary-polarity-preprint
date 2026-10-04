# TP-D Canonical Theory Definition Sheet — v0.2

**Supersedes:** TP-D v0.1 for subsequent calculations  
**Freeze date:** 19 September 2026  
**Status:** surviving low-energy product-discrete scalar EFT; phenomenology and novelty unresolved  
**Not claimed:** experimental confirmation, unique novelty, Standard-Model unification, quantum gravity, or Theory of Everything

## 1. Exact core

\[
G_{\rm TP-D}=Z_3^{(m)}\times Z_3^{(E)}
\cong Z_3^{(P)}\times Z_3^{(K)},
\]

\[
q_P=q_m+q_E,\qquad q_K=q_m-q_E\pmod3.
\]

The projection \(\pi(q_m,q_E)=q_P\) has

\[
\ker\pi=\{(0,0),(1,2),(2,1)\}\cong Z_3.
\]

The field assignments are

| Field | Lorentz and SM representation | \((q_m,q_E)\) | \((q_P,q_K)\) |
|---|---|---:|---:|
| \(H\) | scalar, \((1,2,+\tfrac12)\) | \((0,0)\) | \((0,0)\) |
| \(A\) | complex scalar, \((1,1,0)\) | \((1,0)\) | \((1,1)\) |
| \(B\) | complex scalar, \((1,1,0)\) | \((0,1)\) | \((1,2)\) |

All Standard-Model fields are neutral under both discrete factors. Charges are internal representation labels; \(q=2\) is not negative energy or negative mass.

## 2. Canonical renormalizable action

In four-dimensional Minkowski spacetime with signature \((+,-,-,-)\),

\[
S=\int d^4x\left[\mathcal L_{\rm SM}+|\partial A|^2+|\partial B|^2-V\right],
\]

\[
\begin{aligned}
V={}&-\mu_H^2H^\dagger H+\lambda_H(H^\dagger H)^2
+m_A^2|A|^2+m_B^2|B|^2\\
&+\left(\frac{\mu_A}{3}A^3+\frac{\mu_B}{3}B^3+\mathrm{h.c.}\right)
+\lambda_A|A|^4+\lambda_B|B|^4+\lambda_{AB}|A|^2|B|^2\\
&+\lambda_{HA}(H^\dagger H)|A|^2
+\lambda_{HB}(H^\dagger H)|B|^2.
\end{aligned}
\]

This is the complete renormalizable scalar action for the frozen fields and symmetry. Independent rephasings make \(\mu_A\) and \(\mu_B\) real, leaving nine new continuous scalar parameters:

\[
\{m_A^2,m_B^2,|\mu_A|,|\mu_B|,
\lambda_A,\lambda_B,\lambda_{AB},\lambda_{HA},\lambda_{HB}\}.
\]

The common literature normalization \(\mu_3(S^3+S^{\dagger3})/2\) is related by \(\mu_3=2\mu_A/3\). Published cubic bounds must be converted before use.

## 3. Intended inert vacuum

\[
\langle H\rangle=\frac1{\sqrt2}\binom0v,
\qquad
\langle A\rangle=\langle B\rangle=0.
\]

The physical tree masses are

\[
M_A^2=m_A^2+\frac12\lambda_{HA}v^2,
\qquad
M_B^2=m_B^2+\frac12\lambda_{HB}v^2.
\]

For \(x=H^\dagger H\), \(y=|A|^2\), and \(z=|B|^2\), the exact quartic boundedness test is copositivity of

\[
Q=\begin{pmatrix}
\lambda_H&\lambda_{HA}/2&\lambda_{HB}/2\\
\lambda_{HA}/2&\lambda_A&\lambda_{AB}/2\\
\lambda_{HB}/2&\lambda_{AB}/2&\lambda_B
\end{pmatrix}.
\]

A sufficient analytic global-inert certificate is

\[
\mu_H^2>0,\quad m_A^2>0,\quad m_B^2>0,
\]

\[
\lambda_{HA},\lambda_{HB},\lambda_{AB}\ge0,
\]

\[
|\mu_A|^2\le9\lambda_A m_A^2,
\qquad
|\mu_B|^2\le9\lambda_B m_B^2,
\]

together with exact copositivity. It is sufficient, not necessary.

## 4. Benchmark B0

At \(\mu_0=173\,\mathrm{GeV}\),

\[
M_A=180\,\mathrm{GeV},\quad M_B=400\,\mathrm{GeV},
\quad |\mu_A|=60\,\mathrm{GeV},\quad |\mu_B|=90\,\mathrm{GeV},
\]

\[
\lambda_A=0.20,\quad\lambda_B=0.25,\quad\lambda_{AB}=0.10,
\quad\lambda_{HA}=0.020,\quad\lambda_{HB}=0.030.
\]

B0 has an analytically certified global tree-level inert vacuum. Its full 36-channel high-energy scalar/Goldstone quartic matrix and its 15-channel finite-energy physical-scalar matrix satisfy tree-level partial-wave unitarity over the tested range. It is retained as a theoretical regression point, not as a viable thermal-dark-matter benchmark.

At one loop, B0 loses the BFB condition through the Higgs direction at

\[
\mu_{\rm BFB}\simeq3.57\times10^8\,\mathrm{GeV}.
\]

The leading quartic-bounce diagnostic gives \(S_4\simeq961\) below the first scalar-unitarity boundary and is compatible with a long-lived vacuum, but it is UV sensitive and is not a precision lifetime result.

A leading coupled freeze-out calculation, including annihilation,
semi-annihilation, and \(B\bar B\leftrightarrow A\bar A\) conversion, gives

\[
\Omega_{\rm TP}h^2\simeq1.82
\]

for B0, compared with the measured \(\Omega_ch^2\simeq0.120\). Varying
constant \(g_*\) from 80 to 100 gives \(1.94\) to \(1.72\), and even a
factor-ten increase of all number-changing rates leaves approximately \(0.36\).
Accordingly B0 is rejected as a standard thermal-relic benchmark. Precision
thermal averaging and independent matrix-element regeneration remain required
for future candidate points, not for continued promotion of B0.

## 5. Diagnostic running variants

### B1

\[
\lambda_{HA}=\lambda_{HB}=0.18.
\]

B1 keeps the quartic potential copositive but loses the simple inert certificate when \(\mu_H^2\) crosses zero near \(2.31\times10^8\,\mathrm{GeV}\). It is a trade-off diagnostic, not a promoted benchmark.

### B2

\[
\lambda_{HA}=0.2385,\qquad\lambda_{HB}=0.
\]

B2 concentrates the portal on the lighter species and extends the certificate to approximately \(1.46\times10^{15}\,\mathrm{GeV}\). Its minimum BFB margin is only \(3.3\times10^{-6}\), making it near-critical and sensitive to omitted higher-order effects. It is not a phenomenological benchmark.

## 6. Exact selection rules

Every amplitude conserves both independent charges:

\[
\sum_iq_{m,i}=0,qquad\sum_iq_{E,i}=0\pmod3.
\]

Consequently, the following projected-\(Z_3\)-allowed structures are absent:

\[
\partial A^\dagger\partial B,\quad A^\dagger B,\quad A^2B,\quad AB^2,
\]

\[
|A|^2A^\dagger B,\quad |B|^2A^\dagger B,\quad(A^\dagger B)^2,
\quad(H^\dagger H)A^\dagger B,
\]

plus Hermitian conjugates. Exact symmetry protects these zeros under perturbative renormalization.

For kernel-neutral \(X_0\),

\[
\mathcal M(B\to A+X_0)=0.
\]

This null result falsifies exact TP-D if a nonzero transition is observed under the frozen assumptions. A null observation does not uniquely identify TP-D because a generic single-\(Z_3\) model can tune the same couplings to zero.

## 7. One-loop quantum status

The six scalar-quartic beta functions and the five dimensionful scalar beta functions have each been regenerated using two independent exact methods. The dimensionful pure-scalar system is

\[
\begin{aligned}
16\pi^2\beta_{\mu_H^2}&=12\lambda_H\mu_H^2-2\lambda_{HA}m_A^2-2\lambda_{HB}m_B^2+\text{SM terms},\\
16\pi^2\beta_{m_A^2}&=8\lambda_A m_A^2+2\lambda_{AB}m_B^2-4\lambda_{HA}\mu_H^2+4|\mu_A|^2,\\
16\pi^2\beta_{m_B^2}&=8\lambda_B m_B^2+2\lambda_{AB}m_A^2-4\lambda_{HB}\mu_H^2+4|\mu_B|^2,\\
16\pi^2\beta_{\mu_A}&=12\lambda_A\mu_A,\\
16\pi^2\beta_{\mu_B}&=12\lambda_B\mu_B.
\end{aligned}
\]

Threshold matching, two-loop terms, and a full multi-field tunnelling calculation remain open.

## 8. Physical interpretation and novelty boundary

TP-D is physically more restrictive than a generic theory containing only projected \(Z_3^{(P)}\), because the kernel charge removes operators and amplitudes. Mathematically, however, it is an ordinary \(Z_3\times Z_3\) product-discrete model. A conditional tree-level alignment sum rule has been derived for a separate softly broken branch, TP-Bsoft, but it is standard two-state mixing algebra and has not been shown to be uniquely Ternary Polarity. No experimentally unique prediction has yet been obtained.

The labels \(m\) and \(E\) do not establish matter and energy as new ontological charges. They remain historical/mnemonic names until a deeper construction connects them to independently measurable quantities.

## 9. Current gate status

| Requirement | Status |
|---|---|
| Lorentz-covariant local scalar EFT | Achieved |
| Positive kinetic terms and healthy inert spectrum | Achieved for B0 |
| Exact operator basis | Achieved |
| Exact tree BFB test | Achieved |
| Global inert tree vacuum | Achieved for B0 |
| High-energy scalar unitarity | Achieved for B0 |
| Finite-energy physical-scalar unitarity | Achieved for B0 to 20 TeV |
| Scalar one-loop quartic RGEs | Achieved |
| Scalar one-loop dimensionful RGEs | Achieved |
| Threshold/two-loop stability | Leading 1 TeV step matching completed for TP-G0; finite thresholds, dimensionful parent running, and two loops remain open |
| Gauge-origin/anomaly completion | Minimal scalar-only TP-G0 parent constructed and anomaly-free; scalar parent RG derived, but full gauge-sector unitarity and phenomenology remain open |
| Relic density and current experimental viability | B0 fails the leading coupled thermal-relic test by overproduction; a viable scan is open, and frozen TP-G0 also contains an unintended stable or long-lived \(\rho_E\) state |
| Nonzero TP-specific prediction | Conditional TP-Bsoft tree relation derived; observability, loop completion, and novelty remain open |
| Literature novelty | Not demonstrated |
| Gravity, flavour, or unification | Not part of TP-D v0.2 |

## 10. Promotion and failure rules

No gravity, flavour, cosmology beyond necessary dark-sector tests, or unification module may be promoted from conjecture until:

1. a minimal gauge-origin option is frozen and anomaly audited, or the EFT is explicitly retained without that claim;
2. threshold and relevant higher-order uncertainties are quantified;
3. a viable laboratory/cosmological parameter region exists;
4. a kernel-sensitive observable is statistically identifiable;
5. literature comparison shows what, if anything, is new.

TP-D must be demoted to a conventional product-discrete EFT if no distinctive observable survives these tests.

## 11. Separation from the TP-G0 parent

TP-D v0.2 is the standalone low-energy theory.  A candidate scalar-only
parent, TP-G0, realizes its symmetry through
\(U(1)_m\times U(1)_E\to Z_3^{(m)}\times Z_3^{(E)}\), but adds radial and vector
states around its breaking scale.  Consequently the B0/B1/B2 running in this
document applies only while TP-D is the active EFT.  For the illustrative
TP-G0 point, new thresholds occur near \(0.63\) and \(0.90\,\mathrm{TeV}\), so
the standalone TP-D flow cannot be extrapolated through them.  Matching and
parent beta functions are required before assigning any ultraviolet scale to
TP-G0.

The scalar part of that parent beta system has now been derived. It proves
that the factorized conditions

\[
\lambda_{A\Phi_m}=\lambda_{B\Phi_E}=0
\]

are not RG invariant. At zero coupling,

\[
16\pi^2\beta_{\lambda_{A\Phi_m}}=36\kappa_m^2+108g_m^4,
\qquad
16\pi^2\beta_{\lambda_{B\Phi_E}}=36\kappa_E^2+108g_E^4.
\]

A leading common-threshold evolution gives a Higgs-direction BFB failure near
\(3.56\times10^8\,\mathrm{GeV}\), a scalar-unitarity boundary near
\(3.33\times10^{16}\,\mathrm{GeV}\), and a \(4\pi\) boundary near
\(6.28\times10^{16}\,\mathrm{GeV}\). These are TP-G0 diagnostic scales, not
precision predictions or evidence for UV completion.

The frozen TP-G0 mass hierarchy also fails an initial cosmological prefilter:
the \(E\)-sector radial mode satisfies

\[
m_{\rho_E}<2m_B,\qquad m_{\rho_E}<3m_B,\qquad
m_{\rho_E}<2M_{X_E},
\]

while the relevant parent portals were set to zero at matching. It therefore
has no open tree-level decay in that benchmark and becomes an unintended
stable or long-lived relic. This does not invalidate every TP-G completion,
but it prevents promotion of the frozen TP-G0 point until its lifetime,
abundance, and a minimal repair are audited.
