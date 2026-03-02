# Plan 03: Task 3.2 - Gap Analysis and Learning from Textual Mentors (with AI Agent)

## Purpose

**The key motivation:** This task helps you **improve your writing skills** by:
1. **Identifying specific gaps** between your current writing and excellent writing
2. **Creating a diagnostic report** on these gaps
3. **Developing a learning plan** to learn from model papers (textual mentors)
4. **Practicing through imitation** with AI assistance

---

## Part 1: Understanding the Writing Task

### What You Need to Write

**File to read:** `writing_instructions_formatted.md`

**Key requirements:**
- Write 1000-1500 words (Introduction + Literature Review)
- Follow rhetorical moves (CARS model for Introduction, 4 moves for Literature Review)
- Meet "Excellent" Task Achievement criteria:
  - Extremely clear research background, focus, and objectives
  - Skilful synthesis and critical evaluation of literature
  - Clearly delineated research gap
  - Succinctly highlighted significance
  - Adequate and effective citations

**Action:** Read `writing_instructions_formatted.md` to understand what "Excellent" writing means.

---

## Part 2: Providing Your Writing Sample

### Your Input: One Paper (Your Writing)

**Create:** `writingSample.md`

**What to include:**
- Your recent writing (Introduction and/or Literature Review)
- **Supervisor comments/feedback** (if available - this is very helpful!)
- Self-reflection on strengths and weaknesses

**Why this matters:**
- This is your **baseline** - where you are as a writer
- Supervisor comments help identify issues you might not see
- This becomes the input for gap analysis

**Use the template:** `writingSample_template.md`

---

## Part 3: Gap Analysis (with AI Agent)

### What Happens

**You provide:** `writingSample.md`

**AI Agent does:**
1. Parses your writing sample
2. Identifies rhetorical moves in your writing
3. Extracts linguistic features
4. Compares with assessment rubrics
5. Analyzes supervisor comments (if provided)
6. **Generates diagnostic report**

**Output:** `diagnostic_report.html`

**What the diagnostic report contains:**
- Summary of gaps identified
- Specific issues in each area (Task Achievement, Organisation, Language)
- Comparison with "Excellent" criteria
- Priority areas for improvement
- Issues from supervisor comments

**Example gap identified:**
> **Gap in Research Background:**
> - Your writing: "Many studies have looked at this topic." (vague, no citations)
> - Excellent writing: "Recent research has demonstrated the critical importance of X (Author1, 2023; Author2, 2024), with particular emphasis on Y (Author3, 2024)." (specific, cited, evaluative)
> - **Priority: High** - This affects Task Achievement

---

## Part 4: Learning Plan from Textual Mentors

### What You Get

**AI Agent generates:** `learning_plan.html`

**This includes:**

1. **Analysis Plan** - What to analyze in model papers:
   - Focus areas based on your gaps
   - Specific questions to answer
   - Features to extract from model papers

2. **Feature Recommendations** - What to learn from model papers:
   - **Why:** "Your writing lacks clear centrality statements"
   - **What to analyze:** "Extract opening sentences from model papers, identify evaluative language patterns"
   - **How to practice:** "Imitate 3-5 centrality statements, rewrite your opening using similar patterns"

3. **Practice Exercises** - Imitation with AI assistance:
   - Rewrite exercises based on model paper patterns
   - AI prompts to help you practice
   - Comparison exercises to track progress

**Example recommendation:**
> **Feature: Gap Identification**
> - **Why focus on this:** Your gap statements are vague (identified in diagnostic report)
> - **What to analyze in model papers:**
>   - How they transition from Move 1 to Move 2
>   - Linguistic markers they use ("However", "Despite X, Y remains unclear")
>   - How they enumerate specific limitations
> - **Practice exercise:**
>   - Find 3 gap identification paragraphs in model papers
>   - Use AI: "Help me rewrite my gap paragraph following this pattern: [model excerpt]"
>   - Compare your revision with the model

---

## Part 5: The Complete Workflow

### Step-by-Step Process

```
Step 1: Understand the Task
        ↓
        Read writing_instructions_formatted.md
        Understand what "Excellent" means
        ↓
Step 2: Provide Your Writing Sample
        ↓
        Create writingSample.md
        Include supervisor comments if available
        ↓
Step 3: Gap Analysis (AI Agent)
        ↓
        AI Agent: create_gap_analysis_task(writingSample.md)
        → Generates diagnostic_report.html
        ↓
Step 4: Learning Plan (AI Agent)
        ↓
        AI Agent: generate_learning_plan(diagnostic_report)
        → Generates learning_plan.html
        → Generates analysis_plan.md
        ↓
Step 5: Analyze Model Papers
        ↓
        Follow analysis_plan.md
        Focus on features recommended in learning_plan.html
        ↓
Step 6: Practice with AI Assistance
        ↓
        Complete imitation exercises from learning_plan.html
        Use AI prompts provided
        Compare your revisions with model patterns
        ↓
Step 7: Create Final Analysis
        ↓
        Create task_achievement_analysis.html
        Document: gaps → model paper strategies → your improvements
        ↓
Step 8: Submit
        ↓
        Post in Moodle: file path + reflection
```

