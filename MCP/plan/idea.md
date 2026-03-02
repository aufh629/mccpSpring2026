# MCP Tool for Academic Paper Discourse Analysis

## Project Overview

Build an MCP (Model Context Protocol) tool to help students analyze their academic papers using:
- **Move/Step concepts**: Discourse analysis framework (e.g., Introduction Move 1-3: establishing territory → indicating gap → presenting research)
- **Manchester Academic Phrasebank**: Provide sentence templates and rewriting suggestions

## Deployment Strategy

### Phase 1: Local Development (MVP)
- **Target**: Individual students or small groups
- **Approach**: Students clone GitHub repo and run locally
- **Pros**: Privacy, simple setup, no server maintenance
- **Cons**: Each student needs to install, version management

### Phase 2: Server Deployment (Future)
- **Target**: Entire research group/class
- **Approach**: Centralized server with WebSocket/TCP access
- **Pros**: Unified updates, shared resources, centralized corpus
- **Cons**: Requires infrastructure and network configuration

## Architecture Design

### Recommended Structure: Multi-Tool MCP Server

```
mcp-discourse-analyzer/
├── README.md
├── requirements.txt
├── config.example.json
├── server.py              # Main MCP server entry point
├── tools/
│   ├── __init__.py
│   ├── latex_tools.py     # LaTeX parsing and extraction
│   ├── discourse_tools.py # Move/Step analysis
│   └── phrase_tools.py    # Phrasebank integration
├── resources/
│   └── phrasebank/        # Academic Phrasebank data
└── utils/
    ├── __init__.py
    └── config.py          # Configuration management
```

## Core Tools Design

### 1. LaTeX Analysis Tools (`latex_tools.py`)

**Tool 1: `parse_latex_structure`**
- **Input**: LaTeX file path or content
- **Output**: JSON with:
  - Section/subsection hierarchy
  - Sentence-level breakdown per section
  - Citations, tables, figures locations
  - Section boundaries

**Tool 2: `extract_section`**
- **Input**: Section name (e.g., "Introduction", "Discussion")
- **Output**: Extracted text for that section
- **Purpose**: Allow Agent to focus on specific sections for move/step analysis

### 2. Discourse Analysis Tools (`discourse_tools.py`)

**Tool 1: `get_move_definitions`**
- **Input**: Section type (optional, e.g., "Introduction", "Discussion")
- **Output**: JSON with move/step taxonomy:
  ```json
  {
    "section_type": "Introduction",
    "moves": [
      {
        "move_id": "Move 1",
        "name": "Establishing territory",
        "steps": [
          {"step_id": "1.1", "name": "Topic generalization"},
          {"step_id": "1.2", "name": "Previous research"}
        ]
      }
    ]
  }
  ```
- **Purpose**: Provides reference taxonomy for AI agent to use in classification

**Tool 2: `get_expected_moves`**
- **Input**: Section type (e.g., "Introduction", "Methods", "Discussion")
- **Output**: JSON with expected moves for that section type:
  ```json
  {
    "section_type": "Introduction",
    "expected_moves": ["Move 1", "Move 2", "Move 3"],
    "optional_moves": ["Move 4"],
    "typical_order": ["Move 1", "Move 2", "Move 3"]
  }
  ```
- **Purpose**: Provides reference for AI agent to check completeness

### 3. Phrasebank Tools (`phrase_tools.py`)

**Tool 1: `get_phrasebank_templates`**
- **Input**: Move/Step type (optional: specific move/step ID)
- **Output**: List of typical sentence templates from Phrasebank:
  ```json
  {
    "move": "Move 1: Establishing territory",
    "templates": [
      {
        "category": "General statements",
        "phrases": ["It is generally agreed that...", "It is widely accepted that..."]
      }
    ]
  }
  ```
- **Purpose**: Provides phrasebank templates for AI agent to use in rewriting

**Tool 2: `search_phrasebank`** (Optional enhancement)
- **Input**: Keyword or function (e.g., "comparing", "contrasting", "stating limitations")
- **Output**: Relevant phrasebank entries matching the search
- **Purpose**: Helps AI agent find appropriate phrases for specific writing functions

