# OpenCode MCP Setup: Running GitHub Code Without Downloading

**For AI Agents and Human Developers**

This guide explains how to build an MCP server that uses OpenCode (or similar CLI tools) to execute code directly from GitHub repositories without requiring users to download or clone the repository locally.

---

## Table of Contents

1. [What is OpenCode?](#what-is-opencode)
2. [Why Use OpenCode for MCP?](#why-use-opencode-for-mcp)
3. [Architecture Overview](#architecture-overview)
4. [Building an OpenCode-Based MCP Server](#building-an-opencode-based-mcp-server)
5. [Example Implementation](#example-implementation)
6. [Deployment and Configuration](#deployment-and-configuration)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

---

## What is OpenCode?

OpenCode is a CLI tool (or service) that allows you to execute code from GitHub repositories directly without cloning or downloading them. It works by:

1. **Fetching code on-demand**: Downloads only what's needed at execution time
2. **Temporary execution environment**: Creates isolated execution contexts
3. **Streaming results**: Returns output without storing files locally
4. **No local installation**: Users don't need to install dependencies locally

### Similar Tools/Concepts

- **GitHub Codespaces**: Cloud-based development environments
- **Replit**: Online code execution
- **CodeSandbox**: Browser-based code execution
- **npx (Node.js)**: Execute npm packages without installation
- **pipx (Python)**: Execute Python applications in isolated environments

---

## Why Use OpenCode for MCP?

### Traditional Approach (Download Required)

**❌ Problems:**
```bash
# User must:
git clone https://github.com/user/repo.git
cd repo
pip install -r requirements.txt
python server.py
```

- Requires local storage
- Must install dependencies
- Need to manage updates
- Platform-specific setup
- Multiple users = multiple installations

### OpenCode Approach (No Download)

**✅ Benefits:**
```bash
# User just needs:
opencode run github.com/user/repo --command "python server.py"
```

- **No local storage**: Code runs in cloud/temporary environment
- **No dependency management**: Handled by OpenCode
- **Automatic updates**: Always uses latest code
- **Platform agnostic**: Works on any system with OpenCode CLI
- **Shared execution**: One deployment serves many users

### Use Cases

1. **Educational Tools**: Students can use tools without setup
2. **Quick Prototyping**: Test code without cloning repos
3. **CI/CD Integration**: Run code in pipelines without artifacts
4. **Multi-User Services**: One codebase, many users
5. **Version Management**: Always use latest code automatically

---

## Architecture Overview

### Traditional MCP Server Flow

```
┌─────────────┐
│  AI Agent   │
│  (Client)   │
└──────┬──────┘
       │
       │ 1. Configure local path
       │ 2. Download/clone repo
       │ 3. Install dependencies
       │ 4. Run server.py
       ▼
┌─────────────┐
│ Local MCP   │
│ Server      │
└─────────────┘
```

### OpenCode MCP Server Flow

```
┌─────────────┐
│  AI Agent   │
│  (Client)   │
└──────┬──────┘
       │
       │ 1. Call MCP tool with GitHub URL
       │ 2. MCP server calls OpenCode CLI
       ▼
┌─────────────┐         ┌──────────────┐
│  MCP Server │────────▶│  OpenCode    │
│  (Remote)   │         │  CLI/Service │
└─────────────┘         └──────┬───────┘
                                │
                                │ 3. Fetch from GitHub
                                │ 4. Create temp environment
                                │ 5. Execute code
                                │ 6. Return results
                                ▼
                        ┌──────────────┐
                        │  GitHub Repo │
                        │  (Remote)    │
                        └──────────────┘
```

---

## Building an OpenCode-Based MCP Server

### Step 1: Install OpenCode CLI

**Option A: Using npm (if OpenCode is an npm package)**
```bash
npm install -g opencode-cli
```

**Option B: Using pip (if OpenCode is a Python package)**
```bash
pip install opencode-cli
```

**Option C: Direct Download**
```bash
# Download binary from releases
curl -L https://github.com/opencode/cli/releases/latest/download/opencode -o /usr/local/bin/opencode
chmod +x /usr/local/bin/opencode
```

**Verify Installation:**
```bash
opencode --version
```

### Step 2: Create MCP Server with OpenCode Integration

```python
#!/usr/bin/env python3
"""
OpenCode MCP Server
Executes code from GitHub repositories without downloading
"""

import asyncio
import json
import subprocess
from pathlib import Path
from typing import Any, Sequence, Optional
from urllib.parse import urlparse

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Initialize MCP server
app = Server("opencode-mcp")

# OpenCode CLI path (adjust if needed)
OPENCODE_CLI = "opencode"  # or full path: "/usr/local/bin/opencode"


def parse_github_url(url: str) -> dict:
    """Parse GitHub URL into components"""
    # Support formats:
    # - https://github.com/user/repo
    # - https://github.com/user/repo/tree/branch
    # - https://github.com/user/repo/blob/branch/path/to/file
    # - github.com/user/repo
    # - user/repo
    
    if not url.startswith("http"):
        if "/" in url and not url.startswith("github.com"):
            # Assume user/repo format
            url = f"https://github.com/{url}"
        elif url.startswith("github.com"):
            url = f"https://{url}"
    
    parsed = urlparse(url)
    path_parts = [p for p in parsed.path.split("/") if p]
    
    if len(path_parts) < 2:
        raise ValueError(f"Invalid GitHub URL: {url}")
    
    repo = {
        "owner": path_parts[0],
        "repo": path_parts[1],
        "branch": "main",  # default
        "path": None
    }
    
    # Extract branch if present
    if len(path_parts) > 2:
        if path_parts[2] in ["tree", "blob"]:
            if len(path_parts) > 3:
                repo["branch"] = path_parts[3]
            if path_parts[2] == "blob" and len(path_parts) > 4:
                repo["path"] = "/".join(path_parts[4:])
    
    return repo


async def run_opencode_command(
    repo_url: str,
    command: str,
    args: Optional[list] = None,
    env: Optional[dict] = None
) -> dict:
    """
    Execute a command in a GitHub repository using OpenCode
    
    Args:
        repo_url: GitHub repository URL or user/repo format
        command: Command to execute (e.g., "python", "node", "bash")
        args: Additional arguments for the command
        env: Environment variables
    
    Returns:
        Dictionary with stdout, stderr, returncode
    """
    # Parse GitHub URL
    repo_info = parse_github_url(repo_url)
    repo_identifier = f"{repo_info['owner']}/{repo_info['repo']}"
    
    # Build OpenCode command
    opencode_cmd = [
        OPENCODE_CLI,
        "run",
        repo_identifier,
        "--command", command
    ]
    
    # Add branch if specified
    if repo_info["branch"] != "main":
        opencode_cmd.extend(["--branch", repo_info["branch"]])
    
    # Add path if specified
    if repo_info["path"]:
        opencode_cmd.extend(["--path", repo_info["path"]])
    
    # Add command arguments
    if args:
        opencode_cmd.extend(args)
    
    # Prepare environment
    process_env = None
    if env:
        process_env = {**os.environ, **env}
    
    # Execute command
    try:
        process = await asyncio.create_subprocess_exec(
            *opencode_cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=process_env
        )
        
        stdout, stderr = await process.communicate()
        
        return {
            "status": "success" if process.returncode == 0 else "error",
            "returncode": process.returncode,
            "stdout": stdout.decode("utf-8", errors="replace"),
            "stderr": stderr.decode("utf-8", errors="replace"),
            "command": " ".join(opencode_cmd)
        }
    
    except FileNotFoundError:
        return {
            "status": "error",
            "error": f"OpenCode CLI not found. Install it first: pip install opencode-cli",
            "command": " ".join(opencode_cmd)
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "command": " ".join(opencode_cmd)
        }


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools"""
    return [
        Tool(
            name="run_github_script",
            description="Execute a script from a GitHub repository without downloading it. Supports Python, Node.js, Bash, and other languages.",
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_url": {
                        "type": "string",
                        "description": "GitHub repository URL (e.g., 'https://github.com/user/repo' or 'user/repo') or path to file in repo"
                    },
                    "script_path": {
                        "type": "string",
                        "description": "Path to script file within repository (e.g., 'scripts/process.py' or 'src/main.js')"
                    },
                    "command": {
                        "type": "string",
                        "description": "Command to run (e.g., 'python', 'node', 'bash'). Auto-detected from file extension if not provided."
                    },
                    "args": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Additional arguments to pass to the script"
                    },
                    "branch": {
                        "type": "string",
                        "description": "Git branch to use (default: 'main')"
                    },
                    "env": {
                        "type": "object",
                        "description": "Environment variables as key-value pairs"
                    }
                },
                "required": ["repo_url", "script_path"]
            }
        ),
        Tool(
            name="run_github_command",
            description="Execute any command in a GitHub repository context without downloading. Useful for running CLI tools, tests, or build scripts.",
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_url": {
                        "type": "string",
                        "description": "GitHub repository URL (e.g., 'https://github.com/user/repo' or 'user/repo')"
                    },
                    "command": {
                        "type": "string",
                        "description": "Command to execute (e.g., 'python server.py', 'npm test', 'make build')"
                    },
                    "branch": {
                        "type": "string",
                        "description": "Git branch to use (default: 'main')"
                    },
                    "working_dir": {
                        "type": "string",
                        "description": "Working directory within repository (default: repository root)"
                    },
                    "env": {
                        "type": "object",
                        "description": "Environment variables as key-value pairs"
                    }
                },
                "required": ["repo_url", "command"]
            }
        ),
        Tool(
            name="list_github_files",
            description="List files in a GitHub repository without downloading it. Useful for discovering available scripts or tools.",
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_url": {
                        "type": "string",
                        "description": "GitHub repository URL (e.g., 'https://github.com/user/repo' or 'user/repo')"
                    },
                    "path": {
                        "type": "string",
                        "description": "Directory path within repository (default: root)"
                    },
                    "branch": {
                        "type": "string",
                        "description": "Git branch to use (default: 'main')"
                    },
                    "pattern": {
                        "type": "string",
                        "description": "File pattern to match (e.g., '*.py', 'scripts/*')"
                    }
                },
                "required": ["repo_url"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
    """Handle tool calls"""
    
    try:
        if name == "run_github_script":
            repo_url = arguments["repo_url"]
            script_path = arguments["script_path"]
            command = arguments.get("command")
            args = arguments.get("args", [])
            branch = arguments.get("branch")
            env = arguments.get("env")
            
            # Auto-detect command from file extension
            if not command:
                if script_path.endswith(".py"):
                    command = "python"
                elif script_path.endswith(".js"):
                    command = "node"
                elif script_path.endswith(".sh") or script_path.endswith(".bash"):
                    command = "bash"
                elif script_path.endswith(".ts"):
                    command = "ts-node"
                else:
                    command = "bash"  # default
            
            # Build full command
            full_command = f"{command} {script_path}"
            if args:
                full_command += " " + " ".join(args)
            
            # Construct full repo URL with path if needed
            if branch:
                repo_url = f"{repo_url}/tree/{branch}"
            
            result = await run_opencode_command(
                repo_url,
                command,
                args=[script_path] + args,
                env=env
            )
            
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "run_github_command":
            repo_url = arguments["repo_url"]
            command = arguments["command"]
            branch = arguments.get("branch")
            working_dir = arguments.get("working_dir")
            env = arguments.get("env")
            
            # Parse command into executable and args
            parts = command.split()
            cmd_executable = parts[0]
            cmd_args = parts[1:] if len(parts) > 1 else []
            
            # Add working directory to repo URL if specified
            if working_dir:
                if not repo_url.endswith("/"):
                    repo_url += "/"
                repo_url += f"tree/{branch or 'main'}/{working_dir}"
            elif branch:
                repo_url = f"{repo_url}/tree/{branch}"
            
            result = await run_opencode_command(
                repo_url,
                cmd_executable,
                args=cmd_args,
                env=env
            )
            
            return [TextContent(type="text", text=json.dumps(result, indent=2))]
        
        elif name == "list_github_files":
            repo_url = arguments["repo_url"]
            path = arguments.get("path", "")
            branch = arguments.get("branch")
            pattern = arguments.get("pattern")
            
            # Use OpenCode to list files
            repo_info = parse_github_url(repo_url)
            repo_identifier = f"{repo_info['owner']}/{repo_info['repo']}"
            
            opencode_cmd = [
                OPENCODE_CLI,
                "list",
                repo_identifier,
            ]
            
            if branch:
                opencode_cmd.extend(["--branch", branch])
            if path:
                opencode_cmd.extend(["--path", path])
            if pattern:
                opencode_cmd.extend(["--pattern", pattern])
            
            try:
                process = await asyncio.create_subprocess_exec(
                    *opencode_cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )
                
                stdout, stderr = await process.communicate()
                
                result = {
                    "status": "success" if process.returncode == 0 else "error",
                    "returncode": process.returncode,
                    "files": stdout.decode("utf-8").strip().split("\n") if stdout else [],
                    "error": stderr.decode("utf-8") if stderr else None
                }
                
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            except Exception as e:
                error_result = {
                    "status": "error",
                    "error": str(e)
                }
                return [TextContent(type="text", text=json.dumps(error_result, indent=2))]
        
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
    import os
    asyncio.run(main())
```

### Step 3: Create requirements.txt

```txt
mcp>=0.9.0
aiofiles>=23.0.0
```

### Step 4: Alternative Implementation (If OpenCode Doesn't Exist)

If OpenCode is not a real tool, you can create a similar service using:

**Option A: GitHub API + Temporary Execution**
```python
import requests
import tempfile
import subprocess
import shutil

async def run_github_code_via_api(repo_url: str, script_path: str, command: str):
    """Fetch code from GitHub API and execute in temp directory"""
    
    # Parse repo URL
    repo_info = parse_github_url(repo_url)
    
    # Fetch file content via GitHub API
    api_url = f"https://api.github.com/repos/{repo_info['owner']}/{repo_info['repo']}/contents/{script_path}"
    response = requests.get(api_url)
    content = base64.b64decode(response.json()["content"]).decode("utf-8")
    
    # Create temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        script_file = Path(tmpdir) / Path(script_path).name
        script_file.write_text(content)
        
        # Execute command
        result = subprocess.run(
            [command, str(script_file)],
            capture_output=True,
            text=True,
            cwd=tmpdir
        )
        
        return {
            "status": "success" if result.returncode == 0 else "error",
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
```

**Option B: Use GitHub Codespaces API**
```python
# Use GitHub Codespaces to create temporary environment
# Execute code in cloud environment
# Return results via API
```

**Option C: Use Replit-like Service**
```python
# Use Replit API or similar service
# Create temporary repl
# Execute code
# Get results
```

---

## Example Implementation

### Example 1: Running a Python Script from GitHub

**User Request:**
```
Run the script scripts/process.py from github.com/user/repo
```

**MCP Tool Call:**
```json
{
  "name": "run_github_script",
  "arguments": {
    "repo_url": "github.com/user/repo",
    "script_path": "scripts/process.py",
    "args": ["--input", "data.txt"]
  }
}
```

**What Happens:**
1. MCP server parses GitHub URL
2. Calls OpenCode CLI: `opencode run user/repo --command python scripts/process.py --input data.txt`
3. OpenCode fetches code from GitHub
4. Creates temporary environment
5. Executes script
6. Returns output

**Response:**
```json
{
  "status": "success",
  "returncode": 0,
  "stdout": "Processing data...\nDone!",
  "stderr": "",
  "command": "opencode run user/repo --command python scripts/process.py --input data.txt"
}
```

### Example 2: Running MCP Server from GitHub

**Use Case:** Run Task 3.1 MCP server without downloading

**User Request:**
```
Use the MCP server from github.com/tesolchina/mccpSpring2026 in the MCP/task3.1 folder
```

**MCP Tool Call:**
```json
{
  "name": "run_github_command",
  "arguments": {
    "repo_url": "github.com/tesolchina/mccpSpring2026",
    "command": "python server.py",
    "working_dir": "MCP/task3.1"
  }
}
```

**What Happens:**
1. OpenCode fetches `MCP/task3.1/` from GitHub
2. Installs dependencies from `requirements.txt`
3. Runs `python server.py`
4. MCP server starts and is accessible

### Example 3: Discovering Available Scripts

**User Request:**
```
What scripts are available in github.com/user/repo?
```

**MCP Tool Call:**
```json
{
  "name": "list_github_files",
  "arguments": {
    "repo_url": "github.com/user/repo",
    "pattern": "*.py"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "files": [
    "scripts/process.py",
    "scripts/analyze.py",
    "src/main.py"
  ]
}
```

---

## Deployment and Configuration

### Local Setup

1. **Install OpenCode CLI:**
   ```bash
   pip install opencode-cli
   # or
   npm install -g opencode-cli
   ```

2. **Install MCP Server:**
   ```bash
   cd MCP/AgentReadme
   pip install -r requirements.txt
   ```

3. **Configure Cursor:**
   ```json
   {
     "mcpServers": {
       "opencode-mcp": {
         "command": "python",
         "args": ["/path/to/opencode_mcp_server.py"]
       }
     }
   }
   ```

### Remote Deployment

Deploy the MCP server to a cloud service (Heroku, Railway, etc.) so users can access it without local installation.

**See `howtoBuildMCP.md` for remote server setup.**

---

## Best Practices

### 1. Error Handling

```python
try:
    result = await run_opencode_command(...)
    if result["status"] == "error":
        # Handle OpenCode errors
        return error_response(result["error"])
except FileNotFoundError:
    return error_response("OpenCode CLI not installed")
except Exception as e:
    return error_response(f"Unexpected error: {e}")
```

### 2. Security Considerations

- **Validate GitHub URLs**: Ensure they point to trusted repositories
- **Sandbox Execution**: OpenCode should run in isolated environments
- **Timeout Limits**: Set timeouts for long-running commands
- **Resource Limits**: Limit CPU, memory, disk usage

### 3. Caching

```python
# Cache frequently accessed repositories
from functools import lru_cache

@lru_cache(maxsize=100)
async def get_repo_info(repo_url: str):
    # Cache repository metadata
    pass
```

### 4. Logging

```python
import logging

logger = logging.getLogger("opencode-mcp")

async def run_opencode_command(...):
    logger.info(f"Executing: {command} in {repo_url}")
    # ... execution
    logger.info(f"Result: {result['status']}")
```

---

## Troubleshooting

### OpenCode CLI Not Found

**Error:** `FileNotFoundError: opencode command not found`

**Solution:**
```bash
# Install OpenCode CLI
pip install opencode-cli

# Verify installation
opencode --version

# Update MCP server to use full path
OPENCODE_CLI = "/usr/local/bin/opencode"
```

### GitHub Repository Not Found

**Error:** `Repository not found`

**Solution:**
- Check repository URL format
- Verify repository is public (or provide authentication)
- Check branch name exists

### Execution Timeout

**Error:** `Command timed out`

**Solution:**
- Add timeout parameter to OpenCode command
- Break down long-running tasks into smaller steps
- Use async execution with progress updates

### Permission Denied

**Error:** `Permission denied`

**Solution:**
- Check file permissions in repository
- Ensure script is executable
- Verify OpenCode has necessary permissions

---

## Summary

### Key Benefits

1. **No Local Installation**: Users don't need to clone repos
2. **Always Up-to-Date**: Always uses latest code from GitHub
3. **Isolated Execution**: Code runs in temporary, isolated environments
4. **Easy Sharing**: Just share GitHub URL, not code files
5. **Multi-User**: One codebase serves many users

### When to Use

- ✅ Educational tools and demos
- ✅ Quick prototyping and testing
- ✅ CI/CD pipelines
- ✅ Multi-user services
- ✅ Version-agnostic tools

### When NOT to Use

- ❌ Sensitive data processing (use local execution)
- ❌ Offline requirements
- ❌ Custom local configurations
- ❌ Long-running persistent services

---

## Resources

- **OpenCode Documentation**: (Add link when available)
- **GitHub API**: https://docs.github.com/en/rest
- **MCP Specification**: https://modelcontextprotocol.io
- **Example Implementation**: See `opencode_mcp_server.py` in this directory

---

**Last Updated**: 2026-01-27  
**Version**: 1.0
