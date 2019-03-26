"""
to execute: python3 fetcher.py time_lim ticker_filename info_filename
"""
import os 
import sys 
import time
import pandas
import csv

writefile = sys.argv[3]
writefile += ".csv"
print(writefile)

# TODO: add timing part
# start = time.time
# elapsed = (time.time() - start)
# print(timetoend)
# while time.time < timetoend:
    

# read all tickers from an input file
f = open(sys.argv[2], 'r')
for line in f.readlines():
    print(line, end='')

# this function will update current stock information for ticker passed as arg
# will write/update in an information file (ex: info.csv)
def updateStockInfo(ticker):
    w = open(writefile, 'w')
    with open(writefile, mode='w') as file:
        writer = cvs.writer(file, delimiter=',', quore

