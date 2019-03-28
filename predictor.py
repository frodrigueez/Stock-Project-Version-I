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

"""
A function that reads data from infofile, selects data for specified ticker, 
& trains machine learning based model to predict value of specified col for
next t mins
"""
#def trainData(infofile, ticker, col, t, graphfile):
# read data from info file, select data for specified data 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("ticker")
    parser.add_argument("info_filename")
    parser.add_argument("graph_filename")
    parser.add_argument("col")
    parser.add_argument("t")
    
    args = parser.parse_args()
    queryStock(args.info_filename, "15:03", args.ticker, False)
    # initalizing inital linear regression object 
    model = LinearRegression()
    #regressor.fit()

