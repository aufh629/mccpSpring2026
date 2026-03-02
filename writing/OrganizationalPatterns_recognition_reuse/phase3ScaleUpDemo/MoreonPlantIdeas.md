# More on Planting Ideas: Five-Paper Analysis

**Focus:** How authors plant ideas early in the Introduction so that when the present work is announced, it feels logical and convincing. Each paper is analyzed for introduction paragraph map, **full introduction paragraphs** (for a standalone report), plant→harvest links, and actionable insights. Source files are in `PhDagentSpring2026/writing/buildPaperCollection_arXiv/html_collection/`.

**Published (GitHub Pages):** [More on Planting Ideas — Interactive Report](https://tesolchina.github.io/mccpSpring2026/PhDagentSpring2026/writing/OrganizationalPatterns_recognition_reuse/phase3ScaleUpDemo/MoreonPlantIdeas.html)  
*(Repo: [tesolchina/mccpSpring2026](https://github.com/tesolchina/mccpSpring2026))*

---

## Papers analyzed

1. **Kostric et al.** — Generating Usage-related Questions for Preference Elicitation in Conversational Recommender Systems (2111.13463)
2. **Srivastava et al. (BIG-bench)** — Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models (2206.04615)
3. **BigScience Workshop (BLOOM)** — BLOOM: A 176B-Parameter Open-Access Multilingual Language Model (2211.05100)
4. **Raffel et al. (T5)** — Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (1910.10683)
5. **Brabra et al.** — Identifying Breakdowns in Conversational Recommender Systems using User Simulation (2405.14249)

**Source collection:** [buildPaperCollection_arXiv/html_collection](../../buildPaperCollection_arXiv/html_collection/)

---

## Per-paper analysis

### Paper 1: Kostric et al., Usage-related Questions for CRS (2111.13463)

**Source:** [2111.13463.html](../../buildPaperCollection_arXiv/html_collection/2111.13463.html) (or 2111.13463v2.html)

#### Introduction paragraph map

- **Para 1 — Establish contrast (traditional vs conversational):**  
  *"Traditionally, recommender systems predict users' preference … by performing offline analysis of past interaction data. … A **conversational recommender system** (CRS), on the other hand, is a multi-turn, interactive recommender system that can elicit user preferences in real-time using natural language."*

- **Para 2 — Establish problem and plant “implicit” vs “explicit”:**  
  *"One of the main tasks … is to elicit preferences from users. This is traditionally done by asking questions either about items directly or item attributes. … ordinary users often do not possess this kind of attribute understanding. Instead, they only know where or how they intend to **use** the item. … The novel research objective of this work is to generate **implicit** attribute questions for eliciting user preferences, related to the **intended use** of items. This stands in contrast to **explicit** questions that ask about specific item attributes."*

- **Para 3 — Plant source of data (reviews):**  
  *"Our approach hinges on the observation that **usage-related experiences are often captured in item reviews**. By identifying review sentences that discuss particular item features … that matter in the context of various activities or usage scenarios …, those sentences can then be turned into preference elicitation questions."*

- **Para 4 — Announce contributions:**  
  *"In this paper, our focus is on the **offline question generation** part. … As our first contribution, we address the problem of creating a sentence-to-question dataset by developing a **multi-stage data generation protocol**. … As our second contribution, we propose four **question generation** models. … **Automatic evaluation** … **Human evaluation** …"*

- **Para 5 — Bulleted summary of contributions** (list + link to resources).

#### Full paragraphs (Introduction)

**Para 1.** Traditionally, recommender systems predict users' preference towards an item by performing offline analysis of past interaction data (e.g., click history, past visits, item ratings). These systems often do not take into account that users might have made mistakes in the past (e.g., regarding purchases) or that their preferences change over time. Additionally, for some users, there is little historical data which makes modeling their preferences difficult. A *conversational recommender system* (CRS), on the other hand, is a multi-turn, interactive recommender system that can elicit user preferences in real-time using natural language. Given its interactive nature, it is capable of modeling dynamic user preferences and taking actions based on users current needs.

**Para 2.** One of the main tasks of a conversational recommender system is to elicit preferences from users. This is traditionally done by asking questions either about items directly or item attributes. Asking people to review individual recommendations to establish the characteristics of a single item they need, especially in a domain that they are not expert in, is particularly time consuming; therefore, the research is commonly focused on the estimation and utilization of users preferences towards attributes. Common to these approaches is that the user is explicitly asked about the desired values for a specific product attribute, much in the spirit of slot-filling dialogue systems. For example, in the context of looking for a bicycle recommendation, we might have wheel dimensions or the number of gears as attributes in our item collection. In this case, a system might want to ask a question like "How thick should the tires be?" or "How many gears should the bike have?" However, ordinary users often do not possess this kind of attribute understanding, which might require extensive domain-specific knowledge. Instead, they only know where or how they intend to use the item. For example, a user might only be interested in using this bike for commuting but does not know what attributes might be good for that purpose. The novel research objective of this work is to generate *implicit* attribute questions for eliciting user preferences, related to the intended use of items. This stands in contrast to explicit questions that ask about specific item attributes.

**Para 3.** Our approach hinges on the observation that usage-related experiences are often captured in item reviews. By identifying review sentences that discuss particular item features or aspects (e.g., "fat tires") that matter in the context of various activities or usage scenarios (e.g., "for conquering tough terrain"), those sentences can then be turned into preference elicitation questions. In our envisaged scenario, a large collection of implicit preference elicitation questions is generated offline, and then utilized later in real-time interactions by a CRS.

**Para 4.** In this paper, our focus is on the offline question generation part, whereas the actual item recommendation is left as a separate, downstream task to be addressed. A main challenge associated with the question generation task is the collection of high-quality training data. As our first contribution, we address the problem of creating a sentence-to-question dataset by developing a multi-stage data generation protocol. It starts with *candidate sentence selection*, which can be automated effectively based on part-of-speech tagging and simple linguistic patterns. Then, we employ a multi-step manual data annotation process via crowdsourcing, which involves (1) question generation (given an input sentence, turn it into a question, if possible), (2) question validation (filtering the responses collected in the previous step), and (3) expanding question variety (producing paraphrased versions of the input questions). As our second contribution, we propose four *question generation* models that, given a review as input, produce an implicit question in an end-to-end fashion. … The evaluation of our proposed approach is done against held-back test data using standard metrics for *automatic evaluation* of text generation (BLEU, ROUGE, and METEOR). … In *human evaluation* we measure the effectiveness and the capability of our model to generate questions that are suitable for preference elicitation, can be answered easily, and are grammatically correct.

**Para 5.** In summary, our main contributions in this paper are as follows: Introduce the novel task of eliciting preferences in CRSs via usage-related questions; Develop a multi-stage data annotation protocol using crowdsourcing; Introduce two template-based and two neural approaches for generating usage-related questions based on a corpus of item reviews; Develop human evaluation protocols, conduct both automatic and manual evaluation, and perform an extensive analysis of results.

#### Plant → harvest links

1. **Plant (Para 1):** CRS elicits preferences in real time using natural language.  
   **Harvest (Para 2, 4):** "implicit questions" for preference elicitation; "question generation" models.  
   **Why:** The contribution is framed as answering *how* to ask (implicit, usage-based) within the CRS task already established.

2. **Plant (Para 2):** "users … only know where or how they intend to **use** the item"; "**implicit** … related to the intended **use**."  
   **Harvest (Para 4):** "usage-related questions," "review sentences … turned into preference elicitation questions."  
   **Why:** Exact echo of "use" / "usage" and implicit vs explicit so the contribution feels like the natural solution.

3. **Plant (Para 2):** "**explicit** questions that ask about specific item attributes."  
   **Harvest (Para 4):** "implicit" question generation; contrast with "template-based" / "attribute" baselines.  
   **Why:** The gap (explicit/attribute-heavy) is named early and the harvest explicitly replaces it.

4. **Plant (Para 3):** "**usage-related experiences** … captured in **item reviews**"; "sentences … turned into … questions."  
   **Harvest (Para 4):** "multi-stage data generation protocol," "candidate sentence selection," "given a **review** as input, produce an implicit question."  
   **Why:** The data source (reviews) and the pipeline (sentence → question) are both planted and then harvested.

5. **Plant (Para 2):** "novel research objective … **implicit** attribute questions."  
   **Harvest (Para 5):** "Introduce the **novel task** of eliciting preferences in CRSs via **usage-related questions**."  
   **Why:** The opening "novel objective" is harvested verbatim in the contribution list.

**Verdict:** Strong plant→harvest. The reader is prepared for "implicit," "usage," "reviews," and "question generation" before the contribution paragraph, with clear contrast to "explicit" and "attribute" so the announcement feels inevitable.

---

### Paper 2: BIG-bench — Beyond the Imitation Game (2206.04615)

**Source:** [2206.04615.html](../../buildPaperCollection_arXiv/html_collection/2206.04615.html)

#### Introduction paragraph map

- **Opening — Epigraph:** Turing quote on the teacher being "ignorant of quite what is going on inside" (sets theme: understanding model behavior).

- **Para 1–2 — Establish importance:** Generative LMs produce text continuation; tasks can be framed as text; scaling improves performance predictably.

- **§1.1 Quantity has a quality all its own:** LMs show *qualitatively* new behavior at scale; transformative effects; need to "**understand their capabilities and limitations**" and "how those … are likely to **change as models are improved**."

- **§1.2 Limitations of current benchmarks:** "Current language-modeling benchmarks are **insufficient** … These **existing benchmarks suffer from several limitations**." Restricted scope, short lifespans, non-expert labeling.

- **§1.3 Beyond the imitation game:** "**Motivated by** the importance of predicting … effects … and **by the limitations of current benchmarks**, we introduce a **large-scale, extremely difficult and diverse** benchmark. … we call this benchmark … **BIG-bench**."

#### Full paragraphs (Introduction, key sections)

**Epigraph.** *An important feature of a learning machine is that its teacher will often be very largely ignorant of quite what is going on inside.* — A.M. Turing, *Computing Machinery and Intelligence*, 1950

**§1.1 (excerpt).** Massive increases in quantity often imbue systems with *qualitatively* new behavior. … Due to the potentially transformative effects of language models, it is vitally important that we understand their capabilities and limitations, and that we understand how those capabilities and limitations are likely to change as models are improved. This understanding will directly motivate the development of new technologies; allow us to identify and mitigate potential harmful social effects; enable us to predict other ways in which model behavior may be subtly misaligned with human intent; allow us to direct our research energies in the most promising directions; and enable us to avoid devoting research resources to problems that are likely to be solved by scale alone.

**§1.2 (excerpt).** Current language-modeling benchmarks are insufficient to satisfy our need to understand the behavior of language models and to predict their future behavior. These existing benchmarks suffer from several limitations. First, many benchmarks have restricted scope, largely targeting a single or a few capabilities on which language models have already proven some proficiency. … they are ill-suited to identify *new* and unexpected capabilities … Second, recent language-modeling benchmarks have often had short useful lifespans. … Finally, many current benchmarks use data collected through human labeling that is not performed by experts or by the task authors.

**§1.3 (excerpt).** Motivated by the importance of predicting the potentially transformative effects of large language models, and by the limitations of current benchmarks, we introduce a large-scale, extremely difficult and diverse benchmark. We then measure model performance on this benchmark. We provide a human-evaluator baseline and expert human evaluations on this diverse set of tasks, in order to measure whether model performance is broadly distinguishable from human-evaluator performance. Furthermore, models are measured across scales to facilitate a naive extrapolation of the scale at which they may be indistinguishable from human evaluators. In homage to Alan Turing's imitation game, and because we aim to extract information about model behavior beyond what is available from a binary judgement of whether a model is distinguishable from a human, we call this benchmark the Beyond the Imitation Game benchmark, or BIG-bench.

#### Plant → harvest links

1. **Plant (§1.1):** "it is vitally important that we **understand their capabilities and limitations**, and that we understand **how those capabilities and limitations are likely to change as models are improved**."  
   **Harvest (§1.3):** "We then **measure model performance** on this benchmark. … **models are measured across scales** to facilitate a **naive extrapolation** of the scale at which they may be indistinguishable from human evaluators."  
   **Why:** The need to "understand" and "predict change" is harvested as "measure" and "extrapolation."

2. **Plant (§1.2):** "Current … benchmarks are **insufficient**"; "**limitations** … restricted **scope** … short useful **lifespans** … data … not performed by **experts**."  
   **Harvest (§1.3):** "**Motivated by** … the **limitations of current benchmarks**, we introduce a **large-scale, extremely difficult and diverse** benchmark"; tasks "novel … diverse … not fully solvable by current models."  
   **Why:** Each limitation is answered: scope → large/diverse; lifespans → extremely difficult; experts → open contribution with review.

3. **Plant (§1.2):** benchmarks "ill-suited to identify **new** and **unexpected** capabilities" and "characterize the **breadth** of current capabilities."  
   **Harvest (§1.3):** "204 or more" tasks; "diverse"; "Beyond the Imitation Game" to get "information … **beyond** what is available from a binary judgement."  
   **Why:** "New," "breadth," and "beyond" are explicitly harvested in the benchmark design.

4. **Plant (epigraph):** "teacher will often be very largely **ignorant** of quite what is going on **inside**."  
   **Harvest (§1.3):** "**Beyond** the Imitation Game"; "extract **information** about model **behavior** beyond … binary judgement."  
   **Why:** The motif of understanding what is "inside" / beyond surface judgment is harvested in the benchmark name and goals.

**Verdict:** Very clear plant→harvest. The introduction names "understand capabilities and limitations," "limitations of current benchmarks," and "how behavior changes with scale," then §1.3 opens with "Motivated by" and delivers BIG-bench as the direct response.

---

### Paper 3: BLOOM — 176B-Parameter Open-Access Multilingual LM (2211.05100)

**Source:** [2211.05100.html](../../buildPaperCollection_arXiv/html_collection/2211.05100.html)

#### Introduction paragraph map

- **Para 1 — Establish trend and plant the gap:** Pretrained LMs improve with scale; "the **costs** of training large language models … are **only affordable for well-resourced organizations**. Furthermore, **until recently, most LLMs were not publicly released**. As a result, **the majority of the research community has been excluded** from the development of LLMs. This exclusion has had concrete consequences; for example, most LLMs are primarily trained on **English-language** text."

- **Para 2 — Announce present work:** "**To address these issues**, we present … **BLOOM**. BLOOM is a 176 billion parameter language model trained on **46 natural languages and 13 programming languages** that was developed and released by a **collaboration of hundreds of researchers**. … Our **overall aim** is not only to **publicly release** a large-scale **multilingual** language model … but also to **document the coordinated process** that went into its development."

#### Full paragraphs (Introduction)

**Para 1.** Pretrained language models have become a cornerstone of modern natural language processing (NLP) pipelines because they often produce better performance from smaller quantities of labeled data. The development of ELMo, ULMFiT, GPT, and BERT led to the widespread use of pretrained models as an initialization for finetuning on downstream tasks. The subsequent finding that pretrained language models can perform useful tasks without any additional training further demonstrated their utility. In addition, the empirical observation that a language model's performance tends to increase as the model is made larger—sometimes predictably and sometimes suddenly—has led to a trend of increasing scale. Apart from environmental concerns, the costs of training large language models (LLMs) are only affordable for well-resourced organizations. Furthermore, until recently, most LLMs were not publicly released. As a result, the majority of the research community has been excluded from the development of LLMs. This exclusion has had concrete consequences; for example, most LLMs are primarily trained on English-language text (with notable exceptions in Chinese and Korean).

**Para 2.** To address these issues, we present the BigScience Large Open-science Open-access Multilingual Language Model (BLOOM). BLOOM is a 176 billion parameter language model trained on 46 natural languages and 13 programming languages that was developed and released by a collaboration of hundreds of researchers. The compute for training BLOOM was provided through a French public grant from GENCI and IDRIS, leveraging IDRIS' Jean Zay supercomputer. To build BLOOM, we undertook a thorough design process for each of its components, including the training dataset, model architecture and training objective, and engineering strategy for distributed learning. We also performed an analysis of the model's capabilities. Our overall aim is not only to publicly release a large-scale multilingual language model with performance comparable to recently developed systems, but also to document the coordinated process that went into its development. The purpose of this paper is to provide a high-level overview of these design steps while referencing the individual reports we produced over the course of developing BLOOM.

#### Plant → harvest links

1. **Plant (Para 1):** "costs … **only affordable for well-resourced organizations**"; "most LLMs were **not publicly released**"; "**majority of the research community** has been **excluded**."  
   **Harvest (Para 2):** "**To address these issues**, we present … BLOOM"; "**publicly release**"; "**collaboration of hundreds of researchers**"; "open-access."  
   **Why:** Each problem (cost, no release, exclusion) is answered with open, collaborative, released model.

2. **Plant (Para 1):** "most LLMs are primarily trained on **English-language** text."  
   **Harvest (Para 2):** "trained on **46 natural languages and 13 programming languages**"; "**multilingual**."  
   **Why:** The language limitation is harvested with a concrete multilingual design.

3. **Plant (Para 1):** "**excluded** … from the **development** of LLMs."  
   **Harvest (Para 2):** "**developed and released** by a collaboration"; "**document the coordinated process** that went into its **development**."  
   **Why:** "Development" and inclusion are harvested as open development and documentation.

4. **Plant (Para 1):** "**concrete consequences**" (English-only).  
   **Harvest (Para 2):** "59 [languages] in total"; design of dataset, architecture, engineering.  
   **Why:** Consequences are addressed with concrete design choices.

**Verdict:** Very strong. Para 1 lays out "cost," "not released," "excluded," "English-only"; Para 2 starts with "To address these issues" and harvests every point with BLOOM’s open, multilingual, collaborative design.

---

### Paper 4: T5 — Unified Text-to-Text Transfer Transformer (1910.10683)

**Source:** [1910.10683.html](../../buildPaperCollection_arXiv/html_collection/1910.10683.html)

#### Introduction paragraph map

- **Para 1 — Establish pre-training / transfer:** NLP models need "general-purpose knowledge"; often learned via auxiliary task (e.g. word vectors).

- **Para 2 — Establish trend:** Pre-train entire model on data-rich task; in NLP, unsupervised pre-training on unlabeled text; "remarkable **scalability** … better performance simply by training a **larger** model on a **larger** data set."

- **Para 3 — Plant the gap and motive:** "This **synergy** has resulted in … a **wide landscape** of pre-training objectives, … benchmarks, fine-tuning methods. The **rapid rate of progress and diversity** of techniques … can make it **difficult to compare** different algorithms, **tease apart** the effects of new contributions, and **understand the space** of existing methods. **Motivated by a need for more rigorous understanding**, we leverage a **unified approach** to transfer learning that allows us to **systematically study** different approaches and **push the current limits** of the field."

- **Para 4 — Introduce text-to-text and contribution:** "The **basic idea** underlying our work is to treat every text processing problem as a **'text-to-text'** problem. … **Crucially**, the text-to-text framework allows us to use the **same** model, objective, … across our **diverse** set of tasks. … **exploring the limits** of transfer learning … by **scaling up** models and data sets."

- **Para 5 — Clarify goal and C4:** "We emphasize that our goal is **not to propose new methods** but instead to provide a **comprehensive perspective**. … we introduce the **'Colossal Clean Crawled Corpus' (C4)**."

#### Full paragraphs (Introduction, key)

**Para 3.** This synergy has resulted in a great deal of recent work developing transfer learning methodology for NLP, which has produced a wide landscape of pre-training objectives, unlabeled data sets, benchmarks, fine-tuning methods, and more. The rapid rate of progress and diversity of techniques in this burgeoning field can make it difficult to compare different algorithms, tease apart the effects of new contributions, and understand the space of existing methods for transfer learning. Motivated by a need for more rigorous understanding, we leverage a unified approach to transfer learning that allows us to systematically study different approaches and push the current limits of the field.

**Para 4.** The basic idea underlying our work is to treat every text processing problem as a "text-to-text" problem, i.e. taking text as input and producing new text as output. This approach is inspired by previous unifying frameworks for NLP tasks, including casting all text problems as question answering, language modeling, or span extraction tasks. Crucially, the text-to-text framework allows us to directly apply the same model, objective, training procedure, and decoding process to every task we consider. We leverage this flexibility by evaluating performance on a wide variety of English-based NLP problems, including question answering, document summarization, and sentiment classification, to name a few. With this unified approach, we can compare the effectiveness of different transfer learning objectives, unlabeled data sets, and other factors, while exploring the limits of transfer learning for NLP by scaling up models and data sets beyond what has previously been considered.

**Para 5.** We emphasize that our goal is not to propose new methods but instead to provide a comprehensive perspective on where the field stands. As such, our work primarily comprises a survey, exploration, and empirical comparison of existing techniques. We also explore the limits of current approaches by scaling up the insights from our systematic study (training models up to 11 billion parameters) to obtain state-of-the-art results in many of the tasks we consider. In order to perform experiments at this scale, we introduce the "Colossal Clean Crawled Corpus" (C4), a data set consisting of hundreds of gigabytes of clean English text scraped from the web. Recognizing that the main utility of transfer learning is the possibility of leveraging pre-trained models in data-scarce settings, we release our code, data sets, and pre-trained models.

#### Plant → harvest links

1. **Plant (Para 3):** "**difficult to compare** … **tease apart** the effects … **understand the space**"; "**Motivated by a need for more rigorous understanding**, we leverage a **unified approach** … to **systematically study**."  
   **Harvest (Para 4–5):** "**same** model, objective, … across … **diverse** set of tasks"; "**comprehensive perspective**"; "**systematically**" (implicit in unified framework).  
   **Why:** The need for comparison and systematic understanding is harvested as the unified text-to-text framework and comprehensive study.

2. **Plant (Para 3):** "**push the current limits** of the field."  
   **Harvest (Para 4–5):** "**exploring the limits** of transfer learning … by **scaling up** models and data sets"; "**11 billion** parameters"; "state-of-the-art results."  
   **Why:** "Limits" and scaling are explicitly harvested.

3. **Plant (Para 2):** "**larger** model on a **larger** data set"; "unlabeled text data … **en masse** … **Common Crawl**."  
   **Harvest (Para 5):** "**Colossal Clean Crawled Corpus** (C4), a data set … **hundreds of gigabytes** of **clean English text scraped from the web**."  
   **Why:** Scale and web-crawled data are harvested in C4.

4. **Plant (Para 3):** "**unified approach**."  
   **Harvest (Para 4):** "**text-to-text** … **same** model, objective, training procedure, and decoding process to **every** task."  
   **Why:** "Unified" is harvested as the text-to-text formulation.

5. **Plant (Para 5):** "**not to propose new methods** but … **comprehensive perspective**."  
   **Harvest (Para 5):** "our work **primarily comprises** a **survey, exploration, and empirical comparison** of existing techniques."  
   **Why:** The framing (survey vs new method) is planted and harvested in the same paragraph.

**Verdict:** Strong. The "difficult to compare / need for rigorous understanding / unified approach" is planted in Para 3 and harvested in Paras 4–5 with "text-to-text," "same model," "comprehensive perspective," and C4.

---

### Paper 5: Brabra et al., Identifying Breakdowns in CRSs using User Simulation (2405.14249)

**Source:** [2405.14249.html](../../buildPaperCollection_arXiv/html_collection/2405.14249.html)

#### Introduction paragraph map

- **Para 1 — Establish problem and contrast with prior work:** CRSs aim to provide personalized recommendations; "**ensuring the robustness and effectiveness** … under **any and all** of the possible situations … remains a **critical challenge**. We define a **breakdown** as a moment … where the **flow discontinues or even stops**. … Previously, the **dialogue breakdown detection challenge** … motivated research … in **chat-oriented** dialogues. … **annotated** dialogue corpora. … **labels** … do not give information on the **specific type** of breakdown. … **Our work focuses on recommendation dialogues**, i.e., **task-oriented** dialogues, that are **not annotated**. Furthermore, we aim to **identify specific breakdowns** … we propose a **novel methodology** … **via user simulation**."

- **Para 2 — Plant advantages and contribution:** "**Leveraging user simulation** has several advantages. … our **methodology** identifies **conversational paths** … that **lead to** conversational breakdowns. … we present **detectors** for three specific breakdowns: **system failure**, **dialogue of the deaf**, **conversational flow discontinuation**."

- **Para 3 — Case study:** "we present a **case study** … **breakdown detection** … on **four subsequent versions** of the CRS. … **modification** … to **reduce** the number of breakdowns, **improve** the CRS."

- **Para 4 — Summary contributions:** "**twofold**. First, we propose a **methodology** to identify conversational breakdowns. Second, we present a **case study** … **open-sourced** CRS and user simulator."

#### Full paragraphs (Introduction)

**Para 1.** Conversational recommender systems (CRSs) aim to provide personalized recommendations to user through multi-turn conversations. However, ensuring the robustness and effectiveness of these systems under any and all of the possible situations encountered while engaging with users remains a critical challenge. We define a *breakdown* as a moment in the conversation where the flow discontinues or even stops. This includes system failures and unexpected/irrelevant replies from the CRS. Examples include the CRS recommending an item without knowing what the user wants or prefers (i.e., recommendation before elicitation of the need and preferences) and the CRS repeating itself over and over. Previously, the dialogue breakdown detection challenge motivated research on breakdown detection in chat-oriented dialogues. During the challenge, an annotated dialogue corpora was provided to the participants. Note that the set of labels used does not give information on the specific type of breakdown, despite the availability of at least one detailed breakdown taxonomy. Consequently, most of the proposed solutions were supervised classification approaches determining if a (potential) breakdown occurred or not. Our work focuses on recommendation dialogues, i.e., task-oriented dialogues, that are not annotated. Furthermore, we aim to identify specific breakdowns in dialogues. Therefore, we propose a novel methodology to identify breakdowns and assess the robustness of an existing CRS via user simulation.

**Para 2.** Leveraging user simulation has several advantages. First, it is a simple, cost-effective, and efficient solution to test a CRS that supplements human evaluation. Second, it allows for a comprehensive assessment of a CRS's abilities in various scenarios and even allows for the simulation of the behavior of users with different characteristics (e.g., impatient, selective). In particular, our methodology identifies conversational paths (i.e., sequences of intents) that lead to conversational breakdowns. To achieve this, a set of conversations between the CRS and simulated users is analyzed with regards to a set of pre-defined breakdowns. As a starting point, we present detectors for three specific breakdowns to demonstrate our methodology: *system failure* (bugs), *dialogue of the deaf* (communication breakdowns between parties), and *conversational flow discontinuation* (disruptions with regards to a predefined interaction model). The identification of breakdowns in the conversational flow can provide insights to improve the robustness and effectiveness of the CRS. Furthermore, if changes to the behavior of the CRS can be made (e.g., either by updating the source code or providing it with further training examples), then the process can be repeated iteratively.

**Para 3.** To demonstrate the usefulness of our approach, we present a case study with an existing CRS and user simulator, in which the conversational breakdown detection is performed on four subsequent versions of the CRS. More specifically, after each breakdown detection, a modification is applied to the CRS based on insights extracted (i.e., conversational patterns) with the goal to reduce the number of breakdowns, hence, improve the CRS. The results show that modifying the CRS with regards to one type of breakdown reduces its presence, while also affecting the number of other types of breakdowns detected. Moreover, we note that some breakdowns stem from imperfections in the user simulator. We demonstrate that our methodology can help improve the user simulator, parallel to the CRS, thereby making it a more robust and effective tool.

**Para 4.** In summary, the main contributions of this work are twofold. First, we propose a methodology to identify conversational breakdowns in CRSs. Second, we present a case study where we apply this approach with an existing open-sourced CRS and user simulator. More specifically, we show how we improve the CRS based on the breakdowns identified.

#### Plant → harvest links

1. **Plant (Para 1):** "**breakdown** … **flow discontinues or even stops**"; "**specific type** of breakdown"; "**recommendation** dialogues … **task-oriented** … **not annotated**."  
   **Harvest (Para 1–2):** "**identify specific breakdowns**"; "**methodology** … **via user simulation**"; "**conversational paths** … that **lead to** … breakdowns"; "**detectors** for three **specific** breakdowns."  
   **Why:** "Breakdown," "specific," "task-oriented," and "not annotated" are all harvested in the proposed methodology and detectors.

2. **Plant (Para 1):** Prior work "**chat-oriented**"; "**annotated** … **labels** … do not give … **specific type**."  
   **Harvest (Para 1):** "Our work focuses on **recommendation** … **task-oriented** … **not annotated**. … **identify specific breakdowns**."  
   **Why:** Direct contrast (task-oriented, unannotated, specific types) is stated and then implemented in the contribution.

3. **Plant (Para 1):** "**novel methodology** … **via user simulation**."  
   **Harvest (Para 2–4):** "**Leveraging user simulation**"; "**methodology** … identify … breakdowns … **via user simulation**"; "case study … **user simulator**."  
   **Why:** "User simulation" is planted as the means and harvested throughout.

4. **Plant (Para 2):** "**conversational paths** … that **lead to** … breakdowns"; "**detectors** for three **specific** breakdowns."  
   **Harvest (Para 3–4):** "**case study** … **breakdown detection** … on four **subsequent versions**"; "**modification** … to **reduce** … breakdowns, **improve** the CRS"; "**methodology** to identify … breakdowns."  
   **Why:** Paths, detectors, and improvement loop are harvested in the case study and contributions.

5. **Plant (Para 1):** "**robustness and effectiveness** … **critical challenge**."  
   **Harvest (Para 2–3):** "**improve** the robustness and effectiveness"; "**reduce** the number of breakdowns."  
   **Why:** The high-level goal (robustness/effectiveness) is harvested as the outcome of the methodology.

**Verdict:** Strong. The introduction defines "breakdown," contrasts chat-oriented/annotated vs task-oriented/unannotated/specific, and plants "user simulation" and "methodology"; the same paragraph and the next harvest these in "identify specific breakdowns," "via user simulation," and the case study.

---

## Actionable insights for novice writers

*(Consolidated from all five papers.)*

### 1. Open the contribution with a backward-looking phrase

- **BLOOM:** "**To address these issues**, we present … BLOOM."
- **BIG-bench:** "**Motivated by** the importance of … and **by the limitations of current benchmarks**, we introduce …."
- **Actionable:** Start the contribution sentence with "To address this gap," "Motivated by these limitations," or "In response to this need," so the reader sees the link immediately.

### 2. Plant the exact wording you will harvest

- **Kostric et al.:** "**implicit** … **intended use**" and "**usage-related** … in **item reviews**" → harvested as "implicit questions," "usage-related questions," "review as input."
- **T5:** "**unified approach**," "**systematically study**" → harvested as "text-to-text" (unified), "comprehensive perspective."
- **Actionable:** Use the same or very close terms when you first introduce the idea and when you announce the contribution (e.g. "sole seed" → "sole title"; "limitations of current benchmarks" → "we introduce a benchmark that addresses these limitations").

### 3. One clear gap per paragraph, then one harvest per gap

- **BIG-bench:** §1.2 lists three limitations (scope, lifespans, labeling); §1.3 addresses each with BIG-bench design.
- **BLOOM:** Para 1 lists cost, no release, exclusion, English-only; Para 2 addresses each with BLOOM’s design.
- **Actionable:** Avoid overloading a single paragraph with many unrelated gaps. Prefer 1–2 gaps per paragraph and then explicitly harvest each in the contribution paragraph.

### 4. Contrast "prior/current" vs "our" in the same breath

- **Brabra et al.:** "Previously … **chat-oriented** … **annotated** … **Our work** focuses on **recommendation** … **task-oriented** … **not annotated** … **identify specific** breakdowns."
- **Kostric et al.:** "traditionally … **explicit** questions … **Our** … **implicit** questions … **intended use**."
- **Actionable:** When stating the gap, use a tight contrast (e.g. "Prior work does X; we do Y" or "Existing systems are A; we focus on B") so the harvest feels like a direct alternative.

### 5. Name the contribution early, then unpack it

- **Kostric et al.:** "The **novel research objective** of this work is to generate **implicit** attribute questions" (Para 2) → later "our main contributions" (Para 4–5).
- **Brabra et al.:** "we propose a **novel methodology** … **via user simulation**" (Para 1) → "our methodology" (Para 2), "main contributions" (Para 4).
- **Actionable:** One short sentence that states the contribution (e.g. "We propose X to do Y") early in the intro, then use the rest of the intro to justify and unpack it so the formal "contributions" list feels like a recap.

### 6. Checklist for your own introduction

1. **Backward link:** Does the first sentence of the contribution paragraph refer explicitly to what came before ("this gap," "these limitations," "to address this")?
2. **Echo:** For each key phrase in the contribution (e.g. "user simulation," "implicit questions," "unified framework"), did I use the same or very similar wording when I first introduced the idea?
3. **Gap–harvest match:** Can I list 2–4 specific gaps and point to the exact sentence(s) in the contribution that address each?
4. **Contrast:** Did I clearly contrast prior/current approach with "our" approach in one or two sentences?
5. **Early seed:** Did I state the core contribution in one sentence before the full contribution paragraph so the reader knows what to expect?

---

## Summary

Across the five papers:

- **Kostric et al.:** Plants "implicit," "usage," "reviews," and "question generation" and harvests them in the contribution and bullet list with clear contrast to "explicit" and "attribute."
- **BIG-bench:** Plants "understand capabilities and limitations" and "limitations of current benchmarks" and harvests with "Motivated by" and the design of BIG-bench (scale, diversity, difficulty, extrapolation).
- **BLOOM:** Plants "cost," "not released," "excluded," "English-only" and harvests with "To address these issues," BLOOM’s open, multilingual, collaborative design.
- **T5:** Plants "difficult to compare," "unified approach," "systematically study," "limits" and harvests with text-to-text framework, comprehensive study, C4, and scaling.
- **Brabra et al.:** Plants "breakdown," "task-oriented," "not annotated," "specific," "user simulation" and harvests in the same and next paragraphs with the methodology and case study.

**Common pattern:** State the need or gap in concrete terms (often with a contrast), use the same or echoed wording when announcing the contribution, and tie the contribution sentence explicitly to the preceding sentences ("To address …," "Motivated by …," "Our work focuses on …").
