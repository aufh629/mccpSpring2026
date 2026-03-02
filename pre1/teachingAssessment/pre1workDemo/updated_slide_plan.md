# Updated HTML Slide Plan — KVFlow Presentation

> Based on: `slide_plan.md`, `updatedOutline.md`, and `sample_slides/style.md`

## Design System (from style.md — Monsha deck)

- **Aspect ratio:** 16:9 widescreen
- **Fonts:** Poppins (headings, 600-800 weight), Open Sans (body, 400-700 weight)
- **Primary color:** `#1B4942` (dark teal)
- **Text color:** `#1a1a2e` (near-black)
- **Background:** `#FFFFFF` with subtle `#F8FAF4` accents
- **Accent light:** `#E8F0ED` (for highlight boxes)
- **Max bullets per slide:** 3-5
- **Agent colors:** Planner `#E76F51`, Executor `#2A9D8F`, Writer `#E9C46A`, Reviewer `#264653`

## Slides (10 total)

### Slide 1: Title
- Title: "KVFlow: Making AI Agent Teams Work Faster"
- Subtitle: Research Story-telling — Oral Presentation 1
- Paper citation, presenter name, date
- Clean, centered layout with teal accent bar

### Slide 2: Hook — AI Agents Working as a Team
- Title: "What if your AI team keeps forgetting?"
- CSS diagram: 4 agents in a cycle (color-coded circles with arrows)
- Caption: "Each time an agent finishes, the next re-reads everything from scratch"
- Key question: "How can we make this smarter?"

### Slide 3: Context — The Rise of Multi-Agent AI
- Title: "The Rise of Multi-Agent AI"
- 3 bullets: agents collaborate in teams; each = LLM + fixed instructions; GPU memory is limited
- Simple visual: progression icons (single → team → workflow)

### Slide 4: Problem — LRU Gets It Wrong
- Title: "The Wrong Memory Gets Thrown Away"
- CSS diagram: 4 agents in sequence, Executor active, Expresser's cache evicted with red X
- Caption: "LRU looks backward — KVFlow looks forward"
- Color: Red for wrong, green for right

### Slide 5: Solution — Agent Step Graph
- Title: "KVFlow: Looking Ahead"
- CSS diagram: agents with step-number badges showing steps-to-execution
- Analogy text: "Like hospital triage — prioritize by urgency, not arrival"
- Key idea highlight box

### Slide 6: Innovation — Proactive Prefetching
- Title: "Loading While Working"
- CSS timeline: 3 rows showing Reactive → Proactive → Full KVFlow
- Color blocks showing GPU compute and CPU loading overlapping
- Caption: "Like a relay runner already in motion"

### Slide 7: Results
- Title: "Significant Speedups"
- CSS bar chart: KVFlow vs SGLang vs HiCache
- Key numbers in big-number style: 1.83×, 2.19×, 2.91×
- Small note: "Same output quality guaranteed"

### Slide 8: Significance
- Title: "Bridging AI Design and System Optimization"
- CSS bridge diagram: "Agent Design" ← KVFlow → "System Optimization"
- 3 bullets: workflow awareness → optimization; applicable beyond one system; cost savings

### Slide 9: Writing Lessons (strengthened from updatedOutline.md)
- Title: "What I Learned About Research Writing"
- 4 writing lessons as compact cards:
  1. CARS Model mastery (Territory → Gap → Niche)
  2. Visual storytelling (figures that argue)
  3. Honest evaluation (acknowledging limitations)
  4. Effective synthesis (positioning work relative to literature)
- Quote highlight box: "KVFlow highlights the importance of workflow semantics..."

### Slide 10: Thank You
- Title: "Thank You"
- Key takeaway: "Knowing the game plan isn't just helpful — it's transformative."
- Paper reference
- "Questions?"

## Technical Build Notes

- Single HTML file, all CSS embedded
- Google Fonts (Poppins + Open Sans) loaded via @import
- Arrow key / click navigation via JS
- All diagrams built with CSS flexbox/grid (no images)
- Progress bar at bottom
- Smooth fade transitions between slides
