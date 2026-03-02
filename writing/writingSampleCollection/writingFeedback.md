# Writing Feedback — YUE Kunpeng (岳坤鹏)

## Feedback on YUE Kunpeng's First Draft: Introduction and Literature Review

**Student:** YUE Kunpeng (岳坤鹏)
**Topic:** Adaptive Regularization Parameter Selection in Kernel Ridge Regression
**Date:** 2 March 2026
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your draft:** writing/writingSampleCollection/firstDraft.md
**Your reflection:** writing/writingSampleCollection/reflection.md
**Assessment rubric:** writing/assessment/writing_instructions_formatted.md

---

## Overall Assessment

Your draft demonstrates strong technical knowledge of kernel ridge regression and regularization parameter selection. The content is substantive and covers the key theoretical background well. You have clearly articulated the research territory (KRR and adaptive parameter selection), identified a genuine gap (practical limitations of ASUS under strong assumptions), and proposed a clear research direction. However, the draft has several significant structural and rhetorical issues: (1) the Introduction is a single, very long paragraph that needs to be broken into clearly delineated moves; (2) the Literature Review moves are labeled but read more as summaries than critical analyses; (3) the heavy use of AI throughout the writing process has produced text that, while fluent, lacks the personal analytical voice expected in academic writing; and (4) the reflection and goals sections are mostly unfilled, suggesting insufficient self-reflection on the writing process.

**Estimated current level:** Satisfactory (6–7 range) — The technical content is solid, but the draft needs structural reorganization, critical depth, and a more authentic writing voice to reach Excellent.

---

## Part 1: Introduction Feedback

### What Works Well

- The research topic is clearly defined — adaptive regularization parameter selection in KRR
- You include proper citations from the very beginning (Caponnetto & De Vito, 2007; Steinwart & Christmann, 2008; Blanchard et al., 2019; Lu et al., 2020; Lin, 2024) — this is a significant strength compared to many drafts
- The progression from general context (KRR importance) to specific problem (parameter selection challenge) to proposed solution (ASUS) is logical
- The research gap is genuinely important: practical ASUS variants with relaxed assumptions

### Issue 1: The Entire Introduction Is One Paragraph

Your Introduction is a single block of text that contains all three moves but without any visual or structural separation. This makes it very difficult for readers to follow the argument.

**Action:** Break the Introduction into at least 3–4 paragraphs, one for each move:

- **Paragraph 1 (Move 1):** Establish KRR as important, explain why regularization parameter selection matters
- **Paragraph 2 (Move 1 continued):** Describe existing approaches (cross-validation, Lepskii-type principles, ASUS)
- **Paragraph 3 (Move 2):** Identify the gap — what ASUS and existing methods cannot do
- **Paragraph 4 (Move 3):** State your research purpose, approach, and expected contribution

Currently, the reader has to parse a dense wall of text to find where one move ends and the next begins.

### Issue 2: Move 2 (Identifying the Niche) Is Too Brief

Your Move 2 is essentially one sentence embedded in the long paragraph: the limitations of ASUS under strong assumptions. This needs expansion.

**What's missing:**
- Which specific assumptions are problematic? (Name them explicitly)
- What happens in practice when these assumptions are violated?
- Have any other researchers noted these limitations?

**Suggestion:** Expand Move 2 into its own paragraph. For example: "Despite these advances, the ASUS algorithm relies on assumptions that limit its practical applicability. Specifically, it requires [specific assumption 1] and [specific assumption 2], conditions that are rarely met in real-world datasets such as [example domain]. Furthermore, the proof techniques underlying ASUS impose artificial constraints on [specific parameter], making it difficult for practitioners to apply the method without expert statistical knowledge."

### Issue 3: Move 3 Needs a Clearer Research Question and Contribution Preview

Your Move 3 is implied in the final sentences about ASUS bridging "theoretical optimality and practical scalability" but is not explicitly stated as a research purpose.

**Action:** Add a clear statement such as: "This study aims to develop a simplified variant of the ASUS algorithm that (1) operates under relaxed eigenvalue decay assumptions, (2) provides simplified proofs accessible to practitioners, and (3) demonstrates empirical validity in high-dimensional settings. Specifically, we address the following research question: [state your research question]."

### Issue 4: Source Information Is Unfilled

The metadata at the top (Date, Context, Status) contains placeholders like "[Date]" and "[Draft for the course assignment?]". While this does not affect the writing quality, it suggests incomplete attention to detail.

**Action:** Fill in all metadata fields. Small details matter in academic writing.

---

## Part 2: Literature Review Feedback

### What Works Well

- All four moves are present and labeled — this shows good awareness of the expected structure
- Move 1 provides appropriate context by defining KRR and the key concepts
- You cite relevant foundational works (Caponnetto & De Vito, Blanchard et al., Lu et al., Lin)
- Move 3 identifies three specific gaps, which is a strong structural choice

### Issue 5: Move 2 (Critical Analysis) Reads as Description Rather Than Analysis

