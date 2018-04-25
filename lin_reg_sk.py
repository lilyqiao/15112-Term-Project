##########################################################
# coding from scratch sklearn's linear_model LinearRegession
##########################################################
# 1)Estimate statistical quantities from training data.
# 2)Estimate linear regression coefficients from data.
# 3)Make predictions using linear regression for new data



class LinearRegression(object):
    # y = b0 + b1*x        note: y is predictdata, x is data

    # Fitting a model means obtaining estimators for the unknown population parameters
    # β0 and β1 (and also for the variance of the errors σ
    def fit(self):
        b1 = sum((x(i)-mean(x))*(y(i)-mean(y))) / sum((x(i)-mean(x))**2)
        b0 = mean(y) - b1*mean(x)
        return (b0, b1)  # intercept, slope

    # predict "y" using the linear model with estimated coefficients
    def predict(self, b0, b1):
        next_y = (b1*next_x) + b0
        return next_y

    # returns the coefficient of determination (R^2).
    #       a measure of how well observed outcomes are replicated by the model ,
    #       as the proportion of total variation of outcomes explained by the model
    def score(self, ydot, yorig):
        return sum((ydot-yorig)**2)
