# How Lean Can Help with Proofs in `Adap-KRR.tex`

This note maps proof-heavy parts of the KRR paper to concrete Lean (Lean 4 + mathlib) workflows.

## 1) Proof targets identified in the paper

From `Adap-KRR.tex`, the main formal-proof targets are:

- `Lemma:Optimal-KRR` (optimal rates with oracle `lambda*`).
- `Proposition:crucial-stopping-KRR` (spectral difference bound between `f_{D,lambda}` and `f_{D,lambda'}`).
- `Theorem:ASUS` (adaptive selection achieves optimal rates).
- Supporting lemmas used in the theorem proof:
  - `Lemma:Q` (bounds for `S_{D,lambda}`, `Q_{D,lambda}`, `P_{D,lambda}`, empirical effective dimension relation),
  - `Lemma:Error-Decomp-KRR`,
  - `Lemma:large-app`,
  - `Lemma:uni-large`.

These are good Lean candidates because they follow a clear dependency chain:

`Lemma Q -> Proposition crucial-stopping -> Error decomposition + large/small cases -> Theorem ASUS`.

## 2) What Lean helps with (specifically)

Lean is most useful here for:

- **Dependency checking:** prevents circular arguments; theorem dependencies become explicit.
- **Assumption hygiene:** each lemma must list exact hypotheses (`0 < s <= 1`, `1/2 <= r <= 1`, confidence events, operator positivity, etc.).
- **Operator algebra correctness:** identities like
  - `A⁻¹ - B⁻¹ = B⁻¹ (B - A) A⁻¹`
  - norm bounds after triangle inequality and submultiplicativity
  are checked line-by-line.
- **Case split discipline:** `hat_lambda_uni <= lambda*` vs `hat_lambda_uni > lambda*` can be formalized as two lemmas that combine cleanly.
- **Avoiding hidden steps:** many "directly", "it follows", and "by standard arguments" claims become explicit derivations.

## 3) Practical formalization strategy (recommended)

Do **not** formalize the full probability + RKHS stack first. Use a layered approach:

### Layer A: deterministic algebra skeleton (start here)

Formalize finite-dimensional surrogates first:

- treat operators as matrices or bounded linear maps on finite-dimensional real inner product spaces,
- encode deterministic inequalities and decomposition identities,
- postpone high-probability events as abstract hypotheses.

Why: this captures most proof mechanics while avoiding heavy measure-theory overhead.

### Layer B: abstract probability wrappers

Once deterministic lemmas are stable, add wrappers of the form:

- `with_probability_at_least (1 - delta), statement`

and import concentration results only where needed.

### Layer C: rate arithmetic and asymptotics

Formalize exponent manipulation and rate comparisons:

- powers like `|D|^{-r/(2r+s)}`,
- log factors,
- monotonicity/inclusion arguments for bounds.

This layer is usually easier once inequalities are already structurally correct.

## 4) Mapping paper proofs to Lean tasks

### A. `Lemma:Q` (high-value first target)

Lean tasks:

- define abstract quantities `Q_D_lambda`, `P_D_lambda`, `S_D_lambda`,
- prove the deterministic part of the `Q <= sqrt 2` derivation under `S < 1/2`,
- isolate external concentration inputs as assumptions.

This gives reusable infrastructure for later lemmas.

### B. `Proposition:crucial-stopping-KRR`

Lean tasks:

- formalize operator inverse-difference identity,
- formalize decomposition of `f_{D,lambda} - f_{D,lambda'}`,
- bound each term separately,
- combine with the `Lemma Q` bounds.

This is the core "engine" lemma that explains why uniform subdivision helps.

### C. `Lemma:Error-Decomp-KRR`

Lean tasks:

- prove the max-norm decomposition into bias + sample terms,
- substitute `Q`/`P` bounds,
- conclude deterministic inequality in paper form.

### D. `Lemma:large-app` and `Lemma:uni-large`

Lean tasks:

- encode stop-rule implications,
- prove two case bounds (`hat_lambda <= lambda*` and `hat_lambda > lambda*`),
- handle summation bound in `uni-large` (this is mostly algebra + inequalities).

### E. `Theorem:ASUS`

Lean tasks:

- write final theorem as case split,
- apply two prior lemmas directly,
- conclude final rates.

## 5) Example Lean skeleton (minimal, actionable)

```lean
-- Lean 4 pseudo-skeleton (deterministic layer)
import Mathlib

noncomputable section
open scoped BigOperators

variable {α : Type} [NormedRing α]

-- Abstract placeholders for paper objects
structure KRRContext where
  Dsize : ℕ
  r s : ℝ
  delta : ℝ
  lambda lambda' : ℝ
  -- add assumptions as fields/hypotheses later

-- Example: finite-dimensional "inverse difference" identity pattern
theorem inv_sub_inv
    {A B : Matrix (Fin n) (Fin n) ℝ}
    (hA : IsUnit A) (hB : IsUnit B) :
    A⁻¹ - B⁻¹ = B⁻¹ * (B - A) * A⁻¹ := by
  -- matrix ring algebra
  -- `ring_nf` / `noncomm_ring` style steps
  sorry

-- Case split structure mirroring theorem ASUS
theorem ASUS_rate_template
    (h_case1 : True) (h_case2 : True) :
    True := by
  by_cases h : (0 : ℝ) ≤ 1
  · -- corresponds to hat_lambda <= lambda*
    exact trivial
  · -- corresponds to hat_lambda > lambda*
    exact trivial
```

The point is to mirror paper proof architecture before full operator/probability complexity.

## 6) Suggested workflow for this project

1. **Extract a proof DAG** from `Adap-KRR.tex` (already done above).
2. **Create a Lean file per lemma family**, e.g.:
   - `KPY/LemmaQ.lean`
   - `KPY/CrucialStopping.lean`
   - `KPY/ErrorDecomp.lean`
   - `KPY/ASUS.lean`
3. **Write theorem statements first** (`theorem ... := by` with `sorry`).
4. **Fill deterministic algebra proofs** (operator identities, norm bounds).
5. **Add probabilistic wrappers** as assumptions or imported lemmas.
6. **Remove `sorry` incrementally**; keep a changelog of what is fully verified.

## 7) Immediate, realistic outcomes from Lean

Even a partial formalization gives value:

- verifies critical algebra in `Proposition:crucial-stopping-KRR`,
- clarifies exactly where probabilistic assumptions are used,
- exposes hidden constants and condition dependencies,
- makes the theorem proof (`ASUS`) a clean composition of smaller checked lemmas.

## 8) Scope advice (important)

For this paper, full end-to-end formalization is a large effort. A strong and achievable target is:

- fully formalize deterministic core identities and inequality chaining for
  `Lemma:Q` (deterministic part), `Proposition:crucial-stopping-KRR`, and `Lemma:Error-Decomp-KRR`,
- keep concentration/probability statements as trusted assumptions initially.

This already significantly improves understanding and proof reliability.

