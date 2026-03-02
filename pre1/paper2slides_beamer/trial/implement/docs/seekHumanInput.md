# Human Input Required for Paper2Slides Implementation

**Paper**: "Doubly-Bounded Queue for Constrained Online Learning: Keeping Pace with Dynamics of Both Loss and Constraint" (AAAI 2025)

**Date**: January 31, 2026

---

## 🎯 Critical Decisions Needed Before Implementation

### 1. API Configuration (REQUIRED)

**Status**: ⚠️ **ACTION REQUIRED**

Paper2Slides requires API keys for LLM and image generation services.

**Options**:

- [ ] **OpenAI** (GPT-4, DALL-E)

  - API Key: `OPENAI_API_KEY`
  - Models: GPT-4 for text, DALL-E for images
- [ ] **Google Gemini** (Recommended for academic papers)

  - API Key: `GOOGLE_API_KEY` or `IMAGE_GEN_API_KEY`
  - Models: Gemini Pro for text, Gemini Pro Image for images
  - Better for mathematical notation and technical content
- [X] **OpenRouter** (Default in Paper2Slides)

  - API Key: store in `openRouterKey.md` (gitignored); copy into `.env` as `RAG_LLM_API_KEY` and `IMAGE_GEN_API_KEY`
  - Model (image): `google/gemini-3-pro-image-preview`
  - **No OpenAI key needed:** use the **same OpenRouter key for RAG** — set `RAG_LLM_BASE_URL="https://openrouter.ai/api/v1"` and `RAG_LLM_API_KEY` to your OpenRouter key. RAG/LLM calls then go through OpenRouter (OpenAI-compatible API).

**Decision Required**:

```
Which API provider do you have access to?
[ ] OpenAI
[ ] Google Gemini
[ ] OpenRouter
[ ] Other: ___________

API Key available? [ ] Yes [ ] No (need to obtain)
```

**Next Steps**:

1. Obtain API key from chosen provider
2. Create `.env` file in Paper2Slides directory
3. Configure according to `.env.example`

---

### 2. Presentation Context (REQUIRED)

**Status**: ⚠️ **ACTION REQUIRED**

**Questions**:

#### A. Presentation Length

```
What is the target presentation duration?
[ ] Short (5-10 minutes) → --length short (~8-12 slides)
[ ] Medium (15-20 minutes) → --length medium (~15-20 slides)
[ ] Long (25-30 minutes) → --length long (~25-30 slides)

Recommendation for AAAI conference talk: Medium (20 minutes)
```

#### B. Presentation Style

```
What style best fits your presentation context?
[ ] Academic (clean, professional, formal) → --style academic
[ ] Doraemon (colorful, friendly, illustrated) → --style doraemon
[ ] Custom (describe your vision) → --style "your description here"

Recommendation for AAAI: Academic style
```

#### C. Audience Background

```
Who is your target audience?
[ ] Expert researchers in online learning/optimization
[ ] General machine learning audience
[ ] Mixed audience (experts + students)
[ ] Other: ___________

This helps determine technical depth in slides.
```

---

### 3. Content Emphasis (RECOMMENDED)

**Status**: 🟡 **RECOMMENDED INPUT**

The COLDQ paper has multiple strong contributions. Which aspects should be emphasized?

#### Primary Focus (Choose 1-2)

```
[ ] Novel algorithm design (doubly-bounded virtual queue)
[ ] Theoretical contributions (smooth approach to optimal bounds)
[ ] Experimental results (outperforms state-of-the-art)
[ ] Practical applications (job scheduling, resource allocation)
```

#### Key Messages to Highlight

```
[ ] Problem motivation: Existing work doesn't recover O(1) violation
[ ] Innovation: Both lower AND upper bounds (not just one)
[ ] Main result: O(T^{V_g}) violation → O(1) as V_g → 0
[ ] Lyapunov drift analysis technique
[ ] Experimental validation on 4 scenarios
```

**Recommendation**:

- Primary: Novel algorithm + theoretical contributions
- Secondary: Experimental validation
- Rationale: AAAI values theoretical novelty with empirical support

---

### 4. Technical Details Level (RECOMMENDED)

**Status**: 🟡 **RECOMMENDED INPUT**

How much mathematical detail should slides include?

#### Equations & Proofs

```
[ ] High detail: Include key equations, proof sketches, algorithm pseudocode
[ ] Medium detail: Main theorems, algorithm overview, key equations only
[ ] Low detail: Intuition and results, minimal equations

Recommendation for AAAI: Medium to High (expert audience)
```

#### Specific Content Decisions

```
Include algorithm pseudocode?
[ ] Yes, full COLDQ algorithm
[ ] Yes, simplified version
[ ] No, just conceptual explanation

Include comparison tables (Table 1 & 2)?
[ ] Yes, both tables (time-varying and fixed constraints)
[ ] Yes, one table only (which? _______)
[ ] No, summarize in text

Include experimental figures?
[ ] All 4 figures (fixed_linear, fixed_quadratic, time_varying, job_schedule)
[ ] Selected figures only (which? _______)
[ ] No figures, just summarize results
```

