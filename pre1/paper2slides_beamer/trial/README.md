# Trial Folder - Paper2Slides & Beamer for COLDQ Paper

**Created**: January 31, 2026  
**Purpose**: Teaching PhD students to use AI agents to convert academic papers into presentation slides  
**Paper**: "Doubly-Bounded Queue for Constrained Online Learning" (AAAI 2025)

---

## 📁 Folder Structure

```
trial/
├── README.md (this file)
├── paper/                      # Paper source files
│   ├── aaai25.tex             # LaTeX source
│   ├── aaai25.bbl             # Bibliography
│   ├── aaai25.sty             # Style file
│   ├── fixed_linear.pdf       # Experimental figure 1
│   ├── fixed_quadratic.pdf    # Experimental figure 2
│   ├── time_varying.pdf       # Experimental figure 3
│   └── job_schedule.pdf       # Experimental figure 4
├── plan/                       # Implementation plans
│   ├── p2splan.md             # Paper2Slides comprehensive guide
│   └── beamerPlan.md          # Beamer LaTeX comprehensive guide
└── implement/                  # Paper2Slides implementation
    ├── README.md              # Implementation guide
    ├── seekHumanInput.md      # Human input requirements
    └── preliminarySlides_outline.md  # Detailed slide outline
```

---

## 🎯 Project Overview

### Objective
Teach PhD students two approaches for converting academic papers to presentation slides:
1. **Paper2Slides**: AI-powered automated slide generation
2. **Beamer**: LaTeX-based manual slide creation

### Target Paper
- **Title**: "Doubly-Bounded Queue for Constrained Online Learning: Keeping Pace with Dynamics of Both Loss and Constraint"
- **Authors**: Juncheng Wang, Bingjie Yan, Yituo Liu
- **Venue**: AAAI 2025
- **Topic**: Online convex optimization with time-varying constraints
- **Key Innovation**: Doubly-bounded virtual queue achieving smooth approach to optimal bounds

---

## 📚 Documentation Overview

### Paper Folder (`paper/`)
Contains the source paper and experimental figures:
- **aaai25.tex**: Full LaTeX source (~1000 lines)
- **aaai25.bbl**: Bibliography entries
- **aaai25.sty**: AAAI 2025 style file
- **4 PDF figures**: Experimental results (fixed constraints, time-varying, job scheduling)

### Plan Folder (`plan/`)
Contains comprehensive guides for both tools:

#### p2splan.md (13,550 characters)
- Paper2Slides tool overview and capabilities
- 4-stage pipeline (RAG, Analysis, Planning, Creation)
- Installation and setup instructions
- Detailed workflow for AAAI25 paper
- Command-line options and examples
- Checkpoint and resume strategies
- Human input requirements
- Troubleshooting guide
- Advantages, limitations, and best practices

#### beamerPlan.md (31,791 characters)
- Beamer LaTeX overview and capabilities
- Basic structure and syntax
- Section-by-section slide plan (23 slides)
- Theme selection and customization
- Compilation workflow
- Detailed content extraction guide
- Common pitfalls and solutions
- Estimated time: 5-8 hours for complete presentation

### Implement Folder (`implement/`)
Contains implementation materials for Paper2Slides:

#### README.md (Implementation Guide)
- Quick start guide
- Expected output structure
- Customization options
- Troubleshooting tips
- Quality checklist
- Success metrics

#### seekHumanInput.md (Critical Decisions)
- API configuration requirements (OpenAI/Google/OpenRouter)
- Presentation context decisions (length, style, audience)
- Content emphasis choices
- Technical detail levels
- Installation checklist
- Processing mode selection
- Timeline estimates

#### preliminarySlides_outline.md (Detailed Blueprint)
- 23-slide structure for 20-minute AAAI talk
- Slide-by-slide content breakdown
- Visual design guidelines
- Timing recommendations
- Content extraction checklist
- Presentation tips

---

## 🚀 Getting Started

### For Paper2Slides Approach

1. **Read the plan**:
   ```bash
   open plan/p2splan.md
   ```

2. **Review implementation requirements**:
   ```bash
   open implement/seekHumanInput.md
   ```

3. **Check the slide outline**:
   ```bash
   open implement/preliminarySlides_outline.md
   ```

4. **Follow implementation guide**:
   ```bash
   open implement/README.md
   ```

### For Beamer Approach

1. **Read the plan**:
   ```bash
   open plan/beamerPlan.md
   ```

2. **Review paper source**:
   ```bash
   open paper/aaai25.tex
   ```

3. **Start creating slides**:
   - Follow section-by-section guide in beamerPlan.md
   - Extract content from aaai25.tex
   - Use slide outline as reference

---

## 📊 Comparison: Paper2Slides vs. Beamer

