# Preliminary Slides Outline for COLDQ Paper

**Paper**: "Doubly-Bounded Queue for Constrained Online Learning: Keeping Pace with Dynamics of Both Loss and Constraint"

**Target**: AAAI 2025 Conference Presentation (20 minutes)

**Estimated Slides**: 18-20 slides

---

## Slide Structure Overview

| # | Section | Slides | Time (min) | Content Type |
|---|---------|--------|------------|--------------|
| 1 | Title & Outline | 2 | 1 | Meta |
| 2 | Introduction & Motivation | 3-4 | 3-4 | Context |
| 3 | Problem Formulation | 2-3 | 2-3 | Technical |
| 4 | COLDQ Algorithm | 3-4 | 4-5 | Core Contribution |
| 5 | Theoretical Analysis | 3-4 | 4-5 | Results |
| 6 | Experiments | 3-4 | 3-4 | Validation |
| 7 | Conclusion | 1-2 | 1-2 | Wrap-up |
| **Total** | | **18-23** | **18-24** | |

---

## Detailed Slide-by-Slide Outline

### Section 1: Title & Outline (2 slides)

#### Slide 1: Title Slide
**Content**:
- Title: "Doubly-Bounded Queue for Constrained Online Learning: Keeping Pace with Dynamics of Both Loss and Constraint"
- Authors: Juncheng Wang, Bingjie Yan, Yituo Liu
- Affiliation: Department of Computer Science, Hong Kong Baptist University
- Conference: AAAI 2025
- Optional: HKBU logo, AAAI logo

**Visual Elements**:
- Clean title layout
- Author photos (optional)
- Institution branding

**Source**: Lines 43-52 of aaai25.tex

---

#### Slide 2: Outline
**Content**:
1. Introduction & Motivation
2. Problem Formulation
3. COLDQ Algorithm
4. Theoretical Analysis
5. Experimental Results
6. Conclusion

**Visual Elements**:
- Simple bullet list or visual agenda
- Section icons (optional)

**Purpose**: Orient audience to presentation structure

---

### Section 2: Introduction & Motivation (3-4 slides)

#### Slide 3: Online Convex Optimization (OCO)
**Key Messages**:
- OCO framework: learner selects decisions to minimize time-varying loss functions
- Information revealed only after decision made
- Goal: Minimize **regret** (difference from benchmark)
- Applications: advertisement, load balancing, network virtualization, resource allocation

**Visual Elements**:
- Simple diagram of OCO process (time steps, decisions, losses)
- Application icons

**Source**: Lines 63-68 of aaai25.tex

**Talking Points**:
- "OCO is at intersection of learning, optimization, and game theory"
- "Broad applications in online systems"

---

#### Slide 4: Time-Varying Constraints
**Key Messages**:
- Many applications have constraints that change over time
- Two performance metrics:
  - **Dynamic regret**: Compare to online benchmark
  - **Hard constraint violation**: No compensated violation allowed
- For **fixed** constraints: Best-known bounds are O(√T) regret, O(1) violation

**Visual Elements**:
- Comparison table: Fixed vs. Time-varying constraints
- Highlight O(1) violation for fixed constraints

**Source**: Lines 68-72 of aaai25.tex

**Talking Points**:
- "Hard violation is stronger than soft violation"
- "Best-known O(1) violation for fixed constraints"

---

#### Slide 5: The Gap in Existing Work
**Key Messages**:
- Existing work on time-varying constraints:
  - Best violation bounds: O(√T) or O(√T log T)
  - **Do NOT recover O(1) for fixed constraints**
  - Algorithms don't "keep pace" with constraint dynamics

**Visual Elements**:
- Comparison showing gap:
  - Fixed constraints (Vg=0): O(1) violation ✓
  - Time-varying → Fixed: O(√T) violation ✗
- Highlight the discrepancy

**Source**: Lines 72-74 of aaai25.tex

**Talking Points**:
- "As constraints become less dynamic, violation should improve"
- "But existing work stuck at O(√T)"

---

#### Slide 6: Research Question & Our Answer
**Key Messages**:
- **Research Question**: Can we achieve bounds that smoothly approach O(√T) regret and O(1) violation as dynamics diminish?
- **Our Answer**: YES! COLDQ algorithm achieves this.