**Recommendation**:

- Include full algorithm pseudocode
- Include both comparison tables (key contribution)
- Include all 4 experimental figures (strong validation)

---

### 5. Installation & Setup Status (REQUIRED)

**Status**: ⚠️ **ACTION REQUIRED**

#### Paper2Slides Installation

```
Have you installed Paper2Slides?
[ ] Yes, already installed and tested
[ ] No, need to install

If No, follow these steps:
1. git clone https://github.com/HKUDS/Paper2Slides.git
2. cd Paper2Slides
3. conda create -n paper2slides python=3.12 -y
4. conda activate paper2slides
5. pip install -r requirements.txt
6. Configure .env file with API keys
```

#### Environment Check

```
Python version: [ ] 3.12 [ ] Other: _____
Conda installed: [ ] Yes [ ] No
Git installed: [ ] Yes [ ] No
```

---

### 6. Input File Format (DECISION NEEDED)

**Status**: ⚠️ **ACTION REQUIRED**

Paper2Slides can accept multiple input formats. Which should we use?

#### Available Options

```
[ ] LaTeX source (aaai25.tex) - RECOMMENDED
    Pros: Best for mathematical notation, includes all content
    Cons: Requires LaTeX parsing, may have compatibility issues
  
[ ] PDF (need to compile aaai25.tex to PDF first)
    Pros: Universal format, no parsing issues
    Cons: Harder to extract structured content
  
[ ] Markdown (need to convert from LaTeX)
    Pros: Clean structure, easy parsing
    Cons: May lose mathematical notation fidelity
```

**Current Status**:

- We have: `aaai25.tex`, `aaai25.bbl`, `aaai25.sty`
- We have: 4 PDF figures (experimental results)
- We need: PDF version of paper (if choosing PDF input)

**Recommendation**: Start with LaTeX source (`aaai25.tex`)

**Action if PDF needed**:

```bash
cd paper/
pdflatex aaai25.tex
bibtex aaai25
pdflatex aaai25.tex
pdflatex aaai25.tex
```

---

### 7. Processing Mode (DECISION NEEDED)

**Status**: 🟡 **RECOMMENDED INPUT**

#### Fast Mode vs. Normal Mode

```
[ ] Fast Mode (--fast)
    - Skip RAG indexing
    - Direct LLM query
    - Faster (5-10 minutes)
    - Good for: Quick preview, short papers
  
[ ] Normal Mode (default)
    - Full RAG indexing
    - Deep document analysis
    - Slower (15-30 minutes)
    - Good for: Complex papers, final version
```

**Paper Analysis**:

- AAAI25 paper: ~10 pages, complex mathematical content
- Multiple sections: intro, related work, problem formulation, algorithm, theory, experiments
- Heavy mathematical notation

**Recommendation**:

- **First run**: Fast mode for quick preview
- **Second run**: Normal mode for final slides

---

### 8. Parallel Processing (OPTIONAL)

**Status**: 🟢 **OPTIONAL**

```
Enable parallel slide generation?
[ ] Yes, use 2 workers (--parallel 2) - RECOMMENDED
[ ] Yes, use 4 workers (--parallel 4) - if powerful machine
[ ] No, sequential generation (default)

Recommendation: Use --parallel 2 for faster generation
```

---

### 9. Output Customization (OPTIONAL)

**Status**: 🟢 **OPTIONAL**

#### Custom Style Description (if not using built-in themes)

```
If choosing custom style, describe your vision:
Example: "minimalist design with blue and white color scheme, 
emphasizing mathematical formulas and algorithms, professional 
conference presentation style, clean sans-serif fonts"

Your custom style description:
_____________________________________________________________
_____________________________________________________________
```

#### Additional Preferences

```
[ ] Include title slide with author photos
[ ] Include outline/agenda slide
[ ] Include "thank you" / Q&A slide at end
[ ] Include references/bibliography slide
[ ] Add institution logo (provide logo file: _____)
[ ] Add conference logo (AAAI 2025)
```

---

## 📋 Implementation Plan Summary

Based on the plan in `p2splan.md`, here's the recommended workflow:

### Phase 1: Quick Preview (Estimated: 15 minutes)

```bash
# Activate environment
conda activate paper2slides

# Navigate to paper folder
cd /path/to/trial/paper/

# Run fast mode for preview
python -m paper2slides \
  --input aaai25.tex \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast
```

**Expected Output**:

- 8-12 slides in `outputs/aaai25/paper/fast/slides_academic_short/output/`
- Review to assess quality and coverage

### Phase 2: Full Generation (Estimated: 30 minutes)

```bash
# Run normal mode with parallel processing
python -m paper2slides \
  --input aaai25.tex \
  --output slides \
  --content paper \
  --style academic \
  --length medium \
  --parallel 2
```

**Expected Output**:

- 15-20 slides in `outputs/aaai25/paper/normal/slides_academic_medium/output/`
- Checkpoint files for resume/modification

### Phase 3: Refinement (If Needed)

