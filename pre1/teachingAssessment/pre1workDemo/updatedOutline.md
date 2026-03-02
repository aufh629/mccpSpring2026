# Updated Presentation Outline: KVFlow — Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows

**Paper:** Pan, Z., Patel, A., Hu, Z., Shen, Y., Guan, Y., Li, W.-L., Qin, L., Wang, Y., & Ding, Y. (2025). *KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows.* arXiv:2507.07400. UCSD & AWS.

**Presentation duration:** 8 minutes  
**Target audience:** Non-specialist (classmates and lecturer from different research fields)

> **Update notes:** This version strengthens Section 4 (Impact on My Own Research) with deeper analysis of the paper's writing strategies, drawing on the CARS model, rhetorical moves framework, and academic writing principles from the MCCP6020 course materials (`writing/assessment/` and `writing/academicPhrasebank/`).

---

## Opening (~1 minute)

### Hook
"Imagine you're managing a team of four specialists — a planner, a coder, a writer, and a reviewer — and they take turns working on a project. Each time one finishes, the next person has to start by re-reading all the background documents from scratch, even though they just read them an hour ago. That's essentially what happens today when AI systems run multiple agents together. This paper proposes a smarter way to manage that shared memory."

### Brief Context
- AI systems are increasingly using **multi-agent workflows** — teams of specialized AI agents that collaborate to solve complex tasks
- Each agent is powered by a **large language model (LLM)**, and each needs to process large instruction prompts
- The challenge: how to efficiently manage the **memory** these agents use, especially when it's limited

### Transition
"Let me walk you through how this paper identifies a fundamental inefficiency in current AI systems and proposes an elegant solution called KVFlow."

> **Presenter notes:**
> - Start with a relatable analogy. Avoid mentioning "KV cache" yet.
> - Make eye contact during the hook. Speak slowly and conversationally.
> - Slide: Simple illustration of 4 agents passing documents around.
> - Language: "Today I'd like to share with you a fascinating piece of research that addresses..."

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
> - Use the "team of specialists" metaphor consistently.
> - Transition: "So what exactly did the researchers propose?"
> - Slide: Diagram of 4 agents in a cycle with red "X" on wrong eviction.

---

## Section 2: Key Findings (~2 minutes)

### Finding 1: The Agent Step Graph — a smart scheduling system
- The researchers created an abstraction called the **Agent Step Graph**
- Each agent gets a "**steps-to-execution**" score — "how many steps until this agent needs to work again?"
- This allows the system to **predict** who's needed next, rather than just remembering who worked last
- *Analogy:* It's like a hospital triage system — instead of treating patients in order of arrival, you prioritize based on urgency

### Finding 2: Workflow-aware eviction beats LRU
- Using the Step Graph, KVFlow keeps "notes" of agents who will be needed **soonest** and discards those of agents who won't be needed for a while
- This resulted in **up to 1.83× speedup** for single workflows with large prompts
- And **up to 2.91× speedup** over systems without CPU backup

### Finding 3: Proactive prefetching eliminates waiting
- KVFlow **proactively loads** the next agent's data in the background while the current agent is still working — like a relay runner already in motion before the baton arrives
- Combined with **status-aware scheduling**, this achieves **up to 2.19× speedup** under high concurrency

> **Presenter notes:**
> - Present 3 clear findings with numbers. Slow down for the speedup figures.
> - Transition: "Now, why do these findings matter?"
> - Slide: Bar chart of speedups + timeline diagram of prefetching.

---

## Section 3: Significance of the Research (~1.5 minutes)

### Why do these findings matter?
- **Multi-agent AI is becoming mainstream** — MetaGPT, AutoGen, ChatDev organize AI into teams
- As these systems scale up, **efficiency becomes critical**
- KVFlow shows that **knowing the workflow structure** unlocks major performance gains without changing the AI models themselves

### Broader implications
- **Bridge between AI design and system optimization** — most research focuses on making agents smarter (frontend); this paper shows the backend matters just as much
- **Applicable beyond one system** — adaptable to any LLM serving system
- **Cost and energy savings** — faster execution means less GPU time

> **Presenter notes:**
> - Connect to broader AI trends the audience has heard of.
> - Transition: "This brings me to how this paper connects to my own research and what I've learned about writing..."
> - Slide: Bridge diagram between "Agent Design" and "System Optimization."

---

## Section 4: Impact on My Own Research & Writing Lessons (~1.5 minutes)

### How this paper influences my research thinking
- The concept of **workflow-aware optimization** is powerful: when you tell the system about the structure of your task, it can serve you much faster
- This reminds us that in any research field, **system-level thinking** matters — it's not enough to have good ideas; you also need to think about how they are executed and communicated

### Writing strategies I learned from this article

#### 1. Masterful use of the CARS Model (Creating a Research Space)

The paper's introduction follows the **CARS model** with exceptional clarity:

- **Move 1 — Establishing a Territory:** The authors open by establishing the importance of multi-agent workflows, citing 5 references in the very first sentence. They use a **centrality claim** — *"LLM-based agentic workflows have become a popular paradigm"* — that immediately positions the topic as significant and timely.

