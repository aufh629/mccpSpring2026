# MCP Automation for Task 3.2: Writing Gap Analysis and Learning Plan

## Current Workflow (Manual Process)

### Step 1: Student Provides Writing Sample
**Student creates `writingSample.md`:**
- Pastes their writing (Introduction/Literature Review)
- Includes supervisor comments if available
- Manually reflects on strengths/weaknesses

**Problems:**
- No structured analysis
- Gap identification is subjective
- No systematic comparison with assessment criteria

### Step 2: Manual Gap Identification
**Student manually:**
- Compares writing with assessment rubrics
- Tries to identify gaps
- May or may not be systematic

**Problems:**
- Inconsistent gap identification
- May miss important gaps
- No structured diagnostic report

### Step 3: Model Paper Analysis Planning
**Student manually:**
- Decides what to analyze in model papers
- Creates analysis plan
- May not focus on specific gaps

**Problems:**
- Analysis may not target specific gaps
- No clear connection between gaps and analysis plan
- No recommendations on what features to analyze

## How MCP Can Automate This Process

### MCP Tools for Task 3.2

#### 1. **Writing Analysis Tools** (`writing_analysis_tools.py`)

**Tool: `parse_writing_sample`**
- **Input**: Path to `writingSample.md`
- **Output**: Structured JSON with:
  ```json
  {
    "source_info": {...},
    "supervisor_comments": [...],
    "writing_sections": {
      "introduction": {...},
      "literature_review": {...}
    },
    "self_reflection": {...}
  }
  ```
- **Automates**: Parsing writing sample, extracting sections, comments
- **Benefit**: Standardized structure for analysis

**Tool: `identify_rhetorical_moves`**
- **Input**: Writing sample content
- **Output**: JSON with identified moves:
  ```json
  {
    "introduction": {
      "move1_establishing_territory": {...},
      "move2_identifying_niche": {...},
      "move3_occupying_niche": {...}
    },
    "literature_review": {
      "move1_thematic_overview": {...},
      "move2_critical_analysis": {...},
      "move3_research_gaps": {...},
      "move4_conclusion": {...}
    }
  }
  ```
- **Automates**: Move identification using course materials
- **Benefit**: Systematic move analysis

**Tool: `extract_linguistic_features`**
- **Input**: Writing sample content
- **Output**: JSON with linguistic features:
  ```json
  {
    "centrality_statements": [...],
    "gap_signaling": [...],
    "reporting_verbs": [...],
    "evaluative_language": [...],
    "citation_patterns": [...]
  }
  ```
- **Automates**: Feature extraction for comparison
- **Benefit**: Objective feature identification

#### 2. **Gap Analysis Tools** (`gap_analysis_tools.py`)

**Tool: `compare_with_assessment_rubrics`**
- **Input**: Parsed writing sample, assessment rubrics
- **Output**: Gap analysis JSON:
  ```json
  {
    "task_achievement": {
      "research_background": {
        "current_level": "Satisfactory",
        "target_level": "Excellent",
        "gap_description": "...",
        "specific_issues": [...]
      },
      "gap_identification": {...},
      "literature_synthesis": {...},
      "citations": {...}
    },
    "organisation": {...},
    "language": {...}
  }
  ```
- **Automates**: Systematic comparison with rubrics
- **Benefit**: Objective gap identification

**Tool: `analyze_supervisor_comments`**
- **Input**: Supervisor comments from writing sample
- **Output**: Structured feedback analysis:
  ```json
  {
    "issues_identified": [
      {
        "category": "Task Achievement",
        "aspect": "Gap identification",
        "comment": "...",
        "severity": "high"
      }
    ],
    "suggestions": [...]
  }
  ```
- **Automates**: Comment categorization and analysis
- **Benefit**: Systematic feedback processing

**Tool: `generate_gap_diagnostic_report`**
- **Input**: Gap analysis results
- **Output**: HTML diagnostic report:
  - Summary of gaps
  - Specific issues identified
  - Comparison with assessment criteria
  - Priority areas for improvement
- **Automates**: Report generation
- **Benefit**: Professional diagnostic output

#### 3. **Model Paper Analysis Planning Tools** (`model_paper_tools.py`)

