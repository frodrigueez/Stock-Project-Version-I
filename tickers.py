"""
 a .py file for tickers module. use python3 tickers.py number_of_tickers
 ticker_filename to execute
"""
import os.path
import requests
import re
from iex import Stock
link = "https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&pagesize=200"
tickers = []
d = requests.get(link)

html_file = open('html.txt', 'w')
html_file.write(d.text)
html_file = open('html.txt')

tickerbaselink = "https://www.nasdaq.com/symbol/"
i = 1
for line in html_file.readlines():
    x = re.search(tickerbaselink, line)
    if x is not None:
    #really ratchet  counter, but it works :)
        if i is 1:
            t = os.path.basename(x.string).upper()
            t = t[:-3]
            tickers.append(t)
        if i is 3:
            i = 0
        i = i + 1

# fetches the first n valid tickers from the following URL and write tickes in
# file tickers.txt
def save_tickers(amountOfTickers):
    if amountOfTickers > 150:
        raise IndexError("n passed to save_tickers out of range. n must be <= 150")
    f = open('tickers.txt', 'w')
    
    n = 0
    validTickers = []
    for x in tickers:
        if n == amountOfTickers:
            break
        else:
            try:
                Stock(x).price()
                validTickers.append(x)
                n += 1
                f.write('{0}\n'.format(x))
                print(x)
                print(n)
            except Exception:
                print("not valid")


if __name__ == "__main__":
    save_tickers(150)
