"""
.py file for query module. to execute: python3 query.py -verbose True/False
-file info_filename -ticker ticker -time time. The time format should be HH:MM.
(ex 13:31)
"""
import sys
import re
import os
import logging as log
import argparse


"""
prints details corresponding to specific time and ticker symbol to terminal
"""
def queryStock(infofile, time, ticker, verbose):
    var = []
    if not verbose:
        print(f"verbose is on")
        with open(infofile) as f:
            for line in f:
                if(time == line[:5]):
                    # print("true")
                    r = r",[A-Z]{2,5},"
                    #print(f"searching line {line}")
                    if re.search(r, line) is not None:
                        match = re.search(r, line)
                        match = match.group()
                        match = match[1:-1]
                        if(match == ticker):
                            print(f"{match} is true")
                            allFields = re.search(r, line).string
                            time, ticker, latest_price,latest_volume, close, open_v, low, high = allFields.split(',')
                            print(f"Time: {time}")
                            var.append(time.strip())
                            print(f"Ticker: {ticker}")
                            var.append(ticker.strip())
                            print(f"Latest Price: {latest_price}")
                            var.append(latest_price.strip())
                            print(f"Latest Volume: {latest_volume}")
                            var.append(latest_volume.strip())
                            print(f"Close: {close}")
                            var.append(close.strip())
                            print(f"Open: {open_v}")
                            var.append(open_v.strip())
                            print(f"Low: {low}")
                            var.append(low.strip())
                            print(f"High: {high}")
                            var.append(high.strip())
                            return var
                            
    else:
        print("verbose")



if __name__ == "__main__":
    # initalizing all required flags
    parser = argparse.ArgumentParser()
    parser.add_argument("-verbose", help="will print number of rows, columns and name of columns in info file", action="store_true")
    parser.add_argument("-file", help="info_filename",action="store_true", required=True)
    parser.add_argument("info_filename")
    parser.add_argument("-ticker", help="ticker name",action="store_true", required=True)
    parser.add_argument("tickername")
    parser.add_argument("-time", help="HH:MM format", action="store_true", required=True)
    parser.add_argument("giventime")

    args = parser.parse_args()

    queryStock(args.info_filename, args.giventime, args.tickername, args.verbose)
