#  ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2 - Singapore Housing Data and Kaggle Challenge

In this project, we are tasked to built a Linear Regression Model to predict the HDB resale prices for Project 2 Regression on challenge in Kaggle. The dataset can be found in this link [Dataset](https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data)

The project is broken up into 2 parts. Part 1 of the notebook code will involve data cleaning, exploratory data analysis and feature engineering. Part 2 of the notebook code will involve conceptualising through model selection, model preprocessing, model and feature selection. Part 3 of the notebook code will involve the final analysis and selection of key features for model deployment

## Python Libraries

1. Pandas
2. Numpy
3. Matplotlib
4. Seaborn
5. ScikitLearn (part 2, 3 of the notebook)
6. XGBoost (part 3 of notebook)
7. Streamlit (Model deployment)

## Data Visualisations

Key housing metrics on Singapore's HDB resale flats have been updated and deployed nto Tableau Public Dashboard: [Singapore's HDB Resale Flats Price 2012-2021](https://public.tableau.com/app/profile/kenneth.lim7576/viz/GAProject2Dashboard/HDBdashbaord#1)

## Problem Statement

- In Singapore, getting a HDB is probably one of the biggest financial decisions many Singaporeans will have to make, given its exhorbitant cost. Furthermore, given the fluctuating property prices in the market throughout the recent decade as a result several cooling measures and increasing demand, making a wrong decision could set one back several years in terms of opportunity cost & time value of money. As a Data Scientist employed by an online social networking service headquarterd in Singapore, our team has been requested by the management to design a predictive model that can help property and housing agents in the market to offer prediction services of HDB resale prices, so that they can offer informed consulting advice to their clients.

- In this project, we seek to build a Simple Regression model for deployment by evaluating its feasibility in predicting the housing prices of HDB resale flats in Singapore through the selection of several key features, so as to help Singaporeans make more informed decisions on the different types of resale flats available in the property market. We will be basing the criteria metric by aiming for a low RMSE(Root-Mean Sqaure) score so as to minimise the error cost during the prediction of HDB resale prices in order to reduce the amount of financial errors that clients can incur.

## Results

(From Part 3: Modelling for deployment):

| **Model** | **Train RMSE** | **Test RMSE** | **Features** |
| --- | ---| ---| ---|
| Linear Regression(Baseline) | 53905 | 53889 | 8 |
| Lasso | 54125 | 54189 | 8 |
| Ridge | 53878 | 53889 | 8 |
| Random Forest | 18647 | 28984 | 8 |
| **XGBoost** | 22896 | **28500** | 8 |

Although the Random Forest model had the lowest RMSE, it is not robust towards unseen data based on the RMSE results of our train and validation data. Hence, the XGBoost Regression model will be selected for deployment, scoring an RMSE of 28500 using these key features: 

| **Variable** | **Description** |
| -------- | -------- |
| floor_area_sqm | floor area of the resale flat unit in square metres |
| Mature_Estate | boolean value if the town is a mature estate |
| remaining_lease | number of remaining lease years of HDB flat upon transaction |
| max_floor_lvl | highest floor of the resale flat |
| town| HDB township where the flat is located, e.g. BUKIT MERAH |
| mrt_nearest_distance | distance (in metres) to the nearest MRT station |
| flat_type | type of the resale flat unit, e.g. 3 ROOM |
| mid | middle value of storey_range |

## Conclusion

In summary, we have sucessfully managed to successfully construct a Simple Regression model that is capable of predicting the HDB resale prices in Singapore through the selection of key features that can potentially influence the the target output. Beginning with importing the necessary libraries and cleaning the data, we were able to conduct several key analysis at the exploratory data analysis stage where important features that can impact the HDB resale price were identified and analysed. Thereafter, new features were engineered relative to the existing ones that were found to have certain degree of linearity with regards to the target price variable. These features were eventually selected and compiled into a final dataset which was passed in for Linear Regression modelling, as well as optimising the key variables through Lasso and Ridge regularization to determine the final set of useful features for predicting the HDB resale price. By running through this model workflow, we have managed to achieve an **RMSE** of **28500** for our XGBoost Regression Model. With this chain of thought, we have also understood the important features that can contribute in determining the final price of a HDB resale flat, where our clients can tap upon on to devise a range of prices when advertising for their property. This will allow them to reap better sale profits and commisions in the property market, as well as assist buyers in determining the correct price range when purchasing a desired type of property in the market.

## Model Deployment

The final model has been deployed onto streamlit cloud at the following link: [Singapore HDB price predictor](https://lzwk16-project-submissions-project-2codehdb-app-q54vdr.streamlit.app)

## Future Work

The results from the newly built machine learning model using XGBoost Regression have successfully proven that our top key predictors are what clients tend to look out for when considering to purchase a resale flat, as they can significantly affect the final sale price of HDB resale flats in Singapore. However, these prices will fluctuate overtime with the addition of new data. Hence, we propose a few alternative methods in order to maintain the robustness of our deployed model:

1. Since the dataset only contains resale price data till 2021, an automated pipeline can be created in the future that connects to the HDB resale price API at [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices) to ensure our deployed model is able to continue training using updated data.

2. As the size of dataset continues to increase over the years with addition of new data, the model could be deployed on cloud based platforms such as Google Cloud or Amazon Web Services(AWS) so as to maintain its robustness in training