Your Move 2 summarizes the progression of methods (a priori selection → cross-validation → balancing principles → ASUS) but does not critically evaluate them. You describe what each approach does without discussing:
- **Strengths and weaknesses** of each approach relative to the others
- **Quantitative comparisons** — how much better is ASUS than cross-validation in specific settings?
- **Assumptions and limitations** — under what conditions does each approach fail?

**Your sentence (description):** "Among these, approaches like hold-out validation, cross-validation, and more recently, Lepskii-type principles, have been developed to provide theoretically justified parameter selection without data splitting."

**With critical analysis:** "Hold-out validation and cross-validation remain the most widely used methods in practice due to their simplicity, but they suffer from two key limitations: (1) data splitting reduces the effective sample size, which is particularly costly in high-dimensional settings (Blanchard et al., 2019), and (2) cross-validation lacks theoretical guarantees for optimal convergence rates in general RKHS settings. Lepskii-type balancing principles address the first limitation by avoiding data splitting, but introduce computational overhead through pairwise comparisons that scales as O(M²) with the number of candidate parameters (Lu et al., 2020). ASUS resolves this computational bottleneck through its early-stopping mechanism, achieving O(M) complexity, but at the cost of requiring stronger assumptions on eigenvalue decay."

Notice how the revised version compares methods, identifies specific tradeoffs, and uses citations to support each claim.

### Issue 6: Move 3 Gaps Are Well-Identified But Need More Support

Your three gaps are clear and specific:
1. Lack of simplified ASUS variants under relaxed assumptions
2. Proof techniques impose artificial constraints
3. Limited empirical validation in heterogeneous environments

However, each gap is stated in one sentence without supporting evidence.

**Action:** For each gap, explain:
- Which papers come closest to addressing it? (cite them)
- What specifically remains unresolved?
- Why does this gap matter for practitioners?

### Issue 7: Move 4 Is Adequate But Could Be Stronger

Your conclusion summarizes the literature well but could more explicitly connect to your research contribution.

**Suggestion:** Add a forward-looking sentence: "My proposed work directly addresses gaps 1 and 2 by developing a refined ASUS variant that [specific contribution], which will be validated on [specific datasets/domains]."

---

## Part 3: Language and Style Feedback

### Issue 8: Heavy AI Dependence in Writing

Your reflection states you use AI "throughout the entire writing process" and that your strategy is to break tasks down and "assign each small task to AI to complete." While AI tools are legitimate aids, this approach carries risks:

- The resulting text can lack your personal analytical voice
- AI-generated prose tends to use formulaic academic phrases without the precision that comes from deep understanding
- Examiners and reviewers are increasingly able to detect AI-generated patterns

**How to address this:**
- Write your first draft entirely by yourself, even if it is rough
- Use AI only for specific, bounded tasks: grammar checking, sentence-level rephrasing, formatting
- Never ask AI to write entire paragraphs or sections — you lose control of the argument
- Read your draft aloud: if it doesn't sound like how you would explain the topic to a colleague, rewrite it

### Issue 9: Unfilled Reflection Sections

Your reflection has placeholder text in "My Goals" ("[Be specific about what you want to improve]") and "Additional Notes" ("[Any other thoughts...]"). This is a missed opportunity — self-reflection helps you identify specific areas for improvement and demonstrates metacognitive awareness.

**Action:** Fill in your goals. Based on your draft, I would suggest:
1. Breaking long paragraphs into clearly structured moves
2. Adding critical comparison between methods (not just description)
3. Reducing AI dependence to develop your own academic voice
4. Expanding the gap analysis with supporting evidence

---

## Summary of Priority Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 High | Break Introduction into separate paragraphs for each move | Makes the argument structure visible and readable |
| 🔴 High | Add critical analysis to Move 2 — compare methods, discuss tradeoffs | Transforms description into genuine literature review |
| 🔴 High | Write first draft yourself without AI generating paragraphs | Develops authentic academic voice |
| 🟡 Medium | Expand Move 2 (gap identification) with specific evidence | Strengthens research motivation |
| 🟡 Medium | Add explicit research question in Move 3 | Clarifies your contribution |
| 🟡 Medium | Support each gap in Move 3 with citations | Makes gaps evidence-based |
| 🟢 Lower | Fill in all metadata and reflection sections | Shows attention to detail |
| 🟢 Lower | Add forward-looking connection in Move 4 | Links literature to your contribution |

---

## Next Steps

1. Read the [full writing instructions](https://github.com/tesolchina/mccpSpring2026/blob/main/writing/assessment/writing_instructions_formatted.md) carefully
2. Restructure the Introduction into 3–4 paragraphs with clear move boundaries
3. Rewrite Literature Review Move 2 with critical comparisons between methods
4. Fill in the reflection and goals sections
5. Submit your revised draft by **15 March 2026** via both Moodle forum and Turnitin
6. Please add **tesolchina** as a collaborator on your GitHub repository so I can provide future feedback directly
