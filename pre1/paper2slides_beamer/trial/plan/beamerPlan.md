# Beamer Plan: Converting AAAI25 Paper to LaTeX Slides

## Overview
Beamer is a LaTeX document class for creating professional presentation slides with full typographic control, mathematical notation support, and seamless integration with academic paper source code.

**Official Documentation**: https://ctan.org/pkg/beamer  
**Overleaf Tutorial**: https://www.overleaf.com/learn/latex/Beamer

---

## Tool Capabilities

### Key Features
1. **LaTeX Integration**: Direct reuse of equations, figures, and tables from paper source
2. **Mathematical Typography**: Perfect rendering of complex mathematical notation
3. **Precise Control**: Full customization of layout, fonts, colors, and spacing
4. **Themes**: Professional built-in themes (Berkeley, Copenhagen, Boadilla, etc.)
5. **Overlays**: Progressive reveal of content (bullet points, equations)
6. **PDF Output**: High-quality, portable presentation format
7. **Version Control**: Plain text format works seamlessly with Git

### Advantages for Technical Papers
- **Mathematical Precision**: Best-in-class equation rendering
- **Consistency**: Matches paper's notation and formatting
- **Reusability**: Copy-paste from paper LaTeX source
- **Professional**: Standard for academic conferences
- **Reproducibility**: Source code ensures exact reproduction

---

## Basic Beamer Structure

### Minimal Example

```latex
\documentclass{beamer}

% Theme selection
\usetheme{Boadilla}
\usecolortheme{dolphin}

% Metadata
\title{Your Presentation Title}
\author{Author Name}
\institute{Institution}
\date{\today}

\begin{document}

% Title slide
\begin{frame}
  \titlepage
\end{frame}

% Table of contents
\begin{frame}{Outline}
  \tableofcontents
\end{frame}

% Content slides
\section{Introduction}
\begin{frame}{Introduction}
  \begin{itemize}
    \item First point
    \item Second point
  \end{itemize}
\end{frame}

\end{document}
```

### Key Components

| Component | Purpose | Example |
|-----------|---------|---------|
| `\documentclass{beamer}` | Declare Beamer document | Required first line |
| `\usetheme{}` | Choose visual theme | `Boadilla`, `Copenhagen`, `Berkeley` |
| `\begin{frame}...\end{frame}` | Create individual slide | Container for content |
| `\frametitle{}` | Set slide title | Alternative to `{Title}` in frame |
| `\section{}` | Organize content | Populates table of contents |
| `\pause` | Progressive reveal | Show content step-by-step |

---

## Workflow for AAAI25 Paper (COLDQ)

### Paper Details
- **Title**: "Doubly-Bounded Queue for Constrained Online Learning"
- **Source Files**: `aaai25.tex`, `aaai25.bbl`, `aaai25.sty`
- **Content Type**: Theoretical algorithm paper with mathematical proofs
- **Key Elements**: Equations, algorithms, theorems, experimental results

### Recommended Approach

#### Step 0: Generate a slide outline (before writing .tex)

**Do this first.** Produce a slide-by-slide outline (e.g. in Markdown) that defines:

- **Sections** (e.g. Introduction, Problem, Algorithm, Theory, Experiments, Conclusion).
- **Per-slide plan**: slide number, section, title, key messages, and (optionally) source in the paper (equations, figures, line refs).
- **Timing** (optional): rough minutes per section for the target talk length.
- **Visual notes** (optional): which slides need figures, tables, or blocks.

**Why outline first:** It keeps the narrative clear, avoids missing sections, and makes writing each frame in Beamer faster. You (or an AI) can generate the outline from the paper; then you create the `.tex` by following the outline.

**Example location:** See `implement/docs/preliminarySlides_outline.md` for a full example (slide structure table + detailed slide-by-slide content). Your outline can be shorter (e.g. section titles + one line per slide) or that detailed.

**Output:** One outline document (e.g. `slides_outline.md`) before any Beamer code.

---

#### Step 1: Create Beamer Template
Create `aaai25_slides.tex` in the trial folder:

```latex
\documentclass{beamer}

% Theme
\usetheme{Boadilla}
\usecolortheme{dolphin}

% Packages (reuse from paper)
\usepackage{amsmath,amssymb,amsthm}
\usepackage{algorithm,algorithmic}
\usepackage{graphicx}
\usepackage{tikz}

% Metadata
\title{Doubly-Bounded Queue for Constrained Online Learning}
\subtitle{Pace with Dynamics of Both Loss and Constraint}
\author{Juncheng Wang}
\institute{Hong Kong Baptist University}
\date{AAAI 2025}

\begin{document}

% Title slide
\begin{frame}
  \titlepage
\end{frame}

% Outline
\begin{frame}{Outline}
  \tableofcontents
\end{frame}

% Content sections follow...

\end{document}
```

