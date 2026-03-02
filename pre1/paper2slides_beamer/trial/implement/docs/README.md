# Implementation Folder - Paper2Slides for COLDQ Paper

**Created**: January 31, 2026  
**Paper**: "Doubly-Bounded Queue for Constrained Online Learning" (AAAI 2025)  
**Tool**: Paper2Slides (AI-powered slide generation)

**→ Short instructions**: [INSTRUCTIONS.md](INSTRUCTIONS.md) — API keys, quick runs (first section / first 3 pages), COCO HTML/PDF.  
**→ API keys reference**: [API_KEYS.md](API_KEYS.md) — key files and `.env` (no secrets).  
**→ Current state**: [currentstate.md](currentstate.md) — what works, what doesn’t, folder layout.  
**→ Value**: [howthistoolcreatevalue.md](howthistoolcreatevalue.md) — how this tool creates value.

**Layout:** All docs live in `implement/docs/`; scripts in `scripts/`, inputs in `inputs/`, logs in `logs/`, samples in `samples/`. See [currentstate.md](currentstate.md).

---

## 📁 Folder Contents (docs/)

### Key docs

1. **seekHumanInput.md** - Comprehensive questionnaire for human decisions
   - API configuration requirements
   - Presentation context decisions
   - Content emphasis choices
   - Technical detail levels
   - Implementation checklist

2. **preliminarySlides_outline.md** - Detailed slide-by-slide plan
   - 23 slides structured for 20-minute AAAI talk
   - Section-by-section breakdown
   - Content extraction from paper
   - Visual design guidelines
   - Timing recommendations

3. **README.md** (this file) - Implementation guide

---

## 🎯 Purpose

This folder contains the implementation of the Paper2Slides plan (`../plan/p2splan.md`) for the COLDQ paper (`../paper/aaai25.tex`).

**Goal**: Generate professional presentation slides using AI-powered Paper2Slides tool.

---

## 📋 Implementation Status

### Phase 1: Planning ✅ COMPLETE
- [x] Human input requirements identified
- [x] Preliminary slides outline created
- [x] Content extraction mapped
- [x] Visual design guidelines established

### Phase 2: Setup ⏳ PENDING HUMAN INPUT
- [ ] API keys obtained and configured
- [ ] Paper2Slides installed and tested
- [ ] Presentation context decisions made
- [ ] Input files prepared

### Phase 3: Generation ⏳ PENDING
- [ ] Quick preview (fast mode) generated
- [ ] Preview reviewed and feedback collected
- [ ] Full slides (normal mode) generated
- [ ] Final slides reviewed

### Phase 4: Refinement ⏳ OPTIONAL
- [ ] Style adjustments made (if needed)
- [ ] Content emphasis refined (if needed)
- [ ] Manual polish applied

---

## 🚀 Quick Start Guide

### Step 1: Review Requirements
```bash
# Read the human input requirements
open seekHumanInput.md

# Review the preliminary outline
open preliminarySlides_outline.md
```

### Step 2: Make Decisions
Answer all "REQUIRED" questions in `seekHumanInput.md`:
- [ ] Choose API provider (OpenAI/Google/OpenRouter)
- [ ] Obtain API key
- [ ] Decide presentation length (short/medium/long)
- [ ] Select style (academic/doraemon/custom)
- [ ] Determine content emphasis

### Step 3: Install Paper2Slides (if not already done)
```bash
# Clone repository
git clone https://github.com/HKUDS/Paper2Slides.git
cd Paper2Slides

# Create conda environment
conda create -n paper2slides python=3.12 -y
conda activate paper2slides

# Install dependencies
pip install -r requirements.txt

# Configure .env file
cp paper2slides/.env.example paper2slides/.env
# Edit .env with your API keys
```

### Step 4: Run Quick Preview
```bash
# Activate environment
conda activate paper2slides

# Navigate to paper folder
cd ../paper/

# Run fast mode for preview
python -m paper2slides \
  --input aaai25.tex \
  --output slides \
  --content paper \
  --style academic \
  --length short \
  --fast
```

### Step 5: Review Preview
```bash
# Check output
ls -la outputs/aaai25/paper/fast/slides_academic_short/output/

# View slides
open outputs/aaai25/paper/fast/slides_academic_short/output/slides.pdf
```

### Step 6: Generate Full Slides
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

---

## 📊 Expected Output Structure

