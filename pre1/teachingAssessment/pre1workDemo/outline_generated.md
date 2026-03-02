# Presentation Outline: KVFlow — Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows

**Paper:** Pan, Z., Patel, A., Hu, Z., Shen, Y., Guan, Y., Li, W.-L., Qin, L., Wang, Y., & Ding, Y. (2025). *KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows.* arXiv:2507.07400. UCSD & AWS.

**Presentation duration:** 8 minutes  
**Target audience:** Non-specialist (classmates and lecturer from different research fields)

---

## Opening (~1 minute)

### Hook
"Imagine you're managing a team of four specialists — a planner, a coder, a writer, and a reviewer — and they take turns working on a project. Each time one finishes, the next person has to start by re-reading all the background documents from scratch, even though they just read them an hour ago. That's essentially what happens today when AI systems run multiple agents together. This paper proposes a smarter way to manage that shared memory."

### Brief Context
- AI systems are increasingly using **multi-agent workflows** — teams of specialized AI agents that collaborate to solve complex tasks (e.g., software development, financial analysis)
- Each agent is powered by a **large language model (LLM)**, and each needs to process large instruction prompts
- The challenge: how to efficiently manage the **memory** these agents use, especially when it's limited

### Transition
"Let me walk you through how this paper identifies a fundamental inefficiency in current AI systems and proposes an elegant solution called KVFlow."

> **Presenter notes:**
> - **Content/Structure:** Start with a relatable analogy. Avoid mentioning "KV cache" yet — introduce it naturally later.
> - **Delivery:** Make eye contact with the audience during the hook. Speak slowly and conversationally. Pause after the analogy to let it sink in.
> - **Visual Aid:** Slide with a simple illustration of 4 people passing documents around (or a team of AI agents).
> - **Language:** "Today I'd like to share with you a fascinating piece of research that addresses..."

---

## Section 1: Introduction to the Article (~1.5 minutes)

### What is the research about?
- When AI agents work in a **workflow** (like a relay team), each agent has a fixed set of instructions (its "role description") that gets used repeatedly
- These instructions are processed by the LLM and stored as **key-value (KV) caches** — think of them as "pre-processed notes" that save the AI from re-reading the same instructions every time
- The problem: GPU memory is limited, so the system must decide which notes to keep and which to throw away

### What gap does the paper address?
- Current systems use a simple rule called **LRU (Least Recently Used)** — "throw away whichever notes haven't been used most recently"
- But this is like throwing away the writer's notes while the coder is working, even though the writer is **next in line**
- The paper calls this a "fundamental inefficiency" — the system doesn't look ahead at who's coming next

### Research objective
- Design a **workflow-aware** memory management system that knows the execution order of agents and manages memory accordingly

> **Presenter notes:**
> - **Content/Structure:** Use the "team of specialists" metaphor consistently. Transition: "So what exactly did the researchers propose?"
> - **Delivery:** When explaining KV cache, gesture to the slide visual. Pause after introducing the gap.
> - **Visual Aid:** Diagram showing 4 agents in a cycle (Planner → Executor → Writer → Reviewer → Planner...) with an "X" on the wrong agent's cache being evicted.
> - **Language:** "The research is driven by the need to address..." / "The pressing question the authors seek to answer is..."

---

## Section 2: Key Findings (~2 minutes)

### Finding 1: The Agent Step Graph — a smart scheduling system
- The researchers created an abstraction called the **Agent Step Graph**
- Each agent gets a "**steps-to-execution**" score — essentially, "how many steps until this agent needs to work again?"
- This allows the system to **predict** who's needed next, rather than just remembering who worked last
- *Analogy:* It's like a hospital triage system — instead of treating patients in order of arrival, you prioritize based on urgency

### Finding 2: Workflow-aware eviction beats LRU
- Using the Step Graph, KVFlow keeps the "notes" of agents who will be needed **soonest** and discards those of agents who won't be needed for a while
- This resulted in **up to 1.83× speedup** for single workflows with large prompts on an NVIDIA A10G GPU
- And **up to 2.91× speedup** over systems that don't use CPU backup at all