#### Step 2: Structure content from your outline

Using your **slide outline** from Step 0, add the same sections to the Beamer file:

```latex
\section{Introduction}
\section{Problem Formulation}
\section{COLDQ Algorithm}
\section{Theoretical Analysis}
\section{Experiments}
\section{Conclusion}
```

#### Step 3: Fill frames from outline and paper

For each slide in your outline, identify:
1. **Main message**: What is the key takeaway?
2. **Supporting equations**: Which formulas are essential?
3. **Figures/tables**: Which visuals illustrate the point?
4. **Proofs/algorithms**: What needs detailed explanation?

---

## Section-by-Section Slide Plan

### 1. Title & Outline (2 slides)

```latex
% Slide 1: Title
\begin{frame}
  \titlepage
\end{frame}

% Slide 2: Outline
\begin{frame}{Outline}
  \tableofcontents
\end{frame}
```

**Human Input**: None (automated)

---

### 2. Introduction (3-4 slides)

**Key Messages**:
- OCO with time-varying constraints
- Existing work doesn't recover best-known bounds
- Our contribution: smooth approach to optimal bounds

```latex
\section{Introduction}

\begin{frame}{Online Convex Optimization (OCO)}
  \begin{itemize}
    \item Learner selects decisions $x_t \in \mathcal{X}$ over time
    \item Loss functions $f_t(x)$ revealed after decision
    \item Goal: Minimize \textbf{regret}
    \pause
    \item Applications: advertisement, load balancing, resource allocation
  \end{itemize}
\end{frame}

\begin{frame}{Time-Varying Constraints}
  \begin{block}{Problem}
    Minimize loss while satisfying time-varying constraints $g_t(x) \leq 0$
  \end{block}
  
  \begin{itemize}
    \item \textbf{Dynamic regret}: Compare to online benchmark
    \item \textbf{Hard constraint violation}: No compensated violation
    \pause
    \item Existing bounds: $O(\sqrt{T})$ regret, $O(\sqrt{T})$ violation
    \item \textcolor{red}{Do not recover $O(1)$ violation for fixed constraints}
  \end{itemize}
\end{frame}

\begin{frame}{Research Question}
  \begin{alertblock}{Key Question}
    Can a constrained OCO algorithm provide bounds that \textbf{smoothly approach} 
    $O(\sqrt{T})$ regret and $O(1)$ violation as dynamics diminish?
  \end{alertblock}
  
  \pause
  
  \begin{block}{Our Answer}
    \textbf{Yes!} We propose COLDQ algorithm with:
    \begin{itemize}
      \item $O(\sqrt{T + V_x})$ dynamic regret
      \item $O(\sqrt{T V_g})$ hard constraint violation
      \item Smoothly approaches best-known bounds
    \end{itemize}
  \end{block}
\end{frame}
```

**Human Input Required**:
- Decide level of detail for OCO background
- Choose which applications to highlight
- Determine if progressive reveal (`\pause`) is desired

---

### 3. Problem Formulation (2-3 slides)

**Key Messages**:
- Formal problem definition
- Performance metrics (dynamic regret, hard violation)
- Assumptions

```latex
\section{Problem Formulation}

\begin{frame}{Constrained OCO Problem}
  \begin{block}{Optimization Problem}
    \begin{equation*}
      \min_{x_t \in \mathcal{X}} \sum_{t=1}^T f_t(x_t) 
      \quad \text{s.t.} \quad g_t(x_t) \leq 0, \; \forall t
    \end{equation*}
  \end{block}
  
  \begin{itemize}
    \item $\mathcal{X} \subset \mathbb{R}^p$: Convex feasible set
    \item $f_t(x)$: Convex loss function at time $t$
    \item $g_t(x) = [g_t^1(x), \ldots, g_t^N(x)]^\top$: Constraint functions
  \end{itemize}
\end{frame}

\begin{frame}{Performance Metrics}
  \begin{definition}[Dynamic Regret]
    \begin{equation*}
      \text{Regret}_T = \sum_{t=1}^T f_t(x_t) - \sum_{t=1}^T f_t(x_t^*)
    \end{equation*}
    where $x_t^*$ is the optimal solution at time $t$.
  \end{definition}
  
  \pause
  
  \begin{definition}[Hard Constraint Violation]
    \begin{equation*}
      \text{Violation}_T = \sum_{t=1}^T \max\{g_t(x_t), 0\}
    \end{equation*}
  \end{definition}
\end{frame}

\begin{frame}{System Dynamics}
  \begin{itemize}
    \item $V_x$: Accumulated variation of loss functions
    \begin{equation*}
      V_x = \sum_{t=1}^{T-1} \|x_t^* - x_{t+1}^*\|
    \end{equation*}
    
    \pause
    
    \item $V_g$: Accumulated variation of constraint functions
    \begin{equation*}
      V_g = \sum_{t=1}^{T-1} \|\nabla g_t(x_t^*) - \nabla g_{t+1}(x_{t+1}^*)\|
    \end{equation*}
  \end{itemize}
  
  \pause
  
  \begin{block}{Key Insight}
    As $V_x \to 0$ and $V_g \to 0$, our bounds approach best-known results.
  \end{block}
\end{frame}
```

