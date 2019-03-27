"""
to execute: python3 fetcher.py time_lim ticker_filename info_filename
assumes that proper filenames are passed. (ie: with proper extenstions)
"""
from iex import Stock
import os
import sys
import time
import pandas as pd
import csv
from datetime import datetime

import re

time_lim = sys.argv[1]
ticker_filename = sys.argv[2]
writefile = sys.argv[3]

t = {} # each stock entry
tlist = {} # a dictionary of dictionaries 
tickers = []
whitespace = r"^\s$"

""" this function will update current stock information for ticker passed as arg
will write/update in an information file (ex: info.csv)
"""
def updateStockInfo(ticker):
    keys = ['symbol','low', 'high', 'open', 'close', 'latestPrice', 'latestVolume']
    # check for file existance so you don't overwrite header
    exists = os.path.isfile(writefile)

    with open(writefile, mode='a') as csv_file:
        fieldnames = ['Time', 'Ticker', 'latestPrice', 'latestVolume', 'Close', 'Open', 'low', 'high']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if exists==False:
            writer.writeheader()
        else:
            # just add the new info every min
            sys.stdout = open(os.devnull, 'w')
            updatedInfo = Stock(ticker.strip())
            t = {key:value for key, value in updatedInfo.quote().items() if key in keys}
            sys.stdout = sys.__stdout__
            tlist[ticker] = t
            writer.writerow({'Time': time.strftime("%H:%M"), 'Ticker': ticker, 'latestPrice':
                tlist[ticker]['latestPrice'], 'latestVolume': tlist[ticker]['latestVolume'], 'Close': tlist[ticker]['close'],
                'Open':tlist[ticker]['open'], 'low':tlist[ticker]['low'], 'high':tlist[ticker]['high']})


#newtlist = pd.DataFrame(tlist)
#newtlist.to_csv("tickers.txt")


if __name__ == "__main__":
    #print("now checking 'PHI'")
    #updateStockInfo("PIH")
    #print("now checking 'YI'")
    #updateStockInfo("YI")

# first read tickers from input file 
    f = open(ticker_filename, 'r')
    for ticker in f.readlines():
        if re.search(whitespace, ticker) is None:
            tickers.append(ticker.strip())

    print(tickers)        
=======
writefile += ".csv"
print(writefile)

t = {}


# TODO: add timing part
# start = time.time
# elapsed = (time.time() - start)
# print(timetoend)
# while time.time < timetoend:


# read all tickers from an input file
f = open(sys.argv[2], 'r')
keys = ['low', 'high', 'open', 'close', 'latestPrice', 'latestVolume']
start = time.time()
elapsed = 0
while elapsed < int(sys.argv[1]):
    #for line in f.readlines():
    line = f.readline()
    while line:
        # call parserfunction
        if elapsed < int(sys.argv[1]):
            stock = Stock(line.strip())
            t = {key:value for key, value in stock.quote().items() if key in keys}
            print(t)
            print("elapsed:")
            print(elapsed)
            print("current time:")
            print(time.strftime("%H:%M"))
            elapsed = time.time() - start
            #time.sleep(60)
        else:
            break
        line = f.readline()
    f = open(sys.argv[2], 'r')
    elapsed = time.time() - start
    if int(sys.argv[1])-elapsed > 60:
        time.sleep(60)
    else:
        break
print(elapsed)
# def parsestocks(dictonary):
#    stockdata = []
#    for stock in dictionary:


# this function will update current stock information for ticker passed as arg
# will write/update in an information file (ex: info.csv)
# def updateStockInfo(ticker):
#    w = open(writefile, 'w')
#    with open(writefile, mode='w') as info_file:
#    writer = cvs.writer(file, delimiter=',', quore
>>>>>>> 438a3f8debc858dd2c05e7f0c0ded0d4af8c975a