**Visual Elements**:
- Question in highlighted box
- Answer with checkmark
- Preview of our bounds: O(T^{(1+Vx)/2}) regret, O(T^{Vg}) violation

**Source**: Lines 74-75 of aaai25.tex

**Talking Points**:
- "This is the key question motivating our work"
- "For the first time, we achieve smooth approach to optimal bounds"

---

### Section 3: Problem Formulation (2-3 slides)

#### Slide 7: Constrained OCO Problem
**Key Messages**:
- Formal problem definition
- Decision variable: x_t ∈ X ⊂ ℝ^p
- Loss function: f_t(x) (convex, time-varying)
- Constraint function: g_t(x) = [g_t^1(x), ..., g_t^N(x)]^T
- Goal: min Σf_t(x_t) s.t. g_t(x_t) ≤ 0, ∀t

**Visual Elements**:
- Problem formulation in equation box
- Diagram showing iterative process

**Source**: Section 3 of paper (problem formulation)

**Talking Points**:
- "Standard constrained OCO setup"
- "Both loss and constraints change over time"

---

#### Slide 8: Performance Metrics
**Key Messages**:
- **Dynamic Regret**: Regret_T = Σf_t(x_t) - Σf_t(x_t*)
  - Compare to online optimal x_t*
- **Hard Constraint Violation**: Violation_T = Σmax{g_t(x_t), 0}
  - No compensation over time

**Visual Elements**:
- Two definition boxes
- Visual comparison: Static vs. Dynamic regret

**Source**: Section 3 of paper

**Talking Points**:
- "Dynamic regret is more challenging than static"
- "Hard violation is instantaneous, not averaged"

---

#### Slide 9: System Dynamics
**Key Messages**:
- **V_x**: Accumulated variation of loss functions
  - V_x = Σ||x_t* - x_{t+1}*||
- **V_g**: Accumulated variation of constraint functions
  - V_g = Σ||∇g_t(x_t*) - ∇g_{t+1}(x_{t+1}*)||
- Key insight: As V_x → 0 and V_g → 0, bounds should improve

**Visual Elements**:
- Two equations in boxes
- Diagram showing variation over time

**Source**: Equations (ref{eq:Vx}) and (ref{eq:Vg}) in paper

**Talking Points**:
- "These capture how much the system changes"
- "Lower variation = easier problem"

---

### Section 4: COLDQ Algorithm (3-4 slides)

#### Slide 10: Key Idea - Doubly-Bounded Virtual Queue
**Key Messages**:
- **Existing approaches**: Use either lower OR upper bound on virtual queue
- **COLDQ innovation**: Use BOTH lower AND upper bounds
  - Lower bound: Q_t ≥ 0
  - Upper bound: Q_t ≤ Q_max
- Enables tight control without Slater condition

**Visual Elements**:
- Comparison diagram:
  - Existing: Single bound (lower or upper)
  - COLDQ: Double bounds (both)
- Visual representation of bounded queue

**Source**: Lines 84-85 of aaai25.tex (contributions)

**Talking Points**:
- "This is our key algorithmic innovation"
- "Both bounds work together for tight control"

---

#### Slide 11: COLDQ Algorithm Pseudocode
**Key Messages**:
- Algorithm structure:
  1. Initialize x_1, Q_1 = 0
  2. At each time t:
     - Observe f_t and g_t
     - Update decision: x_{t+1} = Π_X[x_t - η_t(∇f_t(x_t) + Q_t∇g_t(x_t))]
     - Update queue: Q_{t+1} = clip(Q_t + g_t(x_t), 0, Q_max)

**Visual Elements**:
- Algorithm box with pseudocode
- Highlight the clip operation

**Source**: Algorithm 1 in paper

**Talking Points**:
- "Standard gradient descent with queue-weighted constraint gradient"
- "Clip operation enforces double bounds"

---

#### Slide 12: Virtual Queue Update Mechanism
**Key Messages**:
- Queue update: Q_{t+1} = clip(Q_t + g_t(x_t), 0, Q_max)
- **Lower bound (0)**: Prevents negative queue
  - Ensures queue reflects actual violations
- **Upper bound (Q_max)**: Limits queue growth
  - Directly controls constraint violation