| Aspect | Paper2Slides | Beamer |
|--------|--------------|--------|
| **Time** | 15-30 minutes | 5-8 hours |
| **Automation** | High (AI-driven) | Low (manual) |
| **Control** | Limited to prompts | Full control |
| **Math Quality** | Good (needs verification) | Perfect |
| **Learning Curve** | Easy | Moderate to steep |
| **Customization** | Theme-based | Unlimited |
| **Best For** | Quick drafts, iteration | Final presentations |
| **Cost** | API fees | Free (time investment) |

### Recommended Hybrid Approach
1. Use **Paper2Slides** to generate initial draft (30 min)
2. Review AI output for content organization and structure
3. Create **Beamer** slides manually, inspired by AI draft (4-6 hours)
4. Refine in Beamer for final presentation (1-2 hours)

**Benefits**: Speed of AI + Precision of LaTeX = Best of both worlds

---

## 🎓 Learning Objectives

### For PhD Students

#### Technical Skills
- AI tool integration and API configuration
- Prompt engineering for slide generation
- LaTeX Beamer programming
- Mathematical notation in presentations
- Version control for presentation materials

#### Academic Skills
- Content distillation from research papers
- Presentation structure and flow
- Visual design for technical content
- Balancing depth and clarity
- Audience adaptation

#### Critical Thinking
- Evaluating AI-generated content
- Recognizing when manual refinement is needed
- Comparing tool trade-offs
- Making informed tool selection decisions

---

## 📋 Implementation Checklist

### Phase 1: Preparation ✅ COMPLETE
- [x] Paper source files organized
- [x] Implementation plans created
- [x] Human input requirements documented
- [x] Preliminary slide outline prepared

### Phase 2: Paper2Slides Implementation ⏳ PENDING
- [ ] API keys obtained
- [ ] Paper2Slides installed
- [ ] Human input decisions made
- [ ] Quick preview generated
- [ ] Full slides generated
- [ ] Quality review completed

### Phase 3: Beamer Implementation ⏳ OPTIONAL
- [ ] Beamer template created
- [ ] Content extracted from paper
- [ ] Slides compiled and tested
- [ ] Visual design refined
- [ ] Final presentation ready

### Phase 4: Comparison & Learning ⏳ FUTURE
- [ ] Compare Paper2Slides vs. Beamer outputs
- [ ] Document lessons learned
- [ ] Identify best practices
- [ ] Create teaching materials

---

## 🎯 Success Criteria

### For Paper2Slides
- [ ] Slides generated successfully
- [ ] 18-20 slides for 20-minute talk
- [ ] All key contributions included
- [ ] Mathematical notation accurate
- [ ] Figures properly extracted
- [ ] Professional visual design
- [ ] Suitable for AAAI presentation

### For Beamer
- [ ] Slides compile without errors
- [ ] Perfect mathematical notation
- [ ] Consistent formatting
- [ ] Reusable template created
- [ ] Version controlled
- [ ] Presentation-ready quality

### For Learning
- [ ] Students understand both approaches
- [ ] Can make informed tool choices
- [ ] Recognize AI limitations
- [ ] Develop critical evaluation skills
- [ ] Apply to their own papers

---

## 📖 Key Concepts

### Paper2Slides Concepts
- **RAG (Retrieval-Augmented Generation)**: AI technique for document analysis
- **Checkpoint System**: Save progress at each stage for resume/modification
- **Fast vs. Normal Mode**: Trade-off between speed and accuracy
- **Style Prompting**: Natural language descriptions for visual design
- **Parallel Processing**: Generate multiple slides simultaneously

### Beamer Concepts
- **Frame**: Basic unit (can produce multiple slides with overlays)
- **Theme**: Visual design template
- **Overlay**: Progressive reveal of content
- **Block**: Highlighted content box
- **Projection**: Compiling LaTeX to PDF slides

---

## 🔧 Tools & Resources

### Required Software
- **For Paper2Slides**:
  - Python 3.12
  - Conda environment manager
  - Git
  - API access (OpenAI/Google/OpenRouter)

- **For Beamer**:
  - LaTeX distribution (TeX Live, MiKTeX, MacTeX)
  - LaTeX editor (Overleaf, TeXShop, VS Code)
  - PDF viewer

### Helpful Resources
- **Paper2Slides GitHub**: https://github.com/HKUDS/Paper2Slides
- **Beamer Documentation**: https://ctan.org/pkg/beamer
- **Overleaf Beamer Tutorial**: https://www.overleaf.com/learn/latex/Beamer
- **LaTeX Beamer Quick Start**: https://latex-beamer.com/quick-start/

---

## 💡 Best Practices

### For Paper2Slides
1. **Start with fast mode** for quick preview
2. **Use academic style** for technical papers
3. **Enable parallel processing** for speed
4. **Leverage checkpoints** for iteration
5. **Verify mathematical notation** manually
6. **Review critically** - AI is starting point, not final product

