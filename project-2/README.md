#  ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2 - Singapore Housing Data and Kaggle Challenge

In this project, we are tasked to built a Linear Regression Model to predict the HDB resale prices for Project 2 Regression on challenge in Kaggle. The dataset can be found in this link [Dataset](https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data)

The project is broken up into 2 parts. Part 1 of the notebook code will involve data cleaning, exploratory data analysis and feature engineering. Part 2 of the notebook code will involve mainly on model selection, model preprocessing, model and feature selection.

## Python Libraries

1. Pandas
2. Numpy
3. Matplotlib
4. Seaborn
5. ScikitLearn (part 2 of the notebook)
6. statsmodel.api

## Data Visualisations

Key housing metrics on Singapore's HDB resale flats have been updated and deployed nto Tableau Public Dashboard: [Singapore's HDB Resale Flats Price 2012-2021](https://public.tableau.com/app/profile/kenneth.lim7576/viz/GAProject2Dashboard/HDBdashbaord#1)

## Problem Statement

- In Singapore, getting a HDB is probably one of the biggest financial decisions many Singaporeans will have to make, given its exhorbitant cost. Furthermore, given the fluctuating property prices in the market throughout the recent decade as a result several cooling measures and increasing demand, making a wrong decision could set one back several years in terms of opportunity cost & time value of money. As a Data Scientist employed by an online social networking service headquarterd in Singapore, our team has been requested by the management to design a predictive model that can help property and housing agents in the market to offer prediction services of HDB resale prices, so that they can offer informed consulting advice to their clients.

- In this project, we seek to build a Linear Regression model and evaluate its feasibility in predicting the housing prices of HDB resale flats in Singapore through the selection of several key features, so as to help Singaporeans make more informed decisions on the different types of resale flats available in the property market. We will be basing the criteria metric by aiming for a low RMSE(Root-Mean Sqaure) score so as to minimise the error cost during the prediction of HDB resale prices in order to reduce the amount of financial errors that clients can incur.

## Conclusion

In summary, we have sucessfully managed to successfully construct a Linear Regression model that is capable of predicting the HDB resale prices in Singapore through the selection of key features that can potentially influence the the target output. Beginning with importing the necessary libraries and cleaning the data, we were able to conduct several key analysis at the exploratory data analysis stage where important features that can impact the HDB resale price were identified and analysed. Thereafter, new features were engineered relative to the existing ones that were found to have certain degree of linearity with regards to the target price variable. These features were eventually selected and compiled into a final dataset which was passed in for Linear Regression modelling, as well as optimising the key variables through Lasso and Ridge regularization to determine the final set of useful features for predicting the HDB resale price. By running through this model workflow, we have managed to achieve an **RMSE** of **51814** for our Linear Regression Model. With this chain of thought, we have also understood the important features that can contribute in determining the final price of a HDB resale flat, where our clients can tap upon on to devise a range of prices when advertising for their property. This will allow them to reap better sale profits and commisions in the property market, as well as assist buyers in determining the correct price range when purchasing a desired type of property in the market.


## Recommendations

The results from the newly built machine learning model by Linear Regression have successfully proven that our top key predictors are what clients tend to look out for when considering to purchase a resale flat, as they can significantly affect the final sale price of HDB resale flats in Singapore. In spite of this successful outcome on our first prototype model, we can definitely look into further analysis and research to improve the predictive power of the finalised model for deployment to production. Some of these examples include:

1. Experimenting using other advanced regression techniques such Random Forest, Gradient Boosting regression techniques. Linear Regression is a machine learning model which is highly reliant on using features with strong correlation to predict the resale price accurately. Therefore, it will pale in comparison to these tree-based regression techniques that are more robust in handling features with weaker correlations. Hence, we should definitely research and incorporate them so as to further analyse if they will have any impact on the final resale price

2. As there are many available sub-features in the various categorial groups, further in-depth analysis could be done by breaking down to the different attributes surrounding the flat types/flat models where seperate models can be constructed to predict the prices of each type for property and housing agents to tap on, as the resale prices of these different flats might be affected by the different features individually

3. Lastly, we can explore other features that potential buyers could take into consideration also, such as the property's proximity to the Central Business District(CBD) area of Singapore, nature parks, as well as other recreational ammenities that could plausibly affect the overall HDB resale price in the market.



