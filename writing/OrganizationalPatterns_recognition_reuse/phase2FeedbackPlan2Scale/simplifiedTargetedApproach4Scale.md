# Simplified Targeted Approach for Scaling Up Analysis

This document outlines a revised, more focused approach for scaling up the analysis of paper introductions based on feedback from Phase 1 (the Enzo annotation) and the simulated student feedback. The key shift is: **instead of doing full deep annotations on many papers, we focus on specific, targeted aspects and let students choose what matters to them.**

---

## What We Learned

### From the Enzo Analysis (Phase 1)
- Deep annotation (moves, steps, approaches, expanded analysis, actionable insights) is valuable but time-consuming.
- The 10 approaches in `simonAnnotateApproaches.md` (general-to-specific, A-then-B, planting ideas, gap as mismatch, etc.) provide a solid framework.
- The enhanced annotation format (`annotateEnzoEnhanced.md`) is comprehensive but may be overkill for scaling to many papers.

### From Simulated Student Feedback (AIsimulateFeedback01.md)
- Students prefer **one deep example** plus **lighter annotations** for other papers.
- They find **actionable tips** most useful, not dense theoretical analysis.
- They want **targeted help** on specific struggles (e.g., how to state a gap, how to plant ideas, how to explain novelty).
- Cross-paper comparisons are interesting but should be summarized, not exhaustive.
- **Menu-driven choice** appeals: students select the aspect they want to focus on, rather than receiving a one-size-fits-all analysis.

---

## New Approach: Simplified, Targeted, Menu-Driven

### Core Idea

Instead of doing full deep annotations on 10–20 papers, we:
1. Keep **one star paper** (e.g., Enzo) with full deep annotation as a reference.
2. Offer students a **menu of targeted aspects** to choose from.
3. Run **focused, automated analysis** on 10–20 papers, but only for the chosen aspect.
4. Produce **concise outputs** (short annotations, comparison tables, pattern summaries) rather than full deep annotations.

This approach is **simpler** for students to digest and **more efficient** to produce at scale.

---

## Menu of Targeted Aspects

Students choose one (or sometimes two) aspects they want to focus on. Each aspect has:
- **What we analyze:** The specific focus.
- **Output format:** What we produce for the 10–20 papers.
- **What students get:** How this helps their writing.

### Option 1: How to State the Gap

**What we analyze:**
- Where and how the gap is stated.
- Whether it uses a **need–solution mismatch** (as in Enzo) or another pattern.
- Whether the gap is implicit or explicit.
- How the gap connects to the contribution.

**Output format for 10–20 papers:**
- A table summarizing each paper’s gap:
  - Paragraph location.
  - Gap type (e.g., need–solution mismatch, performance limitation, ignored factor).
  - Contrast pattern (e.g., “Users need X, but existing systems assume Y”).
  - Brief quote (1–2 sentences).
- A summary of common gap patterns in the set.

**What students get:**
- Multiple examples of how gaps are stated.
- A sense of what’s typical in their field.
- A template checklist for stating a gap clearly.

---

### Option 2: How to Plant and Harvest Ideas

**What we analyze:**
- Which key concepts/vocabulary are introduced early (planted).
- Where and how these are picked up when the contribution is announced (harvested).
- Whether the harvesting makes the contribution feel earned vs. abrupt.

**Output format for 10–20 papers:**
- For each paper:
  - List of planted terms (with paragraph locations).
  - List of where they are harvested (with paragraph locations).
  - A brief note on whether the connection is clear.
- A summary of common planting/harvesting strategies (e.g., “most papers plant 2–3 key terms 2–3 paragraphs before contribution”).

**What students get:**
- Concrete examples of planting ideas.
- A sense of how much planting is typical.
- A checklist for their own writing: “Have I planted the terms I will harvest in my contribution paragraph?”

---

### Option 3: How to Explain Novelty

**What we analyze:**
- How the paper signals novelty (e.g., “Unlike previous works,” “To the best of our knowledge,” “We propose a novel”).
- What aspect is claimed as novel (method, data, problem, evaluation).
- How novelty is justified (e.g., previous work doesn’t do X, existing methods fail at Y).

**Output format for 10–20 papers:**
- A table summarizing each paper’s novelty claim:
  - Signaling phrase (e.g., “Unlike previous works”).
  - What is claimed as novel.
  - How it is justified (brief).
  - Location (paragraph).
- A summary of common novelty-claiming patterns.

**What students get:**
- Phrases and structures they can adapt for their own work.
- A sense of how bold or modest novelty claims typically are in their field.
- Avoid over-claiming or under-claiming.

---

### Option 4: How to Structure the Opening Funnel (General → Specific)

**What we analyze:**
- How the first 1–2 paragraphs move from broad context to specific domain.
- Whether the funnel is explicit (e.g., “in particular,” “specifically”) or implicit.
- Whether the general-to-specific flow feels natural or forced.

**Output format for 10–20 papers:**
- For each paper:
  - Diagram or outline of the funnel (e.g., “personalized digital experiences → recommender systems → music platforms → playlist titles”).
  - Signaling phrases used.
  - Number of steps in the funnel.
- A summary of typical funnel depth and signaling.

