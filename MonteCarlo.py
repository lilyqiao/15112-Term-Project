##########################################################
# using Monte Carlo Simulation to model asset pricing
# assumes perfectly efficient markets, so ... only used as reference
##########################################################

from webScrape import *
from math import *
from scipy.special import ndtri
import matplotlib.pyplot as plt
import random


######### used for debugging individual file ################
# getting APPL table and list of stock prices from webScrape
APPLdata = getData()
length = len(APPLdata.index)  # how many 'rows (w stock p)'

# accessing the stock price column of the table. will modify later also
data = []
for i in range(length):
    data += [APPLdata.iloc[i][0]]
#############################################################


def predict(APPLdata, days):

    # calculating a list of returns and destructively adding to the table
    APPL_returns = [0]
    for i in range(1, length):
        todayP = APPLdata.iloc[i][0]
        yesterdayP = APPLdata.iloc[i - 1][0]
        dailyReturn = log(todayP / yesterdayP, 10)

        APPL_returns += [dailyReturn]
    APPLdata["returns"] = APPL_returns  # add to APPLdata table

    returns = APPL_returns  # will modify this (not APPL_returns) later

    #############################################################
    def generateColor(n):  # for plotting lines
        if n%10 == 1: return "blue"
        elif n%10 == 2: return "green"
        elif n%10 == 3: return "purple"
        elif n%10 == 4: return "cyan"
        elif n%10 == 5: return "magenta"
        elif n%10 == 6: return "yellow"
        elif n%10 == 7: return "pink"
        elif n%10 == 8: return "darkgreen"
        elif n%10 == 9: return "orange"

    # returns predicted next price given historical(& alr predicted) data
    def onePrediction(returns, data):
        def getVar():
            sum = 0
            for i in range(len(returns)):
                sum += (returns[i] - avgReturns) ** 2
            return sum / (length - 1)
        # replicates what NORMSINV would do in excel.
        def normsinv(n):
            # return scipy.special.ndtri(n)
            return ndtri(n)
        avgReturns = sum(returns)/length

        variance = getVar()
        std = sqrt(variance)
        drift = avgReturns - (variance/2)

        iNormDistr = normsinv(random.random())
        randValue = std * iNormDistr
        todayPrice = data[-1]
        nextPrice = todayPrice*(e**(drift+randValue))  # prediction

        # add next predicted price
        data += [nextPrice]
        # add next predicted return
        nextReturn = log(todayPrice / nextPrice, 10)
        returns += [nextReturn]

    # one cycle is defined by num days. days: prediction period
    def oneCycle(returns, data, days):
        # returns and data modified to include predictions over days
        for i in range(days):
            onePrediction(returns, data)

    # the "monte carlo template"
    def predictionNextP(trials):
        allPredictions = []  # 2d list. list of list of predictions over 1 cycle
        for i in range(trials):
            oneCycle(returns, data, days)
            allPredictions += [data[-days:]]  # predictions only, not whole data
        for i in range(len(allPredictions)):
            color = generateColor(i)
            plt.plot(range(days), allPredictions[i], color=color)
            plt.legend
            plt.show

    """
        finalPredictions = []  # 1d list.
        for i in range(len(allPredictions)):
            sum = 0
            for j in range(trials):
                sum += allPredictions[j][i]
            avg = sum/trials
            finalPredictions += [avg]
        plt.plot(range(len(finalPredictions)), list, color="black")
        plt.legend()
        plt.show
    """



    print("hi")  #debug



    predictionNextP(10)  #trials = 10 = num lines in monte carlo

predict(APPLdata, 30)