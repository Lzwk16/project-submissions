# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone: Non-Personalied Video Games Recommender

## Background and Problem Statement

In the recent decades, recommender systems have been becoming incresingly prevalent in our daily lives. Ranging from e-commerce platforms such as Amazon, ebay, as well as online streaming service giants like Spotify and Netflix, these huge corporations are utilising them widely in their applications to suggest products, movies and musics to users. They have been proven to be highly effective in improving user engagement and generating customer satisfaction so as to drive business revenue and growth. These intelligent systems typically rely on a combination of user feedback data such as ratings, reviews, purchase history, as well as contextual information such as time duration, location and social networks in order to accurately predict user behaviors.

Singapore’s esports sector is a rising industry due to its huge market growth during the Covid-19 pandemic, with much growth potential to emerge as the leader in the South East Asian region having hosted many major esports competition such as The International 2022. Its revenue figure is projected to have approximately 6.5% compounded annual growth rate by 2023. With the abundance of options in online platforms due to numerous amounts of new games released each year, this has led to users experiencing difficulties in finding the right choice of games that aligns well to their area of interests and preferences. As a Data Scientist employed by a local games developer firm, I am tasked to create a video games recommender system for the company’s database of games that will allow gamers to tap on when patronising our virtual store by providing a comprehensive list of recommended game titles. To determine the feasibility of the project,  I will be simulating the building of the recommender system model on Steam’s database of game reviews and features by evaluating and validating the algorithm of various models' performance in predicting the user reviews from the different input features.


## Project Objectives
Steam is the largest open source digital distribution platform for PC gaming as it houses a wide variety of games from many developers and publishers. In the first phase of this project, we will be aiming to conceptualise a prototype of recommendation model that can accurately recommend preferred game titles to players, by implicitly deriving the ratings of the user based on their playtime activity. The selected model will also be deployed through Streamlit app consisting of a simple user interface that directly access the Steam games library of the recommended game titles.


## Datasets

The primary datasets are scrapped from Steam's store and uploaded to [Kaggle](https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam) by Anton Kozyriev.

