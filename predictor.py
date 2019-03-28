"""
a .py file for the predictor module. to execute: python3 predictor.py ticker
info_filename graph_filename col t
"""
from sklearn.linear_model import LinearRegression
from query import queryStock
import sys
"""
A function that reads data from infofile, selects data for specified ticker,
& trains machine learning based model to predict value of specified col for
next t mins
"""
#def trainData(infofile, ticker, col, t, graphfile):

if __name__ == "__main__":
    print("hi")
    queryStock(sys.argv[1], sys.argv[2], sys.argv[3], False)
