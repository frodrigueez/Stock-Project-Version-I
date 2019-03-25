"""
 a .py file for tickers module. use python3 tickers.py number_of_tickers
 ticker_filename to execute
"""

import requests

link = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download"

f = requests.get(link)
print(f.text)

tickerbaselink = "https://www.nasdaq.com/symbol/"

# fetches the first n valid tickers from the following URL and write tickes in
# file tickers.txt
# def save_tickers():



