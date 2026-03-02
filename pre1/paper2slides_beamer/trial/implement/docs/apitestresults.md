# API Test Results — Does Any API Key Work?

**Last updated:** 2026-01-31  
**Sources:** Run log `logs/COCO_paper2slides_run.log`, docs (whynotimage, OPENROUTER_401_FIX, assessSlides, BLTKEY_API).

---

## 1. Short answer

| Use | Does any key work? | Notes |
|-----|--------------------|--------|
| **LLM (RAG / summary / plan)** | **Partially** | At least one run produced a plan and text-only slides (HTML, first section), so **some LLM key worked** in that run. The **logged run** (PDF, full RAG) got **401 on every LLM call** — so in that run no key worked (key missing, wrong, or wrong base URL). |
| **Image generation** | **No** | Poe → 401; GPT-Best → server returns HTML instead of JSON. No image-capable API has been confirmed working. |

So: **at least one LLM key has worked in some run** (plan + text slides exist). **No image key works** in the current setup. In the **single run we have a log for**, the LLM key did **not** work (401 on all RAG queries and summary).

---

## 2. Configured providers (from docs)

| Provider | Key file | Used for | Base URL (typical) |
|----------|----------|----------|---------------------|
| **Poe** | `poeAPIkey.md` | RAG/LLM only (use `--fast`; no embeddings) | `https://api.poe.com/v1` |
| **OpenRouter** | `openRouterKey.md` | RAG/LLM + optional image | `https://openrouter.ai/api/v1` |
| **GPT-Best (Apifox)** | `bltkey.md` | RAG/LLM + tried for image | `https://gpt-best.apifox.cn/v1` |
| **Azure (HKBU)** | `HKBUkey.md` | RAG/LLM | From `HKBUbaseURL.md` or `.env` |

Keys are set in `Paper2Slides/paper2slides/.env` as `RAG_LLM_API_KEY`, `RAG_LLM_BASE_URL`, and (for image) `IMAGE_GEN_API_KEY`, `IMAGE_GEN_BASE_URL`. See [API_KEYS.md](API_KEYS.md).

---

## 3. Logged run: `COCO_paper2slides_run.log`

- **Input:** `COCO_2310.18955v3.pdf`  
- **Stages:** RAG (with MinerU parsing) → then LLM queries and summary.

**Results:**

| Stage | Result | Detail |
|-------|--------|--------|
| RAG (parsing) | ✓ | MinerU parsed PDF; 357 content blocks. |
| RAG (queries) | ✗ | **All 26 LLM queries failed** with `401 - No cookie auth credentials found`. |
| Summary | ✗ | **Failed** with same 401 (key/url not accepted). |
| Plan | — | Not reached (pending). |
| Generate | — | Not reached. |

So in this run the **LLM API key (or base URL) was not accepted** — likely OpenRouter or Poe with missing/wrong key or wrong base URL. No LLM key worked in this run.

---

## 4. Other run (from assessSlides): HTML, first section

- **Input:** `COCO_2310.18955v3_from_arxiv.html`, first section, fast mode.  
- **Output:** `slides_outline.md` and `slides_text.html` under `.../slides_academic_short_1sec/text_slides/`, built from **plan checkpoint and RAG markdown**.

So for that run, **RAG/summary/plan completed** (plan and RAG data existed). Therefore **at least one LLM key worked** in that run. Which provider/key was used is not recorded in the repo. Image generation still failed (server returned HTML → GPT-Best-style response).

---

## 5. Image generation (all tested keys)

| Backend | Result | Reason |
|---------|--------|--------|
| **Poe** | ✗ | 401 "No cookie auth credentials found"; Poe not built for this image API usage. |
| **GPT-Best (bltkey)** | ✗ | Server returned **HTML** (e.g. Apifox page) instead of JSON; client expects `response.choices` → "API response has no choices". |

So **no image API key has worked**: either auth failed (Poe) or wrong response format (GPT-Best). See [whynotimage.md](whynotimage.md).

---

## 6. Summary table

| API / stage | Poe | OpenRouter | GPT-Best (blt) | HKBU Azure |
|-------------|-----|------------|----------------|------------|
| **LLM (RAG/summary/plan)** | Not confirmed in log; 401 in logged run (if OpenRouter was used, key was wrong/missing) | 401 in logged run when key missing/wrong; fix key → can work | Doc says key is usable for chat; one run produced plan (key may have been blt or another) | Not tested in logs |
| **Image generation** | ✗ 401 | Not confirmed with image model | ✗ HTML response | Not tested |

---

## 7. Recommendations

1. **LLM:** Ensure one key is correctly set in `Paper2Slides/paper2slides/.env`: `RAG_LLM_API_KEY` and `RAG_LLM_BASE_URL`. For OpenRouter 401, see [OPENROUTER_401_FIX.md](OPENROUTER_401_FIX.md). Re-run a short test (e.g. first section, HTML) and check log for 401.
2. **Image:** Use an image-capable API that returns JSON with `choices` (e.g. OpenRouter with a supported image model and correct endpoint). Do not use Poe or the current GPT-Best image path until fixed.
3. **Document which key worked:** When a run succeeds, note in this file which provider/key was used so we know "which API key works" for future runs.

---

**Bottom line:** At least one LLM key has worked in some run (plan + text-only slides exist). In the only run we have a log for, no LLM key worked (401). No image API key works in the current setup. Fix and verify one LLM key in `.env`, then re-run and document the result here.
