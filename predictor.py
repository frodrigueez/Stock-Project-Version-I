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

"""
A function that reads data from infofile, selects data for specified ticker,
& trains machine learning based model to predict value of specified col for
next t mins
"""
#def trainData(infofile, ticker, col, t, graphfile):
# read data from info file
# queryStock(args.info_filename, "15:03", args.ticker, False)
# select data for specified ticker
# train machine learning based model to preduct value of col
# for next t minutes
# predict val of col using time column (can split into hrs and 
# mins) based on historical 
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("ticker")
    parser.add_argument("info_filename")
    parser.add_argument("graph_filename")
    parser.add_argument("col")
    parser.add_argument("t")
    
    args = parser.parse_args()

    data = pandas.read_csv(args.info_filename)
    print(data)
    #print(df.keys())
    #print(df.Ticker)
    #print(df)
    #tickers = data."Tickers".tolist()


    hi =queryStock(args.info_filename, "15:03", args.ticker, False)
    print(hi)
# initalizing inital linear regression object 
#    model = LinearRegression()
    #model.fit(x,y)



