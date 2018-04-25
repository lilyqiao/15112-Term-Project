##########################################################
# adding Moving Average columns.
# gotta input step size
##########################################################
import quandl
import pandas as pd
from webScrape import *
import matplotlib.pyplot as plt
quandl.ApiConfig.api_key = "mGtMJWKAbxyxUy5fTm5f"  # my APIkey from Quandl acc.


def addMA(APPLdata):
    length = len(APPLdata.index)  # how many 'rows (w stock p)'
    def MA(n):
        APPL_MA = [0] * (n - 1)
        for i in range(n - 1, length):
            sum = 0
            for j in range(i - (n - 1), i + 1):
                sum += APPLdata.iloc[j][0]
            APPL_MA.append(sum / n)
        ColIndex = ("MA" + str(n))
        APPLdata[ColIndex] = APPL_MA


    MA(5)  # adding column 'MA5' to table APPLdata <--- modifies it
    MA(20)  # adding column 'MA20' to table APPLdata


    # plotting MAs
    stock = []  # for APPL
    for j in range(length):
        stock += [APPLdata.iloc[j][0]]

    plt.plot(range(length), stock, color="grey")
    plt.plot(range(length), APPLdata["MA5"], color="red")
    plt.plot(range(length), APPLdata["MA20"], color="green")
    plt.ylim(110, 200)
    # ax.set(xlabel="dates", ylabel="$$$")
    plt.legend()
    plt.show()  # line pops up



    # debugging purposes:
    # print(APPLdata.head(30))  # prints out first 10 rows of entire table


