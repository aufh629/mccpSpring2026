# OpenRouter 401 Fix — "No cookie auth credentials found"

**If you're in HK (or OpenAI is blocked):** Use **non-OpenAI models only** via OpenRouter. See **`HK_NON_OPENAI.md`** and set `LLM_MODEL=google/gemini-2.0-flash` (or another non-OpenAI model) in `.env`.

---

## What’s happening

The OpenRouter **API is reachable**, but requests are **rejected with 401**:

```text
Error code: 401 - {'error': {'message': 'No cookie auth credentials found', 'code': 401}}
```

So: **OpenRouter is working**, but **authentication is failing** (key missing or wrong).

---

## Likely cause

The app expects your OpenRouter key in the **`Authorization: Bearer <key>`** header.  
“No cookie auth credentials found” usually means either:

1. **No API key is sent** — `RAG_LLM_API_KEY` (and/or `IMAGE_GEN_API_KEY`) is empty or not loaded from `.env`, or  
2. **Wrong or invalid key** — key is mistyped, expired, or revoked.

---

## What to do

### 1. Ensure the key is in `.env`

Edit (do not commit):

**`trial/implement/Paper2Slides/paper2slides/.env`**

Set both:

- `RAG_LLM_API_KEY="<your-openrouter-key>"`
- `IMAGE_GEN_API_KEY="<your-openrouter-key>"`

Use the **same** OpenRouter key from `openRouterKey.md` (or your key store).  
No spaces around `=`, and the key in quotes.

### 2. Run from the Paper2Slides repo directory

So that the code finds `paper2slides/.env`:

```bash
cd ".../trial/implement/Paper2Slides"
conda activate paper2slides
python -m paper2slides --input "../COCO_2310.18955v3.pdf" ...
```

### 3. Check the key

- In [OpenRouter Keys](https://openrouter.ai/keys): confirm the key exists and isn’t revoked.  
- Optionally create a **new** key and put that in `.env` (then re-run).

### 4. Quick test (optional)

From the repo directory with `conda activate paper2slides`:

```bash
cd ".../trial/implement/Paper2Slides"
python -c "
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path('paper2slides/.env'))
key = os.getenv('RAG_LLM_API_KEY')
print('Key set:', bool(key and key.strip()))
print('Key prefix:', (key[:12] + '...') if key else 'EMPTY')
if key:
    from openai import OpenAI
    c = OpenAI(api_key=key, base_url='https://openrouter.ai/api/v1')
    r = c.chat.completions.create(model='openai/gpt-4o-mini', messages=[{'role':'user','content':'Say OK'}], max_tokens=5)
    print('OpenRouter OK:', r.choices[0].message.content)
"
```

- If you see `Key set: False` or `EMPTY` → fix `.env` (step 1).  
- If you see another error (e.g. 401/403) → key is invalid or not allowed for that model (step 3).  
- If you see `OpenRouter OK: ...` → API is working; re-run Paper2Slides.

---

## Summary

| Check                         | Action                                      |
|------------------------------|---------------------------------------------|
| OpenRouter API working?      | Yes — 401 means “rejecting unauthenticated” |
| Fix 401                      | Set valid key in `paper2slides/.env`        |
| After editing `.env`         | Re-run Paper2Slides from `Paper2Slides` dir |
