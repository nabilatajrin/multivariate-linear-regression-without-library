# linear-regression-without-library

This is a multivariate linear regression project without scikit-learn.


-Regression is a method of modelling a target value based on independent predictors. 
This method is mostly used for forecasting and finding out cause and effect 
relationship between variables. Regression techniques mostly differ based on the 
number of independent variables and the type of relationship between the independent 
and dependent variables.

-Simple linear regression is a type of regression analysis where the number of 
independent variables is one and there is a linear relationship between the 
independent(x) and dependent(y) variable.

FORMULA: Y = a + bX1 + cX2 + dX3 + ϵ
 
Where,
Y – Dependent variable
X1, X2, X3 – Independent (explanatory) variables
a – Intercept
b, c, d – Slopes
ϵ – Residual (error)


STEPS:

-load the data, X, Y
-turn X and Y into numpy arrays


Y – the observed value
plot the data
ŷ – the value estimated by the regression 
Y hat (written ŷ ) is the predicted value of y (the dependent variable) 
in a regression equation. It can also be considered to be the average 
value of the response variable.

Predicted Value Y-hat. Y-hat ( ) is the symbol that represents the predicted 
equation for a line of best fit in linear regression. The equation takes the 
form where b is the slope and a is the y-intercept. It is used to differentiate 
between the predicted (or fitted) data and the observed data y.

FORMULA:
b = (X^T . X)^-1 . X^T . y
yhat = X.dot(b)

FORMULA: ȳ – the mean value of a sample

MODEL
the sum of square(due to regression):

FORMULA: SSr = np.sum((Yhat - Ymean)**2)

RESIDUAL
the sum of square(due to error):
FORMULA: SSe = np.sum((Y - Yhat)**2)

TOTAL
the the sum of square(total):

FORMULA: SSt = np.sum((Y - Ymean)**2)

R2
-determine how good the model is by computing the r-squared
-perfect value of r2 = 1 means the perfect linear relationship. 
-when the value decreases it means weaker relationship of the observations
(x is explaining less of y)
-r2 = 0 means no linear relationship

FORMULA: R2 =SSR/SST = 1 − SSE/SST

number of obs, n
FORMULA: n = Y.size

- everytime we include a new variable the r2 is increased, we keep adding
and the r2 keeps increasing, this is greatsince the model will get better.
but when we look at the adj r2 if wesee the value of adj r2 decreases when 
n variable added, say its now 5 variables, this indicates that we had the best 
situation when we had 4 variables not when 5 variables

-The model is multiple because we have k > 1 predictors.
-If k = 1, we have a simple linear regression model

p-value, p = number of explanatory (X variables)



Adj R2
-tutorial: https://www.youtube.com/watch?v=4otEcA3gjLk
- as k increases adj r2 will tend to decrease(holding everything else constant), 
reflecting the reduced power in the model when you have low numbers of df.
- if we add useful variables to the model, adj will also increase, nut if we
are adding use less variables then the adj r2 will decreases to reflect the
fact that you have lost degrees of freedom.
- the value is not bounded to 0 and 1, it can be negative
- the higher the value of adj r2, better the model is in terms of explanatory 
power.
0 ≤ R2 ≤ 1
-Large R2 values do not necessarily imply a good model

FORMULA: adjr2 = 1 - (1 - r2) * ((n - 1) / (n - p - 1))


DEGREES OF FREEDOM (MODEL/ REGRESSION)
Regression df is the number of independent variables in our regression model.

FORMULA: DFr = p


DEGREES OF FREEDOM (RESIDUAL/ ERROR)
FORMULA: DFe = n - p - 1


DEGREES OF FREEDOM (TOTAL)
tutorial: 
https://www.youtube.com/watch?v=4otEcA3gjLk&list=PLTNMv857s9WUI1Nz4SssXDKAELESXz-bi&index=2
https://www.youtube.com/watch?v=-4aiKmPC994
https://www.youtube.com/watch?v=VIlVWeUQ0vs

-when, number of obs, n = 10, 
number of variables, k = 7 
then df = 10 - 7 - 1 = 2, that's not much at all.. it's not a very healthy regression
we need quite a few degrees of freedom to actually be able to explain anything to get
to allow the model to have error to see whether the two or three or four variables are
related to each other.
-for plane 3 obs/var needed. so in this case for n obs, df = n - 3

FORMULA: dfT = dfR + dfE

or, DFt = n - 1


Mean Absolute Error, or L1 loss, MAE:
FORMULA: mae = np.sum(np.absolute(Yhat - Y))

Regression Mean Square, MSr
FORMULA: Regression MS = ∑ (ŷ — ӯ)²/Reg. df
MSr = np.sum(((Yhat - Ymean)**2)/DFr)

Residual Mean Square, MSe
FORMULA: Residual MS = ∑ (y — ŷ)²/Res. df
	 MSe = np.sum(((Y - Yhat)**2)/DFr)


Total Mean Square
FORMULA: MSt = MSr + MSe

MSE — Mean Squared Error for cost function
Mean Squared Errors (MS) — are the mean of the sum of squares or the sum of squares 
divided by the degrees of freedom for both, regression and residuals.
FORMULA: mse = np.sum((Yhat - Y)**2) / n


F — is used to test the hypothesis that the slope of the independent variable is zero. 
Mathematically, it can also be calculated as
FORMULA: F = MSr / MSe


STANDERD ERROR — provides the estimated standard deviation of the distribution of 
coefficients. It is the amount by which the coefficient varies across different cases. 
A coefficient much greater than its standard error implies a probability that the 
coefficient is not 0.

FORMULA: Std. Error = √(Res.MS)
STDe = math.sqrt(MSe)


- t-Stat — is the t-statistic or t-value of the test and its value is equal to the 
coefficient divided by the standard error.
- the larger the coefficient with respect to the standard error, the larger the 
t-Stat is and higher the probability that the coefficient is away from 0.

FORMULA: t-Stat = Coefficients/Standard Error
t = p/STDe



