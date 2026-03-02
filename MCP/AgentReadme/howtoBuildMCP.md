# How to Build MCP Servers: A Comprehensive Guide

**For AI Agents and Human Developers**

This guide explains how to build Model Context Protocol (MCP) servers, why they are superior to prompt-based approaches, and how to create remote MCP servers that can be called without downloading.

---

## Table of Contents

1. [Why MCP Servers vs. Prompt Files](#why-mcp-servers-vs-prompt-files)
2. [Understanding MCP Architecture](#understanding-mcp-architecture)
3. [Building a Local MCP Server (stdio-based)](#building-a-local-mcp-server-stdio-based)
4. [Building a Remote MCP Server (HTTP/SSE)](#building-a-remote-mcp-server-httpsse)
5. [Best Practices](#best-practices)
6. [Example: Task 3.1 Paper Visualizer](#example-task-31-paper-visualizer)

---

## Why MCP Servers vs. Prompt Files

### The Problem with Prompt Files

Traditional approaches rely on storing prompts in files and having AI agents read and execute them:

**❌ Limitations:**
- **Static and Inflexible**: Prompts are text files that can't execute code or access system resources
- **No State Management**: Can't maintain context or remember previous operations
- **Limited Capabilities**: Can only describe tasks, not perform them
- **No Error Handling**: Can't handle edge cases or provide structured error responses
- **No Tool Discovery**: AI agents must manually parse prompts to understand available actions
- **Maintenance Burden**: Changes require editing multiple prompt files
- **No Type Safety**: No validation of inputs/outputs
- **No Reusability**: Each prompt is isolated, can't compose complex workflows

**Example of Prompt File Approach:**
```markdown
# prompt.md
To visualize a paper:
1. Extract the archive
2. Find the .tex file
3. Parse the structure
4. Generate HTML
```

The AI agent must:
- Read the prompt
- Understand the steps
- Manually implement each step
- Handle all edge cases
- Report errors in unstructured format

### The MCP Server Advantage

**✅ Benefits:**
- **Executable Tools**: Tools are actual functions that execute code
- **Type-Safe Interfaces**: JSON Schema validation for inputs/outputs
- **Automatic Discovery**: AI agents automatically discover available tools
- **Structured Responses**: Consistent JSON responses with error handling
- **State Management**: Can maintain context across tool calls
- **Composable Workflows**: Tools can call other tools, building complex operations
- **Error Handling**: Structured error responses with context
- **Reusability**: Tools can be shared across projects
- **Version Control**: Code-based, can be versioned and tested
- **IDE Integration**: Native support in Cursor, VS Code, and other IDEs

**Example of MCP Server Approach:**
```python
# server.py
@app.call_tool()
async def call_tool(name: str, arguments: dict) -> Sequence[TextContent]:
    if name == "extract_archive":
        result = await file_tools.extract_archive(arguments["archive_path"])
        return [TextContent(type="text", text=json.dumps(result))]
```

The AI agent:
- Automatically discovers `extract_archive` tool
- Knows it requires `archive_path` parameter
- Gets structured JSON response
- Can chain with other tools automatically

### Comparison Table

| Aspect | Prompt Files | MCP Servers |
|--------|-------------|-------------|
| **Execution** | Manual interpretation | Automatic execution |
| **Type Safety** | None | JSON Schema validation |
| **Error Handling** | Unstructured text | Structured error objects |
| **Tool Discovery** | Manual parsing | Automatic via `list_tools()` |
| **State Management** | None | Can maintain context |
| **Composability** | Limited | Full tool chaining |
| **Testing** | Manual | Unit testable |
| **IDE Support** | None | Native integration |
| **Version Control** | Text diffs | Code diffs with tests |

---

## Understanding MCP Architecture

### MCP Protocol Overview

MCP (Model Context Protocol) is a standardized protocol for AI agents to interact with external tools and resources. It uses JSON-RPC 2.0 over stdio (local) or HTTP/SSE (remote).

### Two MCP Server Types

#### 1. Local MCP Server (stdio-based)
- **Transport**: Standard input/output (stdio)
- **Use Case**: Local development, single-user scenarios
- **Setup**: Configure IDE to run Python script
- **Example**: Task 3.1 server in this repository

#### 2. Remote MCP Server (HTTP/SSE)
- **Transport**: HTTP with Server-Sent Events (SSE)
- **Use Case**: Multi-user, cloud-based, no-download scenarios
- **Setup**: Deploy to server, access via URL
- **Example**: OpenCode MCP server (can be called without downloading)

### MCP Components

1. **Server**: The MCP server that provides tools
2. **Client**: The IDE or AI agent that calls tools
3. **Tools**: Executable functions exposed to the client
4. **Resources**: Read-only data the server provides
5. **Prompts**: Template prompts the server can generate

---

## Building a Local MCP Server (stdio-based)

### Step 1: Project Structure

```
your-mcp-server/
├── server.py              # Main server entry point
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
├── tools/                # Tool modules
│   ├── __init__.py
│   ├── tool1.py
│   └── tool2.py
└── templates/            # Optional: HTML/template files
    └── template.html
```

### Step 2: Install Dependencies

```bash
pip install mcp>=0.9.0 aiofiles>=23.0.0
```

### Step 3: Create Server Entry Point

```python
#!/usr/bin/env python3
"""
MCP Server: Your Server Name
Description of what your server does
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Import your tool modules
from tools import tool1, tool2

# Initialize MCP server
app = Server("your-server-name")

# Get base directory
BASE_DIR = Path(__file__).parent


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools"""
    return [
        Tool(
            name="tool1_name",
            description="What this tool does",
            inputSchema={
                "type": "object",
                "properties": {
                    "param1": {
                        "type": "string",
                        "description": "Description of param1"
                    }
                },
                "required": ["param1"]
            }
        ),
        Tool(
            name="tool2_name",
            description="What this tool does",
            inputSchema={
                "type": "object",
                "properties": {
                    "param1": {
                        "type": "string",
                        "description": "Description of param1"
                    }
                },
                "required": ["param1"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
    """Handle tool calls"""
    
    try:
        if name == "tool1_name":
            result = await tool1.execute(arguments["param1"])
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "tool2_name":
            result = await tool2.execute(arguments["param1"])
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        else:
            raise ValueError(f"Unknown tool: {name}")
    
    except Exception as e:
        error_msg = {
            "error": str(e),
            "tool": name,
            "arguments": arguments
        }
        return [TextContent(type="text", text=json.dumps(error_msg, indent=2))]


async def main():
    """Main entry point"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
```

### Step 4: Create Tool Modules

```python
# tools/tool1.py
"""Tool 1 implementation"""

from typing import Dict


async def execute(param1: str) -> Dict:
    """Execute tool1"""
    # Your implementation here
    result = {
        "status": "success",
        "data": f"Processed: {param1}"
    }
    return result
```

### Step 5: Configure IDE

**For Cursor:**
1. Open Settings (`Cmd+,` or `Ctrl+,`)
2. Go to Features → MCP Servers
3. Add configuration:
```json
{
  "mcpServers": {
    "your-server-name": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

### Step 6: Test Your Server

```bash
# Test directly
python server.py

# Or test via IDE
# Ask AI agent: "Use tool1_name with param1='test'"
```

---

## Building a Remote MCP Server (HTTP/SSE)

Remote MCP servers allow AI agents to call tools without downloading or installing anything locally. This is ideal for:
- **Cloud-based services**: Deploy once, use everywhere
- **Multi-user scenarios**: Shared tools across teams
- **No-installation workflows**: Users just need the URL
- **Centralized updates**: Update server, all users get updates

### Architecture Overview

```
┌─────────────┐         HTTP/SSE         ┌──────────────┐
│  AI Agent   │ ←──────────────────────→ │  MCP Server  │
│  (Client)   │                          │   (Remote)   │
└─────────────┘                          └──────────────┘
     (IDE)                                      (Cloud)
```

### Step 1: Choose Framework

**Option A: FastAPI (Recommended)**
- Modern async framework
- Built-in SSE support
- Easy to deploy

**Option B: Flask with Flask-SSE**
- Simpler, but less async support

**Option C: Custom HTTP Server**
- Maximum control, more work

### Step 2: Create HTTP/SSE Server

```python
#!/usr/bin/env python3
"""
Remote MCP Server: Your Server Name
Accessible via HTTP/SSE without local installation
"""

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from sse_starlette.sse import EventSourceResponse
import json
import asyncio
from typing import Any, Dict, List
from mcp.server import Server
from mcp.types import Tool, TextContent

# Import your tools
from tools import tool1, tool2

app_fastapi = FastAPI()
mcp_server = Server("your-remote-server")


@app_fastapi.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "server": "your-remote-server",
        "mcp_version": "0.9.0"
    }


@app_fastapi.post("/mcp/list_tools")
async def list_tools():
    """List available tools"""
    tools = await mcp_server.list_tools()
    return {
        "tools": [
            {
                "name": tool.name,
                "description": tool.description,
                "inputSchema": tool.inputSchema
            }
            for tool in tools
        ]
    }


@app_fastapi.post("/mcp/call_tool")
async def call_tool(request: Request):
    """Call a tool via HTTP POST"""
    data = await request.json()
    tool_name = data.get("name")
    arguments = data.get("arguments", {})
    
    try:
        # Call your tool implementation
        if tool_name == "tool1_name":
            result = await tool1.execute(arguments.get("param1"))
        elif tool_name == "tool2_name":
            result = await tool2.execute(arguments.get("param1"))
        else:
            raise ValueError(f"Unknown tool: {tool_name}")
        
        return {
            "status": "success",
            "result": result
        }
    
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }


@app_fastapi.get("/mcp/stream")
async def stream_tools(request: Request):
    """SSE endpoint for streaming tool calls"""
    
    async def event_generator():
        while True:
            # Check if client is still connected
            if await request.is_disconnected():
                break
            
            # In a real implementation, you'd handle tool calls here
            # For now, just send a heartbeat
            yield {
                "event": "heartbeat",
                "data": json.dumps({"status": "connected"})
            }
            
            await asyncio.sleep(30)  # Heartbeat every 30 seconds
    
    return EventSourceResponse(event_generator())


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app_fastapi, host="0.0.0.0", port=8000)
```

### Step 3: Deploy to Cloud

**Option A: Deploy to Heroku**
```bash
# Create Procfile
echo "web: uvicorn server:app_fastapi --host 0.0.0.0 --port \$PORT" > Procfile

# Deploy
git push heroku main
```

**Option B: Deploy to Railway**
```bash
# Railway auto-detects FastAPI
# Just push to GitHub
```

**Option C: Deploy to AWS/GCP/Azure**
- Use container services (ECS, Cloud Run, Container Instances)
- Or serverless (Lambda, Cloud Functions)

### Step 4: Configure Client to Use Remote Server

**For Cursor (if remote MCP support exists):**
```json
{
  "mcpServers": {
    "your-remote-server": {
      "url": "https://your-server.com/mcp",
      "transport": "sse"
    }
  }
}
```

**For Custom Clients:**
```python
import requests

# List tools
response = requests.post("https://your-server.com/mcp/list_tools")
tools = response.json()

# Call tool
response = requests.post("https://your-server.com/mcp/call_tool", json={
    "name": "tool1_name",
    "arguments": {"param1": "value"}
})
result = response.json()
```

### Step 5: Add Authentication (Optional)

```python
from fastapi import Depends, HTTPException, Header

API_KEY = "your-secret-api-key"

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

@app_fastapi.post("/mcp/call_tool")
async def call_tool(request: Request, api_key: str = Depends(verify_api_key)):
    # ... tool implementation
```

### Advantages of Remote MCP Servers

1. **No Local Installation**: Users just need the URL
2. **Centralized Updates**: Update server, all users benefit
3. **Resource Sharing**: Expensive operations run on server
4. **Access Control**: Can implement authentication/authorization
5. **Scalability**: Can handle multiple concurrent users
6. **Monitoring**: Can track usage and performance

---

## Best Practices

### 1. Tool Design

**✅ Do:**
- Use descriptive tool names (`extract_archive` not `tool1`)
- Provide clear descriptions
- Use JSON Schema for validation
- Return structured responses
- Handle errors gracefully

**❌ Don't:**
- Use vague names
- Skip input validation
- Return unstructured text
- Ignore errors

### 2. Error Handling

```python
@app.call_tool()
async def call_tool(name: str, arguments: dict) -> Sequence[TextContent]:
    try:
        # Your implementation
        result = await execute_tool(name, arguments)
        return [TextContent(type="text", text=json.dumps(result))]
    
    except FileNotFoundError as e:
        error = {
            "error": "file_not_found",
            "message": str(e),
            "tool": name
        }
        return [TextContent(type="text", text=json.dumps(error))]
    
    except Exception as e:
        error = {
            "error": "unknown_error",
            "message": str(e),
            "tool": name
        }
        return [TextContent(type="text", text=json.dumps(error))]
```

### 3. Documentation

Always include:
- **README.md**: Overview, installation, usage
- **Tool descriptions**: Clear descriptions in `list_tools()`
- **Examples**: Usage examples in documentation
- **Error codes**: Document possible errors

### 4. Testing

```python
# tests/test_tools.py
import pytest
from tools import tool1

@pytest.mark.asyncio
async def test_tool1():
    result = await tool1.execute("test_input")
    assert result["status"] == "success"
    assert "data" in result
```

### 5. Versioning

Include version in:
- Server initialization: `Server("name", version="1.0.0")`
- API responses: `{"version": "1.0.0", ...}`
- Documentation

---

## Example: Task 3.1 Paper Visualizer

The `task3.1` folder in this repository is a complete example of a local MCP server. Let's examine its structure:

### Architecture

```
task3.1/
├── server.py                    # Main server (stdio-based)
├── requirements.txt             # Dependencies
├── tools/
│   ├── file_tools.py           # Archive extraction, file reading
│   ├── paper_tools.py          # Paper parsing, structure analysis
│   └── visualization_tools.py  # HTML generation
└── templates/
    ├── hierarchical.html        # Hierarchical visualization
    └── interconnected.html      # Network visualization
```

### Key Features

1. **8 Tools Available**:
   - `extract_archive`: Extract tar.gz/zip files
   - `read_paper_file`: Read paper files
   - `fetch_arxiv_paper`: Download from arXiv
   - `parse_paper_structure`: Extract structure
   - `analyze_section_interconnections`: Find relationships
   - `generate_hierarchical_html`: Create hierarchical visualization
   - `generate_interconnected_html`: Create network visualization
   - `create_visualization_task`: Complete workflow

2. **Type Safety**: All tools use JSON Schema for validation

3. **Error Handling**: Structured error responses

4. **Composability**: Tools can be chained (extract → parse → visualize)

### Converting to Remote Server

To convert Task 3.1 to a remote server:

1. **Create HTTP server** (as shown above)
2. **Deploy to cloud** (Heroku, Railway, etc.)
3. **Update client config** to use URL instead of local path
4. **Add authentication** if needed

**Example Remote Configuration:**
```json
{
  "mcpServers": {
    "task3.1-remote": {
      "url": "https://paper-visualizer.herokuapp.com/mcp",
      "transport": "sse"
    }
  }
}
```

Users can then use it without:
- Downloading the code
- Installing Python dependencies
- Configuring local paths
- Managing updates

---

## Summary

### Why MCP Servers?

1. **Superior to Prompts**: Executable, type-safe, discoverable
2. **Better UX**: Automatic tool discovery, structured responses
3. **Maintainable**: Code-based, testable, version-controlled
4. **Composable**: Tools can chain together
5. **IDE Integration**: Native support in modern IDEs

### When to Use Local vs Remote?

**Local (stdio):**
- Single-user development
- Sensitive data processing
- Offline requirements
- Custom tooling

**Remote (HTTP/SSE):**
- Multi-user scenarios
- Cloud-based services
- No-installation workflows
- Centralized updates
- Resource-intensive operations

### Getting Started

1. **Start Simple**: Build a local stdio server first
2. **Test Thoroughly**: Test all tools and error cases
3. **Document Well**: Write clear README and tool descriptions
4. **Iterate**: Add features based on usage
5. **Scale Up**: Convert to remote server when needed

---

## Resources

- **MCP Specification**: https://modelcontextprotocol.io
- **MCP Python SDK**: https://github.com/modelcontextprotocol/python-sdk
- **Example Server**: See `task3.1/` in this repository
- **Cursor MCP Docs**: https://docs.cursor.com/mcp

---

**Last Updated**: 2026-01-27  
**Version**: 1.0
