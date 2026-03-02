# Causal Graph Regression Paper — Macro-Level Structure Analysis

**Paper Title**: A Recipe for Causal Graph Regression: Confounding Effects Revisited  
**Authors**: Yujia Yin, Tianyi Qu, Zihao Wang, Yifan Chen  
**Venue**: ICML 2025 (PMLR 267), Vancouver  
**Field**: Machine Learning / Graph Neural Networks / Causal Learning / OOD Generalization  
**Structure Type**: IMRaD (Introduction, Related Work, Preliminaries, Method, Experiments, Ablation & Conclusion)

---

## Overall Macro-Level Assessment

### Structural Framework
**IMRaD Adaptation**: Introduction → Related Work → Preliminaries & Notations → Revisiting Confounding Effects (Method) → Experiments → Ablation & Discussion  
- **Total Length**: ~9 pages + appendices (conference format)  
- **Citation Style**: Author-year (e.g. Sui et al., 2022; Pearl, 2014)  
- **Disciplinary Conventions**: Heavy emphasis on causal/structural formalism (SCM, GIB, mutual information), OOD benchmarks, and ablations  
- **Rhetorical Style**: Gap (CGL largely classification-only; confounders assumed non-predictive) → Method (enhanced GIB + contrastive intervention) → Empirical validation  

### Hourglass Flow Analysis
**General → Specific → General**:
- **Introduction**: Broad relevance of CGL (drug discovery, climate) → Specific gap (regression overlooked; confounders’ predictive role) → Contributions  
- **Related Work**: OOD/graph learning landscape → Invariant / causal / stable learning → Gaps (classification-focused; confounders ignored)  
- **Preliminaries**: General CGL/GIB/intervention concepts → Formal definitions  
- **Method**: High-level overview → Enhanced GIB → Contrastive causal intervention  
- **Experiments**: Datasets & baselines → GOOD-ZINC & ReactionOOD results → Ablations → General implications  

---

## Section-by-Section Macro Analysis

### Section 1: Introduction (CARS Model Application)

#### Move 1: Establishing Territory (Paragraphs 1–2)
**Content**: Centrality of causal graph learning (CGL) for OOD generalization; relevance to drug discovery, climate modeling.  
**Strengths**:
- Clear application domains
- Causal vs. spurious distinction (Figure 1: C, S, Y)

**Excerpt**: "Causal graph learning (CGL) (Lin et al., 2021) holds particular importance due to its relevance in fields such as drug discovery (Qiao et al., 2024) and climate modeling (Zhao et al., 2024)."

**Excerpt**: "The core methodology of causal learning involves the identification and differentiation of causal features from confounding ones. As shown in Figure 1, causal features C are those directly deciding responses Y, whereas confounding features S (shorthand for 'spurious') solely present spurious correlations."

**Analysis**: Establishes importance and previews SCM. Connects CGL to real-world applications.

#### Move 2: Establishing Niche (Paragraphs 3–5)
**Content**: CGL successes are mostly in **classification**; **regression** (property prediction, traffic forecasting, credit risk) is overlooked. Vanilla extension to regression underperforms ERM. Confounders assumed **non-predictive** in prior work, but real-world (e.g. molecular weight vs. toxicity) shows otherwise.  
**Strengths**:
- Concrete gap: classification vs. regression; finite vs. infinite support
- Critique of “confounders = pure noise” assumption with domain example

**Excerpt**: "However, previous CGL studies focus on classification settings. Some of them cannot be directly extended to regression tasks, such as property prediction (Rollins et al., 2024), traffic flow forecasting (Li et al., 2021), and credit risk scoring (Ma et al., 2024), because the transition from finite to infinite support makes discrete labels unavailable. Graphs thus cannot be informatively grouped. A systematical understanding of how CGL techniques should be adapted to graph-level regression is still under-explored."

**Excerpt**: "Existing CGL methods, such as CAL (Sui et al., 2022) and DisC (Fan et al., 2022), are built on a strong assumption that confounding subgraphs contain strictly no predictive power. We reflect on this assumption and speculate it is hardly practical due to the contradiction with real-world observations: in molecular property prediction, for example, molecular weight is noncausal to toxicity while does exhibit strong correlations."

**Analysis**: Two-pronged gap—(1) regression underexplored, (2) confounder assumption unrealistic—with concrete examples.

