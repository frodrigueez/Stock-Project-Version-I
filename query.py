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
def queryStock(infofile, time, ticker):
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-verbose", help="will print number of rows, columns and name of columns in info file", action="store_true")
    #parser.add_argument("time", help="HH:MM format", action=)
    args = parser.parse_args()

    if args.verbose:
        print("verbose is turned on!")
    else:
        print("verbose is turned off")
    #vflag = sys.argv[1]
        #if vflag == "true":
        #    print(f"vflag is on")
        #else:
        #    print(f"vflag is off")

    # queryStock(sys.argv[1], sys.argv[2], sys.argv[3])
