##########################################################
# train, test, predict data without sklearn
##########################################################
from math import *
import matplotlib.pyplot as plt
import numpy as np
from lin_reg_sk import *


days = 30

############ used for debugging individual file #############
from webScrape import *
# getting APPL table and list of stock prices from webScrape
APPLdata = getData()  # a table of adj close prices and dates
length = len(APPLdata.index)  # how many 'rows (w stock p)'

##############################################################
# formatting data for prediction
##############################################################
"""
# data and predictdata are x and y, as lists

data = []  # list of adj_close stock closing prices
for i in range(length):
    data += [APPLdata.iloc[i][0]]  # from 'adj_close' column

predictdata = []  # list of predicted data
for i in range(length):
    predictdata += [APPLdata.iloc[i][1]]  # from 'Prediction' column
predictdata = predictdata[:-days]
"""

APPLdata['Prediction'] = APPLdata[["adj_close"]].shift(-days)
x = np.array(APPLdata.drop(["Prediction"], 1))  # an array of adj close prices
x_predictions = x[-days:]  # the last 30 data points (of adj_close). an array
x = x[:-days]  # x will be the 'known' data points

y = np.array(APPLdata["Prediction"])  # array of predictions
y = y[:-days]  # last 30 days are NaN


###############################################################
# train and test
###############################################################
"""
data_train, data_test, predictdata_train, predictdata_test = \
    cross_validation.train_test_split(data, predictdata test_size=0.2)  # test size 20% of data


# training
clf = linearRegression()
clf.fir(data_train, predictdata_train)
# testing
confidence = clf.score(data_test, predictdata_test)
# predict
forecast_predict = clf.predict(data_forecast)
"""