#### Move 3: Occupying Niche (Paragraphs 6–7)
**Content**: Enhanced GIB (no longer assuming confounders non-predictive); generalize intervention from class separation to **instance discrimination** via **contrastive learning**; new CGR framework. Three bullet-point contributions.  
**Strengths**:
- Explicit contribution list
- “To the best of our knowledge” + first to consider predictive role of confounders in graph regression

**Excerpt**: "In this work, we develop an enhanced graph information bottleneck (GIB) loss function, which no longer takes the strong assumption. Moreover, some confounding effect processing techniques, such as backdoor adjustment (Sui et al., 2022; 2024) and counterfactual reasoning (Guo et al., 2025), heavily rely on discrete label information and cannot be adapted to regression at all. We follow the principle of those methods and generalize it from class separation to instance discrimination; the discrimination principle aligns with the philosophy of contrastive learning (CL) and CL techniques are therefore leveraged to tackle CGR in our proposal."

**Excerpt**: "In summary, our contributions are as follows: • To the best of our knowledge, we are the first to explicitly consider the predictive role of confounding features in graph regression tasks, a critical yet overlooked aspect in graph OOD generalization. • We introduce a new causal intervention approach that generates random graph representations by leveraging a contrastive learning loss to enhance causal representation, outperforming label-dependent methods. • Extensive experiments on OOD benchmarks demonstrate that our method significantly improves generalization in graph regression tasks."

**Analysis**: Clear positioning: enhanced GIB + contrastive intervention; contributions explicitly enumerated.

#### Key Linguistic Features
- **Nominalization**: “identification,” “differentiation,” “disentanglement”  
- **Technical terminology**: GIB, SCM, mutual information, backdoor adjustment, contrastive learning  
- **Hedging**: “we speculate,” “hardly practical”  

---

### Section 2: Related Work (Literature Review)

#### Move 1: Thematic Overview
**Content**: OOD in graph learning; categorizes **invariant learning**, **causal modeling**, **stable learning**.  
**Strengths**:
- Clear taxonomy
- Links invariant learning to causality (e.g. Wang & Veitch, Mitrovic et al.)

**Excerpt**: "Out-of-distribution (OOD) challenges in graph learning has drawn significant attention, particularly in methods aiming to disentangle causal and confounding factors (Ma, 2024). Existing approaches can be broadly categorized into invariant learning (Wu et al., 2022a), causal modeling (Sui et al., 2024), and stable learning (Li et al., 2022)."

#### Move 2: Critical Analysis
**Content**: Invariant learning (CIGA, GSAT, GALA) → **classification-oriented**; post-hoc explainers (PGExplainer, RegExplainer) do not learn invariants **during** training. Causal methods (CAL, CAL+, DSE, RCGRL, DisC) use backdoor/frontdoor/IV/counterfactuals but **disregard predictive potential of confounders** and use **classification-tailored** losses. Stable learning (e.g. StableGNN) relies on **heuristic reweighting**.  
**Strengths**:
- Systematic critique per category
- Explicit limitation: “they often disregard the predictive potential of confounding features”

**Excerpt**: "However, these approaches are typically designed for classification tasks, limiting their out-of-distribution (OOD) generalization capability in regression settings. Post-hoc methods, such as PGExplainer (Luo et al., 2020) and RegExplainer (Zhang et al., 2023), attempt to discover invariant subgraphs after training. However, these methods fail to equip the model with the ability to learn invariant representations during the training process."

**Excerpt**: "By simulating causal interventions through supervised training, these methods aim to achieve OOD generalization. However, they often disregard the predictive potential of confounding features, which hinders effective disentanglement. Moreover, the supervised loss functions tailored for classification tasks are not easily adaptable to regression problems, as the inherent complexity of regression introduces additional challenges."

**Analysis**: Gaps emerge through structured critique: classification bias, post-hoc only, confounders ignored, regression-specific challenges.

#### Move 3: Traditional ML & Regression
**Content**: Brief mention of non-graph work (e.g. Pleiss et al., Amini et al.) on causality in regression—low-dimensional causal subspace, evidence priors.  
**Analysis**: Positions graph CGR within broader regression+causality landscape.

---

### Section 3: Preliminaries and Notations (3.1–3.3)