## LLM API Usage & Architecture

### Key Insight: No Additional API Needed!

**If users are using MCP in an IDE with an AI agent (like Cursor or VS Code with Copilot), they don't need additional API keys for the MCP tools.**

### Architecture: Separation of Concerns

**MCP Tools (No LLM needed):**
- Provide **structured operations** and **data access**
- Focus on what they're good at: parsing, extraction, data retrieval
- Examples:
  - `parse_latex_structure` - Pure LaTeX parsing (local)
  - `extract_section` - Text extraction (local)
  - `get_phrasebank_templates` - Database lookup (local JSON/SQLite)
  - `get_move_definitions` - Return move/step taxonomy (static data)

**IDE's AI Agent (Handles LLM processing):**
- Uses the student's **existing AI agent** (already configured in IDE)
- Performs intelligent analysis using the structured data from MCP tools
- Examples:
  - Student asks: "Analyze the moves in this Introduction"
  - Agent calls: `extract_section("Introduction")` → gets text
  - Agent calls: `get_move_definitions()` → gets move taxonomy
  - **Agent uses its own LLM** to classify sentences into moves
  - Agent returns analysis to student

### Revised Tool Design (No LLM in MCP)

**Tool 1: `analyze_moves_steps`** → **Changed to: `get_move_definitions`**
- **Old**: MCP tool calls LLM to classify moves
- **New**: MCP tool returns move/step taxonomy (static JSON)
- **AI Agent**: Uses taxonomy + text to classify (using its own LLM)

**Tool 2: `check_move_completeness`** → **Changed to: `get_expected_moves`**
- **Old**: MCP tool calls LLM to identify gaps
- **New**: MCP tool returns expected moves for section type (static data)
- **AI Agent**: Compares found moves vs expected moves (using its own LLM)

**Tool 3: `rewrite_with_phrasebank`** → **Changed to: `get_phrasebank_templates`**
- **Old**: MCP tool calls LLM to rewrite sentences
- **New**: MCP tool returns relevant phrasebank templates
- **AI Agent**: Uses templates to rewrite (using its own LLM)

### Benefits of This Architecture

1. **No Duplicate API Costs**: Students use their existing IDE AI agent
2. **Simpler MCP Tools**: Focus on data/operations, not intelligence
3. **Better Integration**: Leverages IDE's AI capabilities
4. **No API Key Management**: Students don't need to configure additional keys
5. **Consistent Experience**: Uses the same AI model student is already using

### What MCP Tools Actually Do

**Data Providers:**
- Parse LaTeX files → structured data
- Extract sections → clean text
- Retrieve phrasebank entries → templates
- Provide move/step taxonomies → reference data

**The AI Agent Does:**
- Text analysis and classification
- Pattern matching and reasoning
- Sentence rewriting and improvement
- Gap analysis and suggestions

### Example Workflow (No MCP API Calls)

**Student**: "Analyze the moves in my Introduction section"

**Flow:**
1. AI Agent calls `parse_latex_structure()` → gets paper structure
2. AI Agent calls `extract_section("Introduction")` → gets intro text
3. AI Agent calls `get_move_definitions()` → gets move taxonomy
4. **AI Agent uses its own LLM** to classify each sentence
5. AI Agent calls `get_expected_moves("Introduction")` → gets expected moves
6. **AI Agent uses its own LLM** to compare and identify gaps
7. AI Agent returns comprehensive analysis to student

**Result**: Zero API calls from MCP tools, all LLM processing done by IDE's AI agent

### Optional: Hybrid Mode (For Advanced Users)

**If some students want standalone MCP tools without IDE:**
- Can add optional LLM integration for command-line usage
- But default architecture assumes IDE AI agent handles LLM

## Implementation Details

### Technology Stack
- **Language**: Python (recommended) or Node.js
- **MCP SDK**: Official Python/Node MCP SDK
- **LaTeX Parsing**: `pylatexenc` or custom parser
- **Data Storage**: 
  - JSON files for phrasebank templates
  - JSON files for move/step taxonomies
  - SQLite (optional) for larger phrasebank databases
