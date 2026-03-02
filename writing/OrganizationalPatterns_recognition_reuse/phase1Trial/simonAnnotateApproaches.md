# Simon's Approaches to Annotation and Analysis

This document describes Simon's analytical approaches when annotating academic paper introductions for organizational patterns. The goal is to make these approaches explicit so other researchers and AI can learn and reuse them.

---

## 1. General-to-Specific Progression

**Principle:** Watch for moves from broader concepts to narrower, more specific ones.

**Example (Para 1, Enzo):**  
The text moves from "recommender systems" (general) to "music platforms" (specific application). Simon notes: *"We recognize music platform as an example of content delivery system (this is a move from general to specific)."*

**For annotators / AI:** When you see a paragraph that starts with a broad domain and narrows to a subdomain or application, label this as a general-to-specific step. Ask: *What is the hierarchy here? What is the most general concept, and what is the most specific?*

---

## 2. Application ↔ Technology Bridge

**Principle:** Authors often connect application-level concerns (what users do, what problems they face) with technical/system-level concerns (algorithms, systems). Tracking this bridge helps explain why the paper's technical contribution matters.

**Examples:**
- **Para 1:** *"Also see the connection between application (music recommendation) and more technological system (recommender)."*
- **Para 3:** *"Locate title as a key element in recommender system — here is the bridge between application and technology."*

**For annotators / AI:** When a paragraph introduces both user-facing problems and technical solutions, note how they are linked. Ask: *Where does the author connect "what users need" to "what the system does"?*

---

## 3. A-then-B Structure (Prerequisite Focus)

**Principle:** Before introducing the main focus (B), authors often first discuss a related but broader concept (A). This sets up context so B appears natural and motivated.

**Example (Para 2 → 3, Enzo):**  
Para 2 focuses on *tracks* (creating playlists, selecting songs). Para 3 shifts to *titles*. Simon notes: *"The focus here is track — which is related to titles — the main focus of the paper. So before we talk about B (the real focus) we first talk about A that is related to B."*

**For annotators / AI:** Identify the paper's central focus. Then look backwards: What related concept (A) is introduced first? How does A prepare the reader for B? Label this as an A-then-B or prerequisite-focus pattern.

---

## 4. Planting Ideas for Later

**Principle:** Strong introductions "plant" ideas early so that when the present work is announced, it feels logical rather than abrupt. Annotators should track which earlier phrases or concepts are picked up in the "occupy niche" paragraphs.

**Example (Para 5, Enzo):**  
Simon notes: *"This is where the present work is introduced; we should pay attention on how elements and themes in the previous paragraphs are picked up here. A smart author should try to plant some ideas earlier so it would become more logical and natural to announce the present study."*

**For annotators / AI:** When you reach the paragraph that presents the paper's contribution, list which earlier ideas it echoes: e.g. "sole title as input" ← "cold start" / "sole seed" (Para 3); "any complexity" ← "Housewarming Party" etc. (Para 4). Note whether the author successfully plants and harvests.

---

## 5. Practical Context Before Technical Focus

**Principle:** Authors often describe the problem in practical, user-facing terms before introducing technical solutions. This grounds the reader in real-world relevance.

**Example (Para 2, Enzo):**  
*"This is to define the specific task — creating tailored playlist — and discuss the challenges facing users in the more practical context."*

**For annotators / AI:** Separate paragraphs (or parts of paragraphs) that describe *user challenges* or *practical context* from those that describe *technical approach*. Note the order: practical first often increases motivation.

---

## 6. Reference to Previous Studies as Positioning

**Principle:** Citations and references to prior work are used not only for credibility but to position the current focus (e.g. "titles") within the literature.

**Example (Para 3, Enzo):**  
*"There is some reference to previous studies; locate title as a key element in recommender system."*

**For annotators / AI:** When you see "Previous studies have shown…" or similar, ask: *What concept is being legitimized or positioned?* The cited work often supports the author's move to narrow the focus (e.g. from "playlists" to "playlist titles").

---

## 7. Gap as Mismatch Between Need and Solution

**Principle:** The gap is often framed as a mismatch: users need X, but existing systems assume Y. Making this contrast explicit clarifies the contribution.

**Example (Para 4, Enzo):**  
Common titles ("workout", "gaming") have ready-made materials; novel titles ("Housewarming Party", "Spring awakening") don't map to pre-existing categories. Simon (with AI response): The gap is *existing systems assume known categories; this paper targets titles that don't*.

**For annotators / AI:** When identifying the gap, ask: *What do users/situations need? What do existing solutions assume? Where is the mismatch?* State the gap in one sentence using this contrast.

---

## 8. Acknowledging Unclear Technical Details

**Principle:** It's okay to note that you don't yet understand the method. This can drive a second pass (reading Methods, asking AI, or discussing with a student) and may yield additional insights about organization.

**Example (Para 5, 6–7, Enzo):**  
Simon: *"I still don't quite get how the paper's method works. Once I get it (with assistance from AI and the student) I might have more interesting things to say about the paper's organization."*

**For annotators / AI:** If the intro's technical summary is unclear, flag it. Use Methods, figures, or external resources (e.g. slides, code README) to clarify. Return to the intro and ask: *Does the organization make more sense now? Are there planted ideas I missed?*

---

## 9. Valuing Transparency and Signposting

**Principle:** Note when authors do things that help readers: open code/data, clear roadmap (e.g. "The remainder of this paper is structured as follows").

**Examples:**
- **Para 8:** *"It is great that source codes are available. We should read the readme file."*
- **Para 9:** *"Signposting — fine — great."*

**For annotators / AI:** Treat transparency (code, data) and signposting as organizational choices worth annotating. They support trust and navigability.

---

## 10. Using External Resources

**Principle:** When the paper is dense, use supplementary materials (slides, README, repo) to gain insight. AI can fetch or summarize these.

**Example (Para 8, Enzo):**  
*"I found the slides here [link]. AI can fetch the slides to gain more insights."*

**For annotators / AI:** If the author provides links (GitHub, slides, supplementary), use them. Note in your annotation when external resources were consulted and what they clarified.

---

## Summary: Checklist for Annotating an Introduction

1. **General-to-specific:** Where does the text narrow from broad to specific?
2. **Application–technology bridge:** Where are user needs linked to technical solutions?
3. **A-then-B:** What is introduced first (A) to set up the main focus (B)?
4. **Planting and harvesting:** Which ideas in the "occupy niche" paragraph were planted earlier?
5. **Practical before technical:** Is the problem stated in practical terms before the method?
6. **Positioning via citations:** What concept do the citations legitimize?
7. **Gap as mismatch:** What do users need vs. what do existing systems assume?
8. **Flag unclear technical content:** Note when you need more detail; revisit after reading Methods.
9. **Transparency and signposting:** Note open code/data and roadmap.
10. **External resources:** Use slides, README, etc., when available.
