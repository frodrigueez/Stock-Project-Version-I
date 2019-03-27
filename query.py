"""
.py file for query module. to execute: python3 query.py -verbose True/False
-file info_filename -ticker ticker -time time. The time format should be HH:MM.
(ex 13:31)
"""
import sys
import os
import logging as log 
import argparse

"""
prints details corresponding to specific time and ticker symbol to terminal
"""

# def queryStock(infofile, time, ticker):



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