#### 3.1 Causal Graph Learning
**Content**: Graph \(G = (A, X)\); causal vs. confounding subgraphs \(C\), \(S\); learnable masks; mutual information \(I(C; G)\).  
**Excerpt**: "C := (Medge ⊙ A, Mnode · X) ... The confounding subgraph is then the 'complement': S := G − C."

**Excerpt**: "Notably, mutual information plays an essential role in CGL... I(C; G) := E_{C,G}[log p(C|G)/p(C)]."

#### 3.2 Graph Information Bottleneck
**Content**: IB → GIB; objective \(-I(C;Y) + \alpha I(C;G)\); compression vs. prediction trade-off.  
**Excerpt**: "Formally, the GIB objective is expressed as: −I(C; Y) + αI(C; G), where I(C; Y) quantifies the predictive information retained by C (and thus needs to maximize). I(C; G) serves as a regularizer to exclude irrelevant details from the original graph."

#### 3.3 Causal Intervention in GNNs
**Content**: SCM (Figure 1); backdoor path \(S \rightarrow C \rightarrow Y\); backdoor adjustment \(P(Y|do(C))\) via \(P(Y|C,S)\).  
**Excerpt**: "In causal inference, confounder S incurs spurious correlations, preventing the discovery of underlying causality. To address this issue, backdoor adjustment methods focus on the interventional effect P(Y|do(C)), and suggest to estimate it by stratifying over S and calculating the conditional distribution P(Y|C, S) (Pearl, 2014; Sui et al., 2024)."

**Analysis**: Standard CGL formalism; sets up enhanced GIB and contrastive intervention in Section 4.

---

### Section 4: Revisiting Confounding Effects for CGR (Method)

#### 4.1 Overview
**Content**: Pipeline (Figure 2): GNN encoder → attention masks → causal/confounding subgraphs → \(G_c\), \(G_s\) → readouts; **enhanced GIB** \(L_{GIB}\); **contrastive causal intervention** \(L_{CI}\).  
**Excerpt**: "The optimization features an enhanced graph information bottleneck (GIB) loss \(L_{GIB}\), comprising the causal part \(L_c\) and the confounding part \(L_s\), to disentangle causal signals... Also, counterfactual samples (\(H_{mix,ij}\)) are generated by randomly injecting confounding representations into causal ones; unsupervised learning is then performed, guided by contrastive-learning-based causal intervention loss \(L_{CI}\)."

#### 4.2 Enhanced GIB Objective
**Content**: Original GIB assumes \(S\) non-predictive; **enhanced GIB** models **predictive role of \(S\)**, adding \(-βI(S;Y)\). Variational bounds for \(I(C;G)\), \(I(C;Y)\), \(I(S;Y)\); reduces to least-squares-style terms \(L_{CP}\), \(L_{SP}\).  
**Excerpt**: "Original GIB assumes the confounding subgraph S is pure noise and cannot predict the response Y (Chen et al., 2022), while as we discussed in Section 1 S may still contain information that is predictive of the response Y. In its current form, the GIB framework overlooks this aspect, causing the model to allocate all Y-relevant information to C and to potentially lose meaningful content."

**Excerpt**: "Overall, our enhanced GIB objective is defined as follows: −I(C; Y) + αI(C; G) − βI(S; Y), which formally extends the original GIB objective by introducing a confounder-related term I(S; Y) to capture the predictive capacity of S, along with a parameter β."

**Analysis**: Directly addresses “confounders non-predictive” assumption; clearly extends GIB.

#### 4.3 Causal Intervention (Contrastive)
**Content**: Random pairing of confounders with causal subgraphs → \(H_{mix,ij} = H_{c,i} + H_{s,j}\). Avoids forcing mixed graph to discard all confounders; instead **contrastive learning**: positive pair \((H_g, H_{mix})\), negatives other graphs. InfoNCE-style \(L_{CI}\). Total loss \(L = L_{GIB} + λ L_{CI}\).  
**Excerpt**: "To mitigate this issue, we suggest learning causal representations through contrastive learning. Specifically, the causal subgraph, when combined with different confounding subgraphs, consistently produces mixed graph representations that are aligned with the original graph representation. This formulation enables the model to learn causal subgraphs that are invariant across varying confounders."