**Tool: `create_analysis_plan_from_gaps`**
- **Input**: Gap diagnostic report
- **Output**: Analysis plan JSON:
  ```json
  {
    "focus_areas": [
      {
        "gap_area": "Research background clarity",
        "priority": "high",
        "what_to_analyze": [
          "How model papers establish centrality",
          "Linguistic features in opening statements",
          "Citation density and integration"
        ],
        "questions_to_answer": [
          "How do excellent papers begin introductions?",
          "What evaluative language do they use?",
          "How do they balance general and specific?"
        ]
      }
    ],
    "recommended_model_papers": {
      "criteria": "Papers that excel in gap areas",
      "suggestions": [...]
    }
  }
  ```
- **Automates**: Plan generation based on gaps
- **Benefit**: Targeted analysis plan

**Tool: `recommend_textual_mentor_features`**
- **Input**: Gap analysis, course materials
- **Output**: Recommendations JSON:
  ```json
  {
    "features_to_analyze": [
      {
        "feature": "Centrality statements",
        "why": "Your writing lacks clear centrality statements",
        "how_to_analyze": [
          "Extract opening sentences from model papers",
          "Identify evaluative language patterns",
          "Note citation integration strategies"
        ],
        "practice_suggestions": [
          "Imitate 3-5 centrality statements from model papers",
          "Rewrite your opening using similar patterns"
        ]
      }
    ],
    "imitation_exercises": [
      {
        "exercise": "Rewrite gap identification paragraph",
        "model_reference": "Use Paper X, paragraph Y as template",
        "ai_assistance": "Use AI to generate variations"
      }
    ]
  }
  ```
- **Automates**: Feature recommendations and practice suggestions
- **Benefit**: Actionable learning plan

#### 4. **AI-Assisted Practice Tools** (`practice_tools.py`)

**Tool: `generate_imitation_exercises`**
- **Input**: Model paper excerpts, gap areas
- **Output**: Practice exercises:
  ```json
  {
    "exercises": [
      {
        "type": "imitation",
        "model_excerpt": "...",
        "task": "Rewrite your gap paragraph using this pattern",
        "ai_prompt": "Help student rewrite paragraph following model pattern"
      }
    ]
  }
  ```
- **Automates**: Exercise generation
- **Benefit**: Structured practice opportunities

**Tool: `compare_with_model_patterns`**
- **Input**: Student's revised writing, model paper patterns
- **Output**: Comparison showing:
  - Similarities with model patterns
  - Remaining differences
  - Further improvement suggestions
- **Automates**: Pattern comparison
- **Benefit**: Objective progress tracking

#### 5. **Workflow Management Tools** (`workflow_tools.py`)

**Tool: `create_gap_analysis_task`**
- **Input**: Path to `writingSample.md`, assessment rubrics path
- **Output**: Complete gap diagnostic report + analysis plan
- **Automates**: Full gap analysis workflow
- **Benefit**: One-step gap analysis

**Tool: `generate_learning_plan`**
- **Input**: Gap diagnostic report
- **Output**: Complete learning plan with:
  - Gap summary
  - Model paper analysis plan
  - Feature recommendations
  - Practice exercises
  - AI assistance prompts
- **Automates**: Complete learning plan generation
- **Benefit**: Comprehensive action plan

## Automated Workflow with MCP

### Scenario 1: Gap Analysis (Automated)

**Student**: "Analyze my writing sample and identify gaps"

**AI Agent Workflow** (using MCP tools):
1. Calls `parse_writing_sample("writingSample.md")` → gets structured writing
2. Calls `identify_rhetorical_moves(writing_content)` → identifies moves
3. Calls `extract_linguistic_features(writing_content)` → extracts features
4. Calls `compare_with_assessment_rubrics(parsed_writing, rubrics)` → identifies gaps
5. Calls `analyze_supervisor_comments(comments)` → processes feedback
6. Calls `generate_gap_diagnostic_report(gap_analysis)` → creates diagnostic.html
7. Returns: "Gap diagnostic report generated: diagnostic.html"

**Time**: ~15 seconds (vs. hours of manual analysis)

### Scenario 2: Learning Plan Generation (Automated)

**Student**: "Create a plan for learning from model papers based on my gaps"

