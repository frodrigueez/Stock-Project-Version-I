"""
to execute: python3 fetcher.py time_lim ticker_filename info_filename
"""
from iex import Stock
import os
import sys
import time
import pandas
import csv
from datetime import datetime

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
