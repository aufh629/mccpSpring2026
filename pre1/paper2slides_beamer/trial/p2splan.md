# Paper2Slides Plan: Converting AAAI25 Paper to Slides

## Overview
Paper2Slides is an AI-powered tool developed by HKUDS that converts academic papers into professional presentation slides using a 4-stage pipeline with RAG (Retrieval-Augmented Generation) technology.

**GitHub Repository**: https://github.com/HKUDS/Paper2Slides

---

## Tool Capabilities

### Key Features
1. **Multi-format Support**: Accepts PDF, LaTeX, Word, Excel, PowerPoint, and Markdown
2. **RAG-Powered Extraction**: Intelligently captures key insights, figures, tables, and citations
3. **Source Traceability**: Every generated content links back to original source
4. **Custom Styling**: Built-in themes (academic, doraemon) or custom natural language descriptions
5. **Checkpoint System**: Saves progress at 4 stages for pause/resume/regeneration
6. **Fast Mode**: Skip RAG indexing for quick previews
7. **Parallel Processing**: Generate multiple slides simultaneously

### Output Quality
- Professional-grade visuals with publication-quality design
- Automatic figure and table extraction
- Maintains academic rigor with source citations
- Multiple style options for different presentation contexts

---

## 4-Stage Pipeline

| Stage | Description | Checkpoint File | Output |
|-------|-------------|-----------------|--------|
| 🔍 **RAG** | Parse documents and construct intelligent retrieval index | `checkpoint_rag.json` | Searchable knowledge base |
| 📊 **Analysis** | Extract document structure, identify key figures, tables, content hierarchy | `checkpoint_summary.json` | Structured content map |
| 📋 **Planning** | Generate optimized content layout and slide organization strategy | `checkpoint_plan.json` | Presentation blueprint |
| 🎨 **Creation** | Render final high-quality slide visuals | Output directory | Polished presentation materials |

---

## Installation & Setup

### Prerequisites
- Python 3.12
- Conda environment manager
- API keys for LLM services (OpenAI, Google Gemini, or OpenRouter)

### Installation Steps

```bash
# 1. Clone repository
git clone https://github.com/HKUDS/Paper2Slides.git
cd Paper2Slides

# 2. Create and activate conda environment
conda create -n paper2slides python=3.12 -y
conda activate paper2slides

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API keys
# Create .env file in paper2slides/ directory
# Copy from paper2slides/.env.example and fill in:
# - LLM API keys (OpenAI/Google/OpenRouter)
# - IMAGE_GEN_PROVIDER (openrouter or google)
# - IMAGE_GEN_API_KEY
# - IMAGE_GEN_MODEL (default: google/gemini-3-pro-image-preview)
```

---

## Workflow for AAAI25 Paper (COLDQ)

### Paper Details
- **Title**: "Doubly-Bounded Queue for Constrained Online Learning"
- **Source Files**: `aaai25.tex`, `aaai25.bbl`, `aaai25.sty`
- **Content Type**: Academic research paper
- **Topic**: Online convex optimization with time-varying constraints

### Recommended Approach

#### Option 1: From LaTeX Source (Recommended)
```bash
# Navigate to trial folder
cd /path/to/trial/

# Generate slides with academic style
python -m paper2slides \
  --input aaai25.tex \
  --output slides \
  --content paper \
  --style academic \
  --length medium \
  --parallel 2
```

#### Option 2: From PDF (If Available)
```bash
python -m paper2slides \
  --input aaai25.pdf \
  --output slides \
  --content paper \
  --style academic \
  --length medium \
  --parallel 2
```

#### Option 3: Fast Preview Mode
```bash
# For quick iteration and preview
python -m paper2slides \
  --input aaai25.tex \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast
```

---

## Command Line Options Explained

### Essential Parameters

| Option | Description | Recommended for AAAI25 Paper |
|--------|-------------|------------------------------|
| `--input, -i` | Input file(s) or directory | `aaai25.tex` or `aaai25.pdf` |
| `--output` | Output type: `slides` or `poster` | `slides` |
| `--content` | Content type: `paper` or `general` | `paper` |
| `--style` | Style: `academic`, `doraemon`, or custom | `academic` |
| `--length` | Slides length: `short`, `medium`, `long` | `medium` (for 15-20 min talk) |
| `--fast` | Skip RAG indexing for quick preview | Use for iteration |
| `--parallel` | Enable parallel generation (default: 2 workers) | `2` or `4` |