```bash
# Change style only (reuses RAG and summary)
python -m paper2slides \
  --input aaai25.tex \
  --output slides \
  --style "your custom style description" \
  --length medium \
  --from-stage plan

# Or regenerate images only
python -m paper2slides \
  --input aaai25.tex \
  --output slides \
  --style academic \
  --length medium \
  --from-stage generate
```

---

## ✅ Pre-Implementation Checklist

Before running Paper2Slides, ensure:

### Environment Setup

- [ ] Paper2Slides repository cloned
- [ ] Conda environment created (python 3.12)
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file configured with API keys

### Input Files Ready

- [ ] `aaai25.tex` in `paper/` folder
- [ ] `aaai25.bbl` in `paper/` folder
- [ ] `aaai25.sty` in `paper/` folder
- [ ] Experimental figures (4 PDFs) in `paper/` folder
- [ ] (Optional) PDF version of paper compiled

### Decisions Made

- [ ] API provider chosen and key obtained
- [ ] Presentation length decided (short/medium/long)
- [ ] Style selected (academic/doraemon/custom)
- [ ] Processing mode chosen (fast/normal)
- [ ] Content emphasis determined

### Output Location

- [ ] Output directory planned: `implement/outputs/`
- [ ] Sufficient disk space available (~100MB per run)

---

## 🚨 Known Issues & Troubleshooting

### Potential Issues with AAAI25 Paper

1. **Complex LaTeX Macros**

   - Paper uses custom macros: `\ie`, `\st`, `\eg`
   - May need preprocessing if parser fails
   - Solution: Define macros in preamble or replace with text
2. **Mathematical Notation**

   - Heavy use of `$\mathcal{O}$` notation
   - Subscripts and superscripts: `$T^\frac{1+V_x}{2}$`
   - May need manual verification after generation
3. **Tables (Table 1 & 2)**

   - Complex comparison tables with multiple columns
   - May not render well in slides
   - Consider simplifying or splitting
4. **Bibliography**

   - Uses `natbib` with `.bbl` file
   - May need to include `.bib` file if citations fail
   - Or manually add key references
5. **Figures**

   - 4 experimental PDFs need to be accessible
   - Ensure they're in same directory as `.tex` file
   - Or use absolute paths

---

## 📊 Expected Timeline

| Phase           | Task                                | Duration           | Status      |
| --------------- | ----------------------------------- | ------------------ | ----------- |
| Setup           | Install Paper2Slides, configure API | 30 min             | ⏳ Pending  |
| Preview         | Fast mode generation                | 10 min             | ⏳ Pending  |
| Review          | Assess preview quality              | 10 min             | ⏳ Pending  |
| Full Gen        | Normal mode with parallel           | 30 min             | ⏳ Pending  |
| Review          | Check full slides                   | 15 min             | ⏳ Pending  |
| Refine          | Adjust style/regenerate (if needed) | 20 min             | ⏳ Optional |
| **Total** |                                     | **~2 hours** |             |

---

## 🎓 Learning Objectives for PhD Students

Through this implementation, students will learn:

1. **AI Tool Integration**: How to use AI-powered tools for academic work
2. **API Configuration**: Setting up and managing API keys securely
3. **Prompt Engineering**: How style descriptions affect output
4. **Iterative Refinement**: Using checkpoints for efficient iteration
5. **Quality Assessment**: Evaluating AI-generated content critically
6. **Manual Polish**: When and how to refine AI output

---

## 📝 Next Steps

### Immediate Actions (Before Implementation)

1. **Answer all "REQUIRED" questions above**
2. **Obtain API key** from chosen provider
3. **Install Paper2Slides** if not already done
4. **Compile paper to PDF** (if choosing PDF input)

### After Human Input Received

1. Create `.env` file with provided API keys
2. Run Phase 1 (Quick Preview)
3. Share preview slides for feedback
4. Proceed to Phase 2 based on feedback
5. Document results and lessons learned

---

## 📞 Questions to Discuss

1. **API Access**: Do you have existing API keys, or do we need to obtain them?
2. **Presentation Context**: Is this for AAAI conference presentation or practice?
3. **Time Constraints**: When do you need the slides completed?
4. **Budget**: Are there API cost constraints we should consider?
5. **Collaboration**: Will multiple people review/edit the slides?

---

## 💡 Recommendations Summary

Based on the paper content and typical AAAI presentation requirements:

**Recommended Configuration**:

```bash
python -m paper2slides \
  --input aaai25.tex \
  --output slides \
  --content paper \
  --style academic \
  --length medium \
  --parallel 2
```

**Rationale**:

- **LaTeX input**: Best for mathematical notation
- **Academic style**: Appropriate for AAAI conference
- **Medium length**: 15-20 slides for 20-minute talk
- **Parallel processing**: Faster generation

**Expected Result**:

- Professional slides with proper math notation
- Automatic extraction of key contributions
- Inclusion of comparison tables and experimental results
- Source-traceable content for verification

---

## 📄 Document Status

- **Created**: January 31, 2026
- **Status**: Awaiting human input
- **Next Update**: After receiving decisions and running preview

---

**Please provide your decisions on the REQUIRED items above so we can proceed with implementation.**
