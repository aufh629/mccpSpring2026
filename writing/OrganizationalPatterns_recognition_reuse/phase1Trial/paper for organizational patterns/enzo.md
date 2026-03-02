[skip to main content](https://dl.acm.org/doi/10.1145/3705328.3748053#skip-to-main-content)

* [![ACM Digital Library home](https://dl.acm.org/specs/products/acm/releasedAssets/images/acm-dl-logo-white-1ecfb82271e5612e8ca12aa1b1737479.png)](https://dl.acm.org/)
* [![ACM Association for Computing Machinery corporate logo](https://dl.acm.org/doi/10.1145/specs/products/acm/releasedAssets/images/acm-logo-1.png)](https://www.acm.org/ "external site link")

[![](https://dl.acm.org/pb-assets/images/basic-edition-1765756198880.png)](https://dl.acm.org/premium "Basic Edition, Upgrade")

* [Sign in](https://dl.acm.org/action/showLogin?redirectUri=%2Fdoi%2F10.1145%2F3705328.3748053)
* [Register](https://accounts.acm.org/?redirectUri=%2Fdoi%2F10.1145%2F3705328.3748053 "Register")
* [Journals](https://dl.acm.org/journals)
* [Magazines](https://dl.acm.org/magazines)
* [Proceedings](https://dl.acm.org/proceedings)
* [Books](https://dl.acm.org/acmbooks)
* [SIGs](https://dl.acm.org/sigs)
* [Conferences](https://dl.acm.org/conferences)
* [Institutions](https://dl.acm.org/institutions)
* [People](https://dl.acm.org/people)

Search ACM Digital Library[ ]

* [Conference](https://dl.acm.org/conference/recsys)
* [Proceedings](https://dl.acm.org/conference/recsys/proceedings)
* [Upcoming Events](https://dl.acm.org/conference/recsys/upcoming)
* [Authors](https://dl.acm.org/conference/recsys/authors)
* [Affiliations](https://dl.acm.org/conference/recsys/affiliations)
* [Award Winners](https://dl.acm.org/conference/recsys/award-winners)

Several features on this page require Premium Access.

[Learn more](https://dl.acm.org/about/upgrade)[Sign in](https://dl.acm.org/action/showLogin?redirectUri=%2Fdoi%2F10.1145%2F3705328.3748053)

* [Home](https://dl.acm.org/)
* [Conferences](https://dl.acm.org/conferences)
* [RECSYS](https://dl.acm.org/conference/recsys)
* [Proceedings](https://dl.acm.org/conference/recsys/proceedings)
* [RecSys &#39;25](https://dl.acm.org/doi/proceedings/10.1145/3705328)
* [A Language Model-Based Playlist Generation Recommender System](https://dl.acm.org/doi/10.1145/3705328.3748053)

[Click here](https://dl.acm.org/action/clickThrough?id=108253&url=https%3A%2F%2Fwww.acm.org%2Fabout-acm%2Facm-pres-on-oa-transition-and-dl-changes&loc=%2Fdoi%2F10.1145%2F3705328.3748053&pubId=63796627&placeholderId=101024&productId=108184) to read ACM President Yannis Ioannidis’ statement on recent changes to the Digital Library

research-article

Open access

[](https://creativecommons.org/licenses/by/4.0/ "Creative Commons License (CC BY 4.0)")

Share on* [](https://dl.acm.org/#x "share on X")

* [](https://dl.acm.org/#linkedin "share on LinkedIn")
* [](https://dl.acm.org/#reddit "share on Reddit")
* [](https://dl.acm.org/#facebook "share on Facebook")
* [](https://dl.acm.org/#email "share via email")

# A Language Model-Based Playlist Generation Recommender System

**Authors**: [![](https://dl.acm.org/pb-assets/icons/DOs/default-profile-1543932446943.svg)Enzo Charolois-Pasqua](https://dl.acm.org/doi/10.1145/3705328.3748053# "Enzo Charolois-Pasqua"), [![](https://dl.acm.org/pb-assets/icons/DOs/default-profile-1543932446943.svg)Eléa Vellard](https://dl.acm.org/doi/10.1145/3705328.3748053# "Eléa Vellard"), [![](https://dl.acm.org/pb-assets/icons/DOs/default-profile-1543932446943.svg)Youssra Rebboud](https://dl.acm.org/doi/10.1145/3705328.3748053# "Youssra Rebboud"), [![](https://dl.acm.org/action/showDoPubAsset?doi=10.1145/contrib-99658974260&format=rel-imgonly&assetId=face_square.jpg)Pasquale Lisena](https://dl.acm.org/doi/10.1145/3705328.3748053# "Pasquale Lisena"), [![](https://dl.acm.org/action/showDoPubAsset?doi=10.1145/contrib-81100211183&format=rel-imgonly&assetId=raphael.jpg)Raphaël Troncy](https://dl.acm.org/doi/10.1145/3705328.3748053# "Raphaël Troncy")[Authors Info &amp; Claims](https://dl.acm.org/doi/10.1145/3705328.3748053#)

[RecSys &#39;25: Proceedings of the Nineteenth ACM Conference on Recommender Systems](https://dl.acm.org/doi/proceedings/10.1145/3705328)

Pages 1 - 11

[https://doi.org/10.1145/3705328.3748053](https://doi.org/10.1145/3705328.3748053)

**Published**: **07 September 2025** [Publication History](https://dl.acm.org/doi/10.1145/3705328.3748053#)[](https://dl.acm.org/doi/10.1145/3705328.3748053# "Check for updates on crossmark")

[](https://dl.acm.org/doi/10.1145/3705328.3748053#)

[](https://dl.acm.org/doi/10.1145/3705328.3748053#)

[PDF/eReader](https://dl.acm.org/doi/epdf/10.1145/3705328.3748053)

AbstractAI Summary

The title of a playlist often reflects an intended mood or theme, allowing creators to easily locate their content and enabling other users to discover music that matches specific situations and needs. This work presents a novel approach to playlist generation using language models to leverage the thematic coherence between a playlist title and its tracks. Our method consists in creating semantic clusters from text embeddings, followed by fine-tuning a transformer model on these thematic clusters. Playlists are then generated considering the cosine similarity scores between known and unknown titles and applying a voting mechanism. Performance evaluation, combining quantitative and qualitative metrics, demonstrates that using the playlist title as a seed provides useful recommendations, even in a zero-shot scenario.

## 1 Introduction

In the era of personalized digital experiences, recommender systems have become crucial for delivering content tailored to individual tastes. These systems use advanced algorithms and data analytics to understand user preferences and behaviors, making each interaction uniquely relevant. Music platforms, in particular, rely heavily on recommender systems to enhance user engagement and satisfaction by suggesting songs and artists that align with a user’s listening habits and favorite genres.

However, creating tailored playlists remains a challenging and time-consuming task for users. Crafting a playlist that captures the right mood, includes a diverse yet cohesive selection of tracks, and adapts to different listening contexts requires significant effort. Users must manually search for songs, consider the sequence and flow of the playlist, and continuously update it to keep it fresh and engaging. This process can be overwhelming, especially for those with large music libraries or eclectic tastes.

Apart from the tracks, another distinctive characteristic of a playlist is its title. Previous studies have demonstrated that the playlist titles significantly influence users’ expectations, playing a crucial role in their selection process [[17](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0017)]. Moreover, playlists, and even private ones, have generally meaningful titles that reflect their content, mood, genre, or the context in which they were created, such as a specific situation, event, or purpose. As a result, it is common to find similarities in the titles of playlists created by different users, who often include words like “workout”, “gaming”, or “wedding” to indicate the playlist’s purpose [[14](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0014)]. For these reasons, the playlist title can be a key element in recommender systems, specifically if the title reveals a commonsense theme rather than being personal [[28](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0028)]. First, it can serve as the sole seed element to suggest songs for an empty playlist in a *cold start* scenario. Secondly, it can enhance other types of recommender systems (e.g., collaborative-based) by adding a semantic constraint for proposing subsequent songs.

While it is true that titles like those mentioned in the previous paragraph may have abundant ready-made materials, e.g. by streaming services, a user may instead want to have a playlist named “Housewarming Party”, “Spring awakening”, or “Country summer”[^1^](https://dl.acm.org/doi/10.1145/3705328.3748053#fn3) will hardly have a straightforward, one-to-one match with existing categories.

In this paper, we specifically study this challenge in proposing a pipeline for playlist generation using a sole title as input. Unlike previous works [[10](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0010), [19](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0019)], we use language models to capture the semantic meaning of playlist and track titles. In particular, we fine-tune a pre-trained transformer-based language model on playlist groups, clustered based on their track content. Such a fine-tune language model enables the creation of vector representations for any playlist title, whether known or unknown, of any complexity and not necessarily matching a pre-existing category (genre, mood, emotion, purpose) as in previous related work [[5](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0005), [11](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0011)]. Track recommendations for a given playlist title are subsequently made using similarity metrics and a voting mechanism. In addition, we assess the capacity of Large Language Models (LLM) in playlist generation from titles, both in a 0-shot scenario and for ranking a pre-selection of tracks.

The main contributions of this work are:

•

A pipeline for generating playlists from their titles;

•

An evaluation of this pipeline, against different variants and against other title-based recommender systems;

•

An assessment of the capabilities of prompt-based LLM in the task of playlist generation.

The code and data of all our experiments are available in open source at [https://github.com/elea-vellard/LLM-Playlist-Recommender](https://github.com/elea-vellard/LLM-Playlist-Recommender).

The remainder of this paper is structured as follows. Section [2](https://dl.acm.org/doi/10.1145/3705328.3748053#sec-2) provides an overview of previous work related to playlist generation. Section [3](https://dl.acm.org/doi/10.1145/3705328.3748053#sec-3) delves into the details of our proposed approach, outlining each step comprehensively. Section [4](https://dl.acm.org/doi/10.1145/3705328.3748053#sec-4) presents and discusses the results of our study. Finally, Section [5](https://dl.acm.org/doi/10.1145/3705328.3748053#sec-5) concludes the paper, highlights its limitations and outlines potential future work.

## 2 Related work

The inclusion of playlist titles in music recommender system research is relatively recent. Several experiments have been made in generating the title of a playlist, given the list of tracks it includes, using RNN and transformer-based models [[8](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0008), [15](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0015)]. In 2024, an online web application uses a combination of GPT-4 [[22](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0022)] and Claude [[1](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0001)] to generate good and catchy playlist titles given a list of songs.[^2^](https://dl.acm.org/doi/10.1145/3705328.3748053#fn4) While these studies investigate a task that is the inverse of ours, they provide some evidence that language models can successfully capture the semantic content of playlist titles.

An in-depth study on the creation and purpose of playlists was conducted in [[5](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0005)]. The authors of this study identified 9 distinct categories (excluding ‘Other’) that guide the organization of tracks into playlists. Furthermore, the research delves into examples of lengthy and complex playlist titles, which pose challenges when attempting to assign them to specific categories. In [[11](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0011)], a topic model applied on titles is used to classify playlists, and represent them as 10-dimensional topic mixture vectors. The distance between these vectors is used to recommend similar playlists. McFee and Lanckriet [[18](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0018)] apply natural language processing techniques to playlists by treating songs as tokens in a sequence, analogous to words in a sentence. While they do not use natural language directly, songs are modeled as discrete items similar to words in traditional NLP tasks. For example, a playlist containing the songs  *Let It Be* ,  *Hey Jude* , and *Imagine* would be represented as a three-token sequence, just like a sentence composed of three words. Other works intersecting music information retrieval and NLP are reported in [[13](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0013)].

In 2018, the annual RecSys Challenge focused on playlist completion, leading to the release of the Million Playlist Dataset by Spotify [[4](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0004)]. This dataset remains one of the most significant resources for the task today. The inclusion of 0-seeds playlist in the challenge, pushed several participants in having a *cold start* strategy based on playlist titles. The underlying rationale for the proposed implementations is consistent across all participants: playlists with similar titles are more likely to contain the same tracks. In [[10](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0010)], titles are used to create a matrix reporting if a given track (column) appears in at least one playlist having a specific title (row); the matrix is then used to compute a playlist-song pair score. In [[19](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0019)], playlist embeddings have been computed based on the co-occurrences of tracks, and these embeddings are used for clustering and for training a *fastText* model [[2](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0002)], working at the n-gram level.[^3^](https://dl.acm.org/doi/10.1145/3705328.3748053#fn5) In [[16](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0016)], another approach relying on a LSTM that learns word embeddings (based on n-grams), used in input – together with track features – to a Recurrent Neural Collaborative Filtering model is proposed, showing good performances in the no-seed scenario.

Other textual information are used in the literature to generate or to continue playlists. In [[12](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0012)], a Knowledge Graph is used to connect the contextual information of a playlist – extracted from its metadata such as the title – and the genres of the tracks, which is then fed in a classifier. These contextual information are however manually annotated. Emotions are leveraged in [[20](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0020)], extracted with a LSTM from chatbot interactions and mapped to acoustic features of tracks that are proposed as a playlist. In this context, a sad emotion can lead to a selection of sad and slow songs. Text2Playlist [[6](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0006)] is a tool designed to generate relevant playlists based on a textual prompt (e.g., “I want music from the 90s for work”). The system uses an LLM to extract a set of tags from the prompt, which are then used to produce playlist recommendations which are further refined by the LLM. Finally, Text2Tracks [[23](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0023)] and TALKPLAY [[7](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0007)] perform a supervised finetuning of LLMs on pairs including a query (or conversation) and a list of recommended tracks.

These studies do not directly engage with titles, thus distinguishing from our work. Indeed, following the RecSys Challenge 2018, limited attention has been devoted to playlist titles, leaving the state of the art largely globally unchanged while transformer-based approaches and LLM enable nowadays to go one step further.

## 3 Method

**Figure 1:**

![](https://dl.acm.org/cms/10.1145/3705328.3748053/asset/2981b7a1-3496-4da0-a6d0-31c40a046a31/assets/images/medium/recsys25-59-fig1.jpg)Diagram representing our training approach

Diagram representing our training approach

**Figure 2:**

![](https://dl.acm.org/cms/10.1145/3705328.3748053/asset/e8e3882e-65d0-449b-a7b3-cf5e81b64bb3/assets/images/medium/recsys25-59-fig2.jpg)Diagram representing our recommendation approach when a new playlist title is used as seed

Diagram representing our recommendation approach when a new playlist title is used as seed

Our approach to playlist generation exploits the textual information of playlist (name and track titles) to capture the intended scope and topic of the playlist itself. Our methodology is divided into two phases.

The **training phase** (Figure [1](https://dl.acm.org/doi/10.1145/3705328.3748053#fig1)) begins with the preprocessing of the dataset to extract the relevant information for our goal. Afterwards, we employ a pre-trained transformer-based model to generate embeddings that capture the semantic meaning of the titles of both playlist and the included tracks. These embeddings transform the textual information into high-dimensional vectors, which are the representation of the playlists in a semantic space.

We apply a clustering algorithm to the generated embeddings, in order to group playlists based on their thematic similarity and identify distinct themes or moods that are prevalent across the dataset. The resulting clusters serve as the foundation for fine-tuning a language model, making it more capable to capture semantic similarity in this specific context.

In the **generating phase** (Figure [2](https://dl.acm.org/doi/10.1145/3705328.3748053#fig2)), the fine-tuned transformer model extracts the embedding representations of titles from both existing playlists and new input playlists. These embedding representations are then compared using cosine similarity scores. Each new input playlist title is compared with the known titles of existing playlists within the dataset, ranking them based on similarity. This process identifies the most similar playlists.

A voting mechanism is subsequently employed to determine the final selection of tracks in the new playlist being generated. This mechanism considers all tracks included in the most similar playlists, and returns in output those that occur the most.

Separately, we conducted additional experiments with prompt-based LLM for playlist generation from a title, in order to have a comparison with our proposed fine-tuned model.

These steps are further detailed in the following sections.

### 3.1 Processing the dataset

The Million Playlist Dataset (MPD) released by Spotify in 2018 [[4](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0004)] is composed of one million user-generated playlists that are commonly used for understanding music preferences and for developing recommendation algorithms. It is available as a set of JSON slices, each slice containing 1,000 playlists. In the dataset, a playlist is represented with a title and a unique playlist identifier (pid), and includes some additional information such as the timestamp of the last update, the number of included tracks and artist, and an (optional) description. Each playlist is composed of a certain number of tracks and artists, that can be identified by their unique Uniform Resource Identifier (URI).

To better manage the content, the dataset is transformed into easily-readable CSV files:

•

*playlists.csv* contains the main information of each playlist: its pid, its title, the number of tracks, etc.

•

*items.csv* serves as a bridge between tracks and their corresponding playlists. It connects every track (identified by its URI) to its playlist (pid) and writes the track’s position within the playlist.

•

*tracks.csv* contains information about each track: its unique URI, the title, the artist, the album URI and name, and the track duration.

### 3.2 Clustering strategy

We hypothesize that playlist titles and track names convey specific ideas and themes that maintain coherence within the context of the playlist, with this coherence being domain-specific rather than universal. For example, a playlist titled “Let it Snow” could simply suggest a winter theme when just considering the semantic meaning of the words. However, within the context of music playlists, it unmistakably indicates a Christmas-themed collection.

Based on this premise, we propose that playlist titles and track titles that frequently co-occur are more likely to share semantic relatedness, similar to how words that often appear together in sentences do. Just as sentences, when grouped into documents, provide the contextual foundation for fine-tuning language models, the combination of playlist and track titles, organized into thematically coherent clusters, can serve as a valuable dataset for fine-tuning a playlist-aware recommendation model.

#### 3.2.1 Vector representation of playlist content.

There are several methods to represent playlists as vectors based on their content. The one-hot encoding approach, as in [[10](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0010)], was deemed impractical due to its excessive size and computational inefficiency. The skip-gram approach, as described in [[19](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0019)], was also considered and discarded for similar reasons. Consequently, we opted to use text-based embeddings for this vector representation because they offer a more compact dimensionality through aggregation techniques. In this scenario, each playlist is represented by the titles of all its tracks.

Initially, we tested word embedding models such as *fastText* [[2](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0002)], averaging the vectors of all words composing the track titles in the playlist. However, our initial assessment revealed that this model was not sufficiently efficient for our use case, as it primarily focuses on word-level representations and failed to capture the contextual meaning of playlist titles. This was particularly evident in our attempt to cluster playlists, which resulted in poorly defined data separations as illustrated in Figure [3](https://dl.acm.org/doi/10.1145/3705328.3748053#fig3).

**Figure 3:**

![](https://dl.acm.org/cms/10.1145/3705328.3748053/asset/95d9cff2-e415-4947-ab71-dcfdc101eb53/assets/images/medium/recsys25-59-fig3.jpg)T-SNE plot of 10 clusters for the training set using kMeans on fastText embeddings.

T-SNE plot of 10 clusters for the training set using kMeans on fastText embeddings

Thus, we opted for a transformer-based model, which has demonstrated strong performance across a wide range of tasks [[29](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0029)]. In particular, we employed  *Sentence BERT* , which leverages the attention mechanism through Siamese BERT-Networks. This approach involves two BERT blocks processing sentence pairs concurrently, followed by a pooling layer that generates fixed-size sentence embeddings [[24](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0024)]. This enables Sentence BERT to create more effective representations at the sentence-level. Given that playlist titles can be viewed as concise sentences (or at least are more extensive than single words), we conclude that Sentence BERT is the most appropriate choice for our task.

For each playlist, we compute the mean embedding *e* of all the track titles in the playlist itself:

where *n* is the number of tracks within the playlist, and  is the Sentence BERT embedding of the  *i* -th track in the playlist.

By focusing solely on the tracks within the playlists (i.e., their content) and excluding the titles, we achieve two key objectives:

(1)

We prevent the introduction of bias that could arise from similar titles representing in facts different themes or concepts.

(2)

By concealing the titles during the clustering stage, we can confidently extract the test set later, ensuring it contains only titles that were not seen during training. This approach maintains the integrity of our evaluation process.

#### 3.2.2 Clustering algorithm.

The playlist vectors are clustered using the K-Means algorithm. We manually selected the number of clusters instead of relying on density-based algorithms like DBSCAN. This was because the embedding space, composed of mean embeddings, was very dense, making it difficult for DBSCAN to effectively differentiate between various themes. For the same reason, metrics such as the Silhouette or Davies-Bouldin scores, which measure intra- and inter-cluster distances, were not particularly relevant in our specific use case.

We implemented an elbow curve approach to estimate an optimal number of clusters, as in Figure [4](https://dl.acm.org/doi/10.1145/3705328.3748053#fig4). Since our main goal was to ensure coherence within each cluster, the elbow curve served more as a guideline to establish a minimum value rather than a definitive choice for the number of clusters. In fact, although the elbow curve suggested a number *k* of clusters around 25, we ultimately set *k* = 200. We observed that increasing the number of clusters generally improved performance, as visible in Figure [5](https://dl.acm.org/doi/10.1145/3705328.3748053#fig5). However, we also found that a higher number of clusters significantly increased computational cost. Beyond 200 clusters, the computational expense became prohibitive. Therefore, based on our analysis, we settled on 200 clusters as the optimal choice.

**Figure 4:**

![](https://dl.acm.org/cms/10.1145/3705328.3748053/asset/4990ef56-2fec-4167-832a-062f6fae26cf/assets/images/medium/recsys25-59-fig4.jpg)The elbow curve and the suggested number of clusters (in red)

The elbow curve and the suggested number of clusters (in red)

**Figure 5:**

![](https://dl.acm.org/cms/10.1145/3705328.3748053/asset/34edb492-0a02-455a-86ae-f5db5dccc8af/assets/images/medium/recsys25-59-fig5.jpg)The standard error of estimate (SSE) of clusters decreases with the increment of number k of clusters.

The standard error of estimate (SSE) of clusters decreases with the increment of number k of clusters.

The T-SNE plot of an initial experiment made with 50 clusters (Figure [6](https://dl.acm.org/doi/10.1145/3705328.3748053#fig6)) reveals two key observations. First, the clusters are more distinct compared to those in Figure [3](https://dl.acm.org/doi/10.1145/3705328.3748053#fig3), although some overlaps persist, making them challenging to separate completely. Additionally, the presence of clusters that are significantly larger and more dispersed than others is evident. This phenomenon can be attributed to certain clusters containing a broader range of topics[^4^](https://dl.acm.org/doi/10.1145/3705328.3748053#fn6), which we will refer to as *miscellaneous* throughout this paper.

**Figure 6:**

![](https://dl.acm.org/cms/10.1145/3705328.3748053/asset/eeeb8a68-4b46-4932-a828-9460f31285f5/assets/images/medium/recsys25-59-fig6.jpg)T-SNE plot of 50 clusters for the training set using kMeans on Sentence BERT embeddings. It is possible to note at least two miscellaneous clusters, in dark blue and green.

T-SNE plot of 50 clusters for the training set using kMeans on Sentence BERT embeddings. It is possible to note at least two miscellaneous clusters, in dark blue and green.

The presence of these *miscellaneous* clusters poses several challenges. First, their significantly larger size compared to other clusters can lead to imbalanced training, potentially impacting classification accuracy. Secondly, the informative value of these clusters is questionable, as their playlists are included primarily because they do not fit well into other categories. Therefore, we decided to remove those clusters (and playlists) from our training set. Indeed, for the goal of fine-tuning a language model, we prefer having coherent clusters (including only playlists on the same theme), rather than complete ones (with a unique cluster theme). In order to realize this, we found for each cluster the most occurring playlist title and we computed the percentage of exact matches with it among all the playlists’ titles of that cluster. We consider valid the clusters that have the percentage over a threshold *t* and miscellaneous below it. The threshold has been set to *t* = 0.02 empirically. Indeed, most clusters below this percentage include a number of playlists largely above the mean of all other clusters. Although this method is relatively simple, we found it to be effective in identifying miscellaneous clusters, which have been excluded from the dataset. This action removed around 40% of the MPD, resulting in a total of 158 clusters left for the next sections[^5^](https://dl.acm.org/doi/10.1145/3705328.3748053#fn7).

We split our processed dataset into training (80% of the data), validation (10%) and test set (10%), ensuring a representation of each cluster in every set, so that the model can train and evaluate its performance on specific clusters.

### 3.3 Fine-tuning a language model

**Figure 7:**

![](https://dl.acm.org/cms/10.1145/3705328.3748053/asset/745a90eb-aacf-4fb0-bfd0-0203a2841891/assets/images/medium/recsys25-59-fig7.jpg)The cosine similarity scores of pairs of embeddings computed with the three model variants.

The cosine similarity scores of pairs of embeddings computed with the three model variants.

The training and validation set created in the previous step is used to fine-tune a language model, with the ultimate goal of effectively distinguishing and classifying playlist themes. The input for fine-tuning consists of clusters, each represented by concatenating the titles of its associated playlists. These concatenations of titles acts as documents in our fine-tuning, while cluster IDs are used as labels.

Concerning the architecture, we used a sentence transformer backbone [[24](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0024)] and in particular the all-MiniLM-L6-v2[^6^](https://dl.acm.org/doi/10.1145/3705328.3748053#fn8) model. This model maps sentences to a 384 dimensional dense vector space and can be used for tasks like clustering, while being compact enough to ensure computational efficiency. Additional classification layers were included, composed of a dropout layer for regularization and a fully connected layer to predict cluster labels. The model is fine-tuned in two variants:

•

using the  *cross-entropy loss* , commonly used for classification tasks;

•

using the  *triplet loss* , which focuses on making items from the same group closer than those from different groups [[25](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0025)].

We used standard training arguments, including a batch size of 8 and a learning rate of 2 × 10 ^− 5^ . Throughout the process, we monitored the loss on both the training and validation sets to detect any signs of overfitting, which we observed after approximately 15 epochs. Consequently, we stopped the fine-tuning early and retained the model that minimized the validation loss.

On the output model, we observed significant improvements in the model’s ability to adapt to the music playlist context. To illustrate this, we compared the cosine similarity scores between the embedding of the word “Workout” and each of the words “K-pop”, “Running”, and "Sports”. In Figure [7](https://dl.acm.org/doi/10.1145/3705328.3748053#fig7), it is evident how the three model variants differ in the representation. The pre-trained model exhibits less variability in its vectors, indicating a more uniform and compact embedding space where nodes are closer to each other. In contrast, fine-tuning helps to better differentiate semantically distant words, such as “Workout” and “K-pop”, while bringing semantically similar words, like “Workout” and “Running” or "Workout” and “Sports”, closer together. It is noteworthy that in the triplet loss variant, “Workout” is closer to “Sports” than to “Running”. While “Workout” and “Sports” are definitively within the semantic realm of physical activity, “Running” can also appear in metaphorical contexts – such as “running away from sentiments” – and this has probably been captured in the fine-tuned model.

### 3.4 Playlist generation

The final step of our pipeline focuses on generating playlists that align with a user’s input title. Utilizing the fine-tuned model, we aim to recommend tracks that match the input theme, even if they are no exact matches with the proposed title.

The embeddings of each (known) playlist titles in the dataset are computed using the finetuned model. As seed for the generation process, a (unknown) playlist title – that can be composed of one or multiple words – is provided, and the embedding of the title is generated. The latter is compared with the embeddings of all known playlists using cosine similarity.

Formally, the cosine similarity between two embeddings *e~a~* and *e~b~* is defined as:

The 50 playlists with the highest similarity scores are selected. Among these, we count the occurrences of each track. A **voting mechanism** is applied, where tracks that appear more frequently across the matched playlists receive higher scores, indicating their relevance to the input theme. The top *k* most frequently occurring songs are then recommended to the user.

### 3.5 Playlist generation using LLM

We also conducted a playlist generation experiment using three Large Language Models in a implementation using LangChain [[3](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0003)]. In particular, we tested a zero-shot and two few-shot scenarios, including 1 and 5 songs respectively as examples given in the prompt. To ensure a fair comparison with our ground truth, we explicitly instructed the LLM to consider only songs published before the release date of the MPD dataset.

The prompt provided to the LLM is structured as follows. We first assign the LLM the role of an expert in music recommendation and clearly define its task. We then explicitly outline a set of constraints that the LLM must adhere to, restricting its recommendations to songs released before 2017. We ask to generate a playlist of 10 songs, and specify that the output must exclusively be in JSON format to simplify subsequent parsing. Elements in curly brackets ({}) represent configurable parameters. This allowed us to obtain a simple format of recommended songs in order to easily compute quantitative metrics.

**Prompt for LLM Playlist Generation**

You are an expert in music playlist generation.

Your task is to generate the continuation of a playlist given only its title and five example songs with their artists.

**Important:**

•

You have to select only songs released before October 2017.

•

Propose a COMPLETE playlist consisting of exactly 10 songs.

•

Do not output any extra text besides the list of songs.

•

The output must be a JSON list where each item is a dictionary with keys "song" and "artist".

•

Only return the JSON list. Do not repeat the instructions or inputs.

•

In each dictionary, the value for "song" must contain only the song name (without any hyphen or artist information) and the value for "artist" must contain only the artist name.

•

All recommended songs must be UNIQUE and must not repeat any of the five example songs provided.

**Playlist Title:** "{playlist_title}"

**Examples:**

(1)

{"song": "{song1}", "artist": "{artist1}"}

(2)

...

**Output format (strict):**

[

{"song": "`<title>`", "artist": "`<artist>`"},

...

]

**Answer ONLY with the JSON list exactly as specified above. Do not output anything else.**

## 4 Evaluation

To evaluate the effectiveness of our method, we employed a combination of quantitative and qualitative metrics. The quantitative evaluation focuses on commonly used metrics, computed on the playlists from the test set. It is important to recall that the playlists in the test set have not been used during training.

For each playlist, the set of relevant songs *R* is defined as the actual tracks contained within that playlist. The set of recommended songs is noted as  *S* . The metrics we focus on are computed for a playlist of *N* songs [[4](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0004), [26](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0026)]:

•

**precision@N** measures the proportion of recommended tracks that are relevant, with N being the number of recommended songs.

(1)

•

**recall@N** assesses the proportion of relevant tracks that were successfully recommended.

(2)

•

**MRR@N** (Mean Reciprocal Rank) estimates the rank of the first relevant song in the recommended songs.

(3)

•

**R-Precision** evaluates the proportion of recommended tracks *S~T~* and artists *S~A~* that are relevant among all known relevant tracks *G~T~* and artists  *G~A~* .

(4)

•

**NDCG** (Normalized Discounted Cumulative Gain) evaluates the ranking quality of recommended tracks, improving as relevant tracks are positioned higher in the list. If *r~i~* is the position in the ground truth of the  *i* -th recommended track, over the *N* recommended songs, and *IDCG* is the DCG obtainable when the recommended playlist matches perfectly the ground truth:

(5)

(6)

To complement these quantitative metrics, we incorporated a qualitative evaluation process involving human reviews. This step assessed the thematic coherence and overall appeal of the generated playlists. Two reviewers, leveraging their familiarity with the songs and conducting listening sessions when necessary, evaluated each track within the playlists and assigned an overall qualitative score. The integration of qualitative evaluation is essential because quantitative metrics may not fully reflect the model’s quality, given that the recommended tracks may still be relevant according to the playlist title, even if not among the involved ground truth.

### 4.1 Quantitative results

We evaluated each approach using the same metrics on the playlists from the test set. The two fine-tuned models – with cross-entropy loss and with triplet loss – are compared with a pre-trained Sentence BERT. For each model, we computed metrics on the first 10, 66, and 500 tracks for input playlist title, where 66 is the average number of tracks per playlist across the whole dataset, and 500 is the number of requested track to predict in RecSys Challenge 2018.

Table [1](https://dl.acm.org/doi/10.1145/3705328.3748053#tab1) shows the average metrics computed over multiple input playlists. We observed a positive impact from fine-tuning, with all metrics showing approximately double the improvement compared to the pre-trained model. The results between the two fine-tuned model variants are similar, although the cross-entropy variant performed slightly better across almost all metrics. When predicting 500 tracks, the fine-tuning with cross-entropy still yields better scores, although the improvement over the pre-trained model is less pronounced. Conversely, the triplet loss approach results in comparatively lower performance. As the number of predicted songs increases, popular songs are more frequently selected because they are prevalent across various playlists. This prevalence can diminish the distinctions between different variants, and this is reflected in the results.

**Table 1:**

| **Metric**          | **PT**     | **FT-C**   | **FT-T**   |
| ------------------------- | ---------------- | ---------------- | ---------------- |
| **Precision@10**    | 0.1630           | **0.1793** | 0.1616           |
| **Recall@10**       | 0.0332           | **0.0382** | 0.0316           |
| **MRR@10**          | 0.2567           | **0.3254** | 0.3004           |
| **R-Precision@10**  | 0.0358           | **0.0496** | 0.0417           |
| **NDCG@10**         | 0.2780           | **0.3740** | 0.3472           |
| **Precision@66**    | 0.0571           | **0.1228** | 0.1176           |
| **Recall@66**       | 0.0647           | 0.1383           | **0.1424** |
| **MRR@66**          | 0.1896           | **0.3542** | 0.3444           |
| **R-Precision@66**  | 0.0477           | **0.1332** | 0.1059           |
| **NDCG@66**         | 0.2742           | **0.4311** | 0.4156           |
| **HIT@500**         | 0.3868           | **0.3873** | 0.3329           |
| **Precision@500**   | 0.0480           | **0.0489** | 0.0410           |
| **Recall@500**      | 0.3868           | **0.3979** | 0.3329           |
| **MRR@500**         | **0.3499** | 0.3490           | 0.2893           |
| **R-Precision@500** | **0.1570** | 0.1556           | 0.1285           |
| **NDCG@500**        | 0.2731           | **0.2825** | 0.2297           |

Quantitative scores of our method in the three studied variants: the pre-trained model (PT), the fine-tuned model with cross entropy loss (FT-C), and the fine-tuned model with triplet loss (FT-T)

**Table 2:**

| **Method**                                                            | **R-Precision** | **NDCG**   |
| --------------------------------------------------------------------------- | --------------------- | ---------------- |
| Monti et. al [[19](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0019)]    |                       |                  |
| *- Only title*                                                            | 0.0837                | 0.1260           |
| *- Best*                                                                  | *0.1634*            | *0.1717*       |
| Faggioli et. al [[10](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0010)] |                       |                  |
| *- Only title*                                                            | 0.1093                | 0.2451           |
| *- Best*                                                                  | *0.2078*            | *0.3713*       |
| Kim et. al [[16](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0016)]      |                       |                  |
| *- Only title*                                                            | 0.0760                | 0.1866           |
| *- Best*                                                                  | *0.1924*            | *0.3394*       |
| **Our method**                                                        |                       |                  |
| Pre-trained                                                                 | **0.1570**      | 0.2731           |
| Fine-tuned (cross)                                                          | 0.1556                | **0.2825** |
| Fine-tuned (triplet)                                                        | 0.1285                | 0.2297           |

Comparison of our method and other playlist generation solutions relying on the playlist title from RecSys challenge 2018

In Table [2](https://dl.acm.org/doi/10.1145/3705328.3748053#tab2), we compare our strategy with those in previous works. The figures for the methods in [[10](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0010), [16](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0016), [19](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0019)] are sourced from their respective papers. We include results computed using only title information, specifically R-Precision@500 and NDCG@500. Additionally, we present the best results from the relative papers, which also incorporate training over tracks and are marked as *Best* in the table. These *Best* results are not directly comparable with our approach since they have been obtained using track content while our approach relies solely on the playlist title.

Our method demonstrates superior results compared to previous works, in both reported metrics, surpassing of several points the performance of the highest competitors that use only the title information. Our method outperforms in NDCG also some of the best variants, that incorporated additional information about the tracks in the training.

### 4.2 Qualitative assessment

In our qualitative evaluation, we conducted a human assessment of thematic coherence and appeal for the generated playlists. Due to the high costs of human annotation, we limited our evaluation to a set of 22 specifically chosen playlists from the test set, reported in Table [3](https://dl.acm.org/doi/10.1145/3705328.3748053#tab3), selected according to the following criteria:

•

the playlist should include at least 10 tracks;

•

a clear thematic alignment between playlist titles and their tracks should be present. In other words, we excluded titles that were too generic or not enough representative of the playlist content;

•

both niche and more broadly themed playlists should be included in the final set.

**Table 3:**

| PID    | playlist title  | nb. tracks |
| ------ | --------------- | ---------- |
| 673925 | KPOP            | 22         |
| 677580 | workout music   | 63         |
| 321143 | Dance           | 37         |
| 923247 | Rock            | 198        |
| 301195 | Summer          | 37         |
| 490485 | Hawaii          | 36         |
| 575612 | Classic Country | 174        |
| 269088 | older songs     | 8          |
| 606436 | 2016            | 129        |
| 701866 | Dance           | 23         |
| 608829 | FINESSE         | 55         |
| 273344 | Oldies          | 239        |
| 501054 | Rock            | 73         |
| 750528 | sports          | 72         |
| 684261 | Christian       | 10         |
| 44648  | gaming          | 33         |
| 837665 | classics        | 52         |
| 786219 | Party           | 74         |
| 47214  | workout         | 99         |
| 889395 | work            | 51         |
| 497427 | Love songs      | 43         |
| 677006 | Summer          | 29         |

List of 22 playlists used in our evaluation, with the number of tracks included in each of them

Each recommended track for a given playlist title was assessed by two reviewers, who reached a consensus on whether to consider each track as valid. All decisions were thus agreed by consensus by both reviewers. For instance, for a hypothetical playlist titled “Rock classics”, tracks such as “Highway to Hell” by AC/DC, “Smells Like Teen Spirit” by Nirvana, and “It’s My Life” by Bon Jovi would be considered highly relevant, while “My Heart Will Go On” by Céline Dion have to be considered as not fitting. The assigned qualitative score is the percentage of valid tracks over the total, computed as:

(7)

The metric is in the [0,1] range, being 1 when all recommended tracks are valid.

The results in Table [4](https://dl.acm.org/doi/10.1145/3705328.3748053#tab4) demonstrate that, while quantitative metrics offer valuable insights, qualitative assessments provide crucial additional perspectives. Specifically, although quantitative scores may not perfectly align with user-generated playlists, the good qualitative metrics across all three models underscore their ability to create meaningful and coherent playlists, with over 70% of tracks being relevant. The qualitative score confirms the superiority of the model fine-tuned with cross-validation.

**Table 4:**

| **Metric**     | **PT** | **FT-C**   | **FT-T** |
| -------------------- | ------------ | ---------------- | -------------- |
| Qualitative Score@10 | 0.7376       | **0.7789** | 0.7533         |
| Qualitative Score@66 | 0.7231       | **0.7719** | 0.7461         |

Qualitative scores of our method in the three studied variants: the pre-trained model (PT), the fine-tuned model with cross validation loss (FT-C), and the fine-tuned model with triplet loss (FT-T).

### 4.3 Evaluation of the LLM generation

**Table 5:**

| **Model**  | **Llama** | **Zephyr** | **GPT4o** |
| ---------------- | --------------- | ---------------- | --------------- |
| **n-shot** | **0**     | **1**      | **5**     |
| Precision@10     | 0.0591          | 0.0950           | 0.0636          |
| Recall@10        | 0.0067          | 0.0173           | 0.0059          |
| MRR@10           | 0.0966          | 0.1883           | 0.1723          |
| R-Precision@10   | 0.0137          | 0.0269           | 0.0104          |
| NDCG@10          | 0.1199          | 0.2102           | 0.1863          |
| Qualitative      | 0.6416          | 0.6818           | 0.7132          |

Performance metrics for LLM. In bold, the best absolute scores, while in italic the best scores for a zero-shot scenario

We conducted an initial assessment of how LLM perform using the same 22 playlists that were used for the qualitative evaluation. We tested three different LLMs, namely Llama 3.1 [[9](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0009)], Zephyr[^7^](https://dl.acm.org/doi/10.1145/3705328.3748053#fn9) [[27](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0027)], and GPT4o [[21](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0021)] in order to have representatives among open weights models (Llama and derivatives) and closed models (GPT). The results are presented in Table [5](https://dl.acm.org/doi/10.1145/3705328.3748053#tab5). Although the quantitative metrics are based on a different test set than those in Table [1](https://dl.acm.org/doi/10.1145/3705328.3748053#tab1)[^8^](https://dl.acm.org/doi/10.1145/3705328.3748053#fn10), this experiment can already give us some insight on the LLMs performance.

All language models benefit from including a few examples in the prompt. Llama has a unique behavior, as it prefers 1 to 5 examples for most metrics, though not for qualitative assessments. In every configuration, GPT4o demonstrates the best performance. In addition, we noticed that Llama and in particular Zephyr were not completely respecting the provided instruction, recommending songs published after the desired date specified in the prompt. GPT4o still falls short compared to the fine-tuned system, even in the 5-shot scenario. When comparing zero-shot performance – which relies solely on title information as in the fine-tuned system – the gap becomes quite pronounced. However, when examining the qualitative results, the gap is less pronounced (Table [4](https://dl.acm.org/doi/10.1145/3705328.3748053#tab4)), with over 60% of the recommended tracks being of good quality. While Llama and Zephyr fail to match the scores of all transformer-based models, GPT4o succeeds in doing so, albeit only in the 5-shot scenario.

The limited scope of this experiment serves as a preliminary step to assess the feasibility of using LLMs in playlist generation. Despite its preliminary nature, we believe there are valuable outcomes from this exploration:

•

LLMs struggle to replicate the retrieval scores achieved in our previous experiment;

•

However, the relevance of the songs proposed by LLMs remains qualitatively similar.

The real advancement in this context would be to integrate LLMs with other retrieval techniques, as outlined in the conclusions.

## 5 Conclusion and Future Work

Our study investigated the use of language models for playlist generation. The experiments confirmed that the playlist title is a valuable source of information, and capturing its semantic meaning can be particularly beneficial in cold start scenarios. By combining clustering with fine-tuning, we enhanced the model’s ability to generalize across diverse playlist themes, providing a unique and complementary approach to more traditional recommender system techniques. When relying solely on the title, our results outperform existing work in the literature and LLM generation in zero-shot and few-shot settings.

Our approach empowers users to transcend the limitations of predefined categories, having the full potential of their choice of words as seed for generation. This opens up virtually unlimited combinations, offering users a novel way to discover relevant and potentially new and unexpected music. However, this work presents several limitations that necessitate future research.

Firstly, the voting mechanism tends to flatten differences for very common playlist titles, Moreover it tends to favor popular tracks, particularly for generic titles. Our implementation is designed to maximize retrieval-based metrics, as it was the evaluation focus of the RecSys Challenge 2018, which allows us to make meaningful comparisons with the state-of-the-art. Introducing metrics to capture diversity, novelty, and order would undoubtedly enhance the outcomes. For example, for recommending novel songs not yet included in any playlist, it would be possible incorporate SentenceBERT similarity between a novel song title and existing playlists’ title. This approach may result in lower precision metrics, as it prioritizes novelty over exact matches; the right trade-off between the metric would depend on the use case. Additionally, two strategies, could immediately help mitigate the popularity bias:

•

with a ranking system powered by language models, as demonstrated in [[6](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0006)]. The final ranking of tracks can indeed include more than the 50 most similar playlists, introducing more variability in the results;

•

use our system for playlist continuation, where the first *N* songs are used as seeds, to better compare with other systems. Alternative language models can be explored as substitutes for Sentence BERT to provide a more comprehensive comparison of their performance and capabilities.

Furthermore, specializing the model for specific languages could enhance its performance and relevance in diverse linguistic contexts. Implementing the system in a production environment would also be crucial to assess its real-world effectiveness and robustness. This step would involve optimizing for scalability and efficiency, ensuring the model can handle large volumes of data and user interactions seamlessly. In addition, we plan to include explainability of the recommendation system by providing users with insights into why certain tracks were recommended. Lastly, we believe that the value of this work has to be tested in combination with a collaborative-based method, exploiting the best of the two approaches.

## Acknowledgments

This work was supported by the French Public Investment Bank (Bpifrance) i-Demo program within the LettRAGraph project (Grant ID DOS0256163/00).

No AI tools were used for data analysis, experimentation, or the formulation of conclusions, except in the ways it is described in the paper itself.

## Footnotes

^1^

Those real playlist titles that one can find in the Million Playlists Dataset.[Go to Footnote](https://dl.acm.org/doi/10.1145/3705328.3748053#core-fn3-1)

^2^

[https://www.playlistnameai.com/](https://www.playlistnameai.com/)[Go to Footnote](https://dl.acm.org/doi/10.1145/3705328.3748053#core-fn4-1)

^3^

An  *n* -gram is a contiguous sequence of *n* items (phonemes, syllables, letters, etc.) from a given sample of text or speech.[Go to Footnote](https://dl.acm.org/doi/10.1145/3705328.3748053#core-fn5-1)

^4^

In particular, the presence in the MPD of some broad-sense, not-meaningful playlist titles, such as “music” or “my playlist” was already reported in [[10](https://dl.acm.org/doi/10.1145/3705328.3748053#Bib0010)].[Go to Footnote](https://dl.acm.org/doi/10.1145/3705328.3748053#core-fn6-1)

^5^

It is important to specify that we exclude the miscellaneous clusters only during the fine-tuning phase. For this task, a more homogeneous corpus was required to prevent the language model from learning irrelevant associations. However, any title can subsequently be processed by the fine-tuned model, which also leverages its pre-existing knowledge.[Go to Footnote](https://dl.acm.org/doi/10.1145/3705328.3748053#core-fn7-1)

^6^

[https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)[Go to Footnote](https://dl.acm.org/doi/10.1145/3705328.3748053#core-fn8-1)

^7^

[https://huggingface.co/TheBloke/zephyr-7B-beta-AWQ](https://huggingface.co/TheBloke/zephyr-7B-beta-AWQ)[Go to Footnote](https://dl.acm.org/doi/10.1145/3705328.3748053#core-fn9-1)

^8^

For reference, the pre-trained Sentence BERT had Precision 0.0586, Recall 0.1295, and MRR 0.2189 on the same test set of 22 playlists.[Go to Footnote](https://dl.acm.org/doi/10.1145/3705328.3748053#core-fn10-1)

## Supplemental Material

MP4 File - A Language Model-Based Playlist Generation Recommender System - Summary

This video presents our research on generating playlists using language models. We focus on creating playlists based solely on their titles which can reflect various moods genres events or purposes. Using the Million Playlist Dataset from Spotify's RecSys Challenge 2018 we compute text embeddings for playlist titles and cluster them to fine-tune our language model. In the second phase we compare embeddings of new playlist titles to retrieve the most relevant playlists using cosine similarity and a voting mechanism to recommend tracks. Our method shows improved performance over previous techniques. For more detailed insights and evaluations please refer to our paper and access the open-source repository for the code.

<iframe aria-labelledby="auxelement-30-caption" height="140px" width="100%" allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;" loading="lazy" allowfullscreen="true" src="https://iframe.videodelivery.net/eyJraWQiOiI3YjgzNTg3NDZlNWJmNDM0MjY5YzEwZTYwMDg0ZjViYiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjZmE0Y2ZiYmYxYTY1ZTQ3MWM3OGI1N2M3YjA1NGVlNCIsImV4cCI6MTc2OTgzNzAwOSwia2lkIjoiN2I4MzU4NzQ2ZTViZjQzNDI2OWMxMGU2MDA4NGY1YmIifQ.GvkwhZD78eatfc8aW5uEDI5bsug4ag5L0MzSFb9fH6iJE16vjp9qkZTW388WAiNWuD3JiwarIOyJBb0fjbiTaO43FclmgQ7DieGaLoaRR1k5eFA0MaIwV7MoEhPD6h8zJrAxeUdEaisqp6G5Zo8zYgkgv_fveIG8IBUPsrOsk67BTvnjLZij1L5-bH0chJMQ8HSt0Xge3cEezsCaRLrNfaSt7jWHuhEpE2ZF01rhqJGO7F8LOx58IfJQpvPAHmIAXVySNUk4H-bw4l7VFvR9lvH9CSC2_1CKhzIYH0kfTlrYVj8ftpIX68Zj93AUt0I4nh64lN1KdRQ_MZzT8A3V6A?poster=https%3A%2F%2Fvideodelivery.net%2FeyJraWQiOiI3YjgzNTg3NDZlNWJmNDM0MjY5YzEwZTYwMDg0ZjViYiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjZmE0Y2ZiYmYxYTY1ZTQ3MWM3OGI1N2M3YjA1NGVlNCIsImV4cCI6MTc2OTgzNzAwOSwia2lkIjoiN2I4MzU4NzQ2ZTViZjQzNDI2OWMxMGU2MDA4NGY1YmIifQ.GvkwhZD78eatfc8aW5uEDI5bsug4ag5L0MzSFb9fH6iJE16vjp9qkZTW388WAiNWuD3JiwarIOyJBb0fjbiTaO43FclmgQ7DieGaLoaRR1k5eFA0MaIwV7MoEhPD6h8zJrAxeUdEaisqp6G5Zo8zYgkgv_fveIG8IBUPsrOsk67BTvnjLZij1L5-bH0chJMQ8HSt0Xge3cEezsCaRLrNfaSt7jWHuhEpE2ZF01rhqJGO7F8LOx58IfJQpvPAHmIAXVySNUk4H-bw4l7VFvR9lvH9CSC2_1CKhzIYH0kfTlrYVj8ftpIX68Zj93AUt0I4nh64lN1KdRQ_MZzT8A3V6A%2Fthumbnails%2Fthumbnail.jpg%3Ftime%3D10.0s"></iframe>

* [Download](https://dl.acm.org/doi/suppl/10.1145/3705328.3748053/suppl_file/recsys4.mp4)
* 60.67 MB

## References

[1]

Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Tom Brown, and Jared Kaplan. 2022. Constitutional AI: Harmlessness from AI Feedback. arxiv:[https://arXiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073) [cs.CL] [https://arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073)

[Go to Citation](https://dl.acm.org/doi/10.1145/3705328.3748053#core-Bib0001-1)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Constitutional+AI%3A+Harmlessness+from+AI+Feedback&author=Yuntao+Bai&author=Saurav+Kadavath&author=Sandipan+Kundu&author=Amanda+Askell&author=Jackson+Kernion&author=Andy+Jones&author=Anna+Chen&author=Anna+Goldie&author=Azalia+Mirhoseini&author=Cameron+McKinnon&author=Carol+Chen&author=Catherine+Olsson&publication_year=2022)

[2]

Piotr Bojanowski, Edouard Grave, Armand Joulin, and Tomas Mikolov. 2017. Enriching Word Vectors with Subword Information. *Transactions of the Association for Computational Linguistics* 5 (2017), 135–146.

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Enriching+Word+Vectors+with+Subword+Information&author=Piotr+Bojanowski&author=Edouard+Grave&author=Armand+Joulin&author=Tomas+Mikolov&publication_year=2017&pages=135-146)

[3]

Harrison Chase. 2022.  *LangChain* . LangChain AI. [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)

[Go to Citation](https://dl.acm.org/doi/10.1145/3705328.3748053#core-Bib0003-1)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=LangChain&author=Harrison+Chase&publication_year=2022)

[4]

Ching-Wei Chen, Paul Lamere, Markus Schedl, and Hamed Zamani. 2018. Recsys challenge 2018: automatic music playlist continuation. In *Proceedings of the 12th ACM Conference on Recommender Systems* (Vancouver, British Columbia, Canada) ( *RecSys ’18* ). Association for Computing Machinery, New York, NY, USA, 527–528.

[Digital Library](https://dl.acm.org/doi/10.1145/3240323.3240342)

[Google Scholar](https://scholar.google.com/scholar_lookup?title=Recsys+challenge+2018%3A+automatic+music+playlist+continuation&author=Ching-Wei+Chen&author=Paul+Lamere&author=Markus+Schedl&author=Hamed+Zamani&publication_year=2018&pages=527-528&doi=10.1145%2F3240323.3240342)

Show all references

## Cited By

[View all](https://dl.acm.org/action/ajaxShowCitedBy?doi=10.1145/3705328.3748053 "View all cited by in new tab")

* **Vellard E**Charolois-Pasqua E**Rebboud Y**Lisena P**Troncy R**(2025)Interactive Playlist Generation from Titles**Proceedings of the Nineteenth ACM Conference on Recommender Systems**10.1145/3705328.3759336**(1337-1339)**Online publication date: 22-Sep-2025
  [https://dl.acm.org/doi/10.1145/3705328.3759336](https://dl.acm.org/doi/10.1145/3705328.3759336)

## Index Terms

## Recommendations

## Comments

[![Ad about ACM's OA transition and recent DL changes](https://dl.acm.org/sda/108255/acm-pres-on-oa-trans-and-dl-changes.png)](https://dl.acm.org/action/clickThrough?id=108255&url=https%3A%2F%2Fwww.acm.org%2Fabout-acm%2Facm-pres-on-oa-transition-and-dl-changes&loc=%2Fdoi%2F10.1145%2F3705328.3748053&pubId=63796627&placeholderId=101020&productId=108193)

[![Colint COLA Sky Ad](https://dl.acm.org/sda/108263/colint-dl-sky-ad.png)](https://dl.acm.org/action/clickThrough?id=108263&url=https%3A%2F%2Fdl.acm.org%2Fjournal%2Fcola&loc=%2Fdoi%2F10.1145%2F3705328.3748053&pubId=63796627&placeholderId=101021&productId=108184)

[![ACM Books Townsend Ad](https://dl.acm.org/sda/108241/ACM%20Books_Townsend_Ad.jpg)](https://dl.acm.org/action/clickThrough?id=108241&url=https%3A%2F%2Fdl.acm.org%2Fdoi%2Fbook%2F10.1145%2F3640508&loc=%2Fdoi%2F10.1145%2F3705328.3748053&pubId=63796627&placeholderId=101022&productId=108184)

[View full text](https://dl.acm.org/doi/full/10.1145/3705328.3748053)|[Download PDF](https://dl.acm.org/doi/pdf/10.1145/3705328.3748053?download=true)

[View Table of Contents](https://dl.acm.org/doi/proceedings/10.1145/3705328)

## Footer

### Categories

* [Journals](https://dl.acm.org/journals "Browse a listing of ACM’s Journals")
* [Magazines](https://dl.acm.org/magazines "Browse ACM's Magazines")
* [Books](https://dl.acm.org/acmbooks "Browse new Releases of ACM Books")
* [Proceedings](https://dl.acm.org/proceedings "Browse the ACM Proceedings")
* [SIGs](https://dl.acm.org/sigs "Browse the Special Interest Groups")
* [Conferences](https://dl.acm.org/conferences "Browse the Conferences")
* [Collections](https://dl.acm.org/collections "Browse the Special Collections")
* [People](https://dl.acm.org/people "Discover ACM’s community of authors")

### About

* [About ACM Digital Library](https://dl.acm.org/about)
* [ACM Digital Library Board](https://dl.acm.org/about/dlboard "ACM DL Board - Governance and Support Staff")
* [Author Guidelines](https://www.acm.org/publications/authors/information-for-authors "Information for Authors")
* [All Holdings within the ACM Digital Library](https://dl.acm.org/about/content#sec2)
* [ACM Computing Classification System](https://dl.acm.org/ccs "Classify publications using ACM's Computing Classification System")
* [Accessibility Statement](https://dl.acm.org/about/accessibility "Digital Library Accessibility")

### Join

* [Join ACM](https://www.acm.org/membership/join)
* [Join SIGs](https://www.acm.org/special-interest-groups/join)
* [Subscribe to Publications](https://www.acm.org/publications/subscribe)
* [Institutions and Libraries](https://libraries.acm.org/)

### Connect

* [Contact us via email](mailto:dl-team@hq.acm.org)
* [ACM on Facebook](https://www.facebook.com/AssociationForComputingMachinery/)
* [ACM DL on X](https://x.com/acmdl)
* [ACM on Linkedin](https://www.linkedin.com/company/association-for-computing-machinery/)
* [Send Feedback]()
* [Submit a Bug Report]()

The ACM Digital Library is published by the Association for Computing Machinery. Copyright © 2026 ACM, Inc.

* [Terms of Usage](https://libraries.acm.org/digital-library/policies#anchor3)
* [Privacy Policy](https://www.acm.org/about-acm/privacy-policy)
* [Code of Ethics](https://www.acm.org/code-of-ethics)

[![ACM Digital Library home](https://dl.acm.org/specs/products/acm/releasedAssets/images/acm-logo-dl-8437178134fce530bc785276fc316cbf.png)](https://dl.acm.org/)

 [![ACM Association for Computing Machinery corporate logo](https://dl.acm.org/specs/products/acm/releasedAssets/images/acm-logo-3-10aed79f3a6c95ddb67053b599f029af.png)](https://www.acm.org/ "external site link")

<iframe tabindex="-1" role="presentation" aria-hidden="true" title="Blank" src="https://consentcdn.cookiebot.com/sdk/bc-v4.min.html"></iframe>

<iframe height="1" width="1"></iframe>

[PDF](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/pdf/10.1145/3705328.3748053&hl=en&sa=T&oi=ucasa&ct=ufr&ei=dT19abXgIeyj6rQPgIvEoAQ&scisig=AHkA5jS0XjMk76GEr8gOvFy_hxx5)[Help](https://scholar.google.com/scholar/help.html#access)