**Visual Elements**:
- Diagram showing queue evolution over time
- Illustration of clipping at both bounds
- Compare with unbounded queue

**Source**: Algorithm and analysis sections

**Talking Points**:
- "Lower bound: no artificial credits"
- "Upper bound: violation cannot explode"

---

#### Slide 13: No Slater Condition Required
**Key Messages**:
- **Slater condition**: ∃x ∈ X s.t. g_t(x) < -ε < 0
  - Requires strictly feasible point
  - Often hard to verify in practice
- **COLDQ**: Works without Slater condition
  - More practical and general

**Visual Elements**:
- Definition of Slater condition
- Comparison: With vs. Without Slater
- Checkmark for COLDQ (no requirement)

**Source**: Lines 84-85 of aaai25.tex

**Talking Points**:
- "Most existing work requires Slater condition"
- "We remove this restrictive assumption"

---

### Section 5: Theoretical Analysis (3-4 slides)

#### Slide 14: Main Theorem - Performance Bounds
**Key Messages**:
- **Theorem**: COLDQ achieves:
  1. Dynamic Regret: O(T^{(1+Vx)/2})
  2. Hard Constraint Violation: O(T^{Vg})
- **Key property**: Smooth approach to optimal bounds
  - As V_x → 0: Regret → O(√T) (best-known static)
  - As V_g → 0: Violation → O(1) (best-known fixed)

**Visual Elements**:
- Theorem box with bounds
- Diagram showing smooth transition as V_x, V_g → 0

**Source**: Lines 86-87 of aaai25.tex (contributions)

**Talking Points**:
- "First algorithm to achieve this smooth approach"
- "Recovers best-known bounds as special cases"

---

#### Slide 15: Comparison with State-of-the-Art (Time-Varying)
**Key Messages**:
- Table comparing COLDQ with existing work
- Focus on time-varying constraints (V_g > 0)
- Show improvement in violation bound

**Visual Elements**:
- Simplified version of Table 1 from paper
- Highlight COLDQ row
- Show O(T^{Vg}) vs. O(T^{3/4}) or O(√T log T)

**Source**: Table 1 (lines 98-122 of aaai25.tex)

**Talking Points**:
- "Existing work: O(T^{3/4}) or worse"
- "COLDQ: O(T^{Vg}) - much better as V_g decreases"

---

#### Slide 16: Comparison with State-of-the-Art (Fixed Constraints)
**Key Messages**:
- Table comparing COLDQ with existing work
- Focus on fixed constraints (V_g = 0)
- Show recovery of O(1) violation

**Visual Elements**:
- Simplified version of Table 2 from paper
- Highlight COLDQ row
- Show O(1) violation vs. O(log T) or worse

**Source**: Table 2 (lines 124-148 of aaai25.tex)

**Talking Points**:
- "COLDQ recovers O(1) violation for fixed constraints"
- "Existing work: O(log T) at best"
- "This is the key advantage"

---

#### Slide 17: Proof Technique - Lyapunov Drift
**Key Messages**:
- **Lyapunov function**: L_t = ||x_t - x_t*||^2 + VQ_t^2
- **Drift analysis**: E[L_{t+1} - L_t] ≤ regret term + violation term
- **Key innovation**: Leverage both bounds of Q_t
  - Lower bound: Control regret accumulation
  - Upper bound: Control violation accumulation

**Visual Elements**:
- Lyapunov function equation
- Diagram showing drift analysis
- Highlight role of double bounds

**Source**: Theorem proofs in paper

**Talking Points**:
- "New Lyapunov drift design"
- "Both bounds essential for tight analysis"

---

### Section 6: Experiments (3-4 slides)

#### Slide 18: Experimental Setup
**Key Messages**:
- **Datasets**:
  - Synthetic: Quadratic loss with time-varying/fixed constraints
  - Real: Job scheduling, network resource allocation
- **Baselines**:
  - OGD-VQ: Online gradient descent with virtual queue
  - DOGD: Dynamic online gradient descent
  - State-of-the-art constrained OCO algorithms
- **Metrics**: Cumulative regret, cumulative constraint violation

**Visual Elements**:
- Table of datasets and baselines
- Icons for different applications