After running Paper2Slides, the output will be organized as:

```
implement/
├── README.md (this file)
├── seekHumanInput.md
├── preliminarySlides_outline.md
└── outputs/  (created by Paper2Slides)
    └── aaai25/
        └── paper/
            ├── fast/  (quick preview)
            │   ├── checkpoint_rag.json
            │   ├── checkpoint_summary.json
            │   ├── summary.md
            │   └── slides_academic_short/
            │       ├── checkpoint_plan.json
            │       ├── state.json
            │       └── output/
            │           ├── slide_01.png
            │           ├── slide_02.png
            │           ├── ...
            │           └── slides.pdf
            └── normal/  (full generation)
                ├── checkpoint_rag.json
                ├── checkpoint_summary.json
                ├── summary.md
                └── slides_academic_medium/
                    ├── checkpoint_plan.json
                    ├── state.json
                    └── output/
                        ├── slide_01.png
                        ├── slide_02.png
                        ├── ...
                        └── slides.pdf
```

---

## 🎨 Customization Options

### Style Options

**Academic** (Recommended for AAAI):
```bash
--style academic
```
- Clean, professional design
- Suitable for technical conferences
- Emphasizes content over decoration

**Doraemon**:
```bash
--style doraemon
```
- Colorful, friendly style
- Good for less formal presentations
- More engaging visuals

**Custom**:
```bash
--style "minimalist design with blue and white color scheme, emphasizing mathematical formulas and algorithms, professional conference presentation style"
```
- Natural language description
- AI interprets and generates custom style
- Experiment with different descriptions

### Length Options

- `--length short`: 8-12 slides (5-10 min talk)
- `--length medium`: 15-20 slides (15-20 min talk) ← **Recommended for AAAI**
- `--length long`: 25-30 slides (25-30 min talk)

### Processing Options

- `--fast`: Skip RAG indexing (faster, less accurate)
- Default (normal): Full RAG indexing (slower, more accurate)
- `--parallel 2`: Use 2 workers for parallel generation
- `--parallel 4`: Use 4 workers (if powerful machine)

---

## 🔧 Troubleshooting

### Common Issues

**Issue 1: API Key Error**
```
Error: API key not found or invalid
```
**Solution**: 
- Check `.env` file in `Paper2Slides/paper2slides/` directory
- Ensure key is correctly formatted
- Verify key has sufficient credits

**Issue 2: LaTeX Parsing Fails**
```
Error: Failed to parse LaTeX file
```
**Solution**:
- Try converting to PDF first: `pdflatex aaai25.tex`
- Use PDF as input: `--input aaai25.pdf`
- Or simplify LaTeX (remove complex macros)

**Issue 3: Missing Figures**
```
Warning: Figure not found
```
**Solution**:
- Ensure all PDF figures are in same directory as .tex file
- Check figure paths in LaTeX source
- Copy figures to working directory

**Issue 4: Slow Processing**
```
Process taking too long...
```
**Solution**:
- Use `--fast` mode for quick preview
- Reduce `--length` to short
- Enable `--parallel` for faster generation

**Issue 5: Poor Quality Output**
```
Slides don't capture key content
```
**Solution**:
- Try normal mode (not fast) for better analysis
- Increase `--length` for more detail
- Adjust style description for custom styling
- Use `--from-stage plan` to regenerate with different emphasis

---

## 📝 Documentation Links

### Paper2Slides Resources
- **GitHub**: https://github.com/HKUDS/Paper2Slides
- **Documentation**: See README.md in Paper2Slides repository
- **Issues**: https://github.com/HKUDS/Paper2Slides/issues

### Related Files
- **Paper source**: `../paper/aaai25.tex`
- **Implementation plan**: `../plan/p2splan.md`
- **Beamer alternative**: `../plan/beamerPlan.md`

---

## 🎓 Learning Objectives

Through this implementation, you will:

1. **Understand AI-powered tools** for academic work
2. **Learn API integration** and configuration
3. **Practice prompt engineering** through style descriptions
4. **Experience iterative refinement** using checkpoints
5. **Develop critical evaluation** of AI-generated content
6. **Recognize when manual polish** is needed

---

## ✅ Quality Checklist

After generating slides, verify:

### Content Accuracy
- [ ] All key contributions included
- [ ] Mathematical notation correct
- [ ] Figures properly extracted and labeled
- [ ] Tables accurately reproduced
- [ ] Citations and references present