**Human Input Required**:
- Copy equations from `aaai25.tex` (lines with `\begin{equation}`)
- Verify notation consistency
- Decide on level of mathematical detail

---

### 4. COLDQ Algorithm (3-4 slides)

**Key Messages**:
- Virtual queue with double bounds
- Algorithm pseudocode
- Key innovation: lower AND upper bounds

```latex
\section{COLDQ Algorithm}

\begin{frame}{Key Idea: Doubly-Bounded Virtual Queue}
  \begin{columns}
    \column{0.5\textwidth}
    \textbf{Existing Approaches}:
    \begin{itemize}
      \item Lower bound only
      \item Upper bound only
      \item Require Slater condition
    \end{itemize}
    
    \column{0.5\textwidth}
    \textbf{COLDQ}:
    \begin{itemize}
      \item \textcolor{blue}{Both lower and upper bounds}
      \item Tight control of violation
      \item No Slater condition needed
    \end{itemize}
  \end{columns}
  
  \pause
  
  \begin{block}{Virtual Queue Update}
    \begin{equation*}
      Q_{t+1} = \text{clip}(Q_t + g_t(x_t), 0, Q_{\max})
    \end{equation*}
  \end{block}
\end{frame}

\begin{frame}{COLDQ Algorithm}
  \begin{algorithm}[H]
    \caption{COLDQ Algorithm}
    \begin{algorithmic}[1]
      \STATE Initialize $x_1 \in \mathcal{X}$, $Q_1 = 0$
      \FOR{$t = 1$ to $T$}
        \STATE Observe $f_t(x)$ and $g_t(x)$
        \STATE Update decision:
        \begin{equation*}
          x_{t+1} = \Pi_{\mathcal{X}} \left[ x_t - \eta_t (\nabla f_t(x_t) + Q_t \nabla g_t(x_t)) \right]
        \end{equation*}
        \STATE Update virtual queue:
        \begin{equation*}
          Q_{t+1} = \text{clip}(Q_t + g_t(x_t), 0, Q_{\max})
        \end{equation*}
      \ENDFOR
    \end{algorithmic}
  \end{algorithm}
\end{frame}

\begin{frame}{Why Doubly-Bounded Queue Works}
  \begin{itemize}
    \item \textbf{Lower bound (0)}: Prevents negative queue
    \begin{itemize}
      \item Ensures queue reflects actual violations
    \end{itemize}
    
    \pause
    
    \item \textbf{Upper bound ($Q_{\max}$)}: Limits queue growth
    \begin{itemize}
      \item Controls constraint violation directly
      \item Key to achieving $O(\sqrt{T V_g})$ bound
    \end{itemize}
    
    \pause
    
    \item \textbf{No Slater condition}: More practical
    \begin{itemize}
      \item Slater: $\exists x \in \mathcal{X}$ s.t. $g_t(x) < -\epsilon < 0$
      \item Often hard to verify in practice
    \end{itemize}
  \end{itemize}
\end{frame}
```

**Human Input Required**:
- Extract algorithm pseudocode from paper
- Decide on visual representation (algorithm environment vs. itemize)
- Choose whether to include detailed parameter settings

---

### 5. Theoretical Analysis (3-4 slides)

**Key Messages**:
- Main theorem: regret and violation bounds
- Lyapunov drift analysis
- Comparison with state-of-the-art

