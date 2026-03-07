# My First Draft

## Source Information

**Date written:** [7 March 2026 (final revised version)]

**Context:** [Graduate writing course assignment (Introduction and Literature Review)]

**Status:** [Final revised draft]

---

## Introduction


- Move 1: Establishing a Territory

Kernel Ridge Regression (KRR) is an important method in statistical learning. It combines the flexibility and strong generalization ability of nonparametric methods and plays an important role in fields such as image analysis, bioinformatics and finance (Smale & Zhou, 2007; Steinwart & Christmann, 2008; Caponnetto & De Vito, 2007). The regularization parameter λ is a core component of KRR, which minimizes prediction error by balancing empirical fit and model complexity. When prior information is sufficient, KRR can attain minimax-optimal learning rates by smoothness of the target function and spectral properties of the kernel integral operator (Caponnetto & De Vito, 2007; Steinwart et al., 2009). However, the challenge lies in the fact that above prior quantities related to assumptions and data characteristics are often difficult to obtain in practice. Therefore, adaptively and data-driven selection of λ is crucial and extremely challenging.

Regarding the data-driven selection of λ, the first proposed and currently most used methods are hold-out (HO) and cross-validation (CV) (Caponnetto & Yao, 2010; Steinwart et al., 2009). These methods are conceptually simple and require no secondary modification to model, gaining widespread popularity. 
Beyond data splitting, theory-driven alternatives originating in regularization and inverse-problems have gained traction. The discrepancy principle (DP) stops the regularization when residuals match a noise-informed threshold (Celisse & Wahl, 2021). Balancing and Lepskii-type procedures (LP) adapt by comparing estimators across a grid of λ, achieving near-optimal rates without data splitting (De Vito et al., 2010; Lu et al., 2020; Blanchard, Mathé & Mücke, 2019). 

As a recently proposed variant of LP method, the ASUS algorithm (Adaptive Selection with Uniform Subdivision), partitions the parameter domain uniformly and uses a sequential early-stopping rule to reduce comparisons and remove the extra logarithmic factor that often appears in Lepskii-type rates, reaching minimax-optimal performance in both L2 and RKHS norms under classical conditions (Lin, 2024). 

- Move 2: Identifying a Niche 

Despite these advances, practical limitations remain. Many adaptive methods, especially ASUS, depend on strong assumptions that are difficult to verify or are frequently violated:

• Spectral assumptions such as polynomial eigenvalue decay and capacity conditions controlling the effective dimension N(λ) (Caponnetto & De Vito, 2007; Steinwart et al., 2009; Lin, 2024).

• Source assumptions placing the target function within specific interpolation spaces or ranges of powers of the kernel integral operator (Smale & Zhou, 2007; Steinwart & Christmann, 2008).

• Reliable estimation of the noise level (for DP) or of N(λ) (for balancing/Lepskii), which is rarely available and can be unstable in finite samples (Celisse & Wahl, 2021; Lu et al., 2020).

In reality, situations that couldn’t satisfy above conditions are easy to meet, and the resulting parameter choices may not be optimal (Lin et al., 2017; Meister & Steinwart, 2016; Chang et al., 2017; Rudi et al., 2015; Fischer & Steinwart, 2020). For example, spectral attenuation may be non-polynomial or irregular, the objective function may not be in RKHS, and the dataset may be heterogeneous, semi-supervised, or distributed. Therefore, the above methods are difficult to truly implement in real-world practice. 

Furthermore, classic Lepskii-type methods typically require detailed pairwise comparisons on a grid of size M, resulting in a complexity of O(M^2) and an additional logarithmic increase in computational speed (Lu et al., 2020; Blanchard, Mathé & Mücke, 2019), further hindering their scalability. Although ASUS has bypassed pairwise comparisons and eliminated the log factor, the current analysis still relies on the strict spectral and regularity assumptions mentioned above (Lin, 2024).

- Move 3: Occupying the Niche

This study aims to bridge the gap between theoretical optimality and real application, provide a theoretically reasonable parameter selection rule for KRR. Specifically, we address the following research question: How can the ASUS algorithm be refined to achieve minimax optimal rates under significantly weaker assumptions, while maintaining or improving its computational and practical robustness?

To answer this question, we propose a refined ASUS variant designed with three key objectives:

Firstly, more relaxed spectral and regularity assumptions. The ASUS variant allowed for non-polynomial eigenvalue decay and reduced reliance on precise knowledge of the effective dimension.

Secondly, a more tractable bias-variance decomposition. The ASUS variant avoids cumbersome functional analysis mechanisms and artificial constraints on λ by adjusting the analytical framework.

