# Simple-Linear-Regression

This repository contains a simple dataset that is analysed using Simple Linear Regression. 

The output of the code below code (OLS - Ordinary Least Squares)

import statsmodels.api as sm
<P>X = np.append(np.ones((30,1)).astype(int), X, axis = 1)
<P>Reg_OLS = sm.OLS(endog = y, exog = X).fit() 
<P>summary = Reg_OLS.summary()
<P>print(summary)  

is as follows

<img src = 'Screen_shot.png' width='1000'>

From the above output, we can estiablish:

The regressor takes the following equation with the coefficients from the above output:  
Expected_salary = 25790 + 9450*(Years_of_experience)

R-squared and Adj R-Squared are both 0.96

The P values are much lower than 0.05, indicating that the variable X1 (Years of experience) is statistically significant.