### Structure & Flow
- [ ] Logical progression from intro to conclusion
- [ ] Appropriate slide count for time limit
- [ ] Clear section transitions
- [ ] Balanced content distribution

### Visual Quality
- [ ] Readable fonts and sizes
- [ ] Consistent styling across slides
- [ ] Appropriate use of colors
- [ ] Figures clear and well-positioned
- [ ] Not too crowded or too sparse

### Technical Depth
- [ ] Appropriate for target audience
- [ ] Key equations included
- [ ] Algorithm clearly presented
- [ ] Theoretical results highlighted
- [ ] Experimental validation shown

---

## 🔄 Iteration Strategy

### First Iteration: Quick Preview
**Goal**: Assess feasibility and quality
**Command**: Fast mode, short length
**Time**: 10-15 minutes
**Review**: Content coverage, style, structure

### Second Iteration: Full Generation
**Goal**: Generate complete slide deck
**Command**: Normal mode, medium length, parallel
**Time**: 30-45 minutes
**Review**: Detailed content, accuracy, completeness

### Third Iteration: Refinement (if needed)
**Goal**: Improve specific aspects
**Options**:
- Change style: `--from-stage plan`
- Regenerate images: `--from-stage generate`
- Adjust length: Change `--length` parameter
**Time**: 15-30 minutes per iteration

---

## 📊 Success Metrics

### Quantitative
- [ ] Slide count matches target (18-20 for medium)
- [ ] All sections covered (7 sections from outline)
- [ ] All figures included (4 experimental PDFs)
- [ ] All tables included (Tables 1 & 2)
- [ ] Processing time reasonable (<1 hour total)

### Qualitative
- [ ] Slides tell coherent story
- [ ] Key contributions clearly communicated
- [ ] Visual design professional and consistent
- [ ] Mathematical notation accurate
- [ ] Suitable for AAAI conference presentation

---

## 🚦 Next Steps

### Immediate (Before Implementation)
1. Read `seekHumanInput.md` completely
2. Answer all REQUIRED questions
3. Obtain necessary API keys
4. Install Paper2Slides if needed

### Short-term (Implementation)
1. Run quick preview (fast mode)
2. Review and provide feedback
3. Run full generation (normal mode)
4. Evaluate output quality

### Long-term (After Implementation)
1. Compare with manual Beamer approach
2. Document lessons learned
3. Refine for actual presentation
4. Practice with generated slides

---

## 💡 Tips for Success

1. **Start Simple**: Use default settings first, customize later
2. **Iterate Quickly**: Fast mode for rapid experimentation
3. **Use Checkpoints**: Leverage resume capability for efficiency
4. **Review Critically**: AI is a starting point, not final product
5. **Compare Approaches**: Try both Paper2Slides and Beamer
6. **Document Process**: Note what works and what doesn't
7. **Seek Feedback**: Show drafts to colleagues early

---

## 📞 Support

### For Paper2Slides Issues
- Check GitHub issues: https://github.com/HKUDS/Paper2Slides/issues
- Review documentation in repository
- Enable `--debug` flag for detailed logs

### For COLDQ Paper Questions
- Refer to paper source: `../paper/aaai25.tex`
- Check preliminary outline: `preliminarySlides_outline.md`
- Review Beamer plan: `../plan/beamerPlan.md`

---

## 📅 Timeline Estimate

| Phase | Task | Duration |
|-------|------|----------|
| **Setup** | Install, configure API | 30 min |
| **Preview** | Fast mode generation | 15 min |
| **Review** | Assess preview | 15 min |
| **Full Gen** | Normal mode generation | 45 min |
| **Review** | Detailed evaluation | 30 min |
| **Refine** | Adjustments (if needed) | 30 min |
| **Total** | | **~3 hours** |

---

## 🎯 Final Notes

This implementation demonstrates:
- **AI-assisted academic work** - Using modern tools effectively
- **Systematic approach** - From planning to execution
- **Quality control** - Critical evaluation of AI output
- **Practical skills** - API integration, prompt engineering, iteration

**Remember**: Paper2Slides is a powerful starting point, but human judgment and refinement are essential for high-quality presentations.

**Good luck with your implementation!** 🚀

---

**Document Status**: Ready for implementation  
**Last Updated**: January 31, 2026  
**Next Action**: Complete `seekHumanInput.md` questionnaire