### Finding 3: Proactive prefetching eliminates waiting
- Even with smarter eviction, sometimes notes still need to be fetched back from slower storage (CPU memory)
- KVFlow **proactively loads** the next agent's data in the background while the current agent is still working — like a relay runner already in motion before the baton arrives
- Combined with **status-aware scheduling** (skip agents whose data isn't ready yet, work on others first), this achieves **up to 2.19× speedup** under high concurrency (many workflows running simultaneously)

> **Presenter notes:**
> - **Content/Structure:** Present 3 clear findings with numbers. Use the relay runner and hospital triage analogies. Transition: "Now, why do these findings matter?"
> - **Delivery:** Emphasize the speedup numbers — slow down and raise volume slightly when stating "1.83 times faster." Reference the chart on the slide.
> - **Visual Aid:** Bar chart showing KVFlow vs SGLang vs SGLang+HiCache speedups. A timeline diagram showing proactive prefetching vs reactive loading.
> - **Language:** "The findings reveal a significant improvement..." / "Our data indicates that..."

---

## Section 3: Significance of the Research (~1.5 minutes)

### Why do these findings matter?
- **Multi-agent AI is becoming mainstream** — systems like MetaGPT, AutoGen, and ChatDev organize AI agents into teams for software engineering, research, and creative tasks
- As these systems scale up, **efficiency becomes critical** — you can't just throw more expensive GPUs at the problem
- KVFlow shows that **knowing the workflow structure** unlocks major performance gains at the system level, without changing the AI models themselves

### Broader implications
- **Bridge between AI application design and system optimization:** Most research focuses on making agents smarter (frontend); this paper shows the backend matters just as much
- **Applicable beyond one system:** While implemented on SGLang, the approach can be adapted to any LLM serving system
- **Cost and energy savings:** Faster execution means less GPU time, which translates to lower costs and reduced energy consumption — important as AI scales

### A noteworthy writing strategy
- The authors use **progressive complexity** very effectively — they start with a simple 4-agent example (Figure 1), then build up to complex branching workflows and high-concurrency scenarios
- They also maintain **quantitative rigor** throughout, backing every claim with experimental data

> **Presenter notes:**
> - **Content/Structure:** Connect to broader AI trends the audience may have heard of (ChatGPT, AI agents). Transition: "This brings me to how this paper connects to my own research..."
> - **Delivery:** Show enthusiasm when discussing significance. Make the "bridge" point emphatically.
> - **Visual Aid:** Slide showing the growing ecosystem of multi-agent frameworks, with KVFlow positioned as the "system optimizer."
> - **Language:** "This research contributes to the field by..." / "The implications of these findings suggest that..."

---

## Section 4: Impact on My Own Research (~1.5 minutes)

### How might this paper influence my research design?
- My research involves [working with AI and language/technology]. This paper has shown me that **system-level thinking** is essential — it's not enough to design good AI prompts; we also need to think about how efficiently the underlying systems execute them
- The concept of **workflow-aware optimization** is inspiring: the idea that if you tell the system about the structure of your task, it can serve you much faster
- For anyone working with multi-agent AI tools, this paper demonstrates that **the way you organize agent interactions directly affects performance**

### What good writing skills I learned from this article
1. **Clear problem framing:** The authors spend the first page making sure readers understand *why* the problem matters before diving into the solution. The relay-team example (Figure 1) is immediately intuitive
2. **Visual storytelling:** Every key concept has an accompanying figure (the Agent Step Graph, the prefetching timeline, the performance charts). The figures do much of the heavy lifting
3. **Honest evaluation:** The authors note when their approach has diminishing returns (e.g., when output tokens dominate) and clearly state limitations
4. **Evidence from the article:** In the conclusion, the authors write: *"While prior work on multi-agent systems has predominantly focused on designing frontend application logic and interaction protocols, KVFlow highlights the importance of workflow semantics in enabling system-level optimizations."* This single sentence captures the paper's key contribution — a clean, powerful summary

> **Presenter notes:**
> - **Content/Structure:** Be personal and specific. Show genuine reflection. Quote from the paper.
> - **Delivery:** Shift to a more personal, reflective tone. Slow down. This is where you show your critical thinking.
> - **Visual Aid:** Slide with 2-3 key writing lessons and the direct quote from the paper.
> - **Language:** "This paper has taught me that..." / "One of the most effective writing strategies I noticed is..."

---

## Closing (~0.5 minutes)

### Key Takeaway
"KVFlow teaches us something important: in the era of AI agents working as teams, knowing the game plan isn't just helpful — it's transformative. By simply telling the system which agent comes next, the researchers achieved nearly 2× faster execution. This principle — that workflow awareness enables optimization — extends far beyond computer science."

### Thank the audience and invite questions
"Thank you for your attention. I'd be happy to take any questions you may have."

> **Presenter notes:**
> - **Content/Structure:** One strong takeaway sentence. Don't introduce new information.
> - **Delivery:** Slow down for the final sentence. Make eye contact with several audience members. Smile.
> - **Visual Aid:** Clean closing slide with the paper title, key takeaway, and a "Thank you / Questions?" prompt.
> - **Language:** "To sum up..." / "In conclusion..."

---

## Timing Guide

| Section | Duration | Cumulative |
|---|---|---|
| Opening (Hook + Context) | ~1:00 | 1:00 |
| Introduction to the Article | ~1:30 | 2:30 |
| Key Findings (3 findings) | ~2:00 | 4:30 |
| Significance | ~1:30 | 6:00 |
| Impact on My Research | ~1:30 | 7:30 |
| Closing | ~0:30 | 8:00 |

---

## Rubric Alignment Checklist

| Rubric Criterion | How This Outline Addresses It |
|---|---|
| **Content appropriate to non-specialist audience** | All technical concepts (KV cache, LRU, prefetching) explained with everyday analogies (team of specialists, hospital triage, relay runner) |
| **Strategies to explain disciplinary knowledge** | Metaphors, analogies, visual aids, avoiding jargon |
| **In-depth reflection integrated into analysis** | Section 4 provides personal reflection on research design impact and writing skills learned |
| **Well-structured with logical flow** | Clear 4-part structure matching the brief; transition statements between all sections |
| **Transition statements used effectively** | Explicit transitions included in each section's presenter notes |
| **No reading from scripts** | Outline is structured as key points, not a script; presenter notes emphasize natural delivery |
| **Visual aids supplement speech** | Each section has specific slide content recommendations; minimal text, focused on visuals |
| **Body language and delivery** | Presenter notes include delivery tips (pacing, eye contact, gestures, emphasis) |
| **Peer evaluation readiness** | Understanding of rubric criteria helps prepare for Q&A and peer review |