---

## What You Get from AI Agent

### 1. Diagnostic Report (`diagnostic_report.html`)

**Contains:**
- ✅ Systematic gap identification
- ✅ Comparison with assessment rubrics
- ✅ Analysis of supervisor comments
- ✅ Priority areas for improvement
- ✅ Specific issues to address

**Time saved:** Instead of 2-4 hours of manual comparison, AI does it in ~15 seconds

### 2. Learning Plan (`learning_plan.html`)

**Contains:**
- ✅ Analysis plan targeting your specific gaps
- ✅ Feature recommendations (what to learn from model papers)
- ✅ Practice exercises with AI prompts
- ✅ Imitation exercises based on model patterns

**Time saved:** Instead of 1-2 hours of planning, AI generates it in ~10 seconds

### 3. Analysis Plan (`analysis_plan.md`)

**Contains:**
- ✅ What to analyze in model papers (based on your gaps)
- ✅ Specific questions to answer
- ✅ Features to extract
- ✅ Focus areas prioritized

---

## Key Features of This Approach

### 1. **Focus on Gap Identification First**
- Don't start analyzing papers randomly
- First identify your specific gaps
- Then analyze model papers to address those gaps

### 2. **Systematic Gap Analysis**
- Uses assessment rubrics objectively
- Analyzes supervisor comments systematically
- Identifies gaps you might miss

### 3. **Targeted Learning**
- Analysis plan focuses on your specific gaps
- Feature recommendations address your issues
- Practice exercises target your weaknesses

### 4. **AI-Assisted Practice**
- Structured imitation exercises
- AI prompts to help you practice
- Progress tracking through pattern comparison

### 5. **Personalized to Your Writing**
- Based on your actual writing sample
- Considers your supervisor's feedback
- Targets your specific improvement areas

---

## Files You'll Work With

### Input Files (You Create)
1. **`writingSample.md`** - Your writing sample with supervisor comments

### Output Files (AI Agent Generates)
1. **`diagnostic_report.html`** - Gap analysis report
2. **`learning_plan.html`** - How to learn from model papers
3. **`analysis_plan.md`** - What to analyze in model papers

### Files You Create (After Analysis)
4. **`task_achievement_analysis.html`** - Your final analysis showing:
   - Gaps identified
   - How model papers address them
   - Strategies you'll apply
   - Your improvements through practice

---

## How to Use AI Agent

### Simple Commands

**For gap analysis:**
```
"Analyze my writing sample (writingSample.md) and identify gaps"
```

**For learning plan:**
```
"Create a learning plan based on my diagnostic report"
```

**For complete workflow:**
```
"Do task 3.2 for my writing sample"
```

The AI agent will:
1. Parse your writing sample
2. Compare with assessment rubrics
3. Generate diagnostic report
4. Create learning plan
5. Recommend features to analyze
6. Generate practice exercises

**Time:** ~25 seconds for complete analysis and planning

---

## Success Criteria

You have successfully completed this task when you can:

1. ✅ **Provide a writing sample** that shows where you are as a writer
2. ✅ **Get a diagnostic report** identifying specific gaps
3. ✅ **Receive a learning plan** with targeted recommendations
4. ✅ **Follow the analysis plan** to analyze model papers
5. ✅ **Practice through imitation** using AI assistance
6. ✅ **Document your learning** in task_achievement_analysis.html
7. ✅ **Show improvement** by comparing revisions with model patterns

---

## Tips for Success

- **Be honest in your writing sample**: The more accurate your baseline, the better the gap analysis
- **Include supervisor comments**: They help identify issues you might not see
- **Follow the learning plan**: It's personalized to your gaps
- **Practice with AI**: Use the provided AI prompts for imitation exercises
- **Track your progress**: Compare your revisions with model patterns
- **Focus on 2-3 key gaps**: Don't try to address everything at once

---

## Next Steps

1. **Read** `writing_instructions_formatted.md` to understand the assignment
2. **Create** `writingSample.md` with your writing and supervisor comments
3. **Use AI Agent** to generate diagnostic report and learning plan
4. **Follow** the analysis plan to analyze model papers
5. **Practice** through imitation exercises with AI assistance
6. **Create** `task_achievement_analysis.html` documenting your learning
7. **Submit** in Moodle with file path and reflection

**Remember:** The goal is to improve your writing. The AI agent helps you identify gaps systematically and learn from model papers effectively, but you still need to practice and apply what you learn.

---

## Why This Approach Works

1. **Systematic**: Uses assessment rubrics objectively
2. **Personalized**: Based on your actual writing
3. **Targeted**: Focuses on your specific gaps
4. **Actionable**: Provides concrete practice exercises
5. **Efficient**: Saves hours of manual analysis
6. **Effective**: Helps you learn from textual mentors systematically

**The key insight:** Don't analyze papers randomly. First identify your gaps, then learn from model papers to fill those specific gaps.
