# ft_linear_regression
**Predicting car prices with nothing but a CSV and some formulas. _No polyfit. No magic._ Just gradient descent.**\
*A 42 project and my first dive into machine learning.*


## Watch The Model Learn
Here we can see that RMSE, which represents how much the model is wrong (parler de 667), drops iteration by iteration, until it converges.

![TRAIN PROMPT]({F3E69C0D-A328-4654-95AD-6B8F776754FB}.png)

This graph shows the ***regression line fitting the dataset***, minimizing the overall distance to each point. Training also produces a JSON file that ***saves the model parameters and normalization values for prediction.***

![JSON OUT]({38F9D206-CA50-4B30-A64E-2BF686003C4C}.png)![SCATTER RESULT]({1281DEEE-8CD6-4F96-B88B-35ADACA2D842}.png)

Then you can just ***enter any valid number and get your car price***

![PREDICT PROMPT]({1DA1DF36-C7DF-492B-BC2F-9F031EEA8BA4}.png)

## The Business Problem

Imagine you want to know the price of your car before selling it.<br/> We know that a car with high mileage is worth less than a brand new car that never took the road.<br/>***So in order to estimate the price of our car we can just perform a linear regression based on the mileage and price of cars that were sold before ours.***

|	Mileage |	Price 	|
|-----------|-----------|
|	240000  |	3650    |
|	84000	|	6200    |
|	61789   |	8290    |

## Algorithm and Data Flow

*(le "comment" : brut → normalisation → descente de gradient → prédiction — fusionné)*

## OOP Architecture

courte description des classes et leur responsabilité respective

## Installing and Usage