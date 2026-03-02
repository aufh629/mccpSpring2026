# MCP Server for Task 3.1: Paper Structure Visualization

This MCP (Model Context Protocol) server automates the process of extracting, parsing, and visualizing academic paper structures for Task 3.1.

## Features

- **Extract Archives**: Automatically unzip tar.gz and zip files
- **Parse Papers**: Extract structure from LaTeX, PDF, or Markdown files
- **Generate Visualizations**: Create hierarchical and interconnected HTML visualizations
- **Moodle-Compatible**: Output HTML files ready for Moodle Forum sharing

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download

If sharing via GitHub:
```bash
git clone <repository-url>
cd MCP/task3.1
```

Or download and extract the folder to your desired location.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Make Server Executable (Optional)

```bash
chmod +x server.py
```

## Important: Supported File Formats

**✅ Supported Input Formats:**
- **LaTeX files** (`.tex`) - Preferred format
- **HTML files** (`.html`, `.htm`)
- **Markdown files** (`.md`)
- **arXiv links** (e.g., `https://arxiv.org/abs/1234.5678` or `https://arxiv.org/pdf/1234.5678.pdf`)

**❌ NOT Supported:**
- **PDF files** (`.pdf`) - Please use LaTeX source or HTML version instead

## IDE Setup and MCP Installation

**⚠️ Important**: MCP support varies by IDE. Some IDEs have built-in MCP support, while others require extensions.

**See [IDE_SETUP.md](IDE_SETUP.md) for detailed setup instructions for:**
- ✅ **Cursor IDE** (Built-in MCP support - Recommended)
- ⚠️ **VS Code** (May require MCP extension)
- ⚠️ **JetBrains IDEs** (Limited support)
- ⚠️ **Other IDEs** (May not support MCP)

### Quick Setup for Cursor (Recommended)

1. **Open Cursor Settings** (`Cmd+,` or `Ctrl+,`)
2. **Go to**: Features → MCP Servers
3. **Add configuration**:
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
4. **Restart Cursor**
5. **Test**: Ask AI agent to visualize a paper

**For other IDEs and detailed instructions, see [IDE_SETUP.md](IDE_SETUP.md)**

## Local Usage Examples

### Example 1: Using arXiv Link (Recommended for Testing)

**Quick Test**: See `TEST_EXAMPLE.md` for a ready-to-use test case with arXiv paper 2412.20379.

**Ask AI agent:**
```
Do task 3.1 for this paper:
https://arxiv.org/abs/2412.20379
```

Or:
```
Extract and visualize the paper structure from:
https://arxiv.org/abs/2412.20379
```

The AI agent will:
1. Fetch the LaTeX source from arXiv
2. Parse the structure
3. Generate `visual.html`

### Example 2: Using Zipped LaTeX Archive (Local Test File)

**✅ Test file included!** A test archive `test_paper.tar.gz` is included in the MCP folder.

**Ask AI agent:**
```
Extract and visualize the paper structure from:
test_paper.tar.gz
```

Or with relative path:
```
Extract and visualize the paper structure from:
MCP/task3.1/test_paper.tar.gz
```

The AI agent will:
1. Extract the archive (tar.gz or zip)
2. Find the LaTeX source file (.tex) inside
3. Parse the structure
4. Generate `visual.html`

**Supported archives**: `.tar.gz`, `.zip` containing LaTeX/HTML/Markdown files

**Note**: The test file `test_paper.tar.gz` contains the paper "Adaptive Parameter Selection for Kernel Ridge Regression" and is ready to use for testing.

### Example 3: Using Local LaTeX File

**Ask AI agent:**
```
Parse and visualize the paper structure from:
/path/to/paper.tex
```

### Example 4: Using HTML File

**Ask AI agent:**
```
Parse and visualize the paper structure from:
/path/to/paper.html
```

### Example 5: Complete Workflow

**Ask AI agent:**
```
Do task 3.1 for this paper:
https://arxiv.org/abs/2412.20379

First generate hierarchical visualization, then create an interconnected network version.
```

**See TEST_EXAMPLE.md for more test cases including zipped archives.**

## Available Tools

Once connected, the AI agent can use these tools:

