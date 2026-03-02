# OpenCode CLI Usage Guide for Task 3.1 MCP Server

This guide explains how to use OpenCode CLI to call the Task 3.1 MCP server from GitHub without downloading the repository.

## Table of Contents

1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Running the MCP Server](#running-the-mcp-server)
4. [Executing Individual Tools](#executing-individual-tools)
5. [Complete Workflow Examples](#complete-workflow-examples)
6. [IDE Integration](#ide-integration)
7. [Troubleshooting](#troubleshooting)

---

## Installation

### Step 1: Install OpenCode CLI

**Option A: Using pip (Python)**
```bash
pip install opencode-cli
```

**Option B: Using npm (Node.js)**
```bash
npm install -g opencode-cli
```

**Option C: Direct Download**
```bash
# Check OpenCode documentation for your platform
# Example for Linux/Mac:
curl -L https://github.com/opencode/cli/releases/latest/download/opencode -o /usr/local/bin/opencode
chmod +x /usr/local/bin/opencode
```

### Step 2: Verify Installation

```bash
opencode --version
```

Expected output:
```
opencode version 1.0.0
```

---

## Basic Usage

### OpenCode Command Format

```bash
opencode run <github-repo> [options] --command "<command>"
```

**Parameters:**
- `github-repo`: Repository in format `owner/repo` or full URL
- `--path`: Optional path within repository
- `--branch`: Optional branch name (default: main)
- `--command`: Command to execute

### Repository Information

- **Owner**: `tesolchina`
- **Repository**: `mccpSpring2026`
- **Path**: `MCP/openCodeTask3.1`
- **Branch**: `main` (default)

**Full Repository URL**: `https://github.com/tesolchina/mccpSpring2026/tree/main/MCP/openCodeTask3.1`

---

## Running the MCP Server

### Method 1: Start MCP Server (for IDE Integration)

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python server.py"
```

This starts the MCP server in stdio mode, ready to accept tool calls from your IDE.

### Method 2: Test Server Connection

```bash
# List available tools
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
from mcp.server import Server
from server import app

async def list_tools():
    tools = await app.list_tools()
    for tool in tools:
        print(f'{tool.name}: {tool.description}')

asyncio.run(list_tools())
\""
```

---

## Executing Individual Tools

### Tool 1: Extract Archive

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
import json
from tools import file_tools

async def main():
    result = await file_tools.extract_archive('path/to/archive.tar.gz')
    print(json.dumps(result, indent=2))

asyncio.run(main())
\""
```

### Tool 2: Fetch arXiv Paper

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
import json
from tools import file_tools

async def main():
    result = await file_tools.fetch_arxiv_paper('https://arxiv.org/abs/2412.20379')
    print(json.dumps(result, indent=2))

asyncio.run(main())
\""
```

### Tool 3: Parse Paper Structure

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
import json
from tools import paper_tools

async def main():
    result = await paper_tools.parse_paper_structure('path/to/paper.tex')
    print(json.dumps(result, indent=2))

asyncio.run(main())
\""
```

### Tool 4: Generate Hierarchical Visualization

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
import json
from pathlib import Path
from tools import paper_tools, visualization_tools

async def main():
    # First parse the paper
    structure = await paper_tools.parse_paper_structure('path/to/paper.tex')
    # Then generate visualization
    result = await visualization_tools.generate_hierarchical_html(
        structure, 'visual.html', Path('MCP/openCodeTask3.1')
    )
    print(json.dumps(result, indent=2))

asyncio.run(main())
\""
```

---

## Complete Workflow Examples

### Example 1: Complete Workflow - arXiv Paper to Visualization

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
import json
from pathlib import Path
from tools import file_tools, paper_tools, visualization_tools

async def complete_workflow():
    print('Step 1: Fetching paper from arXiv...')
    paper = await file_tools.fetch_arxiv_paper('https://arxiv.org/abs/2412.20379')
    print(f'Downloaded: {paper[\"file_path\"]}')
    
    print('Step 2: Parsing paper structure...')
    structure = await paper_tools.parse_paper_structure(paper['file_path'])
    print(f'Found {len(structure.get(\"sections\", []))} sections')
    
    print('Step 3: Generating hierarchical visualization...')
    result = await visualization_tools.generate_hierarchical_html(
        structure, 'visual.html', Path('MCP/openCodeTask3.1')
    )
    print(f'Generated: {result[\"output_path\"]}')
    
    print('Step 4: Analyzing interconnections...')
    connections = await paper_tools.analyze_section_interconnections(structure)
    print(f'Found {len(connections.get(\"connections\", []))} connections')
    
    print('Step 5: Generating network visualization...')
    network_result = await visualization_tools.generate_interconnected_html(
        structure, connections, 'visual_interconnection.html', Path('MCP/openCodeTask3.1')
    )
    print(f'Generated: {network_result[\"output_path\"]}')
    
    print('\\n✅ Complete! Visualizations generated.')

asyncio.run(complete_workflow())
\""
```

### Example 2: Process Archive File

```bash
# Note: You'll need to provide the archive file path
# OpenCode can access files from the repository or URLs

opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
import json
from pathlib import Path
from tools import file_tools, paper_tools, visualization_tools

async def process_archive(archive_path):
    print(f'Extracting archive: {archive_path}')
    extracted = await file_tools.extract_archive(archive_path)
    print(f'Extracted to: {extracted[\"extract_dir\"]}')
    print(f'Main file: {extracted[\"main_file\"]}')
    
    print('Parsing structure...')
    structure = await paper_tools.parse_paper_structure(extracted['main_file'])
    
    print('Generating visualization...')
    result = await visualization_tools.generate_hierarchical_html(
        structure, 'visual.html', Path('MCP/openCodeTask3.1')
    )
    print(f'✅ Generated: {result[\"output_path\"]}')

# Replace with your archive path
asyncio.run(process_archive('path/to/your/archive.tar.gz'))
\""
```

### Example 3: Batch Process Multiple Papers

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c \"
import asyncio
from tools import file_tools, paper_tools, visualization_tools
from pathlib import Path

async def process_paper(arxiv_url, output_name):
    print(f'\\nProcessing: {arxiv_url}')
    paper = await file_tools.fetch_arxiv_paper(arxiv_url)
    structure = await paper_tools.parse_paper_structure(paper['file_path'])
    result = await visualization_tools.generate_hierarchical_html(
        structure, f'{output_name}.html', Path('MCP/openCodeTask3.1')
    )
    print(f'✅ Generated: {result[\"output_path\"]}')

async def batch_process():
    papers = [
        ('https://arxiv.org/abs/2412.20379', 'paper1'),
        ('https://arxiv.org/abs/2312.05885', 'paper2'),
    ]
    
    for url, name in papers:
        await process_paper(url, name)

asyncio.run(batch_process())
\""
```

---

## IDE Integration

### Cursor IDE Configuration

Add this to your Cursor settings (`Cmd+,` or `Ctrl+,` → Features → MCP Servers):

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

**Restart Cursor** after adding the configuration.

### VS Code Configuration

If VS Code supports MCP, add to `settings.json`:

```json
{
  "mcp.servers": {
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

### Testing in IDE

After configuration, test in your IDE's AI chat:

```
Visualize the paper structure from:
https://arxiv.org/abs/2412.20379
```

The AI agent should automatically use the MCP tools.

---

## Advanced Usage

### Using Environment Variables

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --env OUTPUT_DIR=/tmp/output \
  --command "python -c \"
import os
print(f'Output directory: {os.environ.get(\"OUTPUT_DIR\")}')
\""
```

### Specifying Branch

```bash
opencode run tesolchina/mccpSpring2026 \
  --branch develop \
  --path MCP/openCodeTask3.1 \
  --command "python server.py"
```

### Timeout Settings

```bash
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --timeout 300 \
  --command "python -c 'import time; time.sleep(60)'"
```

---

## Troubleshooting

### Issue: OpenCode Command Not Found

**Solution:**
```bash
# Check if OpenCode is installed
which opencode

# If not found, install it
pip install opencode-cli

# Or add to PATH
export PATH=$PATH:/path/to/opencode
```

### Issue: Dependencies Not Installed

**Solution:**
```bash
# OpenCode should auto-install, but you can manually install:
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "pip install -r requirements.txt"
```

### Issue: Module Not Found Errors

**Solution:**
```bash
# Ensure you're in the correct path
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "pwd && ls -la"
```

### Issue: Permission Denied

**Solution:**
```bash
# Make server.py executable (if needed)
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "chmod +x server.py && python server.py"
```

### Issue: Network/arXiv Access

**Solution:**
```bash
# Test network connectivity
opencode run tesolchina/mccpSpring2026 \
  --path MCP/openCodeTask3.1 \
  --command "python -c 'import urllib.request; print(urllib.request.urlopen(\"https://arxiv.org\").status)'"
```

---

## Quick Reference

### Repository Information
- **GitHub**: `tesolchina/mccpSpring2026`
- **Path**: `MCP/openCodeTask3.1`
- **Branch**: `main`

### Common Commands

```bash
# Start MCP server
opencode run tesolchina/mccpSpring2026 --path MCP/openCodeTask3.1 --command "python server.py"

# Fetch arXiv paper
opencode run tesolchina/mccpSpring2026 --path MCP/openCodeTask3.1 --command "python -c 'from tools import file_tools; import asyncio; print(asyncio.run(file_tools.fetch_arxiv_paper(\"https://arxiv.org/abs/2412.20379\")))'"

# List files in repository
opencode list tesolchina/mccpSpring2026 --path MCP/openCodeTask3.1
```

---

## Additional Resources

- **OpenCode Documentation**: See OpenCode official docs
- **MCP Specification**: https://modelcontextprotocol.io
- **Task 3.1 Full Documentation**: See `../task3.1/README.md`
- **OpenCode Setup Guide**: See `../AgentReadme/OpenCodeSetup.md`

---

**Last Updated**: 2026-01-27  
**Repository**: https://github.com/tesolchina/mccpSpring2026/tree/main/MCP/openCodeTask3.1
