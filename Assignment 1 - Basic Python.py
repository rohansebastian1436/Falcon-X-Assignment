# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:17:50 2022

@author: owner
"""

import pandas as pd
import datetime

March_0122 = pd.read_csv(r'C:\Users\owner\Documents\Rohan\FalconX codes\BTCUSDT-trades-2022-03-01.csv')#data for March 01 2022
March_0222 = pd.read_csv(r'C:\Users\owner\Documents\Rohan\FalconX codes\BTCUSDT-trades-2022-03-02.csv')#data for March 02 2022
March_0322 = pd.read_csv(r'C:\Users\owner\Documents\Rohan\FalconX codes\BTCUSDT-trades-2022-03-03.csv')#data for March 03 2022
Trade_prices = pd.concat([March_0122.iloc[:,1],March_0222.iloc[:,1],March_0322.iloc[:,1]], axis = 0) #consolidating the trade prices of 3 days into 1 dataframe.
Trade_prices = pd.DataFrame(Trade_prices, columns = ['Trade Price'])
print (Trade_prices)
Trade_prices.to_csv('FalconX Assignment 1.csv')