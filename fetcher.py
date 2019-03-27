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

# get all necessary info from argv[]
time_lim = sys.argv[1]
ticker_filename = sys.argv[2]
writefile = sys.argv[3]
t = {} # each stock entry
tlist = {} # a dictionary of dictionaries 
keys = ['symbol','low', 'high', 'open', 'close', 'latestPrice', 'latestVolume']

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
# whole module should be timed

    #print("now checking 'PHI'")
    #updateStockInfo("PIH")
    #print("now checking 'YI'")
    #updateStockInfo("YI")

# first read tickers from input file 
    keys = ['symbol','low', 'high', 'open', 'close', 'latestPrice', 'latestVolume']
    start = time.time()
    elapsed = 0

    f = open(ticker_filename, 'r')

    
    while elapsed < int(time_lim):
        line = f.readline()
        while line:
            print(f"on line: {line}")
            if elapsed < int(time_lim):
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
        f = open(ticker_filename, 'r')
        elapsed = time.time() - start
        if int(time_lim)-elapsed > 60:
            time.sleep(60)
        else:
            break
        print(elapsed)

        #f = open(ticker_filename, 'r')
        #for ticker in f.readlines():
        #    if re.search(whitespace, ticker) is None:
        #        tickers.append(ticker.strip())
    
        #print(tickers)        
        


