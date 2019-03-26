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
    # call parserfunction
    # t[line] =
    stock = Stock(line.strip())
    print(stock.quote())
    t = {key:value for key, value in stock.quote().items() if key in keys}
    print(t)
    


# def parsestocks(dictonary):
#    stockdata = []
#    for stock in dictionary:
	
	
# this function will update current stock information for ticker passed as arg
# will write/update in an information file (ex: info.csv)
# def updateStockInfo(ticker):
#    w = open(writefile, 'w')
#    with open(writefile, mode='w') as info_file:
#    writer = cvs.writer(file, delimiter=',', quore


