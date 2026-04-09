Q1.	Regarding the applications of the method you introduced, you only mentioned "image generation." Could you elaborate on more specific use cases? Can it make AI drawing faster and better? Can it be used to generate videos, design patterns, or create non-existent human faces?

Answer: 
The model I explain here is an improved variant of diffusion model. The primary use of diffusion model is image generation, extendable to tasks like image inpainting and text-to-image generation. Taking AI painting as an example, this model can indeed produce higher-quality and faster AI painting results. As for the three specific applications you mentioned. Regarding the latter two, designing patterns and creating non-existent faces are completely achievable. The generation method of diffusion model starts by sampling from a noise distribution and then performing transformations. The initial sampling results have infinite possibilities, naturally allowing the generation of previously non-existent images. As for video generation, a video itself can be seen as a series of consecutive images. Therefore, we can transform the problem into image generation guided by images or text. Thus, the three specific tasks you mentioned can all be transformed into image generation, which is precisely the main task targeted by diffusion models.

Q2. What exactly do you mean by repeatedly mentioning "improving generation efficiency"? What was slow about the original methods? Specifically, how does your method make it faster? Does it reduce the time for AI to "draw" a picture from several minutes to a few seconds?

Answer: 
Improving generation efficiency is to generate picture faster. As for idea behind model, we can take running as an analogy. Assuming the time to take one step is the same, for the same path, the number of steps needed to complete the path is reduced, thus increasing the generation speed. Previous methods were mainly slow due to randomness, forcing us to make random changes of direction while running. By reducing randomness, we can choose a straighter path, thereby achieving a speed increase. 
Regarding the specific time improvement, we generally measure it by the number of denoising steps. Here's a data point for reference: on a high-performance GPU (like an NVIDIA RTX 3090), generating a 512×512 pixel image using DPM-Solver takes about 1.5 to 2.1 seconds (20 steps). The mathematical theory of the model proposed can ensure that image quality and generation speed will not be affected, as long as the parameter training process is correct. In simulation experiments, for the same generation quality, it achieved halving the number of generation steps.

Q3.	What are those complex formulas on the poster? And what is that "learnable parameter"? How exactly does it work? Is it like giving the model an automatically adjustable "knob" so it can find a faster and better method on its own?

Answer: 
These formulas primarily illustrate the process of how we transition from a basic diffusion model to the DPM-Solver applied here and further introduce learnable parameters to provide a unified framework. The main purpose of the learnable parameters we introduce here is to achieve parameter unification for different order. The learning process for the parameters is implemented through an additionally introduced pre-training stage. In this stage, we compare the model with a more accurate model to achieve parameter learning. Therefore, unlike other data-driven algorithms, it cannot simply directly solve for the parameters and apply them. The parameters we introduce here actually need a pre-training stage.

Q4. You only conducted experiments on "two-dimensional data." Is that the same as real "image generation"? Can a method effective on simple graphics remain equally effective when generating a complex, realistic photo? How big is this gap?

Answer: The difficulty of generating 2D data distributions and generating a image are clearly not on the same level. Our simulation experiments here are merely used to preliminarily demonstrate the effectiveness of our proposed model. As for whether the model remains effective on complex image generation tasks, according to the model construction method, as long as training is completed correctly, the model's performance will not degrade. The gap lies mainly in the pre-training sage, especially on the construction of parameter learning structure and noise-related neural network.

Q5. What is the main benefit of the method? (Is it faster? Or simpler?) At the same time, what is its main shortcoming or unresolved problem? (Is it still immature, only capable of handling simple tasks?)

Answer: 
Regarding the advantages of the proposed method, both increased speed and model simplicity are achieved. However, the proposed method needs a pre-training stage, which incurs some additional computational cost.

Q6. The poster title calls this a "unified solver." What exactly does "unified" refer to? How many different methods existed originally? Were they conflicting with each other? Is your "unification" creating a new tool that can switch modes, or merging the original different methods into one?

Answer: 
Our improvements here are all based on the DPM-Solver. For this class of models, as the order increases, the ultimate generation precision also increases, while the parameter complexity also increases dramatically. Our unification here is introducing learnable parameters to unify models of different orders within the same framework.

Q7. How is the "learning" in this method implemented? Does it require feeding it a lot of extra data to "learn"? Or can it be achieved with a bit of fine-tuning on existing models? Will this increase the complexity or cost of use?

Answer: 
The learning here involves an additional pre-training stage. We adopted other, more precise integration methods to train learning parameters. In the final generation process, our parameters are the results obtained from the pre-training stage. So, unfortunately, we did not achieve a low-cost model improvement. While achieving performance improvement and model simplification, the proposed method also increased the overall computational cost.