```latex
\section{Theoretical Analysis}

\begin{frame}{Main Theorem}
  \begin{theorem}[Performance Bounds]
    COLDQ achieves:
    \begin{enumerate}
      \item \textbf{Dynamic Regret}: $O(\sqrt{T + V_x})$
      \item \textbf{Hard Constraint Violation}: $O(\sqrt{T V_g})$
    \end{enumerate}
  \end{theorem}
  
  \pause
  
  \begin{block}{Key Properties}
    \begin{itemize}
      \item As $V_x \to 0$: Regret $\to O(\sqrt{T})$ (best-known static)
      \item As $V_g \to 0$: Violation $\to O(1)$ (best-known fixed)
      \item \textbf{First algorithm with smooth approach to both bounds}
    \end{itemize}
  \end{block}
\end{frame}

\begin{frame}{Proof Technique: Lyapunov Drift}
  \begin{itemize}
    \item Define Lyapunov function:
    \begin{equation*}
      L_t = \|x_t - x_t^*\|^2 + V Q_t^2
    \end{equation*}
    
    \pause
    
    \item Analyze drift:
    \begin{equation*}
      \mathbb{E}[L_{t+1} - L_t] \leq \text{regret term} + \text{violation term}
    \end{equation*}
    
    \pause
    
    \item \textbf{Key innovation}: Leverage both bounds of $Q_t$
    \begin{itemize}
      \item Lower bound: Control regret accumulation
      \item Upper bound: Control violation accumulation
    \end{itemize}
  \end{itemize}
\end{frame}

\begin{frame}{Comparison with State-of-the-Art}
  \begin{table}
    \centering
    \small
    \begin{tabular}{lcc}
      \hline
      Algorithm & Dynamic Regret & Hard Violation \\
      \hline
      Existing [Ref] & $O(\sqrt{T + V_x})$ & $O(\sqrt{T} \cdot \sqrt{T + V_g})$ \\
      \textbf{COLDQ (Ours)} & $O(\sqrt{T + V_x})$ & $O(\sqrt{T V_g})$ \\
      \hline
      \multicolumn{3}{l}{\textit{As $V_g \to 0$:}} \\
      Existing [Ref] & $O(\sqrt{T})$ & $O(\sqrt{T})$ \\
      \textbf{COLDQ (Ours)} & $O(\sqrt{T})$ & $O(1)$ \\
      \hline
    \end{tabular}
  \end{table}
  
  \begin{itemize}
    \item COLDQ recovers best-known $O(1)$ violation for fixed constraints
    \item Existing work stuck at $O(\sqrt{T})$ violation
  \end{itemize}
\end{frame}

\begin{frame}{Strongly Convex Case}
  \begin{theorem}[Strongly Convex Loss]
    When $f_t(x)$ is $\mu$-strongly convex, COLDQ achieves:
    \begin{enumerate}
      \item \textbf{Static Regret}: $O(\log T)$
      \item \textbf{Hard Constraint Violation}: $O(\sqrt{T V_g})$
    \end{enumerate}
  \end{theorem}
  
  \begin{itemize}
    \item Matches best-known static regret
    \item Maintains smooth violation bound
  \end{itemize}
\end{frame}
```

**Human Input Required**:
- Extract theorem statements from paper
- Decide on proof detail level (full proof vs. sketch vs. intuition)
- Create comparison table from paper's Table 1
- Verify mathematical notation

---

### 6. Experiments (3-4 slides)

**Key Messages**:
- Experimental setup
- Results on synthetic and real datasets
- Comparison with baselines

```latex
\section{Experiments}

\begin{frame}{Experimental Setup}
  \textbf{Datasets}:
  \begin{itemize}
    \item Synthetic: Quadratic loss with time-varying constraints
    \item Real: Network resource allocation, online advertising
  \end{itemize}
  
  \pause
  
  \textbf{Baselines}:
  \begin{itemize}
    \item OGD-VQ: Online gradient descent with virtual queue
    \item DOGD: Dynamic online gradient descent
    \item SOCCO: State-of-the-art constrained OCO
  \end{itemize}
  
  \pause
  
  \textbf{Metrics}:
  \begin{itemize}
    \item Cumulative regret
    \item Cumulative constraint violation
  \end{itemize}
\end{frame}

\begin{frame}{Results: Time-Varying Constraints}
  \begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{figure1.pdf}
    \caption{Regret and violation vs. time on synthetic dataset}
  \end{figure}
  
  \begin{itemize}
    \item COLDQ achieves lowest violation
    \item Comparable regret to best baseline
  \end{itemize}
\end{frame}

\begin{frame}{Results: Fixed Constraints}
  \begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{figure2.pdf}
    \caption{Violation approaches $O(1)$ as $V_g \to 0$}
  \end{figure}
  
  \begin{itemize}
    \item COLDQ violation stabilizes (approaches $O(1)$)
    \item Baselines grow with $O(\sqrt{T})$
    \item Validates theoretical prediction
  \end{itemize}
\end{frame}

\begin{frame}{Ablation Study}
  \textbf{Impact of Doubly-Bounded Queue}:
  \begin{itemize}
    \item Lower bound only: Higher violation
    \item Upper bound only: Higher regret
    \item Both bounds: Best trade-off
  \end{itemize}
  
  \pause
  
  \textbf{Parameter Sensitivity}:
  \begin{itemize}
    \item $Q_{\max}$: Larger values reduce violation but increase regret
    \item Learning rate $\eta_t$: Standard choice $\eta_t = 1/\sqrt{t}$ works well
  \end{itemize}
\end{frame}
```

**Human Input Required**:
- Extract figures from paper (if available as separate files)
- OR regenerate figures from experimental data
- OR use screenshots from paper PDF
- Decide which experiments to highlight
- Create figure captions

---

### 7. Conclusion (2 slides)

**Key Messages**:
- Summary of contributions
- Future work

