# MCP Automation for Task 3.1: Paper Structure Visualization

## Current Workflow (Manual Process)

### Step 1: Initial Visualization Request
**Student sends `visualizeMacro.md` to AI agent:**
```
PhDagentSpring2026/literature/KPY*/25480332_Adaptive Parameter Selection for Kernel Ridge Regression.tar.gz

please unzip and read the paper
take all the headings and sub-headings
and generate a visual.html that can be shared via Moodle Forum
```

**What happens:**
- Student manually provides file path
- AI agent must handle: unzipping, parsing LaTeX/PDF, extracting structure
- AI agent generates HTML from scratch
- Output: `visual.html` (hierarchical structure)

### Step 2: Feedback and Refinement
**Student sends `commentonVisual.md` to AI agent:**
```
PhDagentSpring2026/moodle/task3.1/visual.html

this version looks promising but I expect sth that shows the interrelationship 
among different modules of the paper not just a linear and hierarchical presentation

we need to see how different parts are interconnected; I also want to see some texts 
from each modules and explore links among these texts

please generate visual_interconnection_text.html
```

**What happens:**
- Student provides feedback on previous output
- AI agent must re-parse paper to understand interconnections
- AI agent generates new HTML with network visualization
- Output: `visual_interconnection_text.html` (interconnected structure with text excerpts)

## Problems with Current Manual Approach

1. **Repetitive Instructions**: Student must manually specify file paths and operations
2. **Inconsistent Parsing**: AI agent may parse differently each time
3. **No State Management**: AI agent doesn't remember previous parsing results
4. **Manual File Operations**: Unzipping, file reading handled ad-hoc
5. **Feedback Loop Inefficiency**: Must re-process entire paper for refinements
6. **No Standardization**: Each student/AI interaction may produce different formats

## How MCP Can Automate This Process

### MCP Tools for Task 3.1

#### 1. **File Operation Tools** (`file_tools.py`)

**Tool: `extract_archive`**
- **Input**: Path to tar.gz/zip file
- **Output**: Extracted file paths and structure
- **Automates**: Unzipping, file discovery
- **Benefit**: No manual unzip instructions needed

**Tool: `read_paper_file`**
- **Input**: Path to paper file (LaTeX/PDF)
- **Output**: Structured paper content
- **Automates**: File reading, format detection
- **Benefit**: Consistent file handling

#### 2. **Paper Structure Tools** (`paper_tools.py`)

**Tool: `parse_paper_structure`**
- **Input**: Paper file path or content
- **Output**: JSON with hierarchical structure:
  ```json
  {
    "title": "...",
    "sections": [
      {
        "level": 1,
        "heading": "Introduction",
        "subsections": [...],
        "text_excerpt": "...",
        "citations": [...]
      }
    ]
  }
  ```
- **Automates**: Structure extraction, heading hierarchy
- **Benefit**: Standardized parsing, reusable results

**Tool: `analyze_section_interconnections`**
- **Input**: Parsed paper structure
- **Output**: JSON with relationships:
  ```json
  {
    "sections": [...],
    "connections": [
      {
        "from": "Introduction",
        "to": "Methods",
        "type": "references",
        "evidence": "text excerpt..."
      }
    ]
  }
  ```
- **Automates**: Relationship detection (citations, references, logical flow)
- **Benefit**: Enables network visualization

#### 3. **Visualization Generation Tools** (`visualization_tools.py`)

**Tool: `generate_hierarchical_html`**
- **Input**: Parsed paper structure
- **Output**: HTML file path
- **Template**: Pre-built Moodle-compatible HTML template
- **Automates**: HTML generation with consistent styling
- **Benefit**: Standardized output format

**Tool: `generate_network_html`**
- **Input**: Parsed structure + interconnections
- **Output**: HTML file path with interactive network
- **Template**: Pre-built network visualization template (D3.js/Cytoscape)
- **Automates**: Network diagram generation
- **Benefit**: Professional visualization without manual coding

**Tool: `generate_interconnected_html`**
- **Input**: Parsed structure + interconnections + text excerpts
- **Output**: HTML with network + detail panel
- **Features**: 
  - Interactive network diagram
  - Clickable nodes showing text excerpts
  - Link exploration between sections
- **Automates**: Complete interactive visualization
- **Benefit**: Meets all requirements in one step

#### 4. **Workflow Management Tools** (`workflow_tools.py`)

**Tool: `create_visualization_task`**
- **Input**: Paper file path, visualization type
- **Output**: Task ID, initial visualization
- **Automates**: Complete workflow from paper to visualization
- **Benefit**: One-step process instead of multi-step instructions

**Tool: `refine_visualization`**
- **Input**: Previous visualization file, feedback text
- **Output**: Refined visualization
- **Automates**: Iterative improvement based on feedback
- **Benefit**: Efficient refinement without re-parsing

## Automated Workflow with MCP

### Scenario 1: Initial Visualization (Automated)

**Student**: "Generate visualization for the KPY paper"

**AI Agent Workflow** (using MCP tools):
1. Calls `extract_archive("PhDagentSpring2026/literature/KPY*/...tar.gz")`
2. Calls `read_paper_file(extracted_path)` → detects LaTeX format
3. Calls `parse_paper_structure(paper_content)` → gets structure
4. Calls `generate_hierarchical_html(structure)` → creates visual.html
5. Returns: "Generated visual.html with paper structure"

**Time**: ~10 seconds (vs. minutes of manual instruction)

### Scenario 2: Refined Visualization (Automated)

**Student**: "Make it show interconnections with text excerpts"