### Advanced Options

| Option | Description | Use Case |
|--------|-------------|----------|
| `--density` | Poster density: `sparse`, `medium`, `dense` | Only for poster output |
| `--from-stage` | Force restart from stage: `rag`, `summary`, `plan`, `generate` | Modify style/regenerate |
| `--debug` | Enable debug logging | Troubleshooting |
| `--list` | List all processed outputs | Review previous runs |

---

## Custom Styling Options

### Built-in Styles
1. **academic**: Clean, professional academic presentation style
2. **doraemon**: Colorful, friendly style with illustrations

### Custom Style Example
```bash
python -m paper2slides \
  --input aaai25.tex \
  --output slides \
  --style "minimalist design with blue and white color scheme, emphasizing mathematical formulas and algorithms, professional conference presentation style" \
  --length medium
```

### Style Tips for Technical Papers
- Use **academic** style for formal conference presentations
- Emphasize: "clear mathematical notation", "algorithm visualization", "clean diagrams"
- Avoid: overly decorative elements that distract from technical content

---

## Checkpoint & Resume Strategy

### Automatic Checkpoints
Paper2Slides saves progress at each stage:
- `checkpoint_rag.json`: Parsed document content
- `checkpoint_summary.json`: Extracted figures, tables, structure
- `checkpoint_plan.json`: Content layout plan

### Resume Scenarios

| Scenario | Command |
|----------|---------|
| Resume after interruption | Run the same command again (auto-detects) |
| Change style only | Add `--from-stage plan` |
| Regenerate images | Add `--from-stage generate` |
| Full restart | Add `--from-stage rag` |

### Example: Iterate on Style
```bash
# First run
python -m paper2slides --input aaai25.tex --output slides --style academic --length medium

# Change to custom style (reuses RAG and summary)
python -m paper2slides --input aaai25.tex --output slides \
  --style "modern tech conference style with dark background" \
  --length medium \
  --from-stage plan
```

---

## Expected Output Structure

```
outputs/
└── aaai25/
    └── paper/
        └── normal/  (or fast/)
            ├── checkpoint_rag.json
            ├── checkpoint_summary.json
            ├── summary.md
            └── slides_academic_medium/
                ├── state.json
                ├── checkpoint_plan.json
                └── output/
                    ├── slide_01.png
                    ├── slide_02.png
                    ├── slide_03.png
                    ├── ...
                    └── slides.pdf  ← Final presentation
```

---

## Human Input Required

### Before Running
1. **API Keys Configuration**
   - OpenAI API key OR Google Gemini API key OR OpenRouter API key
   - Image generation API key
   - Set in `.env` file in `paper2slides/` directory

2. **Input File Preparation**
   - Ensure LaTeX source (`aaai25.tex`) is complete
   - Include all referenced files (`.bbl`, `.sty`, figures if any)
   - OR convert to PDF if LaTeX compilation is problematic

3. **Presentation Context**
   - Decide presentation length: short (5-10 min), medium (15-20 min), long (30+ min)
   - Choose style: academic (formal) vs. custom (specify aesthetic)
   - Determine if poster is also needed

### During Processing
1. **Monitor Progress**
   - Check terminal output for stage completion
   - Review checkpoint files if process is interrupted

2. **Quality Control Checkpoints**
   - After RAG stage: Verify document parsing in `checkpoint_rag.json`
   - After Analysis: Review `summary.md` for content extraction accuracy
   - After Planning: Check `checkpoint_plan.json` for slide organization
   - After Generation: Review individual slide images before final PDF

### After Generation
1. **Content Review**
   - Verify all key contributions are included
   - Check mathematical notation rendering
   - Ensure figures and tables are properly extracted
   - Validate citations and references

2. **Style Adjustments**
   - If style doesn't match expectations, regenerate with `--from-stage plan`
   - Try different style descriptions or built-in themes

3. **Length Adjustments**
   - Too many slides? Regenerate with `--length short`
   - Too few slides? Regenerate with `--length long`

---

## Advantages for PhD Students

### Time Savings
- **Automated extraction**: No manual copying of figures, tables, equations
- **Intelligent summarization**: Key points automatically identified
- **Fast iteration**: Checkpoint system allows quick style changes