**AI Agent Workflow** (using MCP tools):
1. Calls `create_analysis_plan_from_gaps(diagnostic_report)` → creates analysis plan
2. Calls `recommend_textual_mentor_features(gap_analysis, course_materials)` → gets recommendations
3. Calls `generate_imitation_exercises(model_papers, gap_areas)` → creates exercises
4. Calls `generate_learning_plan(all_components)` → creates learning_plan.html
5. Returns: "Learning plan generated: learning_plan.html"

**Time**: ~10 seconds (vs. hours of planning)

### Scenario 3: Complete Automated Workflow

**Student**: "Do task 3.2 for my writing sample"

**AI Agent Workflow** (using MCP tools):
1. Calls `create_gap_analysis_task("writingSample.md", "writing_instructions_formatted.md")`
   - Parses writing sample
   - Identifies gaps
   - Generates diagnostic report
2. Calls `generate_learning_plan(diagnostic_report)`
   - Creates analysis plan
   - Recommends features to analyze
   - Generates practice exercises
3. Returns: 
   - `diagnostic_report.html` - Gap analysis
   - `learning_plan.html` - How to learn from model papers
   - `analysis_plan.md` - What to analyze in model papers

**Time**: ~25 seconds total (vs. days of manual work)

## Key Differences MCP Makes

### 1. **Automation vs. Manual Analysis**

| Aspect | Without MCP | With MCP |
|--------|-------------|----------|
| Gap Identification | Manual comparison, subjective | Automatic, systematic, objective |
| Diagnostic Report | Student creates manually | Auto-generated HTML report |
| Analysis Planning | Student decides what to analyze | Plan generated from gaps |
| Feature Recommendations | Student guesses what to focus on | AI recommends based on gaps |
| Practice Exercises | Student creates own exercises | Auto-generated with AI prompts |

### 2. **Systematic vs. Ad-hoc**

**Without MCP:**
- Gap identification may miss important areas
- No systematic comparison with rubrics
- Analysis plan may not target specific gaps
- Practice may not address identified issues

**With MCP:**
- Systematic gap identification using rubrics
- Structured diagnostic report
- Targeted analysis plan based on gaps
- Practice exercises directly address gaps

### 3. **Efficiency & Accuracy**

**Without MCP:**
- Gap analysis: 2-4 hours (manual comparison)
- Analysis planning: 1-2 hours
- **Total: 3-6 hours**

**With MCP:**
- Gap analysis: ~15 seconds
- Learning plan: ~10 seconds
- **Total: ~25 seconds**

### 4. **Personalization**

**Without MCP:**
- Generic gap identification
- One-size-fits-all analysis plan
- Generic practice suggestions

**With MCP:**
- Personalized gap analysis based on student's writing
- Customized analysis plan targeting specific gaps
- Tailored practice exercises for identified issues
- AI assistance prompts specific to student's needs

### 5. **Integration with AI Assistance**

**Without MCP:**
- Student must manually create AI prompts
- No structured way to use AI for practice
- Inconsistent AI assistance

**With MCP:**
- Auto-generated AI prompts for each exercise
- Structured imitation exercises with AI support
- Consistent AI assistance workflow
- Progress tracking through pattern comparison

## MCP Tool Architecture for Task 3.2

```
mcp-writing-gap-analyzer/
├── tools/
│   ├── writing_analysis_tools.py    # parse_writing_sample, identify_moves, extract_features
│   ├── gap_analysis_tools.py        # compare_with_rubrics, analyze_comments, generate_diagnostic
│   ├── model_paper_tools.py         # create_analysis_plan, recommend_features
│   ├── practice_tools.py            # generate_exercises, compare_patterns
│   └── workflow_tools.py            # create_gap_analysis_task, generate_learning_plan
├── templates/
│   ├── diagnostic_report.html       # Gap diagnostic report template
│   ├── learning_plan.html          # Learning plan template
│   └── analysis_plan.md            # Analysis plan template
├── resources/
│   ├── assessment_rubrics.json      # Structured rubrics data
│   ├── rhetorical_moves.json       # Move definitions and patterns
│   └── linguistic_features.json    # Feature definitions
└── parsers/
    └── writing_parser.py            # Writing sample parser
```

## Example: Complete MCP-Enabled Workflow

