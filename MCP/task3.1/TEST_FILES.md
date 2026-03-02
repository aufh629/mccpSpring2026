# Test Files Available

## Included Test Files

The following test files are included in the MCP folder for easy testing:

### 1. Test Archive File

**File**: `test_paper.tar.gz` (32 KB)

**Contents**: "Adaptive Parameter Selection for Kernel Ridge Regression" paper in LaTeX format

**Location**: Same folder as `server.py`

**Quick Test Command**:
```
Extract and visualize the paper structure from:
test_paper.tar.gz
```

### 2. Test arXiv Link

**File**: `test_arxiv_link.txt`

**Contents**: https://arxiv.org/abs/2412.20379

**Quick Test Command**:
```
Do task 3.1 for this paper:
https://arxiv.org/abs/2412.20379
```

### 3. Test Archive Path (Original Location)

**File**: `test_archive_path.txt`

**Contents**: Path to original archive location (for reference)

## Quick Test Commands

Copy and paste these into your IDE's AI chat:

### Test 1: Local Archive (Easiest)
```
Extract and visualize the paper structure from:
test_paper.tar.gz
```

### Test 2: arXiv Link
```
Do task 3.1 for this paper:
https://arxiv.org/abs/2412.20379
```

### Test 3: Complete Workflow
```
Do task 3.1 for this paper:
https://arxiv.org/abs/2412.20379

First generate hierarchical visualization, then create an interconnected network version.
```

## File Locations

All test files are in the same directory as `server.py`:

```
MCP/task3.1/
├── test_paper.tar.gz          # ✅ Ready to use!
├── test_arxiv_link.txt         # Quick reference
├── test_archive_path.txt       # Original location reference
└── TEST_EXAMPLE.md             # Detailed test instructions
```

## Verification

To verify the test file exists:

```bash
cd MCP/task3.1
ls -lh test_paper.tar.gz
```

You should see:
```
-rwx------@ 1 user  staff    32K Jan 27 18:41 test_paper.tar.gz
```

---

**Last Updated**: 2026-01-26