Finally, stronger robustness. The ASUS variant still achieves minimax optimal rate in finite sample, heterogeneous, and distributed scenarios, and demonstrates better performance than HO and LP in small sample practice.

By fulfilling these objectives, this work seeks to provide an adaptive parameter selection rule that is both theoretically sound and readily applicable to modern, complex data environments.


---

## Literature Review


- Move 1: Thematic Overview

Adaptive selection methods for regularization parameter based on KRR can be divided into two categories. One category focuses on practicality and robustness, while the other focuses on theoretical optimality and inverse problems. The classic methods of the first category are hold-out (HO) and cross-validation (CV) (Caponnetto & Yao, 2010; Steinwart et al., 2009), which are widely used in practice due to their simplicity and model independence. The second category focuses on dynamic programming (DP) and balancing, achieving breakthroughs in minimax optimal convergence rate and inverse problems by imposing constraints on the model. 

LP methods achieve breakthroughs in balancing. By imposing additional constraints on the regularization parameter, it proves the possibility of achieving minimax optimal convergence rate for both prediction and reconstruction errors on a single λ. The ASUS algorithm, a recent variant of the LP method, utilizes uniform subdivision and sequential stopping to eliminate additional logarithmic factors and reduce the number of comparisons, achieving a minimax optimal rate under standard assumptions (Lin, 2024). The results of early stopping provide supplementary insights into data-related stopping rules (Raskutti et al., 2015).

- Move 2: Critical Analysis

Comparing HO/CV, DP, balanced/Leps macro II, and ASUS, we can find obvious trade-offs among these methods.

Firstly, sample size and convergence guarantees. While HO and CV processes are widely used, they split the data, potentially slowing convergence in small sample or high-dimensional cases. These methods are limited by theoretical guarantees of optimal convergence and can be highly sensitive to data partitioning design and model selection heuristics (Caponnetto & Yao, 2010; Steinwart et al., 2009).

Secondly, there is the issue of sensitivity to assumptions. DP is attractive due to its residual-based stopping rule, but it relies on accurate noise level estimates. What’s more, model misspecification or heteroscedasticity can lead to conservative or unstable choices (Celisse & Wahl, 2021). LP methods typically achieve near-optimal rates, but they require pairwise estimator comparisons on a λ-grid, resulting in higher computational costs in the case of refined intervals.

Thirdly, robustness. ASUS overcomes the computational bottleneck of LP. It performs sequential early stopping comparisons on a uniform distribution, achieving linear complexity under standard polynomial decay and source conditions, while obtaining a minimum-maximum optimal convergence rate (Lin, 2024). However, existing ASUS analyses rely on assumptions of standard polynomial decay and regularity, which may not hold in distributed, semi-supervised, or heterogeneous environments (Meister & Steinwart, 2016; Fischer & Steinwart, 2020; Lin et al., 2017). The gap between theory and practice indicates that existing methods are difficult to apply in real-world scenarios, and further research is needed on how to relax the restrictions on prior information.

- Move 3: Research Gaps

Gap 1: Relaxed spectral and regularity assumptions.

• Closest efforts: Balancing and Lepskii analyses provide near-optimal rates under spectral and source conditions (De Vito et al., 2010; Lu et al., 2020; Blanchard, Mathé & Mücke, 2019); ASUS removes the log-factor and reduces comparisons under polynomial eigenvalue decay and RKHS regularity (Lin, 2024).

• Unresolved: Robust adaptivity under non-polynomial spectra, weaker source conditions, and misspecification (targets outside RKHS) remains limited. Inverse learning results describe optimal rates for broad spectral filters (Blanchard & Mücke, 2018), but practical parameter selection rules with provable optimality under these weaker conditions are scarce.

• Why it matters: Kernels used in practice (e.g., data-dependent, composite, or learned kernels) can exhibit irregular spectra; insisting on polynomial decay or strict source conditions narrows applicability and risks suboptimal λ choices.

Gap 2: Reduced reliance on effective dimension and artificial λ constraints.

• Closest efforts: The effective dimension N(λ) is central to rate derivations and is often embedded in parameter rules; balancing-type procedures and ASUS analyses use N(λ) or related capacity quantities (Caponnetto & De Vito, 2007; Lu et al., 2020; Lin, 2024).

• Unresolved: Many proofs assume access to or accurate estimation of N(λ), and impose restricted λ ranges or grid designs to ensure comparisons and bounds are tractable. These requirements are unrealistic and may obscure statistical intuition. Furthermore, these requirements may be difficult to meet on heterogeneous datasets.