Q8. The script mentions "dynamic noise scheduling" as a future direction. What's wrong with the current "fixed" noise scheduling? What intuitive benefits can such adjustment bring? More realistic generation, or faster?

Answer: 
The existing noise scheduling is a manually set function, commonly using a cosine form. The problem with this method is: once chosen, it's fixed and cannot adaptively adjust based on the actual situation. Therefore, I personally believe that if dynamic noise scheduling can be achieved, model preformance will be further enhanced. As for intuitive benefits, first, it can achieve higher generation precision based on its theory, meaning the images will become more exquisite. If more exquisite images can be obtained, we can often also achieve faster sampling under the same precision. But whether precision and speed can be improved equally requires further research.

Q9. The "MMD value" and "probability density curve" you used for performance comparison—how do people understand what is good or bad? For example, does a smaller MMD value represent clearer generated images? What quality of the generation results do these numbers and chart curves correspond to? More realistic, more diverse, or fewer errors?

Answer: 
The MMD is used to reflect the gap between the generated data and the original data. A smaller value indicates that the generated data is more similar to the original data distribution. From the experimental results, the generated data quality shows extremely high similarity to the original data distribution, meaning it is more realistic. As for diversity, since our training samples already encompass the major features of data distribution, we primarily focus on similarity here.

Q10. This looks like an academic study. Is its main contribution proposing a new idea, or is it already a mature tool that can be used immediately?

Answer: 
Regarding this research, our proposal focuses more on methodological practice. We made modifications based on methods proposed by others, attempting to enable it to perform better in practical applications.

Q11. The script mentions "simplifying the generation trajectory as much as possible while preserving the potential for generation accuracy." Could this be like "taking shortcuts"? Although faster, might it lead to a decrease in the quality of the final generated image or loss of detail? If not, how do you ensure that "taking shortcuts" doesn't make the generated image look rougher or less accurate?

Answer: 
Regarding the phrase "simplifying the generation trajectory as much as possible while preserving the potential for generation accuracy," what we have simplified here is the random part of the trajectory, without affecting the model's generation capability. In the relevant theoretical deduction, we can prove that compared to previous methods, the proposed randomness reduction method does not result in a decrease in generation accuracy. Essentially, they reflect the same process.

Q12. The poster mentions this work is an "improvement based on DPM-Solver." In the rapidly developing field of AI, is the improvement you propose an important breakthrough, or an incremental optimization?

Answer: 
Our improvement here is merely an incremental optimization, an attempt to improve upon methods already proposed. In the future, we might further improve this model from the perspectives of sampling acceleration and ODE solving.

Q13. The poster points out that DPM-O2-Learning unifies different versions of DPM-Solver by introducing learnable parameters. On which specific term or terms do these parameters act? Is the learning objective to directly optimize generation quality (e.g., MMD), or to optimize a proxy loss related to ODE error?

Answer: 
The learnable parameters introduced here are actually coefficients of the noise prediction function. In the image generation process, they are used to guide how we remove noise from a noisy image to obtain a better image. Here, by introducing a learnable parameter, we aim to enhance model performance. Regarding the learning objective, our fundamental goal is to improve generation performance. The implementation method involves a higher-precision generator and training the learnable parameters by comparing the loss.

Q14. The script mentions "modeling the Taylor expansion error term, rather than simply ignoring it." Can you specify how the error term O(h_i^{k+1}) is modeled? Is it parameterized, or is its upper bound estimated?

Answer: 
Our method for the error term here is to parameterize it, introducing a learnable parameter as the coefficient of the error term, thereby reintroducing the error term into the generation process.

Q15. The poster title emphasizes "A Unified Solver," and the text also mentions achieving "unification of different versions of the DPM-Solver." Does this "unification" specifically refer to unification in mathematical form (e.g., DPM-V1-O2 and DPM-V2-O2 become special cases with specific parameter values under this framework), or unification in algorithmic flow? Can you provide the unified core formula?

Answer: 
The unification here is of the model itself, focusing on unification in mathematical form, so the algorithmic flow hasn't changed significantly. Of course, to introduce learnable parameters, we have added an additional pre-training process, while retaining the original training of the noise prediction function. As for the unified formula, it is as shown in the figure.

Q16. The numerical experiments show that this method surpasses DPM-Solver on two-dimensional data distributions. Choosing low-dimensional, relatively simple distributions for initial validation is a common first step, but is this sufficient to support its effectiveness on high-dimensional complex data (like images)? The script also notes that "on more complex data distributions like images, the model's performance still requires further testing." Are there preliminary plans or ideas to extend it to image generation tasks?