**Source**: Experimental section of paper

**Talking Points**:
- "Comprehensive evaluation on 4 scenarios"
- "Compare with state-of-the-art methods"

---

#### Slide 19: Results - Time-Varying Constraints
**Key Messages**:
- COLDQ achieves lowest violation
- Comparable or better regret than baselines
- Violation grows much slower than O(√T)

**Visual Elements**:
- Figure: time_varying.pdf
- Show regret and violation curves over time
- Highlight COLDQ curve

**Source**: time_varying.pdf in paper folder

**Talking Points**:
- "COLDQ significantly outperforms baselines"
- "Violation grows as O(T^{Vg}), not O(√T)"

---

#### Slide 20: Results - Fixed Constraints
**Key Messages**:
- COLDQ violation stabilizes (approaches O(1))
- Baselines continue growing
- Validates theoretical prediction

**Visual Elements**:
- Figures: fixed_linear.pdf, fixed_quadratic.pdf
- Show violation curves flattening for COLDQ
- Baselines continue growing

**Source**: fixed_linear.pdf, fixed_quadratic.pdf in paper folder

**Talking Points**:
- "COLDQ violation plateaus - approaches O(1)"
- "Baselines stuck at O(√T) growth"
- "Exactly as theory predicts"

---

#### Slide 21: Results - Real Application (Job Scheduling)
**Key Messages**:
- Real-world job scheduling scenario
- COLDQ maintains low violation while minimizing cost
- Practical validation of theoretical results

**Visual Elements**:
- Figure: job_schedule.pdf
- Show performance on real application

**Source**: job_schedule.pdf in paper folder

**Talking Points**:
- "COLDQ works well on real applications"
- "Not just theoretical - practical impact"

---

### Section 7: Conclusion (1-2 slides)

#### Slide 22: Summary of Contributions
**Key Messages**:
1. **COLDQ Algorithm**: Novel doubly-bounded virtual queue
2. **Theoretical Guarantees**:
   - O(T^{(1+Vx)/2}) dynamic regret
   - O(T^{Vg}) hard constraint violation
3. **Smooth Approach**: First to recover best-known bounds
4. **Practical Performance**: Outperforms state-of-the-art
5. **No Slater Condition**: More general and practical

**Visual Elements**:
- Numbered list of contributions
- Key results highlighted

**Source**: Lines 82-91 of aaai25.tex (contributions)

**Talking Points**:
- "COLDQ advances both theory and practice"
- "Solves long-standing open problem"

---

#### Slide 23: Future Directions & Thank You
**Key Messages**:
- **Future work**:
  - Extension to non-convex loss functions
  - Multi-agent constrained OCO
  - Applications to federated learning with fairness constraints
- **Thank you!**
- **Questions?**

**Visual Elements**:
- Brief bullet list of future directions
- Contact information
- "Thank you" message
- Q&A prompt

**Talking Points**:
- "Many exciting directions for future work"
- "Happy to answer questions"

---

## Additional Slides (Optional, Time Permitting)

### Optional Slide A: Strongly Convex Case
**Key Messages**:
- When loss functions are strongly convex:
  - Static regret: O(log T)
  - Violation: Still O(T^{Vg})
- Matches best-known static regret

**Source**: Lines 88-89 of aaai25.tex

---

### Optional Slide B: Expert Tracking Variation
**Key Messages**:
- COLDQ-ET: Expert tracking variation
- Achieves same bounds without prior knowledge of V_x, V_g
- More practical for unknown dynamics

**Source**: Lines 88-89 of aaai25.tex

---

### Optional Slide C: Ablation Study
**Key Messages**:
- Impact of doubly-bounded queue:
  - Lower bound only: Higher violation
  - Upper bound only: Higher regret
  - Both bounds: Best trade-off
- Parameter sensitivity analysis

**Source**: Experimental section

---

## Visual Design Guidelines

