we have a collection of templates and functions found in 
Teaching/Courses/MCCP 6020/PhDagentSpring2026/writing/academicPhrasebank/general-functions
Teaching/Courses/MCCP 6020/PhDagentSpring2026/writing/academicPhrasebank/paper-sections

now we have a collection of papers Teaching/Courses/MCCP 6020/PhDagentSpring2026/writing/buildPaperCollection_arXiv/html_collection

we want to go through each sentence in each paper and check if they serve the functions similar to the templates above 

we need to generate a report for each function to present the original templates, similar sentences found in the paper, source of the paper, and the new template extracted from the paper 

**Matching method:** Sentences from HTML papers are sent to an LLM together with the phrasebank templates/functions; the LLM identifies which sentences match each function (by rhetorical role) and optionally extracts new templates. Pattern matching in Python is not used for this; the script calls an LLM (OpenAI-compatible API).

**Setup:** Set `OPENAI_API_KEY`; optionally `OPENAI_BASE_URL`, `MAP_SENTENCES_MODEL` (default `gpt-4o-mini`). Install `pip install -r MapSentences/requirements.txt`.

**Run:** `python map_sentences.py <html_basename> <out_dir>` — e.g. `python map_sentences.py 2211.12588 trial`. Use `--pattern` to force legacy pattern matching (no LLM).

let's use Teaching/Courses/MCCP 6020/PhDagentSpring2026/writing/buildPaperCollection_arXiv/html_collection/2211.12588.html as a test input file 
generate files in Teaching/Courses/MCCP 6020/PhDagentSpring2026/writing/academicPhrasebank/MapSentences/trial 
if a sentence for a specific function cannot be found from the paper, we can put a placeholder and indicates sentence not found; but the original templates should be added to the file 