### For Beamer
1. **Start with simple template** and add complexity gradually
2. **Compile frequently** to catch errors early
3. **Reuse content** from paper source (don't retype)
4. **Use consistent notation** with paper
5. **Test overlays** to ensure smooth flow
6. **Practice presentation** with slides before finalizing

### For Both
1. **Know your audience** - adjust technical depth accordingly
2. **One message per slide** - avoid crowding
3. **Use visuals effectively** - figures, diagrams, tables
4. **Balance text and whitespace** - readability is key
5. **Practice timing** - ensure slides fit time limit
6. **Seek feedback early** - iterate based on input

---

## 🚨 Common Pitfalls

### Paper2Slides
- ❌ **Not verifying math**: AI can make notation errors
- ❌ **Skipping preview**: Jumping to full generation without testing
- ❌ **Ignoring checkpoints**: Not leveraging resume capability
- ❌ **Poor prompts**: Vague style descriptions yield poor results
- ❌ **No manual polish**: Using AI output as-is without refinement

### Beamer
- ❌ **Too much text**: Cramming paragraphs onto slides
- ❌ **Inconsistent notation**: Different from paper
- ❌ **Complex overlays**: Confusing progressive reveals
- ❌ **Compilation errors**: Not testing frequently enough
- ❌ **Time underestimation**: Expecting quick results

---

## 📅 Timeline Estimates

### Paper2Slides Approach
| Phase | Duration |
|-------|----------|
| Setup & API config | 30 min |
| Quick preview | 15 min |
| Review preview | 15 min |
| Full generation | 45 min |
| Review & refine | 30 min |
| Manual polish | 1 hour |
| **Total** | **~3.5 hours** |

### Beamer Approach
| Phase | Duration |
|-------|----------|
| Template setup | 30 min |
| Content extraction | 2-3 hours |
| Slide compilation | 1 hour |
| Visual refinement | 1-2 hours |
| Practice & iterate | 1-2 hours |
| **Total** | **~6-9 hours** |

---

## 🎓 Teaching Notes

### For Instructors

**Session 1: Introduction (1 hour)**
- Overview of both approaches
- Demo Paper2Slides quick preview
- Show Beamer example
- Discuss trade-offs

**Session 2: Paper2Slides Workshop (2 hours)**
- Hands-on API setup
- Generate slides for sample paper
- Review and critique output
- Discuss AI limitations

**Session 3: Beamer Workshop (3 hours)**
- LaTeX basics review
- Create simple Beamer template
- Extract content from paper
- Compile and test

**Session 4: Comparison & Best Practices (1 hour)**
- Compare outputs from both approaches
- Discuss when to use each
- Share best practices
- Q&A and troubleshooting

### Assessment Ideas
- Generate slides for their own paper
- Compare Paper2Slides vs. manual approach
- Present using generated slides
- Write reflection on tool selection

---

## 📞 Support & Questions

### For Technical Issues
- **Paper2Slides**: Check GitHub issues or enable `--debug`
- **Beamer**: Consult TeX Stack Exchange or official docs
- **API**: Review provider documentation

### For Content Questions
- Refer to paper source: `paper/aaai25.tex`
- Check slide outline: `implement/preliminarySlides_outline.md`
- Review plans: `plan/p2splan.md` or `plan/beamerPlan.md`

---

## 🎯 Next Steps

### Immediate
1. Choose approach (Paper2Slides, Beamer, or both)
2. Read relevant plan document
3. Complete setup requirements
4. Begin implementation

### Short-term
1. Generate/create initial slides
2. Review and iterate
3. Practice presentation
4. Gather feedback

### Long-term
1. Apply to own research papers
2. Develop personal workflow
3. Share experiences with peers
4. Contribute improvements to tools

---

## 📊 Project Status

- **Phase**: Implementation ready
- **Paper**: Organized in `paper/` folder
- **Plans**: Complete in `plan/` folder
- **Implementation**: Ready in `implement/` folder
- **Next Action**: Complete `implement/seekHumanInput.md` and begin generation

---

## 🏆 Expected Outcomes

By completing this trial, students will:
1. ✅ Understand AI-powered slide generation
2. ✅ Learn LaTeX Beamer for presentations
3. ✅ Develop critical evaluation skills
4. ✅ Make informed tool selection decisions
5. ✅ Create high-quality academic presentations
6. ✅ Apply techniques to their own research

---

**Ready to begin? Start with `implement/README.md` for Paper2Slides or `plan/beamerPlan.md` for Beamer!**

---

**Document Created**: January 31, 2026  
**Last Updated**: January 31, 2026  
**Status**: Ready for implementation  
**Contact**: See course materials for instructor information
