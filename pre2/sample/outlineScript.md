# Outline and script for poster presentation (2–3 minutes)

Use this outline and script to prepare the oral presentation that accompanies the sample poster. Aim for **2–3 minutes**, then take questions.

---

## Presentation outline

1. **Opening (15–20 s)**  
   Hook + title + one-sentence takeaway.

2. **Problem and gap (25–30 s)**  
   What is graph similarity search / GED; why current method (AStar-LSa) is limited (memory/scalability).

3. **What we did (40–50 s)**  
   Two-stage idea: tighter bound lbBMa → efficient variant lbBMao; main guarantee (faster + less memory).

4. **Result in one line (15–20 s)**  
   Experiments: AStar-BMao runs faster and uses much less memory than AStar-LSa on real data.

5. **Closing (10–15 s)**  
   So what / impact + thank you / invite questions.

---

## Script (approx. 2 min 30 s)

**Opening**  
“Hi. I’m going to walk you through our work on **accelerating graph similarity search**. In one sentence: we make it **faster and much more memory-efficient** than the current best method, so it can scale to larger graphs.”

**Problem and gap**  
“In many applications we have a database of graphs—networks—and we want to find graphs that are *similar* to a query. Similarity is measured by the *graph edit distance*, or GED: the minimum number of edits to turn one graph into the other. The state-of-the-art exact method is **AStar-LSa**. The problem is that its **memory use grows very quickly** when graphs or the similarity threshold get larger, so it doesn’t scale well.”

**What we did**  
“We propose a **two-stage** approach. First we design a **tighter lower bound**, lbBMa, based on branch matching instead of label sets—so the search space is smaller, but the cost is high, order n to the four. So we introduce a **second, practical** bound, **lbBMao**, that relaxes lbBMa just enough to bring the cost down to order n cubed, while still being tighter than the old bound. The resulting algorithm is **AStar-BMao**.”

**Result**  
“On real datasets, **AStar-BMao runs faster and uses much less memory** than AStar-LSa. So we get both speed and scalability.”

**Closing**  
“So we’ve made graph similarity search more practical for larger data. I’m happy to take questions—about the problem, the bounds, or the experiments. Thank you.”

---

## Possible Q&A — short answers

- **What is GED?**  
  The minimum number of edit operations (add/delete/relabel node or edge) to transform one graph into the other.

- **Why “two stages”?**  
  The first bound (lbBMa) is ideal for tightness but too expensive; the second (lbBMao) keeps most of the benefit with feasible complexity.

- **Compared to machine learning methods?**  
  This work is about *exact* GED computation; the paper shows orders-of-magnitude gains over the previous exact method (AStar-LSa). Comparison to approximate/ML methods is in the paper.

- **What datasets?**  
  Real graph datasets; see the paper for names and sizes. The poster placeholders are where you’d put time/memory plots.

- **For a non-specialist:**  
  “We help search big networks more efficiently: we found a way to use less memory and less time than the previous best method, so it works on larger networks.”

---

## Timing checklist

- [ ] Rehearse with a timer; stay within 2–3 minutes.
- [ ] Point at the poster (title, layman’s summary, methodology diagram, results placeholders) while speaking.
- [ ] Prepare 2–3 backup slides or notes for “if they ask about X” (e.g. GED definition, complexity, datasets).
- [ ] Practise one sentence each for: problem, gap, contribution, result, impact.
