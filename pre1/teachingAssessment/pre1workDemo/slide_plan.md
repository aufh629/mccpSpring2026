# HTML Slide Plan — KVFlow Presentation

## Overview

- **Total slides:** 10 (for an 8-minute presentation)
- **Format:** Single-file HTML using custom CSS (no external framework dependencies)
- **Navigation:** Arrow keys (← →) and click to advance; progress bar at bottom
- **Design:** Clean, modern, dark-on-light theme; minimal text; large fonts; high contrast
- **Responsive:** Works on laptop screens and projectors

---

## Slide-by-Slide Plan

### Slide 1: Title Slide
**Title:** KVFlow: Making AI Agent Teams Work Faster  
**Subtitle:** Research Story-telling — Oral Presentation Assessment 1  
**Content:**
- Paper title: *KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows*
- Authors: Pan, Patel, Hu, Shen, Guan, Li, Qin, Wang, & Ding (UCSD & AWS, 2025)
- Presenter name and date

**Visual:** Clean title layout with university/course branding  
**Design notes:** Large title text, minimal content, professional appearance

---

### Slide 2: The Hook — AI Agents Working as a Team
**Title:** What if your AI team keeps forgetting?  
**Content:**
- Icon/illustration of 4 agents: Planner → Executor → Writer → Reviewer
- Caption: "Each time an agent finishes, the next one re-reads everything from scratch"
- Key question: "How can we make this smarter?"

**Visual:** Simple animated or static diagram showing 4 agents in a cycle with a "memory loss" icon  
**Design notes:** Large icons, minimal text. The diagram should be the focal point. Use color coding for each agent role.

---

### Slide 3: Why This Matters — Context
**Title:** The Rise of Multi-Agent AI  
**Content:**
- Bullet: AI agents now collaborate in teams (MetaGPT, AutoGen, ChatDev)
- Bullet: Each agent = LLM + fixed instructions + dynamic task input
- Bullet: Challenge: GPU memory is limited → system must decide what to keep

**Visual:** 3 simple icons representing the trend (single AI → multi-agent → workflow)  
**Design notes:** Max 3 bullet points. Large font. One key visual element.

---

### Slide 4: The Problem — LRU Gets It Wrong
**Title:** The Wrong Memory Gets Thrown Away  
**Content:**
- Diagram: 4 agents in sequence, Executor is active
- LRU evicts Expresser's cache (hasn't been used recently)
- But Expresser is NEXT in line → cache miss → slow restart
- Caption: "Looking backward instead of forward"

**Visual:** Adapted version of Figure 1 from the paper — simplified with color-coded agents and a red "X" on the wrong eviction  
**Design notes:** This is the key problem slide. Use red/green to show wrong vs right decisions. Animate if possible (highlight the eviction, then the cache miss).

---

### Slide 5: The Solution — KVFlow's Agent Step Graph
**Title:** KVFlow: Looking Ahead  
**Content:**
- The **Agent Step Graph** assigns each agent a "steps-to-execution" score
- Analogy: Hospital triage — prioritize by urgency, not arrival time
- Key idea: Keep data for agents coming soon, discard data for agents coming later

**Visual:** Simplified version of Figure 3(a) — agents with step numbers, showing how the graph predicts execution order  
**Design notes:** Use numbered badges on agents. Contrast with LRU (backward-looking) vs KVFlow (forward-looking). Clean layout with the graph as center piece.

---

### Slide 6: The Innovation — Proactive Prefetching
**Title:** Loading While Working  
**Content:**
- Even smart eviction can't prevent all cache misses
- KVFlow **proactively loads** the next agent's data while the current agent works
- Like a relay runner already in motion before the baton arrives
- **Status-aware scheduling:** If data isn't ready, skip to other ready tasks

**Visual:** Timeline diagram (adapted from Figure 4) showing 3 approaches:
1. Reactive loading (wait)
2. Proactive prefetching (overlap)
3. KVFlow full solution (prefetch + status-aware scheduling)

**Design notes:** Use a horizontal timeline with color blocks. Show the GPU idle time shrinking across the 3 approaches. This is the most technical slide — keep labels large and clear.

---