1. **`extract_archive`** - Extract tar.gz or zip files containing LaTeX/HTML sources
2. **`read_paper_file`** - Read LaTeX (.tex), HTML (.html), or Markdown (.md) files (PDF not supported)
3. **`fetch_arxiv_paper`** - Download paper from arXiv (gets LaTeX source or HTML)
4. **`parse_paper_structure`** - Parse paper and extract hierarchical structure
5. **`analyze_section_interconnections`** - Analyze relationships between sections
6. **`generate_hierarchical_html`** - Generate hierarchical HTML visualization
7. **`generate_interconnected_html`** - Generate network HTML visualization
8. **`create_visualization_task`** - Complete workflow (extract → parse → visualize)

## Example Usage

### Example 1: Using arXiv Link (Recommended)

**Student to AI Agent:**
```
Do task 3.1 for this paper:
https://arxiv.org/abs/2312.05885
```

**AI Agent will:**
1. Fetch LaTeX source from arXiv
2. Parse the paper structure
3. Generate `visual.html` with hierarchical structure
4. Return the file path

### Example 2: Using Local LaTeX File

**Student to AI Agent:**
```
Extract and visualize the paper from:
PhDagentSpring2026/literature/KPY*/25480332_Adaptive Parameter Selection for Kernel Ridge Regression.tar.gz
```

**AI Agent will:**
1. Extract the archive
2. Find and parse the LaTeX file (.tex)
3. Generate `visual.html` with hierarchical structure
4. Return the file path

### Example 3: Refinement Workflow

**Student to AI Agent:**
```
Now generate an interconnected visualization showing relationships between sections
```

**AI Agent will:**
1. Analyze section interconnections
2. Generate `visual_interconnection_text.html` with network diagram
3. Return the interactive visualization

### Example 4: Using HTML File

**Student to AI Agent:**
```
Parse and visualize the structure from:
/path/to/paper.html
```

**AI Agent will:**
1. Read the HTML file
2. Parse structure from HTML headings
3. Generate visualization

## Sharing with Others

### Method 1: GitHub Repository (Recommended)

1. **Create a GitHub Repository**
   ```bash
   cd MCP/task3.1
   git init
   git add .
   git commit -m "Initial MCP server for Task 3.1"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Share Repository Link**
   - Others can clone: `git clone <repo-url>`
   - Follow installation steps above

### Method 2: Zip File Distribution

1. **Create Zip File**
   ```bash
   cd MCP
   zip -r task3.1-mcp.zip task3.1/
   ```

2. **Share Zip File**
   - Upload to cloud storage (Google Drive, Dropbox, etc.)
   - Share download link
   - Recipients extract and follow installation steps

### Method 3: Direct Folder Sharing

1. **Copy Folder**
   - Copy the entire `task3.1` folder
   - Share via USB, network drive, or cloud sync

2. **Recipients**
   - Place folder in their project directory
   - Follow installation steps
   - Update MCP configuration with their local path

## Configuration for Recipients

When sharing, recipients need to:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Update MCP configuration** with their local path:
   ```json
   {
     "mcpServers": {
       "task3.1-visualizer": {
         "command": "python",
         "args": ["/their/absolute/path/to/task3.1/server.py"]
       }
     }
   }
   ```

3. **Restart their IDE**

## Submitting Work to Moodle Forum

After generating your HTML visualizations, you need to:

1. **Commit and push to GitHub**
2. **Get a shareable link to your HTML files**
3. **Reply to the Moodle forum post** with the link

### Step 1: Commit and Push HTML Files to GitHub

**Option A: If HTML files are in your repository folder:**

```bash
# Navigate to your repository
cd /path/to/your/repo

# Add the HTML files
git add visual.html visual_interconnection_text.html

# Commit with a message
git commit -m "Task 3.1: Add paper structure visualizations"

# Push to GitHub
git push origin main
```

**Option B: If HTML files are in a different location:**

```bash
# Copy HTML files to your repository
cp /path/to/visual.html /path/to/your/repo/
cp /path/to/visual_interconnection_text.html /path/to/your/repo/

# Then commit and push (same as Option A)
git add visual.html visual_interconnection_text.html
git commit -m "Task 3.1: Add paper structure visualizations"
git push origin main
```

### Step 2: Get Shareable Link to HTML Files

You have several options to share your HTML files:

#### Option 1: GitHub Raw Link (Simple, but requires GitHub account to view)

1. Go to your GitHub repository
2. Navigate to the HTML file (e.g., `visual.html`)
3. Click "Raw" button
4. Copy the URL (format: `https://raw.githubusercontent.com/username/repo/branch/visual.html`)
5. Use this URL directly in Moodle

