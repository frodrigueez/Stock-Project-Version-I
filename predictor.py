"""
a .py file for the predictor module. to execute: python3 predictor.py ticker
info_filename graph_filename col t
"""
from sklearn.linear_model import LinearRegression
import numpy
import pandas
import argparse
import matplotlib.pyplot as plt
from query import queryStock
from sklearn.model_selection import train_test_split
import re
import sys 
import os
"""
this function will return a list of all mins for which there are entries
to help gather historical stock data
"""
def getAllMins(infofile):
    r = r"^\d{2}:\d{2},\b"
    mins = set()
    f = open(infofile)

    for line in f.readlines():
        search = re.search(r, str(line))
        if search is not None:
            mins.add(search.group()[:-1])

    return mins

def getHistoricalData(infofile, mins, ticker):
    hd = []

    for m in mins:
        sys.stdout = open(os.devnull, 'w')
        hd.append(queryStock(infofile, m, ticker, False))
        sys.stdout = sys.__stdout__

    return hd

def getColData(col, historicaldata):
    latestPrices = []
    latestVolumes = []
    
    i = 0 
    for data in historicaldata:
        if col == "latestPrice": # get 3rd column of data
            latestPrices.append(historicaldata[i][2])
        elif col == "latestVolume": # get 4th column of data
            latestVolumes.append(historicaldata[i][3])
        i+=1

    if latestPrices:
        print(f"latestPrices= {latestPrices}")
        return latestPrices
    if latestVolumes:
        print(f"latestVolumes= {latestVolumes}")
        return latestVolumes
"""
A function that reads data from infofile, selects data for specified ticker,
& trains machine learning based model to predict value of specified col for
next t mins
"""
def trainData(infofile, ticker, col, t, graphfile):
    mins = getAllMins(infofile)
    hdata = getHistoricalData(infofile, mins, ticker)
    latestColData = getColData(col,hdata)
    

    model = LinearRegression()
    # model.fit(x,y)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    parser.add_argument("info_filename")
    parser.add_argument("graph_filename")
    parser.add_argument("col")
    parser.add_argument("t")
    args = parser.parse_args()

    data = pandas.read_csv(args.info_filename)
    

    trainData(args.info_filename, args.ticker, args.col, args.t, args.graph_filename)