### Slide 7: Results — How Much Faster?
**Title:** Significant Speedups  
**Content:**
- **Single workflow (large prompts):** up to **1.83× faster** than SGLang+HiCache; **2.91×** over GPU-only baseline
- **High concurrency (many workflows):** up to **2.19× faster**
- Benefits grow with larger prompt sizes
- No impact on output quality — only system performance improves

**Visual:** Bar chart comparing KVFlow vs SGLang vs SGLang+HiCache across configurations  
**Design notes:** Use bold numbers for the speedup figures. Color-code the bars consistently (green for KVFlow). Include a small note: "Same output quality guaranteed."

---

### Slide 8: Why This Research Is Important
**Title:** Bridging AI Design and System Optimization  
**Content:**
- Most multi-agent research focuses on making agents smarter (frontend)
- KVFlow shows the backend matters just as much
- **Workflow awareness → system-level optimization** — a general principle
- Applicable beyond one system; cost and energy savings

**Visual:** A bridge diagram — "Agent Design" on one side, "System Optimization" on the other, with KVFlow as the bridge  
**Design notes:** Conceptual diagram, not a data chart. Use a memorable visual metaphor.

---

### Slide 9: What I Learned — Research Design & Writing
**Title:** Lessons for My Own Research  
**Content:**
- **Research design:** System-level thinking matters; workflow structure affects performance
- **Writing lesson 1:** Clear problem framing before solution (Figure 1 as the hook)
- **Writing lesson 2:** Visual storytelling — every concept has a figure
- **Writing lesson 3:** Honest evaluation — acknowledging diminishing returns
- Quote: *"KVFlow highlights the importance of workflow semantics in enabling system-level optimizations."*

**Visual:** 3 writing lesson icons + the quoted text highlighted in a box  
**Design notes:** Use a quote block for the direct quote from the paper. Keep personal and reflective tone in the presenter notes (not on slide — speak it).

---

### Slide 10: Thank You & Questions
**Title:** Thank You  
**Content:**
- Key takeaway: "Knowing the game plan isn't just helpful — it's transformative."
- Paper reference: Pan et al. (2025). KVFlow. arXiv:2507.07400
- "Questions?"

**Visual:** Clean closing slide with the takeaway message prominent  
**Design notes:** Large text. Minimalist. Warm and inviting for Q&A.

---

## HTML Technical Specifications

### Structure
```
presentation.html (single file, self-contained)
├── <style> block — all CSS embedded
├── <div class="slide"> × 10 — one per slide
├── <div class="progress-bar"> — bottom progress indicator
└── <script> block — navigation logic
```

### CSS Design System
- **Font:** System sans-serif stack (clean, professional, no external dependencies)
- **Colors:**
  - Background: `#FFFFFF` (white)
  - Text: `#1a1a2e` (near-black)
  - Accent: `#0077B6` (professional blue)
  - Highlight: `#00B4D8` (lighter blue for emphasis)
  - Agent colors: Planner `#E76F51`, Executor `#2A9D8F`, Writer `#E9C46A`, Reviewer `#264653`
- **Font sizes:** Title 2.5em, subtitle 1.5em, body 1.2em, captions 0.9em
- **Slide dimensions:** 100vw × 100vh (fullscreen)

### Navigation
- **Arrow keys:** ← previous slide, → next slide
- **Click/tap:** Advance to next slide
- **Keyboard:** Space bar advances, Escape toggles overview
- **Progress bar:** Visual indicator at bottom showing current position

### Responsive Design
- Flexbox-based layouts
- Media queries for different screen widths
- Scales gracefully from laptop to projector

### Diagrams and Charts
- Built with CSS/HTML (boxes, arrows, bars) — no external image dependencies
- Color-coded agent roles consistent across all slides
- Bar charts using CSS `div` elements with percentage widths
- Timeline diagrams using flexbox rows

### Animations (optional, subtle)
- Fade-in on slide transition
- Highlight effects on key numbers
- No distracting animations — keep professional

---

## Build Steps

1. Create the HTML file with all 10 slides
2. Embed CSS styles in the `<style>` block
3. Build diagrams using HTML/CSS (agent cycles, timelines, bar charts)
4. Add navigation JavaScript
5. Test in browser — check all slides, navigation, responsive behavior
6. Review against rubric — minimal text, visual focus, professional design
