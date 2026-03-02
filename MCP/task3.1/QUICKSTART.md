# Quick Start Guide

## 5-Minute Setup

### 1. Install (30 seconds)
```bash
cd MCP/task3.1
pip install -r requirements.txt
```

### 2. Configure Cursor (2 minutes)

**Note**: Cursor has built-in MCP support - no extension installation needed!

1. Open Cursor Settings (`Cmd+,` or `Ctrl+,`)
2. Go to "Features" → "MCP Servers"
3. Add this configuration:

```json
{
  "mcpServers": {
    "task3.1-visualizer": {
      "command": "python",
      "args": ["/FULL/PATH/TO/task3.1/server.py"]
    }
  }
}
```

**Get the full path:**
- Mac/Linux: Run `pwd` in the task3.1 folder
- Windows: Right-click folder → Properties → Copy path

**Example:**
```json
{
  "mcpServers": {
    "task3.1-visualizer": {
      "command": "python",
      "args": ["/Users/simonwang/Library/CloudStorage/OneDrive-HongKongBaptistUniversity/GTD/Areas/Teaching/Courses/MCCP 6020/PhDagentSpring2026/MCP/task3.1/server.py"]
    }
  }
}
```

### 3. Restart Cursor (30 seconds)
- Close Cursor completely
- Reopen Cursor

### 4. Test It (1 minute)

**Supported formats**: LaTeX (.tex), HTML (.html), Markdown (.md), or arXiv links
**NOT supported**: PDF files

**Quick Test**: Use the example in `TEST_EXAMPLE.md` or try:

In Cursor chat, try:
```
Do task 3.1 for this paper:
https://arxiv.org/abs/2412.20379
```

Or with the included test archive (recommended):
```
Extract and visualize the paper from:
test_paper.tar.gz
```

Or with original location:
```
Extract and visualize the paper from:
PhDagentSpring2026/literature/KPY*/25480332_Adaptive Parameter Selection for Kernel Ridge Regression.tar.gz
```

Or with a local file:
```
Extract and visualize the paper from:
/path/to/paper.tex
```

The AI agent should now use the MCP tools automatically!

**See TEST_EXAMPLE.md for multiple test cases including arXiv links and zipped archives.**

## Sharing with Others

### Option 1: GitHub (Best for Updates)
1. Create GitHub repo
2. Push this folder
3. Share repo link
4. Others: `git clone <repo>` then follow steps above

### Option 2: Zip File (Simple)
1. Zip the `task3.1` folder
2. Share zip file
3. Recipients: Extract, then follow steps above

### Option 3: Cloud Folder (OneDrive/Dropbox)
1. Share folder link
2. Recipients: Sync folder, then follow steps above

## Troubleshooting

**"Server not found"**
- Check the path in MCP config is absolute and correct
- Make sure Python is installed: `python --version`

**"Module not found"**
- Run: `pip install -r requirements.txt`

**"Permission denied"**
- Mac/Linux: `chmod +x server.py`

## Submitting to Moodle

After generating your HTML files:

1. **Commit and push to GitHub:**
   ```bash
   git add visual.html visual_interconnection_text.html
   git commit -m "Task 3.1: Add visualizations"
   git push origin main
   ```

2. **Enable GitHub Pages** (Settings → Pages → Deploy from main branch)

3. **Get your links:**
   - `https://yourusername.github.io/repo-name/visual.html`

4. **Reply to Moodle forum:**
   - https://buelearning.hkbu.edu.hk/mod/forum/discuss.php?d=345204
   - Post your GitHub Pages links

**See SUBMIT_TO_MOODLE.md for detailed instructions.**

## Other IDEs

**VS Code, JetBrains, etc.**: See [IDE_SETUP.md](IDE_SETUP.md) for detailed instructions
- Some IDEs require MCP extensions
- Cursor has the best built-in MCP support

## Need Help?

- **IDE setup**: See [IDE_SETUP.md](IDE_SETUP.md)
- **General setup**: See full README.md
- **Submission**: See SUBMIT_TO_MOODLE.md