```latex
\section{Conclusion}

\begin{frame}{Summary}
  \textbf{Contributions}:
  \begin{enumerate}
    \item \textbf{COLDQ Algorithm}: Doubly-bounded virtual queue
    \item \textbf{Theoretical Guarantees}: 
      \begin{itemize}
        \item $O(\sqrt{T + V_x})$ dynamic regret
        \item $O(\sqrt{T V_g})$ hard constraint violation
      \end{itemize}
    \item \textbf{Smooth Approach}: First to recover best-known bounds
    \item \textbf{Practical Performance}: Outperforms state-of-the-art
  \end{enumerate}
\end{frame}

\begin{frame}{Future Directions}
  \begin{itemize}
    \item Extension to non-convex loss functions
    \item Multi-agent constrained OCO
    \item Adaptive parameter selection
    \item Applications to:
      \begin{itemize}
        \item Federated learning with fairness constraints
        \item Online resource allocation in cloud computing
        \item Real-time bidding with budget constraints
      \end{itemize}
  \end{itemize}
  
  \vspace{1em}
  
  \begin{center}
    \Large Thank you for your attention!
    
    \vspace{0.5em}
    
    \normalsize Questions?
  \end{center}
\end{frame}
```

**Human Input Required**:
- Decide on future work emphasis
- Add contact information if desired

---

## Theme Selection Guide

### Popular Themes for Technical Presentations

| Theme | Style | Best For |
|-------|-------|----------|
| `Boadilla` | Clean, professional | Conference talks |
| `Copenhagen` | Minimalist | Theory-heavy presentations |
| `Berkeley` | Sidebar navigation | Long presentations |
| `Madrid` | Simple, elegant | General purpose |
| `Warsaw` | Traditional | Academic seminars |
| `Singapore` | Modern, colorful | Engaging talks |

### Color Themes

```latex
\usecolortheme{dolphin}    % Blue tones
\usecolortheme{beaver}     % Red tones
\usecolortheme{crane}      % Yellow/orange tones
\usecolortheme{seahorse}   % Purple tones
```

### Recommended Combination for AAAI25 Paper

```latex
\usetheme{Boadilla}
\usecolortheme{dolphin}
```

**Rationale**: Clean, professional look suitable for algorithm/theory paper at top-tier conference.

---

## Making Beamer Slides Beautiful

Yes — Beamer can create beautiful, professional slides. Use theme + color + font + layout together.

### Theme + color combinations (modern and readable)

| Combination | Look | Use when |
|-------------|------|----------|
| `\usetheme{Madrid}` `\usecolortheme{default}` | Clean, light, minimal | General talks |
| `\usetheme{Boadilla}` `\usecolortheme{dolphin}` | Blue, professional | Conference / academic |
| `\usetheme{Copenhagen}` `\usecolortheme{beaver}` | Warm, structured | Seminars |
| `\usetheme{Berlin}` `\usecolortheme{crane}` | Strong contrast, sidebar | Long talks |
| `\usetheme{Singapore}` | Colorful, modern | Engaging / less formal |

### Font themes (typography)

```latex
\usefonttheme{professionalfonts}  % Use LaTeX fonts (good for math)
\usefonttheme{serif}             % Serif body text
\usefonttheme{structurebold}     % Bold section titles
```

For a polished look: pick one theme + one colortheme and keep them consistent.

### Layout and design tips

- **One main idea per slide** — avoid crowding; split into more frames if needed.
- **Whitespace** — use `\vspace{}`, don’t fill every line.
- **Blocks** — use `\begin{block}{}`, `\begin{alertblock}{}`, `\begin{exampleblock}{}` for definitions, key results, and examples.
- **Hierarchy** — clear frametitle; short bullets (5–7 per slide); sub-bullets only when necessary.
- **Math** — use `\Large` or `\LARGE` inside a frame if equations are central.
- **Figures** — one clear figure per slide when possible; use `\centering` and sensible `width=` (e.g. `0.8\textwidth`).

### Minimal “beautiful” preamble example

```latex
\documentclass{beamer}
\usetheme{Madrid}
\usecolortheme{dolphin}
\usefonttheme{structurebold}
\setbeamertemplate{itemize items}[circle]
\setbeamercolor{structure}{fg=blue!70!black}
```

Result: clear structure, readable text, and a consistent, professional look. Adjust theme/color to match your venue (e.g. academic vs. industry).

---

## Advanced Beamer Features

### Progressive Reveal (Overlays)

```latex
\begin{frame}{Key Points}
  \begin{itemize}
    \item<1-> First point (appears on slide 1)
    \item<2-> Second point (appears on slide 2)
    \item<3-> Third point (appears on slide 3)
  \end{itemize}
  
  \onslide<4->{
    All points visible from slide 4 onwards.
  }
\end{frame}
```

### Blocks for Emphasis

