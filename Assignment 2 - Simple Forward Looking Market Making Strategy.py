# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:45:07 2022

@author: owner
"""

import pandas as pd
import datetime
import json
import requests
import numpy as np

Trade_prices = pd.read_csv(r'C:\Users\owner\Documents\Studies\Python\IIQF_python\FalconX Assignment 1.csv')
print (Trade_prices)

#Fetching BTCUSDT live prices from source
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
BTCUSDT_0 = requests.get(key)  
BTCUSDT_0 = BTCUSDT_0.json()
print(f"{BTCUSDT_0['symbol']} live price is {BTCUSDT_0['price']}")
BTCUSDT = float(BTCUSDT_0['price'])


# Steps for converting the offer size BTC equivalent amount according to live prices and also setting Hedge limit
BID_ASK_size = 1000 #in USD (notional)
BTC_Amount = (1/BTCUSDT)*BID_ASK_size
print (BTC_Amount)
Hedge_limit = 5000 #in USD (notional)

#Declaring variables for Bid price and Ask price at each live BTCUSDT.
Bid_price = BTCUSDT - 0.0003*BTCUSDT
Ask_price = BTCUSDT + 0.0003*BTCUSDT
B = Hedge_limit/(BTC_Amount*Bid_price)
A = Hedge_limit/(BTC_Amount*Ask_price)
#A and B are varibale that help in exiting trade at Hedge limit. This is used because a passive hedging approach was required.
print (Ask_price, Bid_price, A, B)

#Conversion of Trade Orders dataframe to list for Convenience
TP = Trade_prices['Trade Price'].to_list()

#Defining arrays and function for entering and exiting trades
SVB = []
SVA= []
SVB_1 = []
SVA_1 =[]
for i in TP:
    if ((i <= Bid_price) and (len(SVB_1) < round(B))):
        SVB.append(Bid_price*BTC_Amount)
        SVB_1.append(Bid_price*BTC_Amount)
    else:
        SVB.append(0)
for i in TP:
    if ((i >= Ask_price) and (len(SVA_1) < round(A))):
        SVA.append(Ask_price*BTC_Amount)
        SVA_1.append(Ask_price*BTC_Amount)
    else:
        SVA.append(0)
        

#Conversion of created arrays to Dataframes
df = pd.DataFrame(SVB, columns = ['Buy value'])
df1 = pd.DataFrame(SVA, columns = ['Sale value'])
df2 = pd.DataFrame(SVB_1, columns = ['Executed Buys'])
df3 = pd.DataFrame(SVA_1, columns = ['Executed Sells'])
e = pd.DataFrame(TP, columns = ['Order Price'])
# Compiling data into one Dataframe
Trades = pd.concat([e.iloc[:,0], df.iloc[:,0], df1.iloc[:,0], df2.iloc[:,0], df3.iloc[:,0]], axis = 1)
print (Trades)
Trades.to_csv('FalconX Assignment 2.csv')

# All the assumtions mentioned in the question has been considered here. A passive hedger approach has been used.
# It has been assumed that the trading cost is 0.
# Trades have been executed when the order price has crossed the Bid/Ask price