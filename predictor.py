"""
a .py file for the predictor module. to execute: python3 predictor.py ticker
info_filename graph_filename col t
"""
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt
from query import queryStock
from sklearn.model_selection import train_test_split
import re
import sys 
import os
from fetcher import updateStockInfo
from orderedset import OrderedSet
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

def getAllMins(infofile):
    r = r"^\d{2}:\d{2},\b"
    mins = OrderedSet()
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

def plotHistoricalData(mins, hd, col,graph):
    plt.plot(mins, hd)
    plt.xlabel('Mins')
    plt.ylabel(col)
    plt.show()
    plt.savefig(graph,transparent=True)

"""
A function that reads data from infofile, selects data for specified ticker,
& trains machine learning based model to predict value of specified col for
next t mins
"""

    

def trainData(infofile, ticker, col, t, graphfile):
    mins = getAllMins(infofile)
    hdata = getHistoricalData(infofile, mins, ticker)
    latestColData = getColData(col,hdata)

    minsnp = np.asarray(list(mins))
    lcdnp = np.asarray(latestColData)

    plotHistoricalData(minsnp, lcdnp, col, graphfile) 

    model = LinearRegression()

    lcdnp2 = lcdnp
    #print(np.asarray(lcdnp2))
    #model.fit(lcdnp2, lcdnp2)
    #price_predict = model.predict([0])
    #print(price_predict)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    parser.add_argument("info_filename")
    parser.add_argument("graph_filename")
    parser.add_argument("col")
    parser.add_argument("t")
    args = parser.parse_args()

    # load data set
    data = pd.read_csv(args.info_filename)
    #print(data.info())
    #print(data.head())
    # have to use Time as predictor variable 
    X = data['Time'].replace(':','')
    print(type(X))
    print(f"X:\n{X}")
    y = data['latestPrice']

    # split data into training and test sets
    x_training_set, x_test_set, y_training_set, y_test_set = train_test_split(X,y)

    # cast data options from series into 1D arrays
    #x_training_set, x_test_set, y_training_set, y_test_set = x_training_set.values, x_test_set.values, y_training_set.values, y_test_set.values
    #x_training_set, x_test_set, y_training_set, y_test_set = x_training_set.reshape(-1,1), x_test_set.reshape(-1,1), y_training_set.reshape(-1,1), y_test_set.reshape(-1,1)

    #plt.title('Relationship between dependent and target variable')
    #plt.scatter(x_training_set,y_training_set, color = 'green', alpha = 0.35)
    #plt.show()

    # fit model to data
    lm = linear_model.LinearRegression()
    lm.fit(x_training_set, y_training_set)
    print('Slope: ', lm.coef_)
    print('Intercept: ', lm.intercept_)

# evaluate model
    #model_score = lm.score(x_training_set, y_training_set)
    #print('Model score: {:.4f} '.format(model_score))

    #y_predicted = lm.predict(x_test_set)

    #r_squared_score = r2_score(y_test, y_predicted)
    #print('r square: {:.4f}'.format(r_squared_score))

# lower value is prefered
    #mse = mean_squared_error(y_test_set, y_predicted)
    #print('MSE: {:.4f}'.format(mse))


    #plt.title('Comparison of Y values in test and the predicted values')


    #plt.plot(x_test_set, y_predicted, color='red', alpha=0.35)
    #plt.scatter(x_test_set, y_test_set, color = 'pink', alpha = 0.25)

    #plt.show()








#tickerdata = data.loc[(data['Ticker'] == "YI")]
    #print(tickerdata) 
    #trainData(args.info_filename, args.ticker, args.col, args.t, args.graph_filename)