- **Move 2 — Identifying a Niche:** The gap identification is razor-sharp. The authors don't just say "existing systems are inefficient." They construct a specific, vivid scenario (Figure 1: the Expresser agent's cache being evicted right before it's needed) that makes the gap **concrete and intuitive**. The language is precise: *"We observe that this strategy can lead to suboptimal performance"* — using cautious hedging ("can lead to") while presenting strong evidence.

- **Move 3 — Occupying the Niche:** The transition to their solution is clean: *"To address the limitations... we present KVFlow"* — a clear purpose statement that directly responds to the identified gap.

**Lesson:** A strong introduction tells a *story* — from importance, through problem, to solution. Each move builds on the last.

#### 2. Visual storytelling that carries the argument

Every key concept has an accompanying figure:
- Figure 1: The LRU eviction problem (makes the gap tangible)
- Figure 3: The Agent Step Graph (makes the solution intuitive)
- Figure 4: The prefetching timeline (makes the mechanism clear)
- Figures 5-8: Performance results (makes the evidence compelling)

**Lesson:** In good academic writing, visuals don't just *illustrate* — they *argue*. Each figure in this paper advances the narrative.

#### 3. Honest, quantified evaluation with clear limitations

The authors state clearly when benefits diminish: *"As the number of output tokens increases, the relative gain from KVFlow diminishes"* — and they explain why (decoding latency dominates). They also acknowledge that HiCache sometimes performs poorly and offer reasoned hypotheses rather than glossing over anomalies.

**Lesson:** The best academic writing earns trust by acknowledging limitations. The rubric rewards this: *"In-depth reflection is well-integrated into the analysis."*

#### 4. Effective synthesis and source integration

In the Related Work section, the authors synthesize multiple citation clusters naturally:
- *"A broad line of work improves online LLM serving by optimizing request scheduling, including continuous batching... multi-level feedback queues... quality-of-experience aware schedulers..."*
- Each cluster is summarized and **positioned** relative to KVFlow, using the phrase *"orthogonal to KVFlow"* or *"complementary to ours"* to show how the work relates without being competitive.

**Lesson:** Good literature synthesis doesn't just list papers — it *organizes* them by theme and *positions* your work relative to each group.

### Key quote from the paper
> *"While prior work on multi-agent systems has predominantly focused on designing frontend application logic and interaction protocols, KVFlow highlights the importance of workflow semantics in enabling system-level optimizations."*

This single sentence captures the paper's entire contribution — a model of concise, powerful academic writing.

> **Presenter notes:**
> - This is where you show your critical thinking. Be personal and specific.
> - Shift to a reflective tone. Slow down. Reference the CARS model by name — the audience will have learned about it in Session 1.
> - Don't try to cover all 4 writing points in equal depth — pick 2 to elaborate on verbally, mention the others briefly.
> - Slide: 4 writing lessons with icons + the direct quote in a highlight box.

---

## Closing (~0.5 minutes)

### Key Takeaway
"KVFlow teaches us something important: in the era of AI agents working as teams, knowing the game plan isn't just helpful — it's transformative. By simply telling the system which agent comes next, the researchers achieved nearly 2× faster execution. And the paper itself demonstrates that clear, structured writing — following the moves from territory to gap to solution — is what makes complex research accessible."

### Thank the audience and invite questions
"Thank you for your attention. I'd be happy to take any questions you may have."

> **Presenter notes:**
> - One strong takeaway connecting both the technical contribution and the writing lesson.
> - Make eye contact. Smile. Pause after the final sentence.
> - Slide: Clean closing with takeaway, paper reference, "Questions?"

---

## Timing Guide

| Section | Duration | Cumulative |
|---|---|---|
| Opening (Hook + Context) | ~1:00 | 1:00 |
| Introduction to the Article | ~1:30 | 2:30 |
| Key Findings (3 findings) | ~2:00 | 4:30 |
| Significance | ~1:30 | 6:00 |
| Impact on Research & Writing | ~1:30 | 7:30 |
| Closing | ~0:30 | 8:00 |

---

## Rubric Alignment Checklist

| Rubric Criterion | How This Outline Addresses It |
|---|---|
| **Content appropriate to non-specialist audience** | All technical concepts explained with everyday analogies (team, triage, relay runner) |
| **Strategies to explain disciplinary knowledge** | Metaphors, analogies, visual aids, avoiding jargon |
| **In-depth reflection integrated into analysis** | Section 4 provides detailed analysis of 4 writing strategies with specific evidence from the paper, referencing the CARS model and synthesis techniques |
| **Well-structured with logical flow** | Clear 4-part structure matching the brief; transition statements between all sections |
| **Transition statements used effectively** | Explicit transitions in each section |
| **No reading from scripts** | Outline is key points, not a script; notes emphasize natural delivery |
| **Visual aids supplement speech** | Each section has specific slide content; minimal text, focused on visuals |
| **Body language and delivery** | Notes include delivery tips (pacing, eye contact, gestures, emphasis) |
| **Peer evaluation readiness** | Understanding of rubric criteria helps prepare for Q&A and peer review |