Answer: 
From an experimental perspective, results obtained from experiments on simple 2D data distributions cannot be directly transferred to image tasks. However, combined with the model construction theory, as long as the pre-training process is correct, the performance of the proposed model will not degrade. 
There are plans to extend it to image domain in the future. The biggest challenge is modifying the pre-training stage. While it performs well in simple cases, for complex images, we must update the pre-trained model.

Q17. Which specific version (e.g., DPM-Solver++?) and which order (O1, O2, O3) does the "DPM-Solver" compared in the experiments refer to? As the sampling efficiency and accuracy of different orders and versions inherently differ, clear baseline comparisons are crucial.

Answer: 
Depending on the prediction function, DPM-Solver is specifically divided into DPM-Solver and DPM-Solver++; essentially, they represent the same process. Therefore, for each order model, we have two corresponding baseline models. The comparison model is the second-order model with learnable parameters introduced.

Q18. Does introducing learnable parameters incur additional training or fine-tuning costs? Are these parameters learned separately for each specific noise schedule or each dataset, or are they expected to learn a relatively general adjustment strategy?

Answer: 
To introduce learnable parameters, we need to additionally introduce a pre-training stage for parameter learning. Therefore, it incurs additional training and computational costs. However, the learnable parameters are used in solver itself, so what is learned is a relatively general adjustment. Therefore, for the same order model and the same dataset, even if we use different numbers of generation steps, we do not need to retrain; we can directly apply the adjusted parameters.

Q19. The discussion section mentions that the learnable parameters rely on the calculation of gradient integrals, and calculating their actual values using Riemann sums which introduces errors. Has the use of more precise integration approximation methods been considered, or how much impact does this error show in experiments?

Answer: 
During the experiments, we introduced a more precise solver to train the learnable parameters. Here, we are only exploring model validity and chose the Riemann sum calculation. Errors originating from the calculation method directly affect parameter training, thereby impacting model performance. The larger the calculation method's own error, the less accurate the adjusted parameters, and the worse the model performance we have.

Q20. What is the fundamental difference between the framework you propose and other fast ODE solvers like "DPM-Solver++"? Where are the main advantages demonstrated?

Answer: 
If we talk about fundamental differences, none have actually been achieved. We merely introduced learnable parameters to optimize the solver, thereby achieving more precise solving and a unified framework.

Q21. The end of the script mentions that "exploring dynamic noise scheduling" is a key future focus. How does your learnable parameter framework combine with dynamic noise scheduling? Is the idea to make the parameters adaptive to dynamic scheduling, or to treat the two as independent improvement directions?

Answer: 
Regarding dynamic noise scheduling, the current idea is that we could consider matching the design of noise scheduling with our current image generation process. In the early stages, we might need noise that changes rapidly; in the later stages, we might need noise that changes slowly and more precisely. Previous methods directly constructed such functions, but why don't we directly control noise based on the process itself? As for the specific combination method, currently planned to be adjusted simultaneously with learnable parameters during the pre-training stage. For example, during parameter learning, treat noise scheduling also as parameters needing to be learned, but it should be time-dependent, and the model in the pre-training stage needs modification.

Q22. Is the unified framework you propose mathematically general? That is, can it strictly derive or encompass all existing higher-order forms of DPM-Solver (e.g., O3), or has it currently only been verified for the O2 (second-order) case? What are the main theoretical obstacles to extending from "unification" to "higher-order solvers"?

Answer: 
The proposed unified framework is mathematically general; it can completely cover the general form of DPM-Solver. The main difficulty lies in how to precisely adjust the learnable parameters.

Q23. For the MMD value used in quantitative evaluation, which specific kernel function is used (e.g., Gaussian kernel)? How is its bandwidth parameter chosen? Because the MMD value is relatively sensitive to the choice of kernel function; different choices may affect the judgment of performance superiority.

Answer: 
The bandwidth parameter here is manually specified; no related analysis was conducted. However, to avoid overly relying on the MMD value to judge generation results, we also performed visualization of the data distribution for auxiliary judgment.

Q24. Is the performance of your method sensitive to the starting point of the reverse process (i.e., the initial noise sample) or minor changes in the noise schedule? Has robustness testing been conducted, for example, observing the impact of different initial noises or slight perturbations to the noise schedule curve on the final generation quality and consistency under the same number of steps?

Answer: 
The method we studied here is not sensitive to the starting point, i.e., the initial noise sample. However, it is sensitive to the noise schedule and the integration model. The former directly affects the parameter training method, and the latter directly limits the performance of parameter learning. If we choose an incorrect noise schedule, then even after training, the results we obtain might still be inferior to an unadjusted model using a more effective schedule. Therefore, this is also why we finally mentioned that dynamic noise scheduling could be further considered.
