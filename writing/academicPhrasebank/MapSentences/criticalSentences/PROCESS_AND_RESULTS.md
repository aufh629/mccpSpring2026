# Critical Sentences: Process and Results

**Template source:** `findCriticalSentences.md`  
**Paper collection:** `buildPaperCollection_arXiv/html_collection`  
**Date:** February 2026

---

## Overview

This document describes the steps used to find sentences in the HTML paper collection that serve **critical** rhetorical functions similar to the Manchester Academic Phrasebank templates:

1. **Explaining the inadequacies of previous studies** — e.g. prior work is limited, failed to address X, existing approaches inadequate.
2. **Identifying the paucity or lack of previous research** — e.g. little attention paid to X, few studies, no systematic study, understudied.

No external LLM API was used. Sentences were extracted with a Python script, filtered by keywords, then classified and templated by the in-session AI.

---

## Step 1: Extract sentences from HTML papers

**Script:** `find_critical_sentences.py` with `--extract-only`

**What it does:**

- Scans all `.html` files in `buildPaperCollection_arXiv/html_collection`.
- Parses each file for paragraph elements (`<p class="ltx_p">`) and extracts their text (LaTeXML ar5iv format).
- Keeps only lines with at least 15 characters.
- Writes one JSON file: **`sentences_all.json`**, keyed by paper ID (e.g. `1910.10683`, `2111.13463`), with values being lists of sentence strings.

**Result:**

| Metric        | Value |
|---------------|--------|
| Papers scanned | 28   |
| Sentences extracted | 6,601 |

**Output file:** `sentences_all.json`

---

## Step 2: Filter candidate sentences (keyword-based)

**Script:** `find_critical_sentences.py` with `--candidates`

**What it does:**

- Loads `sentences_all.json`.
- For each sentence, checks whether it contains any of a fixed set of **critical** keywords/phrases (e.g. *previous stud*, *prior work*, *little attention*, *few studies*, *no previous*, *paucity*, *understudied*, *lack of*, *failed to address*, *limited to*, *no single study*, *contrasts with*, *overlooked*).
- Writes **`candidates.tsv`**: one row per candidate, with columns `paper_id` and `sentence` (tab-separated).

**Result:**

| Metric           | Value |
|------------------|--------|
| Candidate sentences | 128  |

**Output file:** `candidates.tsv`

---

## Step 3: Classify candidates and extract templates (AI, no external API)

**Performed by:** In-session AI (Cursor agent)

**What was done:**

- Read all 128 lines of `candidates.tsv`.
- For each candidate sentence:
  - **Category 1** — Explaining the inadequacies of previous studies (prior work limited, failed to address, contrasts with prior work, existing approaches inadequate, etc.).
  - **Category 2** — Identifying the paucity or lack of previous research (lack of X, no systematic study, overlooked, understudied, etc.).
- Discarded false positives (e.g. “rather than” in non-critical sense, non-academic content).
- Assigned a short **extracted template** (generalized phrase with placeholders X, Y, Z) for each kept sentence where useful.

**Result:**

| Metric   | Value |
|----------|--------|
| Matches kept | 69  |
| Category 1 (inadequacies) | 50 |
| Category 2 (paucity/lack) | 19 |

**Output file:** `matches_from_ai.json` (list of objects: `paper_id`, `sentence`, `category`, `extracted_template`)

---

## Step 4: Generate reports

**Script:** `find_critical_sentences.py --from-matches matches_from_ai.json`

**What it does:**

- Loads `matches_from_ai.json` and the template text from `findCriticalSentences.md`.
- Writes two reports:
  - **`report_criticalSentences.md`** — Original phrasebank templates, then sentences found by category (with paper ID and optional extracted template), then a deduplicated list of new/extracted templates.
  - **`report_criticalSentences.html`** — Same content in a table-based, dark-theme layout with links to the MD report.

**Output files:** `report_criticalSentences.md`, `report_criticalSentences.html`

---

## Summary of results

| Stage              | Count |
|--------------------|--------|
| Papers             | 28    |
| Sentences extracted| 6,601 |
| Candidates (keyword filter) | 128 |
| **Final matches**  | **69** |
| → Inadequacies (cat. 1) | 50 |
| → Paucity/lack (cat. 2) | 19 |

**Artifacts:**

- **Inputs:** `findCriticalSentences.md`, HTML files in `html_collection`
- **Intermediate:** `sentences_all.json`, `candidates.tsv`, `matches_from_ai.json`
- **Outputs:** `report_criticalSentences.md`, `report_criticalSentences.html`

---

## How to re-run

```bash
cd ".../MapSentences/criticalSentences"

# 1. Extract sentences (if HTML collection changed)
python3 find_critical_sentences.py --extract-only

# 2. Regenerate candidates
python3 find_critical_sentences.py --candidates

# 3. (Optional) Update matches_from_ai.json by reviewing candidates.tsv

# 4. Regenerate reports from current matches
python3 find_critical_sentences.py --from-matches matches_from_ai.json
```

For a **visually oriented** summary of this process and the same results, open **`PROCESS_AND_RESULTS.html`** in a browser.
