# Critical sentences in academic phrasebank
_Exported on 02/02/2026 at 0:27:28 GMT+8 from Cursor (2.4.23)_

---

**User**

Teaching/Courses/MCCP 6020/PhDagentSpring2026/writing/academicPhrasebank/MapSentences/criticalSentences/findCriticalSentences.md

---

**Cursor**


Exploring the paper collection and planning how we'll find sentences that match the templates and produce the reports.



Checking HTML paper structure and existing report format so we match the expected output.



Checking how the trial report presents found sentences and how the dashboard links to reports:



Checking for existing scripts that extract text from the HTML papers:



Reading `map_sentences.py` to reuse its extraction and reporting logic.



Implementing step by step: creating a task list and starting implementation.



Parsing findCriticalSentences.md to extract the two template sections:



Implementing the script: adding a parser for the critical-sentences file and the main processing logic.



Fixing the script: ensuring we use the local log and returning `template_data` from `run_all_papers` so we don't parse twice. Checking imports and fixing the fallback so it doesn't require the LLM.



Escaping HTML in the report output and passing the log path from __main__.



Renaming the outer `html` variable so it doesn't shadow the `html` module used in `row()`.



Showing a short sample of the generated reports:



Summary of what’s in place:

---

## Status

The instructions in `findCriticalSentences.md` are implemented and the pipeline has been run once.

### 1. **Script: `criticalSentences/find_critical_sentences.py`**

- **Parses** `findCriticalSentences.md` into two template groups:
  - Explaining the inadequacies of previous studies  
  - Identifying the paucity or lack of previous research  

- **Scans** all papers in  
  `Teaching/.../buildPaperCollection_arXiv/html_collection` (28 HTML files).

- **Matches** paragraph text to those templates using either:
  - **LLM** (if `OPENAI_API_KEY` or Poe key is set): assigns category 1 or 2 and suggests extracted templates, or  
  - **Keyword fallback** (with `--pattern`): phrases like “previous stud”, “prior work”, “little attention”, “few studies”, “no previous”, “paucity”, “understudied”, etc.

- **Writes**:
  - `report_criticalSentences.md` – templates, then found sentences by category, then new/extracted templates.
  - `report_criticalSentences.html` – same content in a table view (dark theme, link to the .md).

### 2. **Run so far**

- Executed with **pattern-only** (`--pattern`): 39 sentences found, all grouped under “Explaining the inadequacies…” (keyword fallback doesn’t assign category 2). Both reports were generated under `criticalSentences/`.

### 3. **How to run**

- **Pattern-only (no API):**  
  `cd ".../MapSentences/criticalSentences" && python3 find_critical_sentences.py --pattern`

- **With LLM (categories + extracted templates):**  
  Set `OPENAI_API_KEY` (or Poe key in `LLM/poe.md`), then run:  
  `python3 find_critical_sentences.py`  
  (no `--pattern`). This will call the API once per paper.

If you tell me your priority (e.g. add category-2 keywords for pattern mode, or run with LLM and inspect the reports), I can do that next.

---

**User**

actually I don't want to call external LLM 
I want you to call tools to read the sentences from the html files and compare with the templates 
use your own AI 

---

**Cursor**


Using tools to extract sentences from the HTML files, then comparing them to the templates and building the report. Extracting sentences from all papers into a single file we can process.



Adding an extract-only mode to dump all sentences to JSON, then we'll read the JSON and perform the matching ourselves.



Adding an extract-only mode, running it, then reading the extracted sentences and performing the matching ourselves.



Reading the extracted sentences and processing them paper-by-paper so we can compare each to the templates.



Reading the JSON in sections and processing each paper's sentences.



Creating a candidate filter to reduce the set we'll compare, then we'll classify each candidate ourselves.



Reading all 128 candidates and classifying each as category 1 (inadequacies) or 2 (paucity/lack) and extracting templates.



Classifying each candidate and writing matches (category + extracted template), then generating the report.



Fixing the truncated sentence in the matches file and running the report generator.



Summary of what’s in place:

## No external LLM – tools + my classification

1. **Extract**  
   Script reads all HTML papers and writes paragraph text to `sentences_all.json` (28 papers, ~6.6k sentences).

2. **Candidates**  
   Script filters with your template-style keywords and writes `candidates.tsv` (128 lines: `paper_id` + sentence).

3. **My classification**  
   I went through all 128 candidates and:
   - **Category 1 – Explaining inadequacies of previous studies:** e.g. prior work is limited, fails to address X, contrasts with our approach, existing methods inadequate.
   - **Category 2 – Identifying paucity/lack of previous research:** e.g. lack of X, no systematic study, overlooked by prior work, under-represented.
   - Dropped clear false positives (e.g. “rather than” in non-critical sense, non-academic content, “in contrast to” for methods only).
   - Added short **extracted templates** (with X, Y, Z placeholders) for each kept sentence.

4. **Matches file**  
   Wrote `matches_from_ai.json` with **69 matches** (each has `paper_id`, `sentence`, `category`, `extracted_template`).

5. **Reports**  
   Ran the script with `--from-matches matches_from_ai.json` to produce:
   - **report_criticalSentences.md** – templates, then found sentences by category, then new/extracted templates.
   - **report_criticalSentences.html** – same content in a table view.

**How to re-run later (no LLM):**

```bash
cd ".../MapSentences/criticalSentences"
python3 find_critical_sentences.py --extract-only    # if HTML collection changed
python3 find_critical_sentences.py --candidates     # refresh candidates.tsv
# (You or I then produce/update matches_from_ai.json from candidates.tsv)
python3 find_critical_sentences.py --from-matches matches_from_ai.json
```

All of this uses only local tools (read HTML, keyword filter, my classification); no external API is called.

---

**User**

write an html file and a md file to describe the steps taken to process the papers and the results 
html file should be visually appealing 

---

**Cursor**


Checking key paths and counts for the documentation:



Creating the Markdown and HTML documentation files.



Summary of what was added:

## Created files

### 1. **PROCESS_AND_RESULTS.md**
- **Overview** — What “critical” means and that no external LLM was used.
- **Step 1** — Extract sentences from HTML → `sentences_all.json` (28 papers, 6,601 sentences).
- **Step 2** — Keyword filter → `candidates.tsv` (128 candidates).
- **Step 3** — AI classification and template extraction → `matches_from_ai.json` (69 matches: 50 cat. 1, 19 cat. 2).
- **Step 4** — Report generation → `report_criticalSentences.md` and `.html`.
- **Summary table** and **artifacts** list.
- **Re-run** instructions (copy-paste commands).

### 2. **PROCESS_AND_RESULTS.html**
- **Layout** — Single column, max-width 900px, DM Sans + JetBrains Mono.
- **Summary cards** — 6 cards: 28 papers, 6,601 sentences, 128 candidates, **69** matches (emphasized), 50 inadequacies, 19 paucity/lack.
- **Pipeline** — Four numbered steps in cards with left accent border; each has title, short description, command/code, and result.
- **Tables** — “Results at a glance” and “Artifacts” (inputs, intermediates, outputs).
- **Links** — Buttons to sentence report (HTML/MD) and to the MD version of this doc.
- **Styling** — Light background, white cards, blue accent, green result callouts, rounded corners and light shadow.

Both files are in  
`.../MapSentences/criticalSentences/`.  
Open **PROCESS_AND_RESULTS.html** in a browser to see the visual version.