```latex
\begin{block}{Definition}
  Content here
\end{block}

\begin{alertblock}{Important}
  Highlighted content
\end{alertblock}

\begin{exampleblock}{Example}
  Example content
\end{exampleblock}
```

### Two-Column Layout

```latex
\begin{frame}{Comparison}
  \begin{columns}
    \column{0.5\textwidth}
    Left column content
    
    \column{0.5\textwidth}
    Right column content
  \end{columns}
\end{frame}
```

### Including Figures

```latex
\begin{frame}{Experimental Results}
  \begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{figure1.pdf}
    \caption{Caption text}
  \end{figure}
\end{frame}
```

---

## Compilation Workflow

### Using Command Line

```bash
# Navigate to trial folder
cd /path/to/trial/

# Compile Beamer presentation
pdflatex aaai25_slides.tex

# If using bibliography
bibtex aaai25_slides
pdflatex aaai25_slides.tex
pdflatex aaai25_slides.tex  # Second pass for references

# View output
open aaai25_slides.pdf  # macOS
```

### Using Overleaf (Recommended for Beginners)

1. Go to https://www.overleaf.com
2. Create new project → Upload Project
3. Upload `aaai25_slides.tex` and supporting files
4. Click "Recompile" to generate PDF
5. Edit and preview in real-time

### Using Local LaTeX Editor

- **TeXShop** (macOS): Open `.tex` file, click "Typeset"
- **TeXworks** (Windows/Linux): Open file, click green play button
- **VS Code** with LaTeX Workshop extension: Save file to auto-compile

---

## Human Input Required

### Before Creating Slides

1. **Content Selection**
   - Which sections of paper to include?
   - What level of detail for each section?
   - Target presentation length (10 min, 20 min, 30 min)?
   - Audience background (experts, general, mixed)?

2. **Visual Design**
   - Choose theme and color scheme
   - Decide on progressive reveal vs. static slides
   - Determine figure/table inclusion strategy

3. **Mathematical Content**
   - Which equations are essential?
   - Which proofs to include (full, sketch, or omit)?
   - How to simplify notation for clarity?

### During Slide Creation

1. **Content Extraction**
   - Copy equations from `aaai25.tex`
   - Extract algorithm pseudocode
   - Identify key figures/tables
   - Summarize long paragraphs into bullet points

2. **Structure Decisions**
   - How many slides per section?
   - Which content to emphasize?
   - Where to add pauses/overlays?
   - How to transition between sections?

3. **Visual Elements**
   - Create/extract figures from paper
   - Design comparison tables
   - Add highlighting/colors for emphasis
   - Include logos or branding if needed

### After Initial Draft

1. **Content Review**
   - Verify mathematical notation accuracy
   - Check equation numbering consistency
   - Ensure all figures are properly referenced
   - Validate citations and bibliography

2. **Design Refinement**
   - Adjust font sizes for readability
   - Balance text density across slides
   - Ensure consistent formatting
   - Test progressive reveals

3. **Practice & Iterate**
   - Practice presentation with slides
   - Time each section
   - Identify confusing slides
   - Revise based on feedback

---

## Detailed Slide Breakdown for AAAI25 Paper

### Estimated Slide Count

| Section | Slides | Time (min) |
|---------|--------|------------|
| Title & Outline | 2 | 1 |
| Introduction | 3-4 | 3-4 |
| Problem Formulation | 2-3 | 2-3 |
| COLDQ Algorithm | 3-4 | 4-5 |
| Theoretical Analysis | 3-4 | 4-5 |
| Experiments | 3-4 | 3-4 |
| Conclusion | 2 | 1-2 |
| **Total** | **18-23** | **18-24** |

**Recommendation**: Aim for 20 slides for a 20-minute conference talk (1 min/slide average).

---

## Content Extraction Checklist

### From `aaai25.tex`

- [ ] Title, authors, affiliation (from preamble)
- [ ] Abstract (summarize to 3-4 bullet points)
- [ ] Introduction paragraphs (convert to bullet points)
- [ ] Problem formulation equations (copy with `\begin{equation}`)
- [ ] Algorithm pseudocode (from `\begin{algorithm}` environment)
- [ ] Theorem statements (from `\begin{theorem}` environment)
- [ ] Proof sketches (simplify for slides)
- [ ] Experimental setup description
- [ ] Figure references (e.g., `\includegraphics{figure1.pdf}`)

### From `aaai25.bbl`

- [ ] Key citations for related work slide
- [ ] Bibliography entries (if including references slide)

### Additional Materials Needed

- [ ] Figure files (`.pdf`, `.png`, `.jpg`)
- [ ] Table data (if not in LaTeX source)
- [ ] Logo files (institution, conference)
- [ ] Custom macros or notation definitions

---

## Common Pitfalls & Solutions

