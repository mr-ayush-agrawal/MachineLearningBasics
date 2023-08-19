# Notes - Basic Design and structure

## Sci-Kit Learn -> ML module

Primarly 3 Types of Objcets

1. **Estimators** -> Estimates a paramerter based on dataset. Eg - Imputer<br>
    It has 2 methods
    - **Fit** :Fits the dataset and calculate the internal parameters
    - **Transform**
1. **Transformers** -> Transforms the methods, Takes input and return the output based on the learnings from fit().<br>
It also has a convinence function called *fit_transform()* -> fits and then  transfrom.<br>
*fit_transform()* -> This is optimsed this could even be done calling both *fit and Transform* seperatly.
1. **Predictors** -> Model functions which are made for predecting  the values. Eg - Linear Regression model ...<br>
It has 2 common and most imp functions and there are some others too. 
    - *fit()* - use to fit the ML model
    - *predict()* - For predecting the values from the model
    - *score()* - It provides the score of hte model.


*Imputer* : Used for filling the missing values at the by some strategy like **Mean / Median**