### Student Request
```
"Analyze my writing sample (writingSample.md) and create a learning plan 
for improving through model paper analysis"
```

### AI Agent Execution (Automatic)
```python
# Step 1: Parse writing sample
writing_sample = parse_writing_sample("writingSample.md")
moves = identify_rhetorical_moves(writing_sample)
features = extract_linguistic_features(writing_sample)

# Step 2: Identify gaps
rubrics = load_assessment_rubrics("writing_instructions_formatted.md")
gap_analysis = compare_with_assessment_rubrics(writing_sample, rubrics)
comment_analysis = analyze_supervisor_comments(writing_sample.comments)

# Step 3: Generate diagnostic report
diagnostic_report = generate_gap_diagnostic_report(
    gap_analysis, comment_analysis
)
# Returns: "diagnostic_report.html created"

# Step 4: Create analysis plan
analysis_plan = create_analysis_plan_from_gaps(gap_analysis)
features_to_analyze = recommend_textual_mentor_features(
    gap_analysis, course_materials
)

# Step 5: Generate practice exercises
exercises = generate_imitation_exercises(
    model_papers, gap_analysis.focus_areas
)

# Step 6: Generate learning plan
learning_plan = generate_learning_plan(
    diagnostic_report, analysis_plan, features_to_analyze, exercises
)
# Returns: "learning_plan.html created"
```

### Result
- ✅ `diagnostic_report.html` - Complete gap analysis
- ✅ `analysis_plan.md` - What to analyze in model papers
- ✅ `learning_plan.html` - How to learn from textual mentors
- ✅ Practice exercises with AI prompts
- ✅ Feature recommendations
- ✅ **Time: ~25 seconds total**

## File Structure for Task 3.2

### Input Files
1. **`writingSample.md`** - Student's writing sample with supervisor comments
2. **`writing_instructions_formatted.md`** - Assessment requirements and rubrics
3. **Course materials** - Session 1 & 2 handouts (for move definitions)

### Output Files (Generated by MCP)
1. **`diagnostic_report.html`** - Gap analysis report
2. **`analysis_plan.md`** - Plan for analyzing model papers
3. **`learning_plan.html`** - Complete learning plan with:
   - Gap summary
   - Features to analyze from model papers
   - Practice exercises
   - AI assistance prompts
4. **`task_achievement_analysis.html`** - Final analysis (after model paper analysis)

## Benefits Summary

| Benefit | Impact |
|---------|--------|
| **Time Savings** | 3-6 hours → 25 seconds (400-800x faster) |
| **Systematic Analysis** | Objective gap identification using rubrics |
| **Personalization** | Tailored to each student's writing |
| **Targeted Learning** | Analysis plan focuses on specific gaps |
| **AI Integration** | Structured AI assistance for practice |
| **Progress Tracking** | Compare revisions with model patterns |
| **Consistency** | Standardized diagnostic reports |

## Workflow Comparison

### Without MCP (Manual)
```
1. Student writes writingSample.md (30 min)
2. Student manually compares with rubrics (2-4 hours)
3. Student identifies gaps subjectively (1 hour)
4. Student creates analysis plan (1-2 hours)
5. Student decides what to analyze (30 min)
6. Student creates practice exercises (1 hour)
Total: 6-9 hours
```

### With MCP (Automated)
```
1. Student writes writingSample.md (30 min)
2. AI agent: create_gap_analysis_task() (15 sec)
   → diagnostic_report.html generated
3. AI agent: generate_learning_plan() (10 sec)
   → learning_plan.html generated
Total: 30 minutes + 25 seconds
```

## Conclusion

MCP transforms Task 3.2 from a **manual, time-consuming, subjective process** into a **one-command, automated, systematic workflow**. Students can:

1. **Focus on writing improvement** rather than gap identification
2. **Get objective diagnostic reports** based on assessment criteria
3. **Receive personalized learning plans** targeting their specific gaps
4. **Practice with AI assistance** through structured exercises
5. **Track progress** by comparing revisions with model patterns

The AI agent becomes a **writing diagnostician and learning coach** rather than just a text analyzer, providing systematic, personalized support for writing improvement.

---

**Key Insight**: MCP enables **systematic gap analysis → targeted learning plan → AI-assisted practice**, creating a complete learning cycle for writing improvement.