**AI Agent Workflow** (using MCP tools):
1. Calls `analyze_section_interconnections(previous_structure)` → gets relationships
2. Calls `generate_interconnected_html(structure, connections, text_excerpts)` → creates visual_interconnection_text.html
3. Returns: "Generated interactive network visualization"

**Time**: ~5 seconds (vs. re-parsing entire paper manually)

### Scenario 3: Complete Automated Workflow

**Student**: "Do task 3.1 for the KPY paper"

**AI Agent Workflow** (using MCP tools):
1. Calls `create_visualization_task("KPY paper", "hierarchical")` → generates visual.html
2. Shows preview to student
3. If student wants refinement:
   - Calls `refine_visualization("visual.html", "show interconnections")` → generates visual_interconnection_text.html
4. Returns: Both visualizations ready for Moodle

**Time**: ~15 seconds total (vs. multiple back-and-forth interactions)

## Key Differences MCP Makes

### 1. **Automation vs. Manual Instructions**

| Aspect | Without MCP | With MCP |
|--------|-------------|----------|
| File Operations | Manual instructions: "unzip, read file" | Automatic: `extract_archive()`, `read_paper_file()` |
| Paper Parsing | AI agent parses from scratch each time | Standardized: `parse_paper_structure()` |
| HTML Generation | AI agent writes HTML code | Template-based: `generate_hierarchical_html()` |
| Feedback Loop | Re-process entire paper | Reuse parsed structure: `refine_visualization()` |

### 2. **Consistency & Standardization**

**Without MCP:**
- Each AI interaction may parse differently
- HTML format varies by student/AI
- No guarantee of Moodle compatibility

**With MCP:**
- Standardized parsing algorithm
- Consistent HTML templates (Moodle-compatible)
- Predictable output format

### 3. **Efficiency & Speed**

**Without MCP:**
- Step 1: 5-10 minutes (manual instructions, parsing, HTML coding)
- Step 2: 5-10 minutes (re-parsing, new HTML generation)
- **Total: 10-20 minutes**

**With MCP:**
- Step 1: ~10 seconds (automated workflow)
- Step 2: ~5 seconds (refinement using cached structure)
- **Total: ~15 seconds**

### 4. **Error Reduction**

**Without MCP:**
- File path errors
- Parsing inconsistencies
- HTML formatting issues
- Missing Moodle compatibility

**With MCP:**
- Validated file operations
- Standardized parsing
- Pre-tested HTML templates
- Guaranteed Moodle compatibility

### 5. **Enhanced Capabilities**

**Without MCP:**
- Basic hierarchical visualization
- Manual interconnection detection
- Limited text excerpt handling

**With MCP:**
- Advanced network analysis
- Automatic relationship detection (citations, references, logical flow)
- Rich text excerpt extraction
- Interactive visualizations (clickable nodes, link exploration)

### 6. **Student Experience**

**Without MCP:**
- Must learn file paths and formats
- Must provide detailed instructions
- Must wait for each step
- Must debug parsing/formatting issues

**With MCP:**
- Simple request: "Do task 3.1 for this paper"
- Instant results
- Consistent quality
- Focus on learning, not tool usage

## MCP Tool Architecture for Task 3.1

```
mcp-paper-visualizer/
├── tools/
│   ├── file_tools.py          # extract_archive, read_paper_file
│   ├── paper_tools.py          # parse_paper_structure, analyze_interconnections
│   ├── visualization_tools.py  # generate_*_html functions
│   └── workflow_tools.py       # create_task, refine_visualization
├── templates/
│   ├── hierarchical.html       # Moodle-compatible hierarchical template
│   ├── network.html            # Network visualization template
│   └── interconnected.html     # Full interactive template
└── resources/
    └── paper_parsers/          # LaTeX/PDF parsing libraries
```

## Example: Complete MCP-Enabled Workflow

### Student Request
```
"Generate task 3.1 visualization for the KPY paper, 
starting with hierarchical, then show interconnections"
```

### AI Agent Execution (Automatic)
```python
# Step 1: Extract and parse
archive_path = "PhDagentSpring2026/literature/KPY*/...tar.gz"
extracted = extract_archive(archive_path)
paper_content = read_paper_file(extracted['main_file'])
structure = parse_paper_structure(paper_content)

# Step 2: Generate hierarchical
visual_html = generate_hierarchical_html(structure)
# Returns: "visual.html created"

# Step 3: Analyze interconnections
connections = analyze_section_interconnections(structure)

# Step 4: Generate interconnected version
interconnected_html = generate_interconnected_html(
    structure, connections, include_text=True
)
# Returns: "visual_interconnection_text.html created"
```

### Result
- ✅ Both HTML files generated
- ✅ Moodle-compatible format
- ✅ Interactive network visualization
- ✅ Text excerpts and link exploration
- ✅ **Time: ~15 seconds total**

## Benefits Summary

| Benefit | Impact |
|---------|--------|
| **Time Savings** | 10-20 minutes → 15 seconds (40-80x faster) |
| **Consistency** | Standardized output every time |
| **Error Reduction** | Validated operations, tested templates |
| **Enhanced Features** | Advanced network analysis, interactivity |
| **Student Focus** | Learn paper structure, not tool usage |
| **Scalability** | Works for any paper format |
| **Reusability** | Parsed structure cached for refinements |

## Conclusion

MCP transforms Task 3.1 from a **manual, multi-step, error-prone process** into a **one-command, automated, reliable workflow**. Students can focus on understanding paper structures rather than managing file operations and HTML generation. The AI agent becomes a powerful assistant with specialized tools rather than a general-purpose parser that must be carefully instructed for each step.

---

**Key Insight**: MCP doesn't just automate—it **standardizes, accelerates, and enhances** the entire visualization workflow, making it accessible to all students regardless of their technical skills.
