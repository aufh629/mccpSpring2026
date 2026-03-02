# Using Paper2Slides from Hong Kong (OpenAI Blocked)

OpenAI blocks access from some regions (including Hong Kong). You can still use Paper2Slides by using **OpenRouter** with **non-OpenAI models** only.

---

## How it works

- **OpenRouter** is a separate service (openrouter.ai). It is **not** OpenAI, so OpenAI’s geo-blocking does **not** apply to OpenRouter.
- You call **OpenRouter’s API** with your OpenRouter key; OpenRouter then calls the model provider (e.g. Google, Anthropic) on their side.
- If you **never request an OpenAI model**, you never touch OpenAI, so blocking in HK is irrelevant.

---

## What to set in `.env`

In **`Paper2Slides/paper2slides/.env`** (local only; do not commit):

1. **OpenRouter key** (from openRouterKey.md or openrouter.ai/keys):
   ```bash
   RAG_LLM_API_KEY="<your-openrouter-key>"
   IMAGE_GEN_API_KEY="<your-openrouter-key>"
   RAG_LLM_BASE_URL="https://openrouter.ai/api/v1"
   IMAGE_GEN_BASE_URL="https://openrouter.ai/api/v1"
   ```

2. **Use a non-OpenAI model** so no request goes to OpenAI:
   ```bash
   LLM_MODEL="google/gemini-2.0-flash"
   ```
   This is used for RAG, summary, and planning. Image generation is already set to a Google model in the template (`IMAGE_GEN_MODEL="google/gemini-3-pro-image-preview"` or similar).

---

## Recommended non-OpenAI models (OpenRouter IDs)

| Use case        | OpenRouter model ID                    | Provider  |
|----------------|----------------------------------------|-----------|
| RAG / summary  | `google/gemini-2.0-flash`             | Google    |
| RAG / summary  | `google/gemini-2.5-pro-preview`       | Google    |
| RAG / summary  | `anthropic/claude-3.5-sonnet`         | Anthropic |
| RAG / summary  | `meta-llama/llama-3.3-70b-instruct`   | Meta      |
| Image gen      | `google/gemini-3-pro-image-preview`   | Google    |

Full list: https://openrouter.ai/models

---

## Do **not** use these from HK

- Any model ID starting with `openai/` (e.g. `openai/gpt-4o-mini`, `openai/gpt-4o`) — these go through OpenAI and can be blocked in HK.

---

## Summary

| Item              | Setting for HK / no OpenAI     |
|-------------------|---------------------------------|
| API               | OpenRouter only                |
| Key               | OpenRouter key in `.env`       |
| RAG/LLM model     | `LLM_MODEL=google/gemini-2.0-flash` (or another non-OpenAI model) |
| Image model       | `IMAGE_GEN_MODEL=google/...` (already non-OpenAI in template) |

With this, Paper2Slides uses only OpenRouter + non-OpenAI models, so OpenAI blocking in HK does not affect you.
