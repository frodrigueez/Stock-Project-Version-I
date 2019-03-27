# python-stock-project

COP4930 Stocks Project
Team: Fernanda Rodriguez and Guillermo Villegas

Files:
	tickers.py: will produce ticker_filename file that holds the first n valid tickers from 
	url http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download
	* to run: python3 tickers.py number_of_tickers ticker_filename
 
	fetcher.py: updates current stock information for all tickers in ticker_filename every minute
	and write the updates to info_filename (a .csv file) 
	* to run: python3 fetcher.py time_lim ticker_filename info_filename

	query.py:
	
	* predictor.py:

