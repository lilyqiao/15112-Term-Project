##########################################################
# this file scrapes data from the web, return reformatted version
##########################################################

import quandl
import pandas as pd
quandl.ApiConfig.api_key = "mGtMJWKAbxyxUy5fTm5f"  # my APIkey from Quandl acc.
import datetime as dt


def getData():
    ##########################################################
    # getting (end of day stock) data from Quandl: APPL
    # used a bit of help from Bernard Brenyah (medium.com)
    ##########################################################

    # paginate=True bc Quandl limits tables API to 10,000 rows per call
    APPL_data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL'],
                            qopts={'columns': ['ticker', 'date', 'adj_close']},
                            date={'gte': '2017-12-31',
                                  'lte': dt.datetime.now()},
                            paginate=True)  # code from medium.com

    APPL_new = APPL_data.set_index('date')  # create new data frame.'data' as index
    # APPLdata will be the table I'm using for APPL stock data
    APPLdata = APPL_new.pivot(columns='ticker')  # format adj_close by ticker

    return APPLdata

