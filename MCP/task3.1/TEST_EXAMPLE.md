# Test Examples for MCP Server

This file provides multiple test examples for the MCP server, showing different input formats.

## Example 1: arXiv Link (Recommended)

Use this arXiv link to test the MCP server:

**Paper**: NeutronTP: Load-Balanced Distributed Full-Graph GNN Training with Tensor Parallelism

**arXiv Link**: https://arxiv.org/abs/2412.20379

## How to Test

### Step 1: Open Your IDE (Cursor recommended)

### Step 2: In the AI Chat, try one of these commands:

#### Option A: Complete Workflow
```
Do task 3.1 for this paper:
https://arxiv.org/abs/2412.20379
```

#### Option B: Step-by-Step
```
Fetch and visualize the paper structure from:
https://arxiv.org/abs/2412.20379
```

#### Option C: Detailed Request
```
Extract and visualize the paper structure from:
https://arxiv.org/abs/2412.20379

First generate a hierarchical visualization, then create an interconnected network version showing relationships between sections.
```

### Step 3: Expected Results

The AI agent should:
1. ✅ Use `fetch_arxiv_paper` tool to download the paper
2. ✅ Use `parse_paper_structure` tool to extract structure
3. ✅ Generate `visual.html` with hierarchical structure
4. ✅ Optionally generate `visual_interconnection_text.html` with network visualization

### Step 4: Verify Output

Check that these files are created:
- `visual.html` - Hierarchical structure visualization
- `visual_interconnection_text.html` - Interactive network visualization (if requested)

---

## Input Format Summary

The MCP server supports multiple input formats:

| Format | Example | Tool Used |
|--------|---------|-----------|
| **arXiv Link** | `https://arxiv.org/abs/2412.20379` | `fetch_arxiv_paper` |
| **Zipped Archive** | `paper.tar.gz` or `paper.zip` | `extract_archive` |
| **LaTeX File** | `/path/to/paper.tex` | `read_paper_file` + `parse_paper_structure` |
| **HTML File** | `/path/to/paper.html` | `read_paper_file` + `parse_paper_structure` |
| **Markdown File** | `/path/to/paper.md` | `read_paper_file` + `parse_paper_structure` |

**Note**: PDF files are NOT supported. Use LaTeX source or HTML version instead.

## Troubleshooting

### "Tool not found" or "MCP server not available"
- Check that MCP server is configured in your IDE (see IDE_SETUP.md)
- Restart your IDE
- Verify the server path is correct

### "Failed to fetch from arXiv"
- Check internet connection
- Verify the arXiv link is accessible
- Try again (arXiv may be temporarily unavailable)

### "PDF not supported" error
- This should NOT happen with arXiv links (we fetch LaTeX/HTML)
- If you see this, the MCP server may need updating

## Paper Information

**Title**: NeutronTP: Load-Balanced Distributed Full-Graph GNN Training with Tensor Parallelism

**Authors**: Xin Ai, Hao Yuan, Zeyu Ling, Qiange Wang, Yanfeng Zhang, Zhenbo Fu, Chaoyi Chen, Yu Gu, Ge Yu

**arXiv ID**: 2412.20379

**Subjects**: Distributed, Parallel, and Cluster Computing (cs.DC)

**Publication**: VLDB 2025

**Abstract**: Graph neural networks (GNNs) have emerged as a promising direction. Training large-scale graphs that relies on distributed computing power poses new challenges. Existing distributed GNN systems leverage data parallelism by partitioning the input graph and distributing it to multiple workers. However, due to the irregular nature of the graph structure, existing distributed approaches suffer from unbalanced workloads and high overhead in managing cross-worker vertex dependencies. In this paper, we leverage tensor parallelism for distributed GNN training...

## Example 2: Zipped LaTeX Archive (Local Test File)

**✅ Test file included in MCP folder!**

A test archive file is included in the MCP folder for easy testing:

**File**: `test_paper.tar.gz` (located in the same folder as `server.py`)

### Test Command (Recommended - Using Local File):

If you're in the MCP/task3.1 folder:
```
Extract and visualize the paper structure from:
test_paper.tar.gz
```

Or with relative path from project root:
```
Extract and visualize the paper structure from:
MCP/task3.1/test_paper.tar.gz
```

Or with full absolute path:
```
Extract and visualize the paper structure from:
/absolute/path/to/MCP/task3.1/test_paper.tar.gz
```

### Alternative: Using Original Location

You can also test with the original file location:

**Path**: `PhDagentSpring2026/literature/KPY*/25480332_Adaptive Parameter Selection for Kernel Ridge Regression.tar.gz`

```
Extract and visualize the paper structure from:
PhDagentSpring2026/literature/KPY*/25480332_Adaptive Parameter Selection for Kernel Ridge Regression.tar.gz
```

### What Happens:

1. ✅ MCP tool `extract_archive` extracts the tar.gz file
2. ✅ Finds the LaTeX source file (.tex) inside
3. ✅ Parses the paper structure
4. ✅ Generates `visual.html` visualization

### Supported Archive Formats:

- **tar.gz** files (`.tar.gz`)
- **zip** files (`.zip`)

The archive should contain:
- LaTeX source files (`.tex`) - **Preferred**
- HTML files (`.html`) - Also supported
- Markdown files (`.md`) - Also supported

**Note**: PDF files in archives are NOT supported. The MCP server will look for LaTeX/HTML/Markdown files first.

## Example 3: Direct LaTeX File

If you have a LaTeX file directly (not in an archive):

```
Parse and visualize the paper structure from:
/path/to/paper.tex
```

## Example 4: Direct HTML File

If you have an HTML file:

```
Parse and visualize the paper structure from:
/path/to/paper.html
```

## Alternative Test Papers

You can also test with other arXiv papers:

- **Machine Learning**: https://arxiv.org/abs/2312.05885
- **Computer Vision**: https://arxiv.org/abs/2308.04079
- **NLP**: https://arxiv.org/abs/2508.02929

Just replace the URL in the test commands above!

---

**Last Updated**: 2026-01-26