### Color Scheme (Academic Style)
- **Primary**: Dark blue (#1f4788) for headings
- **Secondary**: Light blue (#5b9bd5) for highlights
- **Accent**: Orange (#ed7d31) for emphasis
- **Background**: White or light gray (#f5f5f5)
- **Text**: Dark gray (#333333)

### Typography
- **Headings**: Sans-serif (Arial, Helvetica)
- **Body**: Sans-serif for readability
- **Math**: Computer Modern or similar (LaTeX style)
- **Code**: Monospace (Courier, Consolas)

### Layout Principles
- **Whitespace**: Generous margins, avoid crowding
- **Hierarchy**: Clear visual hierarchy (title > subtitle > body)
- **Consistency**: Uniform style across all slides
- **Focus**: One main message per slide
- **Readability**: Large fonts (24pt+ for body, 36pt+ for titles)

---

## Content Extraction Checklist

### From Paper Source
- [x] Title, authors, affiliation (lines 43-52)
- [x] Abstract (lines 59-61)
- [x] Introduction key points (lines 63-75)
- [x] Contributions (lines 82-91)
- [x] Problem formulation (Section 3)
- [x] Algorithm pseudocode (Algorithm 1)
- [x] Main theorems (Section 4)
- [x] Comparison tables (Tables 1 & 2, lines 98-148)
- [x] Experimental setup (Section 5)
- [x] Experimental figures (4 PDFs in paper folder)

### Visual Assets Needed
- [ ] HKBU logo (if available)
- [ ] AAAI 2025 logo (if available)
- [ ] Author photos (optional)
- [ ] Diagrams for OCO process
- [ ] Diagrams for virtual queue mechanism
- [ ] Experimental figures (already have PDFs)

---

## Timing Guide (20-minute presentation)

| Slide Range | Section | Time | Pace |
|-------------|---------|------|------|
| 1-2 | Title & Outline | 1 min | Quick |
| 3-6 | Introduction | 4 min | Moderate |
| 7-9 | Problem | 3 min | Moderate |
| 10-13 | Algorithm | 5 min | Detailed |
| 14-17 | Theory | 4 min | Moderate |
| 18-21 | Experiments | 3 min | Quick |
| 22-23 | Conclusion | 1 min | Quick |
| **Total** | | **21 min** | |
| Buffer | Q&A prep | -1 min | |
| **Target** | | **20 min** | ✓ |

### Pacing Notes
- **Spend most time** on Algorithm (slides 10-13) and Theory (slides 14-17)
- **Move quickly** through Introduction (audience likely familiar with OCO)
- **Highlight** experimental validation but don't dwell on details
- **Leave time** for questions

---

## Presentation Tips

### For Each Section

**Introduction** (Slides 3-6):
- Set context quickly - audience knows OCO
- Emphasize the gap in existing work
- Build excitement for the solution

**Problem Formulation** (Slides 7-9):
- Be precise but concise
- Ensure notation is clear
- Define V_x and V_g carefully (key to understanding results)

**Algorithm** (Slides 10-13):
- This is the core contribution - take time
- Use visuals to explain doubly-bounded queue
- Emphasize novelty (both bounds, no Slater)

**Theory** (Slides 14-17):
- State results clearly
- Use tables to show improvement over baselines
- Don't get lost in proof details

**Experiments** (Slides 18-21):
- Show figures clearly
- Point out key trends
- Validate theoretical predictions

**Conclusion** (Slides 22-23):
- Summarize key takeaways
- End on strong note

---

## Backup Slides (Prepare but Don't Present)

1. **Detailed Proof Sketch**: For technical questions
2. **Parameter Settings**: Specific values used in experiments
3. **Additional Experimental Results**: More figures if available
4. **Related Work Details**: Deeper comparison with specific papers
5. **Slater Condition Details**: Why it's restrictive

---

## Notes for Paper2Slides Implementation

When running Paper2Slides, this outline will guide the AI to:
1. **Extract** the right content from each section
2. **Organize** slides in logical flow
3. **Emphasize** key contributions (doubly-bounded queue, smooth approach)
4. **Include** comparison tables and experimental figures
5. **Balance** technical depth with clarity

The AI should produce slides closely matching this structure, with appropriate visual design based on the chosen style (academic).

---

## Document Status

- **Created**: January 31, 2026
- **Status**: Preliminary outline ready
- **Next Step**: Run Paper2Slides with this guidance
- **Expected Output**: 18-20 slides matching this structure

---

**This outline serves as a blueprint for both Paper2Slides generation and manual Beamer creation.**