### Problem 1: Too Much Text
**Symptom**: Slides feel crowded, hard to read  
**Solution**: 
- Use bullet points, not paragraphs
- Limit to 5-7 bullets per slide
- Split into multiple slides if needed

### Problem 2: Equations Too Small
**Symptom**: Audience can't read equations  
**Solution**:
```latex
% Use larger math font
\begin{frame}
  \Large  % or \LARGE
  \begin{equation*}
    ...
  \end{equation*}
\end{frame}
```

### Problem 3: Inconsistent Notation
**Symptom**: Variables defined differently than paper  
**Solution**:
- Copy notation directly from paper
- Define macros in preamble:
```latex
\newcommand{\calX}{\mathcal{X}}
\newcommand{\vx}{\mathbf{x}}
```

### Problem 4: Missing Figures
**Symptom**: `\includegraphics` fails to compile  
**Solution**:
- Ensure figure files are in same directory
- Use relative paths: `./figures/figure1.pdf`
- Check file extensions (`.pdf` for pdflatex)

### Problem 5: Bibliography Not Working
**Symptom**: Citations show as `[?]`  
**Solution**:
- Run `bibtex` after first `pdflatex`
- Or use `\bibitem` manually:
```latex
\begin{frame}{References}
  \begin{thebibliography}{99}
    \bibitem{ref1} Author, "Title", Conference, Year.
  \end{thebibliography}
\end{frame}
```

---

## Customization Examples

### Custom Title Page

```latex
\begin{frame}
  \titlepage
  \begin{center}
    \includegraphics[width=0.3\textwidth]{hkbu_logo.pdf}
  \end{center}
\end{frame}
```

### Custom Footer

```latex
\setbeamertemplate{footline}{
  \leavevmode%
  \hbox{%
    \begin{beamercolorbox}[wd=.333333\paperwidth,ht=2.25ex,dp=1ex,center]{author in head/foot}%
      \usebeamerfont{author in head/foot}\insertshortauthor
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.333333\paperwidth,ht=2.25ex,dp=1ex,center]{title in head/foot}%
      \usebeamerfont{title in head/foot}\insertshorttitle
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.333333\paperwidth,ht=2.25ex,dp=1ex,right]{date in head/foot}%
      \usebeamerfont{date in head/foot}\insertshortdate{}\hspace*{2em}
      \insertframenumber{} / \inserttotalframenumber\hspace*{2ex}
    \end{beamercolorbox}}%
  \vskip0pt%
}
```

### Highlight Box

```latex
\begin{frame}{Key Result}
  \begin{alertblock}{Main Theorem}
    COLDQ achieves $O(\sqrt{T V_g})$ hard constraint violation.
  \end{alertblock}
\end{frame}
```

---

## Advantages of Beamer for AAAI25 Paper

### 1. Mathematical Precision
- Perfect rendering of complex equations
- Consistent notation with paper
- Easy to copy-paste from paper source

### 2. Professional Appearance
- Standard for academic conferences
- Clean, distraction-free design
- Customizable themes

### 3. Reproducibility
- Plain text source (version control friendly)
- Exact reproduction from source code
- Easy to update and maintain

### 4. Integration with Paper
- Reuse packages and macros
- Direct copy of equations and algorithms
- Consistent bibliography

### 5. Flexibility
- Full control over layout
- Progressive reveal of content
- Custom styling and branding

---

## Limitations & Considerations

### Limitations

1. **Steep Learning Curve**: Requires LaTeX knowledge
2. **Time-Consuming**: Manual creation takes hours
3. **Design Constraints**: Limited to LaTeX capabilities
4. **Compilation Issues**: Debugging LaTeX errors can be frustrating
5. **Not Interactive**: Static PDF output only

### When NOT to Use Beamer

- **Tight Deadline**: Use PowerPoint/Keynote for speed
- **Non-Technical Audience**: Visual tools may be more engaging
- **Heavy Graphics**: Design software (Illustrator) may be better
- **Collaborative Editing**: Google Slides easier for teams
- **Beginner**: Consider Overleaf or PowerPoint first

### Best Practices

1. **Start Simple**: Use basic template, add complexity gradually
2. **Test Early**: Compile frequently to catch errors
3. **Reuse Content**: Copy from paper, don't retype
4. **Practice Presentation**: Slides are only part of the talk
5. **Get Feedback**: Show draft to colleagues before finalizing

---

## Recommended Workflow for AAAI25 Paper

### Phase 1: Setup (30 min)

1. Create `aaai25_slides.tex` with basic template
2. Choose theme and color scheme
3. Add title, author, affiliation
4. Create section structure

### Phase 2: Content Extraction (2-3 hours)

1. **Introduction** (30 min)
   - Summarize motivation
   - Extract key problem statement
   - Highlight contributions

2. **Problem Formulation** (30 min)
   - Copy main problem equation
   - Define performance metrics
   - Extract key assumptions