- **No LLM Integration Needed**: MCP tools don't call LLMs directly
  - IDE's AI agent handles all LLM processing
  - MCP tools only provide structured data and operations

### Configuration Management
- **Config File**: `config.json` (students copy from `config.example.json`)
  - Path to phrasebank data
  - Path to move taxonomy definitions
  - LaTeX parsing options
- **No API Keys Required**: Students use their existing IDE AI agent
- **Optional Settings**: 
  - Custom phrasebank paths
  - Custom move taxonomy files
  - LaTeX parsing preferences

### VS Code/Cursor Integration

**Configuration Example** (for Cursor/VS Code):
```jsonc
{
  "mcpServers": {
    "discourse-analyzer": {
      "command": "python",
      "args": ["/path/to/mcp-discourse-analyzer/server.py"]
      // No API keys needed - uses IDE's existing AI agent
    }
  }
}
```

**Note**: The IDE's AI agent (Cursor AI, GitHub Copilot, etc.) will use these MCP tools and handle all LLM processing using the student's existing AI configuration.

## User Workflow Examples

### Example 1: Analyzing Introduction Section
**Student Action**: Select Introduction text in VS Code
**Student Query**: "请帮我分析这一段 Introduction 的语步，并指出缺少哪些典型 Move。"

**Agent Workflow** (AI Agent uses its own LLM):
1. Calls `extract_section("Introduction")` → gets intro text
2. Calls `get_move_definitions("Introduction")` → gets move taxonomy
3. **AI Agent uses its LLM** to classify each sentence into moves/steps
4. Calls `get_expected_moves("Introduction")` → gets expected moves
5. **AI Agent uses its LLM** to compare found vs expected moves
6. Returns: Move labels + missing moves + suggestions

**Note**: All LLM processing done by IDE's AI agent, MCP tools only provide data

### Example 2: Improving Sentence with Phrasebank
**Student Action**: Select a sentence
**Student Query**: "帮我用更学术的句式重写这句话"

**Agent Workflow** (AI Agent uses its own LLM):
1. **AI Agent uses its LLM** to identify move type of the sentence
2. Calls `get_phrasebank_templates(move_type)` → gets relevant templates
3. **AI Agent uses its LLM** to rewrite sentence using phrasebank patterns
4. Returns: Rewritten sentence + explanation

**Note**: MCP tool provides templates, AI agent does the actual rewriting

## Development Phases

### Phase 1: MVP (Minimal Viable Product)
- [ ] Basic MCP server setup
- [ ] LaTeX parsing (basic structure extraction)
- [ ] Move/step taxonomy data (static JSON)
- [ ] Basic Phrasebank integration (local JSON)
- [ ] VS Code/Cursor configuration guide
- [ ] No LLM integration needed - IDE AI agent handles it

### Phase 2: Enhanced Features
- [ ] Advanced move/step detection
- [ ] Full Phrasebank integration
- [ ] Batch analysis capabilities
- [ ] Export analysis results

### Phase 3: Advanced Features
- [ ] Fine-tuned move/step classifier
- [ ] Multi-paper comparison
- [ ] Progress tracking
- [ ] Server deployment option

## Key Design Principles

1. **Modularity**: Each tool is independent, easy to extend
2. **No API Keys Required**: Uses IDE's existing AI agent for LLM processing
3. **Data-Focused**: MCP tools provide structured data, not intelligence
4. **Privacy-First**: Local processing by default, no external API calls from MCP
5. **Student-Friendly**: Clear README, minimal setup steps, no additional configuration
6. **Extensibility**: Easy to add new tools or modify existing ones
7. **Separation of Concerns**: MCP = data/operations, IDE AI = intelligence

## Next Steps

1. Set up GitHub repository structure
2. Implement basic MCP server with one tool (proof of concept)
3. Test with sample LaTeX papers
4. Gather student feedback
5. Iterate and expand functionality

---

**Source**: Conversation from https://poe.com/s/eaJSHEgFrYbN6OXR38GR
**Last Updated**: 2026-01-26