• Why it matters: Practitioners need methods that do not depend on delicate spectral quantities or tuned λ ranges. Simpler analyses based on concentration and bias–variance control can make adaptive rules more transparent and reliable.

Gap 3: Empirical robustness in distributed, semi-supervised, and heterogeneous environments.

• Closest efforts: Distributed and semi-supervised KRR has been analyzed under regularity and capacity assumptions (Lin et al., 2017; Chang et al., 2017). Nyström approximations connect statistical and computational regularization (Rudi et al., 2015).

• Unresolved: The systematic evaluation of adaptive parameter selection rules (such as cross-validation, dynamic programming, balanced/Lepskii, ASUS) on complex, non-independent, and distributed datasets remains limited. Existing evidence typically comes from synthetic datasets or well-behaved benchmark datasets.

• Why it matters: Real-world deployments increasingly involve federated, distributed, or partially labeled data with heterogeneity; adaptive rules must remain stable and sample-efficient under these conditions to be practically useful.

- Move 4: Conclusion of the Literature Review

This field has moved from simple but suboptimal validation methods to theoretically sophisticated adaptive algorithms like ASUS. While ASUS resolves key computational issues and achieves minimax rates, its practical impact is limited by restrictive theoretical assumptions and complex analyses. The proposed work directly targets Gaps 1 and 2 by designing a refined ASUS variant that operates under weaker spectral and regularity assumptions without relying on effective-dimension knowledge, and by providing simplified, accessible proofs. It addresses Gap 3 through comprehensive empirical validation on high-dimensional, distributed, and semi-supervised datasets. Together, these contributions aim to deliver a robust, scalable, and theoretically sound parameter selection rule for KRR that better aligns with modern practice.

---
Word count: 1486
---

## Bibliography
1. Smale S, Zhou D X. Learning theory estimates via integral operators and their approximations[J]. Constructive approximation, 2007, 26(2): 153-172.
2. Steinwart I, Christmann A. Support vector machines[M]. Springer Science & Business Media, 2008.
3. Caponnetto A, De Vito E. Optimal rates for the regularized least-squares algorithm[J]. Foundations of Computational mathematics, 2007, 7(3): 331-368.
4. Steinwart I, Hush D R, Scovel C. Optimal Rates for Regularized Least Squares Regression[C]//COLT. 2009: 79-93.
5. Caponnetto A, Yao Y. Cross-validation based adaptation for regularization operators in learning theory[J]. Analysis and Applications, 2010, 8(02): 161-183.
6. De Vito E, Pereverzyev S, Rosasco L. Adaptive kernel methods using the balancing principle[J]. Foundations of Computational Mathematics, 2010, 10(4): 455-479.
7. Lu S, Mathé P, Pereverzev S V. Balancing principle in supervised learning for a general regularization scheme[J]. Applied and Computational Harmonic Analysis, 2020, 48(1): 123-148.
8. Blanchard G, Mathé P, Mücke N. Lepskii principle in supervised learning[J]. arXiv preprint arXiv:1905.10764, 2019.
9. Lin S B. Adaptive parameter selection for kernel ridge regression[J]. Applied and Computational Harmonic Analysis, 2024, 73: 101671.
10. Celisse A, Wahl M. Analyzing the discrepancy principle for kernelized spectral filter learning algorithms[J]. Journal of Machine Learning Research, 2021, 22(76): 1-59.
11. Lin S B, Guo X, Zhou D X. Distributed learning with regularized least squares[J]. Journal of Machine Learning Research, 2017, 18(92): 1-31.
12. Chang X, Lin S B, Zhou D X. Distributed semi-supervised learning with kernel ridge regression[J]. Journal of Machine Learning Research, 2017, 18(46): 1-22.
13. Meister M, Steinwart I. Optimal learning rates for localized SVMs[J]. Journal of Machine Learning Research, 2016, 17(194): 1-44.
14. Fischer S, Steinwart I. Sobolev norm learning rates for regularized least-squares algorithms[J]. Journal of Machine Learning Research, 2020, 21(205): 1-38.
15. Rudi A, Camoriano R, Rosasco L. Less is more: Nyström computational regularization[J]. Advances in neural information processing systems, 2015, 28.
16. Zhang T. Learning bounds for kernel regression using effective data dimensionality[J]. Neural computation, 2005, 17(9): 2077-2098.
17. Raskutti G, Wainwright M J, Yu B. Early stopping and non-parametric regression: an optimal data-dependent stopping rule[J]. The Journal of Machine Learning Research, 2014, 15(1): 335-366.
18. Blanchard G, Mücke N. Optimal rates for regularization of statistical inverse learning problems[J]. Foundations of Computational Mathematics, 2018, 18(4): 971-1013.