**Note**: Some browsers may download the file instead of displaying it. For better viewing, use Option 2 or 3.

#### Option 2: GitHub Pages (Recommended - Best viewing experience)

1. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Click "Settings" → "Pages"
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click "Save"

2. **Wait 1-2 minutes** for GitHub Pages to deploy

3. **Get your GitHub Pages URL:**
   - Format: `https://username.github.io/repo-name/visual.html`
   - Or: `https://username.github.io/repo-name/visual_interconnection_text.html`

4. **Test the link** - it should display your HTML visualization directly in the browser

#### Option 3: Use HTML Preview Services

If you don't want to use GitHub Pages, you can use:

- **HTMLPreview**: `https://htmlpreview.github.io/?https://raw.githubusercontent.com/username/repo/branch/visual.html`
- **RawGit** (deprecated but still works): `https://raw.githack.com/username/repo/branch/visual.html`

### Step 3: Reply to Moodle Forum Post

1. **Go to the Moodle forum post:**
   - Navigate to: https://buelearning.hkbu.edu.hk/mod/forum/discuss.php?d=345204
   - (You may need to log in first)

2. **Click "Reply"** to the forum post

3. **In your reply, include:**
   - A brief description of your visualization
   - Links to your HTML files
   - Example format:

   ```
   Task 3.1 Submission
   
   I have generated two visualizations for the paper:
   
   1. Hierarchical Structure:
   [Link to visual.html]
   
   2. Interconnected Network:
   [Link to visual_interconnection_text.html]
   
   Both visualizations are available in my GitHub repository:
   [Link to your GitHub repo]
   ```

4. **For GitHub Pages links**, format like this:
   ```
   Hierarchical Structure: https://yourusername.github.io/repo-name/visual.html
   
   Interconnected Network: https://yourusername.github.io/repo-name/visual_interconnection_text.html
   ```

5. **Click "Post to forum"** to submit

### Quick Checklist

- [ ] HTML files generated (`visual.html` and/or `visual_interconnection_text.html`)
- [ ] Files committed to Git
- [ ] Changes pushed to GitHub
- [ ] GitHub Pages enabled (if using Option 2)
- [ ] Links tested in browser
- [ ] Reply posted to Moodle forum with links

### Troubleshooting Submission

**"Link doesn't work"**
- Check that files are pushed to GitHub
- Verify the file path in the URL is correct
- For GitHub Pages, wait a few minutes after enabling

**"HTML doesn't display properly"**
- Use GitHub Pages (Option 2) for best results
- Check that HTML files are valid
- Try opening the raw file directly in browser first

**"Can't find the Moodle post"**
- Make sure you're logged into HKBU Moodle
- Check that you have access to the course forum
- Contact instructor if you can't access the post

## Troubleshooting

### Server Not Found

- **Check path**: Ensure the absolute path in MCP config is correct
- **Check Python**: Verify `python` command works: `python --version`
- **Check permissions**: Ensure server.py is executable (optional)

### Import Errors

- **Install dependencies**: Run `pip install -r requirements.txt`
- **Check Python version**: Requires Python 3.8+

### File Not Found Errors

- **Use absolute paths**: When specifying paper files, use full paths
- **Check file permissions**: Ensure files are readable

### HTML Generation Issues

- **Check templates**: Ensure `templates/` folder exists with HTML files
- **Check output directory**: Ensure write permissions for output directory

## Project Structure

```
task3.1/
├── server.py                 # Main MCP server
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── tools/
│   ├── __init__.py
│   ├── file_tools.py        # Archive extraction, file reading
│   ├── paper_tools.py        # Paper parsing, structure analysis
│   └── visualization_tools.py  # HTML generation
└── templates/
    ├── hierarchical.html     # Hierarchical visualization template
    └── interconnected.html  # Network visualization template
```

## License

This MCP server is provided for educational purposes as part of the MCCP 6020 course.

## Support

For issues or questions:
1. Check this README
2. Review error messages in IDE console
3. Verify file paths and permissions
4. Contact course instructor

---

**Last Updated**: 2026-01-26
