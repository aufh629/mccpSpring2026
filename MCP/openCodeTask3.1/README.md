# Task 3.1 MCP Server - OpenCode Version

This is an OpenCode-compatible version of the Task 3.1 MCP server that can be called directly from GitHub without downloading the repository.

## Repository Location

**GitHub**: `https://github.com/tesolchina/mccpSpring2026/tree/main/MCP/openCodeTask3.1`

## Quick Start with OpenCode

### Prerequisites

1. **Install OpenCode CLI**:
   ```bash
   # Option 1: Using pip
   pip install opencode-cli
   
   # Option 2: Using npm
   npm install -g opencode-cli
   
   # Option 3: Direct download
   # See OpenCode documentation for your platform
   ```

2. **Verify Installation**:
   ```bash
   opencode --version
   ```

### Using the MCP Server via OpenCode

#### Method 1: Run MCP Server Directly

```bash
# Start the MCP server from GitHub
opencode run tesolchina/mccpSpring2026 --path MCP/openCodeTask3.1 --command "python server.py"
```

#### Method 2: Use in Cursor/IDE

Configure your IDE to use OpenCode to run the server:

```json
{
  "mcpServers": {
    "task3.1-opencode": {
      "command": "opencode",
      "args": [
        "run",
        "tesolchina/mccpSpring2026",
        "--path", "MCP/openCodeTask3.1",
        "--command", "python server.py"
      ]
    }
  }
}
```

#### Method 3: Execute Individual Tools

```bash
# Extract an archive
opencode run tesolchina/mccpSpring2026 --path MCP/openCodeTask3.1 --command "python -c \"from tools import file_tools; import asyncio; print(asyncio.run(file_tools.extract_archive('archive.tar.gz')))\""

# Fetch arXiv paper
opencode run tesolchina/mccpSpring2026 --path MCP/openCodeTask3.1 --command "python -c \"from tools import file_tools; import asyncio; print(asyncio.run(file_tools.fetch_arxiv_paper('https://arxiv.org/abs/2412.20379')))\""
```

## Available Tools

This MCP server provides 8 tools:

1. `extract_archive` - Extract tar.gz or zip files
2. `read_paper_file` - Read LaTeX, HTML, or Markdown files
3. `fetch_arxiv_paper` - Download papers from arXiv
4. `parse_paper_structure` - Parse paper structure
5. `analyze_section_interconnections` - Analyze section relationships
6. `generate_hierarchical_html` - Generate hierarchical visualization
7. `generate_interconnected_html` - Generate network visualization
8. `create_visualization_task` - Complete workflow

## Example Usage

### Example 1: Visualize arXiv Paper

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
from tools import file_tools, paper_tools, visualization_tools

async def main():
    # Fetch paper
    paper = await file_tools.fetch_arxiv_paper('https://arxiv.org/abs/2412.20379')
    # Parse structure
    structure = await paper_tools.parse_paper_structure(paper['file_path'])
    # Generate visualization
    result = await visualization_tools.generate_hierarchical_html(structure, 'visual.html', None)
    print(f'Generated: {result[\"output_path\"]}')

asyncio.run(main())
\""
```

### Example 2: Process Local Archive

```bash
# First, upload your archive to a temporary location or use a URL
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
from tools import file_tools, paper_tools, visualization_tools

async def main():
    # Extract archive
    extracted = await file_tools.extract_archive('path/to/archive.tar.gz')
    # Parse and visualize
    structure = await paper_tools.parse_paper_structure(extracted['main_file'])
    result = await visualization_tools.generate_hierarchical_html(structure)
    print(f'Success: {result[\"output_path\"]}')

asyncio.run(main())
\""
```

## Benefits of OpenCode Approach

✅ **No Local Installation**: Don't need to clone or download the repository  
✅ **Always Up-to-Date**: Always uses the latest code from GitHub  
✅ **Isolated Execution**: Code runs in temporary, isolated environments  
✅ **Easy Sharing**: Just share the GitHub URL  
✅ **Multi-User**: One codebase serves many users  

## Troubleshooting

### OpenCode CLI Not Found

```bash
# Install OpenCode
pip install opencode-cli

# Or check if it's in your PATH
which opencode
```

### Dependencies Not Installed

OpenCode should automatically install dependencies from `requirements.txt`. If not:

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "pip install -r requirements.txt && python server.py"
```

### Permission Issues

Ensure OpenCode has necessary permissions:

```bash
# On Unix systems
chmod +x server.py
```

## For More Information

- See `OpenCodeReadme.md` for detailed CLI usage instructions
- See `../task3.1/README.md` for full MCP server documentation
- See `../AgentReadme/OpenCodeSetup.md` for OpenCode setup guide

---

**Last Updated**: 2026-01-27
