# Plan: AI-Assisted Organizational Pattern Recognition & Reuse

## Vision

Develop an AI-assisted workflow that helps researchers organize manuscripts by learning from published papers—recognizing structural patterns (macro/micro levels) and reusing insights, building toward reusable MCP tools and Cursor skills.

---

## Phase 1: Pilot with One Paper Set (Current)

**Goal:** Validate the workflow and refine the analytical framework.

### Steps

1. **Select one paper set**
   - Choose a focused collection (e.g. 5–10 papers) in one student’s research area
   - Criteria: same sub-field, similar venues, common genre (e.g. empirical, survey)

2. **Manual annotation of one paper**
   - Annotate one paper for organizational patterns:
     - **Macro:** sections, moves (e.g. CARS), overall argument flow
     - **Micro:** paragraph roles, step patterns, transitions
   - Record decisions and criteria (e.g. move boundaries, labels)

3. **Document analytical approach**
   - Use the annotated paper as input to AI
   - Have AI produce a clear **analytical guide** that describes:
     - The taxonomy (patterns, moves, steps)
     - How to identify them
     - Rationale for labels and boundaries

4. **Automated analysis of remaining papers**
   - Use the analytical guide as instructions for AI
   - Apply the same analysis to the rest of the paper set (10+ papers)
   - Collect recurring patterns, variants, and outliers

5. **Synthesis and reflection**
   - Summarize what the set teaches about organization
   - Draft a reusable template or checklist for writing in that genre
   - Note refinements for the analytical framework

**Outputs:** Annotated exemplar, analytical guide, comparative analysis report, writing template/checklist.

---

## Phase 2: Student Feedback & Iteration

**Goal:** Test usability and value with research students.

### Steps

1. **Recruit 1–2 research students** (different areas if possible)
2. **Provide materials:** analytical guide, example annotations, template
3. **Observe:** students apply the workflow to their own paper sets
4. **Collect feedback:** what worked, what was unclear, what was missing
5. **Iterate:** improve the guide, templates, and prompts
6. **Document** best practices and common pitfalls

**Outputs:** Refined analytical guide, revised templates, feedback notes.

---

## Phase 3: MCP & Skills for Broader Use

**Goal:** Package the workflow as reusable tools for researchers.

### Deliverables

1. **MCP Server (e.g. `paper-patterns`)**
   - Tools to:
     - Load and parse PDF/text papers
     - Apply organizational pattern analysis
     - Compare patterns across papers
     - Export annotations and reports

2. **Cursor Skills**
   - `analyze-paper-structure`: guide AI to follow the analytical framework
   - `compare-papers-patterns`: comparative analysis across a set
   - `generate-writing-template`: derive templates from analyzed papers

3. **Documentation**
   - Quick-start guide
   - Taxonomy reference (patterns, moves, steps)
   - Examples for different genres/subfields

**Success criteria:** A researcher can use MCP + skills to analyze their own paper set and get actionable organizational insights without starting from scratch.

---

## Dependencies & Notes

- **Phase 1 → 2:** Needs a stable analytical guide and at least one solid example
- **Phase 2 → 3:** Needs student validation and refined prompts
- **Scalability:** MCP assumes PDF/text input; consider extraction quality and multi-format support
- **Generalization:** Start with one genre (e.g. empirical CS papers); extend later

---

## Timeline (Suggestion)

| Phase | Duration   | Milestone                           |
|-------|------------|-------------------------------------|
| 1     | 2–3 weeks  | Analytical guide + pilot analysis   |
| 2     | 2–4 weeks  | Student feedback and refinements    |
| 3     | 4+ weeks   | MCP prototype + initial skills      |
