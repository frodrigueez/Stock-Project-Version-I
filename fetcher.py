"""
to execute: python3 fetcher.py time_lim ticker_filename info_filename
"""
import os 
import sys 
import time

timestarted = time.time
timetorun = int(sys.argv[1])
timetoend = int(timetorun + timestarted)

print(timetoend)

# while time.time < timetoend:
    

# read all tickers from an input file
f = open(sys.argv[2], 'r')
for line in f.readlines():
    print(line, end='')

# this function will update current stock information for ticker passed as arg
# will write/update in an information file (ex: info.csv)
def updateStockInfo(ticker):
    w = open(sys.argv[3], 'w')


