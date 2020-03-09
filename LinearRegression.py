# Simple Linear Regression Analysis

# Importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

# Importing the dataset

ds = pd.read_csv('Salary_Data.csv')
X = ds.iloc[:,:-1].values
y = ds.iloc[:,-1].values

# Visualising the dataset
# Visually we see that the data is highly correlated, therefore simple linear regression should suffice

plt.scatter(X, y, c='red')
plt.title('Years experience Vs Salary')
plt.show()

# There is no missing data

# There is no categorical data that requires encoding

# Splitting the data into the training set and testing set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# The linear_model library will take care of the feature scaling so we do not need to perform this step for
# Linear Regression, Multi-Linear Regression and polynomial Regression.

# Fitting the linear regression to the dataset

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predicting the test set results

y_pred = lr.predict(X_test)

# Visualising the training set

plt.scatter(X_train, y_train, c='red')
plt.plot(X_train, lr.predict(X_train), c='blue')
plt.title('Training set')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

# Visualising the testing set
# We observe that our test dataset points are close to the regression line, indicating that the model that has been trained well on the training set data

plt.scatter(X_test, y_test, c='red')
plt.plot(X_train, lr.predict(X_train), c='blue')
plt.title('Testing set')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()

# Statsmodels for model evaluation

import statsmodels.api as sm
X = np.append(np.ones((30,1)).astype(int), X, axis = 1)
Reg_OLS = sm.OLS(endog = y, exog = X).fit()
summary = Reg_OLS.summary()

# Calculating the Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE)
# MSE is more popular than MAE because MSE "punishes" larger errors. But, RMSE is even more popular than MSE because 
# RMSE is interpretable in the "y" units.

print(metrics.mean_absolute_error(y_test, y_pred))
print(metrics.mean_squared_error(y_test, y_pred))
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

