##########################################################
# Lily Qiao (recitation L)
# 15112 s'18 Term Project: Algo Trading
##########################################################

import module_manager  # from course website
module_manager.review()  # from course website
import quandl
import pandas as pd
import matplotlib.pyplot as plt
quandl.ApiConfig.api_key = "mGtMJWKAbxyxUy5fTm5f"  # my APIkey from Quandl acc.

##########################################################
# getting (end of day stock) data from Quandl: APPL
##########################################################

# paginate=True bc Quandl limits tables API to 10,000 rows per call
APPL_data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL'],
                        qopts={'columns': ['ticker', 'date', 'adj_close']},
                        date={'gte': '2016-12-31', 'lte': '2017-12-31'},
                        paginate=True)  # code from medium.com

APPL_new = APPL_data.set_index('date')  # create new data frame.'data' as index
# APPLdata will be the table I'm using for analyzing APPL stock data
APPLdata = APPL_new.pivot(columns='ticker')  # format adj_close by ticker













##########################################################
# adding Moving Average columns. input step size
##########################################################
length = len(APPLdata.index)  # how many 'rows (w stock p)'
stock = []  # for APPL
for j in range(length):
    stock += [APPLdata.iloc[j][0]]

def MA(n):
    APPL_MA = [0] * (n - 1)
    for i in range(n - 1, length):
        sum = 0
        for j in range(i - (n - 1), i + 1):
            sum += APPLdata.iloc[j][0]
        APPL_MA.append(sum / n)
    ColIndex = ("MA" + str(n))
    APPLdata[ColIndex] = APPL_MA

MA(5)  # adding column 'MA5' to table APPL data
MA(20)  # adding column 'MA20' to table APPL data


# debugging purposes:
print(APPLdata.head(200))  # prints out first 10 rows of entire table


plt.plot(range(length), stock)
plt.legend()
plt.show()