**Excerpt**: "Remark 4.1. The ultimate loss used in our paradigm is a simple combination of the GIB objective and the causal intervention loss: L = L_{GIB} + λ L_{CI}."

**Analysis**: Translates intervention idea from classification to regression via contrastive learning; no discrete labels required.

---

### Section 5: Experiments

#### 5.1–5.2 Datasets & Baselines
**Content**: **GOOD-ZINC** (Scaffold/Size × Covariate/Concept); **ReactionOOD** (Cycloaddition, RDB7, E2&SN2). Baselines: ERM, IRM, VREx, Mixup, DANN, CORAL, CIGA, GSAT, DIR.  
**Excerpt**: "GOOD-ZINC includes four specific OOD types: Scaffold-Covariate, Scaffold-Concept, Size-Covariate, and Size-Concept. Scaffold OOD involves changes in molecular structures, while Size OOD varies graph size."

#### 5.3 Results on GOOD-ZINC
**Content**: Proposed method **SOTA** on GOOD-ZINC; substantial gains over GSAT and others in both ID and OOD MAE.  
**Excerpt**: "As shown in Table 1, our proposed method achieves SOTA performance on GOOD-ZINC, consistently outperforming all baseline methods across both domains (Scaffold and Size) and under different distribution shifts (Covariate and Concept)."

**Excerpt**: "For instance, in the Scaffold domain under the Covariate shift, our method achieves an MAE of 0.0514±0.0061 (ID) and 0.1046±0.0007 (OOD), outperforming GSAT, the next-best method, by 42.2% in ID and 26.3% in OOD performance. Similarly, under the Concept shift, our method achieves 0.0659±0.0041 (ID) and 0.0518±0.0007 (OOD), representing improvements of 29.0% and 48.1%, respectively, over GSAT."

**Excerpt**: "In addition to achieving lower MAE values, our method exhibits significantly reduced variances compared to other approaches, highlighting its stability under diverse conditions."

#### 5.4 Results on ReactionOOD
**Content**: Best or second-best OOD in most settings; when second, gap small. RDB7: best OOD under concept shift; E2&SN2: best under covariate shift, competitive under concept.  
**Excerpt**: "Our method achieves the best OOD performance in 6 out of 10 cases and ranks second in 2 cases. Notably, in cases where another method outperforms ours, the performance gap is within a small margin."

**Excerpt**: "In RDB7, a smaller dataset... our method achieves the lowest OOD RMSE (15.73 ± 0.37) under the concept shift. Our method's principled focus on true causal features... leads to better OOD generalization ability and stability."

**Excerpt**: "As noted in OOD-GNN (Tajwar et al., 2021), no method consistently performs best on every dataset due to varying distribution shifts and inductive biases. Our approach, designed under more general and weaker assumptions which do not assume that spurious features are non-predictive, aims to tackle a wider range of real-world distribution shifts."

#### 5.5 Ablation (GOOD-Motif Classification)
**Content**: Ablations on **enhanced GIB** (predictive confounders) and **\(L_{CI}\)** (contrastive intervention). Ignoring confounders’ predictive role hurts OOD; contrastive intervention effective also in classification.  
**Excerpt**: "The results show that ignore the predictive role of confounding subgraphs leads to incomplete disentanglement and weaker OOD generalization, demonstrating that accounting for their influence is crucial."

**Excerpt**: "The results show that our contrastive learning approach, initially validated in regression tasks, is equally effective in classification tasks, highlighting its general applicability."

**Excerpt**: "These studies confirm the importance of explicitly modeling confounding subgraphs and the robustness of our contrastive learning loss for OOD generalization."

---

## Cross-Disciplinary Comparison

| Aspect | This Paper (ML / GNN) | Traditional Academic |
|--------|------------------------|----------------------|
| **Literature Review** | Dedicated section; taxonomy (invariant / causal / stable) | Often integrated in introduction |
| **Technical Detail** | High (GIB, SCM, variational bounds, loss equations) | Medium (methods overview) |
| **Evaluation** | OOD benchmarks, multiple datasets, ablations, MAE/RMSE | Theoretical or small-scale empirical |
| **Contribution Claims** | Method (enhanced GIB + contrastive intervention) + empirical validation | Theoretical advance + evidence |
| **Formalism** | SCM, mutual information, contrastive learning | Less formal notation |

### Key Learning Points for Imitation