Additional information on the game titles were scrapped from [SteamSpy's customised API](https://pypi.org/project/steamspypi/) which gives more details about the various game titles found in the games.csv dataset that will be essential in building our models.


## Data Dictionary
The main datasets (recommendations, games, metadata and users) will be primarily utilised for my analysis. Additional data features from app_list will consist of namely the developer and publisher data which is used for content filtering modelling. Due to the huge size of the datasets, it will be uploaded onto my google drive directory: https://drive.google.com/drive/u/1/folders/1ntBLyIWNW_tTm2yszy5l6ZvAYNq-wHGo

### Data Dictionary

**Features common to multiple datasets**
|Feature|Type|Dataset|Description|
|---|---|---|---|
|app_id|int|games.csv, receommendations.csv, app_list.csv|Unique app id of game title on steam| 
|title|string|games.csv, receommendations.csv, app_list.csv| Name of game title on steam|
|user_id|int|users.csv, receommendations.csv| Unique user id of player|

**Features used in games.csv**
|Feature|Type|Dataset|Description|
|---|---|---|---|
|date_release|string|games.csv|Product release date|
|win|boolean|games.csv|Windows compatibility|
|mac|boolean|games.csv|Mac compatibility|
|linux|boolean|games.csv|Linux compatibility|
|rating|string|games.csv|Overall rating of the game title|
|Postive ratio|int|games.csv|Overall ratio of postivie feedbacks from users|
|price_final|float|games.csv|final(current) price of the game|
|price_original|float|games.csv|Initial price(USD) of the game after discount|
|discount|float|games.csv|discount price of the game|
|steam_deck|boolean|games.csv|Steam console compatibility|

**Features used in recommendations.csv**
|Feature|Type|Dataset|Description|
|---|---|---|---|
|helpful|int|recommendations.csv|no of users who found recommendation helpful|
|funny|int|recommendations.csv|no of users who found recommendation funny|
|date|string|recommendations.csv|date of review|
|is_recommended|boolean|recommendations.csv|is the game recommended by the user?|
|hours|int|recommendations.csv|no. of hours played by the user|
|review_id|int|recommendations.csv|unique review id of review|

**Features used in users.csv**
|Feature|Type|Dataset|Description|
|---|---|---|---|
|products|int|users.csv|no. of products in user's steam library|
|reviews|int|users.csv|Number of reviews published|

**Features used in app_list.csv**
|Feature|Type|app_list|Description|
|---|---|---|---|
|average_forever|int|app_list|Permament average playtime(mins)|
|average_2weeks|int|app_list|average playtime in last 2 weeks(mins)|
|median_forever|int|app_list|Permament median playtime(mins)|
|median_2weeks|int|app_list|median playtime in last 2 weeks(mins)|
|developer|int|app_list|developer name|
|publisher|int|app_list|publisher name|
|ccu|int|app_list|no. of concurrent users|


## Feature engineering: User Playtime

Since the dataset does not have a direct explicit ratings feedback from the users, feature engineering will be performed by inferring that a user's playtime is reflective of their true ratings, on a scale of 1 to 5. This is on the assumption that the longer the playtime hours, they truly like the game.


## Modelling

In order to build an appropriate recommender system model that will be able to cater to diffeernt users' preferences, we will be exploring namely 2 commonly known approaches to building these models, namely content filtering and collaborative filtering. Content filtering takes into account of the different attributes and features of the various titles being recommended. The model analyses the content of items as well as the user's past interactions with similar items in order to make recommendations. On the other hand, collaborative filtering takes the approach on relying the behaviour and preferences from existing users. It analyses users interactions with the various titles, such as ratings and purchase history in order to find similarities between users. Once that is done, the model recommends these selected items based on the similar items which users have favoured in the past. 

Content filtering models are usually evaluated through similarity metrics by determining the similarities between the features of items that the user interacts with. Some of these common metrics include cosine similarity and euclidean distance which are computed between different items. On the other hand, collaborative filtering models rely on more complex mathematical algorithms to determine the users' behaviour and interactions with the items. The results for the collaborative filtering model in the project are summarised in tabular format as shown below: 

| **Model No.**| **Model** | **RMSE** |
| --- | --- | ---|
| 1 | Random Predictor (Baseline) | 1.444 |
| 2 | Baseline Estimate | 0.985 |
| 3 | **SVD (Matrix Factorization)** | **0.984** |
| 4 | SVD++ (Matrix Factorization) | 0.981 |
| 5 | SlopeOne | 1.009 |
| 6 | Co-Clustering | 1.119 |

| **Model No.**| **Model** | **Precision@10** | **Recall@10** |
| --- | --- | ---| ---|
| 1 | Random Predictor (Baseline) | 0.454 | 0.505 |
| 2 | Baseline Estimate | 0.559 | 0.730 |
| 3 | **SVD (Matrix Factorization)** | **0.557** | **0.734** |
| 4 | SVD++ (Matrix Factorization) | 0.558 | 0.735 |
| 5 | SlopeOne | 0.537 | 0.691 |
| 6 | Co-Clustering | 0.435 | 0.443 |


We can see that the performances of the matrix factorization based models and baseline estimate using regularization models have similar performance where they scored similar RMSE between 0.981-0.985, Precision@10 between 0.730 - 0.735 and Recall@10 of 0.577-0.559. The recall@10 scores are significantly higher than precision@10, as this aligns well with the goal of our initial objective which is to provide a comprehensive list of recommended game titles among the wide diversity of game titles to users. Hence, we will be prioritising this metric to be used for evaluating our selected model.

Considering the scope of our project and these scores, our final selected model will be the SVD algorithm due its simpler interpretability, as well as requiring less computational power and being able to identify possible hidden latent features that can affect the playtime derived ratings while compared to the baseline estimate model.


## Conclusion and Limitations

- We have successfully executed the first built a protoype content based and collaborative filtering model that is able to predict the inferred ratings well based on the user's playtime of a specific game. On top of that, we have also designed and deployed a simple content filtering model onto streamlit that is able to accurately recommend new game titles on steam platform based on their past games, as well as their preferences, through the use of an NLP based predictor. This information collected from the data about the different models can be used for further assessment in the next step of our business problem for pitching to relevant stakeholders in our idea to eventually create a robust recommender system for the company's games database, so as to ensure that potential clients can continue to tap on explore different game titles across various genres. 

On the whole, although the research and protoyping phase was a sucess, there were some challenges that we have faced when building these 2 different model types. In content filtering, we faced the issue of cold start where the model was unable to recommend game titles to new users with little to information regarding their gaming behaviour. However, this roadblock can be resolved through the means of collaborative filtering, where users who have reviewed little game titles are able to be successfully recommended common game titles played by most users with numerous reviews. From these results, it can be justified that the combination of a collaborative and content filtering model will be able to definitely pull off more precise recommendations by accurately predicting more similar game titles to new users. Handling a large dataset that involves training on selected models in determining the predictability of content filtering, collaborative filtering, as well as hybrid based recommenders requires many considerations as it also limits to amount of feature exploration that can be done as a result of limitation on computational resources, which is something that we have faced in this project


## Recommendations 

Although we have managed to successfully evaluated the different prototype recommender system models using the steam dataset, there were many challenges that we have faced along the way which has caused us to take certain detours. One such key roadblock was the lack of computational resources available, which leads us to scaling down our dataset so as to focus only on the key features that can impact the models' predictive ability. For future work, it can be proposed that subsequent model training and evaluation should consider these approaches:

1. Train model using the original dataset consisting of approximately 10 million rows on data cloud-based platforms such as Google Cloud Platform(GCP), Amazon Web Services(AWS) or Microsoft Azure. These virtual platforms can provide million of memory in RAM that can scale up and accomodate towards training the model on huge datasets.

2. Employ Implicit based prediction algorithms for the training of our collaborative-based models, as well as hybrid based models that can effectively handle the cold-start issue 


3. Incorporate the use of advanced NLP based models that function using Deep Learing techniques such as BERT(Bi-Directional Encoder Representations for Tranformers), GPT(Generative Pre-trained Transformer) when designing an NLP based recommender in order to further improve its accuracy and precision in recommending game titles as it factors sequential textual data into consideration



Source: https://www.jtugman.com/posts/singapore-gaming-industry-2021 
