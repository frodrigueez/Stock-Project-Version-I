"""
to execute: python3 fetcher.py time_lim ticker_filename info_filename
"""
from iex import Stock
import os 
import sys 
import time
import pandas
import csv

writefile = sys.argv[3]
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
for line in f.readlines():
    sys.stdout = open(os.devnull, 'w')

    stock = Stock(line.strip())
    t = {key:value for key, value in stock.quote().items() if key in keys}
    sys.stdout = sys.__stdout__

    print(t)

# this function will update current stock information for ticker passed as arg
# will write/update in an information file (ex: info.csv)
#def updateStockInfo(ticker):
 #   with open(writefile, mode='w') as info_file:
  #  fields = ['Time', 'Ticker', 'latestPrice', 'latestVolume', 'Close', 'Open', 'low', 'high']
   # writer = cvs.writer(file, delimiter=',', quore


