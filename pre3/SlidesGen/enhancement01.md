# Enhancement 01: Enhanced Diagram Editor

**File:** `editableImageEnhance01.html`
**Base:** `editableImage.html`

## New Features

### 1. Resize Components
- Click any rectangle to see **8 resize handles** (corners + midpoints)
- Drag handles to resize width/height interactively
- Minimum size enforced (8px) to prevent collapse
- Width/Height fields in properties panel for precise numeric entry

### 2. Undo / Redo
- **Ctrl+Z** to undo, **Ctrl+Y** to redo
- Up to 40 undo states stored
- Toolbar buttons with disabled state when stack is empty

### 3. Delete Element
- Select any element and press **Delete** or **Backspace**
- Also available via toolbar button

### 4. Duplicate Element
- **Ctrl+D** duplicates the selected element (offset by 10px)
- Works for text, rects, and groups

### 5. Add New Elements
- **T** button: click on canvas to add a new text element
- **Rectangle** button: click on canvas to add a new styled rectangle
- Press Escape to cancel add mode

### 6. Zoom Controls
- **+** / **-** buttons to zoom in/out
- **Fit** button to reset to 100%
- **Ctrl+Scroll** for smooth zoom
- Zoom range: 25% to 400%

### 7. Enhanced Properties Panel
- **Stroke width** — numeric input
- **Opacity** — slider (0 to 1)
- **Width / Height** — for rect elements
- **Position x / y** — for positioned elements
- All existing properties from v1 retained (text, fill, stroke, font size)

### 8. Improved Drag
- Drag groups (cylinder stacks, vector grids) by updating transform
- Drag text labels and larger rectangles
- Small grid squares excluded from accidental drag

### 9. Keyboard Shortcuts
| Shortcut | Action |
|---|---|
| Ctrl+Z | Undo |
| Ctrl+Y | Redo |
| Ctrl+D | Duplicate |
| Delete / Backspace | Delete selected |
| Escape | Deselect / cancel add mode |

## What's Unchanged
- Same SVG diagram content (UpANNS architecture)
- Download HTML / Download SVG buttons
- Double-click text to edit inline
- Reset button
