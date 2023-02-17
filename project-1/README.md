# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Exploring climate data of Singapore

### Problem Statement

- In the past years, Singapore has encountered a growing number of flash floods due to unpredictable weather conditions, including heavy rainfall caused by climate change and global warming. These floods can significantly affect daily business operations and threaten the stability of Singapore's food supply. As a Data Analyst employed by the Singapore Food Agency, we would like to incorporate the use of weather analytics to examine how the rainfall parameters concerning Singapore's weather can impact the overall seafood supply and demand in the local market.The analysis results will provide valuable insights to various audiences and stakeholders in Singapore such as restaurants, F&B retailers and grocery suppliers relying on the local seafood market for their sales and operations, as well as to assist them in better optimising their seafood resources during the rainy seasons.

---

### Selected Datasets

- [Monthly Number of Rainy Days](https://data.gov.sg/dataset/rainfall-monthly-number-of-rain-days): Monthly number of rain days from 1982 to 2022. A day is considered to have “rained” if the total rainfall for that day is 0.2mm or more.

- [Monthly Total Rainfall](https://data.gov.sg/dataset/rainfall-monthly-total): Monthly total rain recorded in mm(millimeters) from 1982 to 2022

- [Surface Air Temperature](https://data.gov.sg/dataset/surface-air-temperature-mean-daily-minimum): Monthly mean surface air temperature in celsius from 1982 to 2022

- [Monthly Mean Sunshine Duration](https://data.gov.sg/dataset/sunshine-duration-monthly-mean-daily-duration): Monthly mean sunshine hours from 1982 to 2022

- [Relative Humidity](https://data.gov.sg/dataset/relative-humidity-monthly-mean): Monthly mean relative humidity from 1982 to 2022

- [Monthly Maximum Daily Rainfall](https://data.gov.sg/dataset/rainfall-monthly-maximum-daily-total): Monthly maximum rainfall in a day from 1982 to 2022

- [Hourly wet bulb temperature](https://data.gov.sg/dataset/wet-bulb-temperature-hourly): Hourly wet bulb temperature from 1982 to 2022

- [Singapore Seafood Supply](https://tablebuilder.singstat.gov.sg/table/TS/M890741#!): Singapore's seafood supply from 1999 to 2022

### Data Sources:
1. https://data.gov.sg
2. https://tablebuilder.singstat.gov.sg
---

### Outside Research
Since the recent decades, climate change has resulted in a rapid overall increase in the average temperature of our planet. This has resulted severe consequences such as the melting of polar ice caps which caused the rise in global sea levels, and also being subjected to extreme weather conditions. As a result, communities and nations along the coastlines are becoming increasingly vulnerable to floods and threats such as tsunamis. 

Out of all the regions in the world, countries in Asia and Southeast Asia have been assessed to have the highest risk towards the impacts of sea level rise and extreme weather conditions on the local population, with 12 out of 20 countries having the greatest exposure to sea level rise being found in Asia(IPCC Sixth Assessment Report 2022: Chapter 10: Asia. In Climate Change 2022: Impacts, Adaptation and Vulnerability). 

Singapore is a small tropical island nation surrounded by coastlines in all directions with high amounts of annual rainfall. It is therefore a prime candidate in being exposed to these extreme weather conditions and threats resulting from rising sea levels, which can result in disruptions to business supply chains as well as volatile food pricings due to its reliance on imported food supply which accounts for up to 90%(A sustainable food system for Singapore and beyond, SFA Singapore). 


### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|total_rainfall|float|rainfall-monthly-total|Total rainfall in mm| 
|no_of_rainy_days|float|rainfall-monthly-number-of-rain-days| Number of Rainy days|
|maximum_rainfall_in_a_day|float|rainfall-monthly-highest-daily-total|Maximum rainfall in a day|
|mean_air_temp|float|surface-air-temperature-monthly-mean|Monthly mean surface air temperature|
|mean_sunshine_hrs|float|sunshine-duration-monthly-mean-daily-duration|Monthly mean sunshine hours in a day|
|mean_rh|float|relative-humidity-monthly-mean|Monthly mean relative humidity|
|year|int|Singapore_climate_data_2022|Years ranging from 1982 - 2022|
|Month|string|Singapore_climate_data_2022|Month in a year|
|Seafood Wholesale (Tonnes)|int|SG-seafood-supply|Refers to seafood sold at Singapore's fishery ports and include local landings of seafood and imports of seafood. Includes fresh, frozen seafood and 'Low-value fish'.|

---

### Exploratory Data Analysis

1. 1997 is suggested to be the driest month with the least amount of total rainfall and rainy days according to the analysis

2. Having a higher average relative humidity results in a higher amount of rainy days per month, amount of total overall rainfall and maximum rainfall in a day. This suggests that the likelihood of precipitation is higher due to greater amount of water vapor per volume in the air for cloud formation to take place through condendation

3. Having a higher average relative humidity indicates a lower overall average sunshine hours and air temperature due to greater cloud cover in the atmosphere which lowers the evaporation rate of water vapor formation in the atmosphere

4. The average annual air temperature has been steadily increasing after 1990

5. The average annual sunshine temperature, relative humidity has been steadily increasing and decreasing respectively after 2013. Exception years that do not follow these trends include 2017 and 2019. 2017 recorded significantly higher annual mean relative humidity which corresponds to greater overall number of rainy days throughout the year

6. There are abnormally high amounts of maximum rainfall in a day across the year through out time period from 1982 - 2022

7. Months of January, November and December have considerably lower mean air temperature and mean relative humidity. November and December also have significantly fewer sunshine hours.

8. Having a higher relative mean humidity indicates that more seafood for consumption is being sold at fishery ports throughout the time period from 1982 - 2022. This can possibly suggest that certain groups of seafood sold in the fisheries can thrive under high humidity

## Conclusions and Recommendations
---
*Conclusion

We have analysed how the performance of the different weather variables vary over the last 20 years according to the Singapore's tropical climate. The amount of rainfall received and number of rainy days are relatively influenced by common weather metrics such as air temperature, relative humidity and sunshine hours. While referencing to our EDA findings, we have also discovered that the relative humidity in Singapore seems to be the key variable in influencing other weather variables as supported scientific theories behind the different stages of the hydrologic cycle, beginning from evaporation and ending at precipitation. However, the likelihood of whether rainfall will occur in any given day will still highly co-depend on the other weather variables.

In the explansion towards the business problem that we have defined earlier in our problem statement, we have also observed that the overall supply and trade of local seafood can be affected by the relative humidity in the environment. With the support of some additional research online, we have found out that the relative humidity could influence the conditions for planktons, the marine organism at the bottom of the marine food chain, to thrive in marine ecosystems. 

According to research articles and websites online, it has been extensively studied that planktons are the key components in regulating and keeping the carbon cycle in check which controls the amount of CO2 stored in the oceans. With disruptions to its population as a result of climate change and global warming, it can possibly result in an excessive build up of CO2 in the oceans and threaten the marine ecosystem. Therefore, it is essential to understand how the different weather conditions can affect the overall state of the marine ecosystem and its current role towards climate change.

*Recommendations

The findings from this analysis can help business owners and organisations in the Fishery, F&B and aquaculture sectors to make more informed decisions and optimise their resources more effectively 

From this study, we can possibly expand the research towards other environment or weather variables in order to further verify our hypothesis on how the relative humidity can influence the seafood and supply and wholesale trade in Singapore to ensure future sustainability on the production and demand for seafood in Singapore. Some of this examples include:

1. Quantify how other weather variables such as atmospheric pressure, wind speed and cloud cover to further verify if there is any relationship with respect to the overall seafood supply. 

2. Incorporating pollutant metrics that are strongly associated with climate change such the emission of common greenhouse gasses(Carbon dioxide, Methane) to see how they can affect seafood catches in wild fisheries and harvests from local fish farms 

3. Quantify the relationship between the sales of different seafood sub-types, and also analyse how the different prices of various seafoods can vary with respect to weather parameters.


## Sources and Citations

1. IPCC Sixth Assessment Report 2022: Chapter 10: Asia. In Climate Change 2022: Impacts, Adaptation and Vulnerability

2. A sustainable food system for Singapore and beyond, SFA Singapore, 11 Nov 2022:
https://www.sfa.gov.sg/food-for-thought/article/detail/a-sustainable-food-system-for-singapore-and-beyond

3. IN FOCUS: How climate change can threaten food production in Singapore, CNA Singapore, 19 Dec 2020: 
https://www.channelnewsasia.com/singapore/climate-change-singapore-food-production-fish-eggs-1340266

4. Enhanced phytoplankton bloom triggered by atmospheric high-pressure systems over the Northern Arabian Sea, Prasad G.Thoppil, 14 Jan 2023: https://www.nature.com/articles/s41598-023-27785-z

5. Climate change effects on aquaculture production, Global Seafood Alliance, 20 Sept 2021: https://www.globalseafood.org/advocate/climate-change-effects-on-aquaculture-production/

6. Climate of Singapore: http://www.weather.gov.sg/climate-climate-of-singapore/

7. National Geographic: Hydrologic Cycle: https://education.nationalgeographic.org/resource/hydrologic-cycle

8. What are Phytoplankton? NASA Earth Observatory: https://earthobservatory.nasa.gov/features/Phytoplankton

9. Singapore food statistics 2021: https://www.sfa.gov.sg/docs/default-source/publication/sg-food-statistics/singapore-food-statistics-2021.pdf 