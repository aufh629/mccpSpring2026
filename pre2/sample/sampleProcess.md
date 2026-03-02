# Sample poster process and requirement alignment

This document describes how the sample poster was produced and how it aligns with pre2 instructions and institutional guidelines.

---

## 1. Source and scope

- **Paper:** AStar-BMao — *Accelerating Graph Similarity Search via Efficient GED Computation* (Lijun Chang, Xing Feng, Kai Yao, Lu Qin, Wenjie Zhang; IEEE-style, ~15 pages).
- **Source file:** `mccpSpring2026/literature/JJG*/AStarBMaoVisualization.html` (macro-level structure and content).
- **Instructions used:** `mccpSpring2026/pre2` materials: MCCP6020 Assessment (poster presentation) and HKBU Department of Mathematics poster guidelines (`pre2/demo/institutionalGuidelines/math.md`).

---

## 2. Process followed

1. **Extract content from the paper**
   - Read the visualization HTML to identify: problem (graph similarity search, GED), baseline (AStar-LSa, lbLSa), contributions (lbBMa ideal, lbBMao practical), and main result (faster + less memory).

2. **Map to required sections**
   - Introduction → problem, gap, two-stage contribution.
   - Methodology → baseline, lbBMa, lbBMao (with complexity and tightness).
   - Results → empirical findings (speed, memory, scalability).
   - Discussion/Conclusion → summary and impact.
   - References → paper and baseline.
   - Layman’s summary → short non-technical overview (as per HKBU guidelines).

3. **Apply layout and design rules**
   - Header: title (centred), presenter and principal supervisor placeholders, logo placeholder (top left), department (top right).
   - Typography: sans-serif for title and section headings; serif for body and layman’s summary.
   - Structure: single-column flow with clear section headings; placeholder boxes for “graphs/tables” to meet text–visual balance intent.
   - Dimensions: HTML/CSS set for A0 portrait proportions (841×1189 px) so the layout can be exported to PDF at 600 dpi for submission if required.

4. **Deliverables**
   - `samplePoster.html`: single-file poster; replace placeholders (name, supervisor, logos, and insert real figures/tables) for actual use.
   - `sampleProcess.md`: this process and alignment.
   - `outlineScript.md`: presentation outline and 2–3 minute script.

---

## 3. How the poster aligns with requirements

### MCCP6020 (Assessment 2 – Poster presentation)

| Requirement | Alignment |
|-------------|-----------|
| Summarize research topic, objectives, methodologies, findings, conclusions | Poster has Introduction (topic + objectives), Methodology (baseline + lbBMa + lbBMao), Results (findings), Discussion/Conclusion. |
| A1 or A3 size (A4 not acceptable) | HTML layout uses A0 portrait proportions; can be printed at A1 or A3 by scaling or by exporting at the required size. |
| Clear headings, bullet points, visuals | Section headings (h2), bullet lists in Methodology and References; placeholder boxes for graphs/tables to keep ~50–60% text / 40–50% visuals when figures are added. |
| Readable font size | Title and headings set large; body text 18px (scale up for print so body is ≥24 pt / ≥30 pt from 1.8 m per HKBU). |

### HKBU Department of Mathematics guidelines

| Requirement | Alignment |
|-------------|-----------|
| A0, 841×1189 mm, portrait | CSS width/height on `.poster` match A0 portrait; export to PDF at 600 dpi for submission. |
| Logo: HKBU (top left); Department (top right) | Header grid: left = logo placeholder, centre = title block, right = “Department of Mathematics”. |
| Header: title, presenter, principal supervisor (centred) | Centred block with poster title and “Presenter: [Name] · Principal Supervisor: [Name]”. |
| Sections: Introduction, Methodology, Results, Discussion/Conclusion, References | All five sections present in that order. |
| Layman’s summary | First content block after header; non-technical one-paragraph overview. |
| Titles/headings: sans-serif, ≥100 pt (on final PDF) | Headings use Arial/Helvetica; in this HTML they are 28–42px — **when exporting to PDF, increase font sizes so that the main title is ≥100 pt and section headings are clearly dominant** (e.g. via print stylesheet or design tool). |
| Body: serif, ≥24 pt (≥30 pt recommended) | Body uses Times New Roman; 18px in HTML — **scale up for final PDF** so body is ≥24 pt (or ≥30 pt) when measured in the PDF. |
| Text 50–60%, visuals 40–50% | Layout reserves space for figures/tables (placeholder boxes); adding real graphs/tables will achieve the balance. |
| Graphs/tables minimum 216×280 mm | Placeholder boxes mark where to insert figures; final PDF should use images at or above this size. |
| Accessibility and comprehensibility for non-specialists | Layman’s summary and short, clear section text support this; avoid jargon in the summary. |

### Gaps / next steps for a real submission

- Replace `[HKBU logo]`, `[Your Name]`, `[Supervisor Name]` with real content.
- Insert actual figures and tables (running time, memory, scalability) in place of the placeholder boxes; ensure minimum graph/table size 216×280 mm in the final PDF.
- When generating the submission PDF: use print CSS or a headless browser (e.g. Puppeteer) to export at A0 and 600 dpi; verify title ≥100 pt and body ≥24 pt (or ≥30 pt) in the PDF.
- If the unit requires A1 rather than A0, scale the layout or adjust page size at export.

---

## 4. References

- `createPoster.md` — task specification (sample poster from AStar-BMao, pre2 instructions, sample folder).
- `pre2/demo/institutionalGuidelines/math.md` — HKBU Math poster guidelines.
- `pre2/materials/pre2AssessmentRubrics.md` — MCCP6020 poster presentation instructions.
- `literature/JJG*/AStarBMaoVisualization.html` — paper structure and content source.