**What students get:**
- Examples of how to open broadly without rambling.
- A sense of how many narrowing steps are typical.
- Phrases they can use to signal the funnel.

---

### Option 5: How to Connect Application and Technology

**What we analyze:**
- Where and how the paper links user-facing problems (application) to technical solutions (technology).
- Whether this connection is made in one breath or across paragraphs.
- How clearly the value of the technical work for users is stated.

**Output format for 10–20 papers:**
- A table summarizing each paper’s application–technology connection:
  - Where the link is made (paragraph).
  - The problem (application) and solution (technology) in brief.
  - Whether the connection is explicit or implicit.
- A summary of common connection patterns.

**What students get:**
- Examples of how to justify technical work in terms of user benefit.
- A sense of how explicit they should be.
- Avoid “methods without motivation.”

---

### Option 6: How to Use Citations for Positioning

**What we analyze:**
- How citations are used (e.g., to legitimize a focus, to show a gap, to position within a niche).
- Whether citations are integrated smoothly or dropped in.
- What concept each citation cluster is supporting.

**Output format for 10–20 papers:**
- For each paper:
  - A list of citation clusters with:
    - What concept is being legitimized or positioned.
    - The paragraph location.
    - The pattern (e.g., “Previous studies have shown [concept]”).
- A summary of common citation-positioning patterns.

**What students get:**
- Examples of how to cite purposefully, not just to pad references.
- A sense of how many citations are typical in the introduction.
- Avoid “citation dumps.”

---

## Workflow for Each Student

### Step 1: Choose from the Menu

- Student reviews the menu above and selects **one aspect** (sometimes two if related).
- Instructor confirms the choice and ensures the student has the relevant materials (star paper, menu description).

### Step 2: Select Papers for Analysis

- Student provides **10–20 papers** from their area (or instructor selects based on the student’s criteria: same venue, subfield, or genre).
- Papers should be accessible (PDF or text). If not available, instructor may provide a pre-selected set.

### Step 3: Automated Focused Analysis

- Instructor (or AI) analyzes the selected papers **only for the chosen aspect**, using the star paper (Enzo) as a reference.
- Analysis follows the **output format** specified for that option (e.g., gap table, planting/harvesting list).
- This is **lighter than a full deep annotation** — focused and concise.

### Step 4: Review and Apply

- Student reviews the output (tables, summaries, examples).
- Student identifies patterns that resonate and notes any gaps or questions.
- Student applies insights to their own writing (e.g., rewrites their gap statement using patterns from the analysis).

### Step 5: Optional Feedback

- Student shares how they used the analysis and what was helpful/missing.
- Instructor refines the approach, outputs, or menu options based on feedback.

---

## Advantages Over Full Deep Annotation

| Aspect | Full deep annotation (10–20 papers) | Simplified targeted approach |
|--------|------------------------------------|-----------------------------|
| **Time to produce** | High (days) | Low to moderate (hours) |
| **Time to consume** | High (students unlikely to read all) | Low (students read focused output) |
| **Relevance to student needs** | One-size-fits-all | Customizable via menu |
| **Actionability** | High but diluted by volume | High and concentrated |
| **Scalability** | Limited by effort | Highly scalable |
| **Student choice** | Minimal | High (choose aspect) |

---

## Example: A Student Choosing Option 2 (Plant/Harvest)

**Student’s request:** “I want to understand how to plant ideas so my contribution feels earned.”

**Steps:**
1. Instructor selects 12 papers from the student’s area (e.g., recommender systems papers from RecSys ’23–’25).
2. AI analyzes each paper for **planting/harvesting** only:
   - Lists planted terms (e.g., “sole seed,” “cold start,” “any complexity”) with locations.
   - Lists where they are harvested (e.g., “sole title as input” in contribution paragraph).
   - Notes whether connection is clear.
3. AI produces a summary: “Most papers plant 2–3 key terms 2–3 paragraphs before the contribution. Commonly planted terms: problem context, gap keywords, scope boundaries.”
4. Student reviews the list and summary.
5. Student rewrites their introduction to plant 2–3 terms that will be harvested in their contribution paragraph.
6. (Optional) Student shares their rewrite and notes that this helped them “avoid abrupt contribution announcement.”

---

## Deliverables

### For the Project
- Menu document (this file).
- Output templates for each option (tables, lists, summaries).
- AI prompts to produce focused analyses.
- Example outputs (one per option) for demonstration.

### For Each Student
- Focused analysis output for their chosen aspect (10–20 papers).
- Summary of patterns observed.
- Actionable tips tailored to their choice.

---

## Next Steps

1. **Refine menu:** Add, remove, or merge options based on instructor input and actual student feedback.
2. **Create templates:** Draft table structures, list formats, and summary templates for each option.
3. **Test with one student:** Run a pilot with one student choosing one option; review quality and usefulness of output.
4. **Iterate:** Refine prompts, templates, and menu options based on pilot results.
5. **Scale:** Offer the menu to more students; collect aggregated feedback to improve the approach over time.

---

## Summary

The simplified targeted approach shifts from **volume** (many deep annotations) to **focus** (one star paper + targeted, menu-driven analyses of many papers). This aligns with student preferences (actionable, relevant, not overwhelming) and makes scaling feasible and valuable.
