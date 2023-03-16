# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP Classification of SubReddit Posts

### Description

In week four we've learned about a few different classifiers. In week five we'll learn about webscraping, APIs, and Natural Language Processing (NLP). This project will put those skills to the test.

## Problem Statement:

Singapore has recently lifted all its Covid-19 pre-departure testing in Feb 2023 as part of the big move to lift its remaining border measures at the end of the pandemic. As a Data Analyst hired by a local travel agency, we are tasked to research on some of the latest popular travel destinations in order to assist the marketing and operations team in their campaign to promote tour package services in these countries for the upcoming 2023 Travel Fair. In order to ensure a successful campaign, we would need to gather essential reviews on the latest hit attractions that are currently trending among Singaporeans. Our preliminary research studies have shown that Japan and Thailand have emerged as one of the top few holiday destinations for Singaporeans. In this project, we will be attempting to build a binary classifer model that can correctly categorise these reviews into both countries.

As a novel apporach, text information from subreddits r/JapanTravel and r/ThailandTourism will be scraped using Reddit's Pushshift API to collect the necesary data and train the model. Further analysis on the text data, as well as evaluation on the model's ability to successfully classify the corresponding texts would be elaborated throughout the notebook

## Libraries Used

1. Pandas
2. Numpy
3. Matplotlib
4. Seaborn
5. Sklearn
6. NLTK

## Modelling

In this NLP classifer project, we will be selecting the following classification models to be trained on as follows:

1. Multinomial Naive Bayes
2. Logistic Regression
3. Decision Tree
4. RandomForest
5. GradientBoosting

Taking into consideration the requirements of the project with respect to its business problem statement, the accuracy score of the model various models will be optimised in the execution of the project through Jupyter Notebook and the related libraries involved as mentioned above

| **Model No.**| **Model** | **Accuracy** | **Precision** | **Recall** | **F1** | **AUC** |
| --- | --- | ---| ---| ---| ---| ---|
| 1 | Multinomial Naive Bayes(CountVectorizer) | 0.864 | 0.961 | 0.759 | 0.848 | 0.95  |
| 2 | Multinomial Naive Bayes(TFIDF) | 0.860 | 0.952 | 0.759 | 0.844 | 0.95    |
| 3 | **Logistic Regression(TFIDF)** | **0.856** | 0.881 | 0.824 | 0.851 | **0.94** |
| 4 | Decision Tree(TFIDF) | 0.674 | 0.616 | 0.923 | 0.739 |  0.73 |
| 5 | Random Forest(TFIDF) | 0.810 | 0.812 | 0.808 | 0.810 |  0.88 |
| 6 | Gradient Boosting (TFIDF) | 0.818 | 0.803 | 0.843 | 0.822 |  0.91 |


According to the summary table concerning the different classification metrics, it can be inferred that the Logistic Regression Model has the highest performing accuracy score while at the same time being able to maintain its consistency across the other metrics. From this numerical information, it can be concluded that logistic regression is a simple and all-rounder classification model that can be used in the early phase of correctly predicting the class of incoming unseen posts into r/JapanTravel and r/ThailandTourism, as the individual misclassification rate for both posts are the most balanced among the top 3 performing models. Hence, Logistic Regression will be selected as the final model to be considered for potential depolyment to production



## Conclusion

- We have successfully built a novel NLP classifier model that is able to classify incoming unseen travel posts into subreddit categories JapanTravel and ThailandTourism. This can be used for gathering feedbacks from past travellers about the important sights, places and activities that potential tourists tend to lookout for. The marketing and operations team will be able to effectively use them to conduct their research on the latest travel trends in these 2 countries and execute their campaign for the upcoming travel fair amidst the reopening of Singapore's international borders. Using the selected model (Model 3: Logistic Regression TFIDF), it scored 85.6% on accuracy. These numbers indicate with good confidence that the prototype model can predict and classify well on incoming unseen posts. The results are encouraging and eligible for subsequent fine-tuning on broader dataset for validation in the future, in order to be potentially considered for actual deployment to production




## Recommendations

Although we have managed to successfully built a novel prototype NLP model that can be used to classify incoming unseen posts, there are definitely other ways which we can improve the model's predictive performance. Some of the possible ways are listed as such:

1. Duration of the dataset was scrapped with posts created from early to middle of March. Japan has seasonal sights that vary throughout the year, which will affect the type of words passed and selected by the model, which could impact the model's performance during different season cycles. It would be feasible to consider training on a larger validation dataset in groups of the various months corresponding to the different seasons


2. Employ Deep Learning techniques such as Recurrent Nerual Networks(RNN) or Transformer-models that have better predictability in processing sequential text data in order to better classify incoming unseen posts accurately in JapanTravel or ThailandTourism


3. The subreddits were taken from an international community due to lack of forum feedback from Singaporean travellers to these places. Hence, the validation dataset could be trained on text information taken from local subreddit forums instead when possible to validate its performance