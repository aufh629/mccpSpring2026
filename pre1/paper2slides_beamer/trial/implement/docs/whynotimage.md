# Why Image Generation Failed

Paper2Slides’ **generate** stage produces one image per slide (and then `slides.pdf`) by calling an **image-generation API**. That step failed in our runs; only text-only slides were produced.

---

## 1. What the pipeline expects

- **Stage:** Generate (after RAG → Summary → Plan).
- **Config:** `IMAGE_GEN_API_KEY` and `IMAGE_GEN_BASE_URL` in `Paper2Slides/paper2slides/.env`. Optional: `IMAGE_GEN_PROVIDER` (e.g. `openrouter`), `IMAGE_GEN_MODEL` (e.g. an image-capable model).
- **Behavior:** The code uses the OpenAI client against that base URL to call a **chat/completions-style** endpoint that can return **images** (e.g. vision/image-generation models). It expects a normal API JSON response with `response.choices` (and image data in the message).

---

## 2. Why it failed in our runs

### 2.1 Poe as image backend

- When the image stage used **Poe** (or an unset image config that fell back to a Poe-like endpoint), the call failed with **401** and message like: **“No cookie auth credentials found”.**
- Poe’s API is built for **chat**, not for the **image-generation** usage Paper2Slides assumes. So with Poe (or cookie-based auth) as the image backend, the image stage fails with 401.

### 2.2 GPT-Best (Apifox) as image backend

- When we set **IMAGE_GEN_*** to the same key and base URL as **GPT-Best** (bltkey), the image request did **not** return a valid API response.
- The server responded with **HTML** (the Apifox docs page) instead of JSON. The client then reported something like: **“API response has no choices”.**
- So either:
  - The **image endpoint** (or model) we used is not supported / not correctly configured on GPT-Best, and the server returns an error page (HTML), or  
  - The **path or model name** for image generation is different from the chat path, and we hit a non-API URL that serves HTML.

In both cases, the code expects `response.choices`; getting HTML instead causes the stage to fail.

---

## 3. What would be needed for images to work

1. **Use an image-capable API** that:
   - Accepts the same style of request (e.g. chat/completions with image-capable model), and  
   - Returns JSON with `choices` and image data (or a supported response format the code can handle).
2. **Correct base URL and model:**  
   For GPT-Best (or any proxy), use the **exact** base URL and **model name** documented for **image generation**, not just the chat endpoint.
3. **Valid key and auth:**  
   Ensure `IMAGE_GEN_API_KEY` (and any provider-specific auth) is valid for that image endpoint (no 401).

Until the image stage is pointed at such an API and model, Paper2Slides will only produce **text-only** slides (e.g. via `plan2slides_text.py`).

---

## 4. Short summary

| Cause | Effect |
|-------|--------|
| Poe / cookie auth used for image API | 401 “No cookie auth credentials found”; image stage fails. |
| GPT-Best (or proxy) returns HTML for image request | “API response has no choices”; image stage fails. |
| Missing or wrong image model/endpoint | Same: no valid `choices` in response. |

**Bottom line:** Image generation failed because the configured image backend did not return a valid API response (either 401 with Poe, or HTML instead of JSON with GPT-Best). Fixing it requires using a supported image API and the correct endpoint/model for image generation.
