# IDE Setup Guide for MCP Server

This guide explains how to set up the MCP server in different IDEs. **MCP support is built into some IDEs, while others require installation of MCP extensions.**

## Important: Supported File Formats

**✅ Supported:**
- LaTeX files (`.tex`)
- HTML files (`.html`, `.htm`)
- Markdown files (`.md`)
- arXiv links (e.g., `https://arxiv.org/abs/1234.5678`)

**❌ NOT Supported:**
- PDF files (`.pdf`) - Please use LaTeX source or HTML version instead

## IDE-Specific Setup Instructions

### 1. Cursor IDE (Recommended - Built-in MCP Support)

**MCP Installation:** ✅ **Built-in** - No additional installation needed

#### Setup Steps:

1. **Open Cursor Settings**
   - **Mac**: Press `Cmd + ,` (Command + Comma)
   - **Windows/Linux**: Press `Ctrl + ,`

2. **Navigate to MCP Settings**
   - Click on **"Features"** in the left sidebar
   - Click on **"MCP Servers"** or search for "MCP"

3. **Add MCP Server Configuration**
   
   Click **"Add Server"** or **"Edit in settings.json"** and add:

   ```json
   {
     "mcpServers": {
       "task3.1-visualizer": {
         "command": "python",
         "args": ["/ABSOLUTE/PATH/TO/task3.1/server.py"]
       }
     }
   }
   ```

   **Get the absolute path:**
   - **Mac/Linux**: Open terminal in the `task3.1` folder and run: `pwd`
   - **Windows**: Right-click the `server.py` file → Properties → Copy the full path
   - **Example Mac path**: `/Users/yourname/path/to/PhDagentSpring2026/MCP/task3.1/server.py`
   - **Example Windows path**: `C:\Users\yourname\path\to\PhDagentSpring2026\MCP\task3.1\server.py`

4. **Verify Python Path** (if needed)
   
   If `python` doesn't work, use full path:
   ```json
   {
     "mcpServers": {
       "task3.1-visualizer": {
         "command": "/usr/bin/python3",
         "args": ["/ABSOLUTE/PATH/TO/task3.1/server.py"]
       }
     }
   }
   ```

5. **Restart Cursor**
   - Close Cursor completely
   - Reopen Cursor

6. **Test the Setup**
   
   In Cursor's AI chat, try:
   ```
   Extract and visualize the paper from:
   https://arxiv.org/abs/2312.05885
   ```
   
   The AI agent should automatically use the MCP tools.

---

### 2. VS Code (Requires MCP Extension)

**MCP Installation:** ⚠️ **Extension Required**

#### Step 1: Install MCP Extension

1. **Open VS Code Extensions**
   - Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac)
   - Search for **"MCP"** or **"Model Context Protocol"**

2. **Install Extension**
   - Look for official MCP extension (if available)
   - Or install: **"MCP Server Manager"** or similar
   - If no MCP extension exists, you may need to use Cursor or another IDE

#### Step 2: Configure MCP Server

1. **Open Settings**
   - Press `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)
   - Or: File → Preferences → Settings

2. **Add MCP Configuration**
   
   Search for "MCP" in settings, or edit `settings.json` directly:
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
   - Type "Preferences: Open User Settings (JSON)"
   
   Add to `settings.json`:
   ```json
   {
     "mcp.servers": {
       "task3.1-visualizer": {
         "command": "python",
         "args": ["/ABSOLUTE/PATH/TO/task3.1/server.py"]
       }
     }
   }
   ```

3. **Restart VS Code**

---

### 3. JetBrains IDEs (IntelliJ IDEA, PyCharm, etc.)

**MCP Installation:** ⚠️ **Plugin Required** (may not be available)

#### Option A: Use Built-in AI Assistant (if available)

1. **Check for AI Assistant**
   - Some JetBrains IDEs have built-in AI features
   - Check if MCP is supported in AI Assistant settings

2. **Configure if Available**
   - Settings → Tools → AI Assistant → MCP Servers
   - Add server configuration similar to Cursor

#### Option B: Use Terminal/Command Line

If MCP plugin is not available, you can still use the server via command line:

```bash
# Test the server directly
cd /path/to/task3.1
python server.py
```

Then use AI tools that support MCP protocol externally.

---

### 4. Other IDEs (Sublime Text, Vim, etc.)

**MCP Installation:** ⚠️ **May not be supported**

For IDEs without MCP support:

1. **Use Cursor or VS Code** (recommended)
2. **Use Command Line Interface** (see below)
3. **Wait for MCP plugin** to be developed for your IDE

---

## Command Line Testing (All IDEs)

You can test the MCP server works correctly from any terminal:

```bash
# Navigate to the server directory
cd /path/to/task3.1

# Test Python import
python -c "import mcp; print('MCP installed correctly')"

# Run server (will wait for MCP protocol messages)
python server.py
```

If the server starts without errors, it's working correctly.

---

## Verification Checklist

After setup, verify:

- [ ] Python is installed: `python --version` (should be 3.8+)
- [ ] Dependencies installed: `pip install -r requirements.txt` completed
- [ ] MCP server path is correct (absolute path, not relative)
- [ ] IDE restarted after configuration
- [ ] AI agent can see MCP tools (test with a simple request)

---

## Troubleshooting

### "MCP Server not found"

**Solutions:**
- Check the absolute path is correct (no typos)
- Verify `server.py` exists at that path
- Try using full Python path: `/usr/bin/python3` instead of `python`

### "Module 'mcp' not found"

**Solutions:**
- Install dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.8+)
- Try: `python3` instead of `python` in config

### "IDE doesn't have MCP support"

**Solutions:**
- Use **Cursor IDE** (best MCP support)
- Use **VS Code** with MCP extension (if available)
- Use command line interface
- Contact instructor for alternatives

### "AI agent doesn't use MCP tools"

**Solutions:**
- Verify MCP server is running (check IDE console/logs)
- Restart IDE completely
- Check MCP configuration syntax (valid JSON)
- Test with simple request first

---

## Quick Reference: Configuration Template

**For Cursor:**
```json
{
  "mcpServers": {
    "task3.1-visualizer": {
      "command": "python",
      "args": ["/FULL/ABSOLUTE/PATH/TO/task3.1/server.py"]
    }
  }
}
```

**For VS Code:**
```json
{
  "mcp.servers": {
    "task3.1-visualizer": {
      "command": "python",
      "args": ["/FULL/ABSOLUTE/PATH/TO/task3.1/server.py"]
    }
  }
}
```

**Replace `/FULL/ABSOLUTE/PATH/TO/` with your actual path!**

---

## Need Help?

1. Check this guide first
2. Review README.md for general setup
3. Check IDE-specific documentation
4. Contact course instructor

---

**Last Updated**: 2026-01-26