3. **Algorithm** (45 min)
   - Copy algorithm pseudocode
   - Create visual explanation of doubly-bounded queue
   - Highlight key innovation

4. **Theory** (45 min)
   - Extract main theorem
   - Simplify proof sketch
   - Create comparison table

5. **Experiments** (30 min)
   - Extract key figures
   - Summarize results
   - Highlight main findings

6. **Conclusion** (15 min)
   - Summarize contributions
   - List future work

### Phase 3: Refinement (1-2 hours)

1. **Visual Balance** (30 min)
   - Adjust text density
   - Resize figures
   - Add emphasis (colors, boxes)

2. **Progressive Reveal** (30 min)
   - Add `\pause` commands
   - Create overlays for complex slides
   - Test flow

3. **Consistency Check** (30 min)
   - Verify notation
   - Check equation numbering
   - Validate citations

### Phase 4: Practice & Iterate (1-2 hours)

1. **First Practice** (30 min)
   - Present to yourself
   - Time each section
   - Identify problem slides

2. **Revisions** (30 min)
   - Simplify complex slides
   - Add missing transitions
   - Fix timing issues

3. **Final Practice** (30 min)
   - Present to colleague
   - Get feedback
   - Make final adjustments

**Total Time**: 5-8 hours for high-quality 20-slide presentation

---

## Comparison: Beamer vs. Paper2Slides

| Aspect | Beamer | Paper2Slides |
|--------|--------|--------------|
| **Time** | 5-8 hours | 15-30 minutes |
| **Control** | Full control | Limited to prompts |
| **Quality** | Professional polish | Good starting point |
| **Math** | Perfect rendering | May need verification |
| **Customization** | Unlimited | Theme-based |
| **Learning Curve** | Steep | Easy |
| **Reproducibility** | Exact (source code) | Varies (AI-generated) |
| **Integration** | Seamless with paper | Separate process |
| **Best For** | Final presentation | Quick draft |

### Recommended Hybrid Approach

1. **Use Paper2Slides** to generate initial draft (30 min)
2. **Export to PowerPoint/Keynote** for visual reference
3. **Create Beamer slides** manually, inspired by AI draft (4-6 hours)
4. **Refine in Beamer** for final presentation (1-2 hours)

**Benefits**:
- Speed of AI generation for content organization
- Precision of LaTeX for final output
- Best of both worlds

---

## Resources for Learning Beamer

### Official Documentation
- **Beamer User Guide**: https://ctan.org/pkg/beamer (367 pages, comprehensive)
- **CTAN Beamer Package**: https://www.ctan.org/pkg/beamer

### Tutorials
- **Overleaf Beamer Tutorial**: https://www.overleaf.com/learn/latex/Beamer
  - Part 1: Getting Started
  - Part 2: Lists, Columns, Highlighting
  - Part 3: Blocks, Code, Hyperlinks
  - Part 4: Themes and Handouts
  - Part 5: Animations

- **LaTeX Beamer Quick Start**: https://latex-beamer.com/quick-start/

### Example Templates
- **Overleaf Gallery**: https://www.overleaf.com/gallery/tagged/presentation
- **GitHub Beamer Templates**: Search "beamer template academic"

### Community Support
- **TeX Stack Exchange**: https://tex.stackexchange.com/questions/tagged/beamer
- **LaTeX Community**: https://latex.org/forum/

---

## Conclusion

Beamer is the gold standard for academic presentations, especially for technical papers with heavy mathematical content. While it requires more time and LaTeX knowledge than automated tools, the precision, control, and professional quality make it worthwhile for important presentations like conference talks.

**For AAAI25 Paper (COLDQ)**:
- Beamer is ideal due to complex mathematical notation
- Estimated 20 slides for 20-minute talk
- 5-8 hours total creation time
- Seamless integration with paper LaTeX source

**Key Takeaway**: Invest time in learning Beamer for long-term benefits. Use Paper2Slides for quick drafts, but finalize in Beamer for professional presentations at top-tier conferences.

---

## Next Steps

1. **Choose Approach**:
   - Quick draft? → Start with Paper2Slides
   - Final presentation? → Use Beamer
   - Hybrid? → Paper2Slides first, then Beamer

2. **Set Up Environment**:
   - Install LaTeX distribution (TeX Live, MiKTeX, MacTeX)
   - Choose editor (Overleaf, TeXShop, VS Code)
   - Test compilation with minimal example

3. **Create Template**:
   - Start with basic Beamer template
   - Add paper metadata
   - Choose theme and colors

4. **Extract Content**:
   - Work through sections systematically
   - Copy equations and algorithms from paper
   - Create slides incrementally

5. **Practice & Refine**:
   - Present to yourself
   - Get feedback from colleagues
   - Iterate until satisfied

**Good luck with your presentation!**
