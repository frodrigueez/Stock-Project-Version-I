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
    if verbose:
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
                #if
                # print("false")
                else:
                    print("lll")

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
    print(f".info_filename: {type(args.info_filename)} .giventime:{type(args.giventime)}, .tickername:{type(args.tickername)}, .verbose:{type(args.verbose)}")
    queryStock(args.info_filename, args.giventime, args.tickername, args.verbose)

    #if args.file and args.info_filename and args.ticker and args.tickername and args.time and args.giventime:
    #    if args.verbose:
    #        print("verbose is turned on!")
    #    else:
    #        print("correct arguments with no verbose")
    #else:
    #    print("usage: python3 [-verbose] -file info_filename -ticker ticker -time time")


    # queryStock(sys.argv[1], sys.argv[2], sys.argv[3])