1. **Reframing assumptions**: Explicitly question “confounders = non-predictive”; support with domain examples.  
2. **Bridge classification → regression**: Generalize class separation to instance discrimination via contrastive learning.  
3. **Modular method**: Separate GIB vs. intervention; clearly state total loss (\(L = L_{GIB} + λ L_{CI}\)).  
4. **OOD breadth**: Multiple benchmarks (GOOD, ReactionOOD), shift types, and ablations.  
5. **Transparency**: Code/publication link (e.g. GitHub); discuss limitations (e.g. no method wins everywhere).  

---

## Imitation Opportunities for Future Papers

### Structural Elements to Adapt
- **Enhanced objective**: Extend a standard objective (e.g. GIB) by relaxing a key assumption and adding interpretable terms.  
- **Contrastive intervention**: Replace label-dependent intervention with contrastive objectives for regression.  
- **Two-part loss**: Clear separation of “representation” vs. “intervention” terms.  
- **Ablations**: Isolate enhanced objective vs. intervention; optionally test on classification to show generality.  

### Rhetorical Strategies
- **Gap via assumption critique**: “Prior work assumes X; we argue X is unrealistic because …”  
- **“To the best of our knowledge”**: Claim novelty (e.g. first to consider predictive confounders in graph regression).  
- **Explicit contribution list**: Numbered bullets.  
- **Benchmark diversity**: Multiple OOD types and datasets; acknowledge “no single winner” where appropriate.  

### Quality Indicators
- **Formal clarity**: SCM, objectives, and losses spelled out.  
- **Empirical coverage**: ID/OOD, multiple shifts, ablations.  
- **Code/data**: Public implementation.  
- **Limitations**: E.g. dataset-specific performance, heuristic choices.  

---

## Key Excerpts from Original Paper

### Introduction
- **Centrality**: "Causal graph learning (CGL) (Lin et al., 2021) holds particular importance due to its relevance in fields such as drug discovery (Qiao et al., 2024) and climate modeling (Zhao et al., 2024)."  
- **Gap (regression)**: "A systematical understanding of how CGL techniques should be adapted to graph-level regression is still under-explored."  
- **Gap (confounders)**: "Existing CGL methods... are built on a strong assumption that confounding subgraphs contain strictly no predictive power... in molecular property prediction, for example, molecular weight is noncausal to toxicity while does exhibit strong correlations."  
- **Contributions**: "To the best of our knowledge, we are the first to explicitly consider the predictive role of confounding features in graph regression tasks... We introduce a new causal intervention approach... Extensive experiments on OOD benchmarks demonstrate that our method significantly improves generalization."  

### Related Work
- **Invariant vs. regression**: "However, these approaches are typically designed for classification tasks, limiting their... generalization capability in regression settings."  
- **Causal methods**: "However, they often disregard the predictive potential of confounding features, which hinders effective disentanglement. Moreover, the supervised loss functions tailored for classification tasks are not easily adaptable to regression problems."  

### Method
- **Enhanced GIB**: "Overall, our enhanced GIB objective is defined as follows: −I(C; Y) + αI(C; G) − βI(S; Y)."  
- **Contrastive intervention**: "We suggest learning causal representations through contrastive learning... the causal subgraph, when combined with different confounding subgraphs, consistently produces mixed graph representations that are aligned with the original graph representation."  
- **Total loss**: "L = L_{GIB} + λ L_{CI}."  

### Experiments
- **GOOD-ZINC**: "Our proposed method achieves SOTA performance on GOOD-ZINC... outperforming GSAT... by 42.2% in ID and 26.3% in OOD" (Scaffold Covariate).  
- **ReactionOOD**: "Our method achieves the best OOD performance in 6 out of 10 cases and ranks second in 2 cases."  
- **Ablation**: "Ignore the predictive role of confounding subgraphs leads to incomplete disentanglement and weaker OOD generalization... Our contrastive learning approach... is equally effective in classification tasks."  

### Limitation / Scope
- "No method consistently performs best on every dataset due to varying distribution shifts and inductive biases. Our approach... aims to tackle a wider range of real-world distribution shifts."  

---

*Analysis follows the macro-level structure framework (activity 1.2) and KellerInsights.md style. Emphasis on section-by-section moves, technical formalism, and **excerpts from the original paper**.*