### Quality Improvements
- **Professional design**: Publication-quality visuals
- **Consistent formatting**: Uniform style across all slides
- **Source traceability**: Easy to verify content against original paper

### Learning Opportunities
- **Content organization**: See how AI structures complex technical content
- **Presentation design**: Learn from AI-generated layouts
- **Iterative refinement**: Experiment with different styles and lengths

---

## Limitations & Considerations

### Technical Limitations
1. **LaTeX Complexity**: Very complex LaTeX with custom macros may not parse correctly
2. **Figure Quality**: Depends on source figure resolution in paper
3. **Mathematical Notation**: May need manual verification for complex equations
4. **Context Window**: Extremely long papers may require normal mode (not fast)

### Requires Manual Review
1. **Content Accuracy**: AI may misinterpret technical concepts
2. **Emphasis**: May not highlight the most important contributions
3. **Flow**: Logical progression may need human adjustment
4. **Audience Adaptation**: AI doesn't know your specific audience

### Best Practices
1. **Start with Fast Mode**: Quick preview to assess output quality
2. **Iterate on Style**: Try different styles to find best fit
3. **Manual Polish**: Use AI output as starting point, refine manually
4. **Verify Math**: Always check mathematical notation and formulas
5. **Test Presentation**: Practice with generated slides, adjust as needed

---

## Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| LaTeX parsing fails | Convert to PDF first, or simplify LaTeX |
| Missing figures | Ensure figure files are in same directory |
| Poor quality output | Try different style or increase length |
| API errors | Check `.env` configuration and API credits |
| Slow processing | Use `--fast` mode or reduce `--length` |

### Getting Help
- Check GitHub issues: https://github.com/HKUDS/Paper2Slides/issues
- Review documentation: README.md in repository
- Enable `--debug` flag for detailed logging

---

## Recommended Workflow for AAAI25 Paper

### Step-by-Step Process

1. **Setup** (One-time)
   ```bash
   git clone https://github.com/HKUDS/Paper2Slides.git
   cd Paper2Slides
   conda create -n paper2slides python=3.12 -y
   conda activate paper2slides
   pip install -r requirements.txt
   # Configure .env file with API keys
   ```

2. **Quick Preview**
   ```bash
   python -m paper2slides \
     --input /path/to/trial/aaai25.tex \
     --output slides \
     --content paper \
     --style academic \
     --length short \
     --fast
   ```

3. **Review & Iterate**
   - Check generated slides in `outputs/` directory
   - Assess content coverage and style
   - Decide on adjustments

4. **Full Generation**
   ```bash
   python -m paper2slides \
     --input /path/to/trial/aaai25.tex \
     --output slides \
     --content paper \
     --style academic \
     --length medium \
     --parallel 2
   ```

5. **Style Refinement** (if needed)
   ```bash
   python -m paper2slides \
     --input /path/to/trial/aaai25.tex \
     --output slides \
     --style "clean modern design with emphasis on algorithms and mathematical proofs" \
     --length medium \
     --from-stage plan
   ```

6. **Manual Polish**
   - Export slides to PowerPoint or Keynote
   - Add speaker notes
   - Adjust emphasis and flow
   - Practice presentation

---

## Comparison: When to Use Paper2Slides vs. Beamer

| Criterion | Paper2Slides | Beamer |
|-----------|--------------|--------|
| **Speed** | Fast (minutes) | Slow (hours) |
| **Automation** | High (AI-driven) | Low (manual) |
| **Customization** | Limited to prompts | Full control |
| **Quality** | Good starting point | Professional polish |
| **Learning Curve** | Easy | Moderate to steep |
| **Best For** | Quick drafts, iteration | Final presentations |

### Recommended Approach
1. Use **Paper2Slides** to generate initial draft quickly
2. Export to editable format (PowerPoint/Keynote)
3. Use **Beamer** for final version if LaTeX integration is important
4. Combine: Paper2Slides for content, Beamer for precise formatting

---

## Conclusion

Paper2Slides is an excellent tool for PhD students to:
- Quickly generate presentation drafts from papers
- Learn presentation structure from AI organization
- Iterate on different styles and lengths
- Save time on manual slide creation

**Key Takeaway**: Use Paper2Slides as a powerful starting point, but always apply human judgment for final refinement and adaptation to your specific audience and presentation context.
