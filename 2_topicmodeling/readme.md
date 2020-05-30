# Stage 2. Topic Modeling

Topic modeling was performed on the science fiction corpus using the scikit-learn Latent Dirichlet allocation (LDA) library. This technique enabled us to identify a topic that was concerned with urban space and retrieve the novels with the highest proportion of said topic.

The model was fine-tuned by running the algorithm several times and evaluating each result depending on: how even is the topics’ distribution in the topic space; the presence of a topic about urban space; and what novels have the highest percentage of this topic.

Three were the algorithm's parameters I decided to manipulate in fine-tuning. Max_df, which regulates the presence of highly occurring words in the word-document matrix, was set either to 0.25 or 0.30. Hence, only the words that occurred in less than 25% or 30% of the documents were considered. Max_features, which regulates the number of unique words and the presence of rare words in the matrix, was set to 1000 or 10000. I decided to keep 10000 in order to have less common words in the model too and so that the presence of highly occurring once would not sway the model as much. N_components, which regulates the number of topics in the model, was set to 50, 60, 70, 80, 90, 100, 120. This is the parameter that most affects the results and there. Several attempts were made by changing these parameters. The best

The best model was obtained setting the number of topics at 80, the number of features (or unique words) at 10000, and the maximum document frequency for each word at 30%. The HTML visualization of this model is available at [pyLDAvis-80_10000_0.30.html](https://github.com/federicabologna/thesis_space_scifi/blob/master/2_topicmodeling/pyLDAvis-80_10000_0.30.html).

The code written by Matthew Wilkens to perform LDA on the corpus is available in [lda_80_10000_0.30.ipynb](https://github.com/federicabologna/thesis_space_scifi/blob/master/2_topicmodeling/lda_80_10000_0.30.ipynb). 
