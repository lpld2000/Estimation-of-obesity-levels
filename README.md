# Estimation-of-obesity-levels

For this project we had a dataset for the estimation of obesity levels in people from the countries of Mexico,
Peru and Colombia, with ages between 14 and 61 and diverse eating habits and physical condition.

The attributes related with eating habits are: Frequent consumption of high caloric food (FAVC), Frequency of consumption of vegetables
(FCVC), Number of main meals (NCP), Consumption of food between meals (CAEC), Consumption of
water daily (CH20), and Consumption of alcohol (CALC). 

The attributes related with the physical condition are: Calories consumption monitoring (SCC), Physical activity frequency (FAF), Time using
technology devices (TUE), Transportation used (MTRANS).

Other variables obtained were: Gender, Age, Height and Weight.

Finally, all data was labeled and the class variable NObesity was created with the values of: 
Insufficient Weight, Normal Weight, Overweight Level I, Overweight Level II, Obesity Type I,
Obesity Type II and Obesity Type III. 

The data contains numerical data and continous data, so it can be used for analysis based
on algorithms of classification, prediction and clustering.

So to deal with this dataset, first we saw that we don't have to clean it deleting null datas so it was easy for us to begin.
Then we use different libraries like seaborn, matplotlib or bokeh to visualize them and to conclude about their significativity.
And after that we did some models like KNN, Decision tree, Support vector machine and Random Forest.
Then we saw that we had a good prediction result with KNN so we decided to change the hyperparameters in the KNN and we obtained an accuracy of 81%.

To conclude, the most difficult parts for us was to create the models and to adapt them for our dataset and previously to make the visualization of the data with the plot.
