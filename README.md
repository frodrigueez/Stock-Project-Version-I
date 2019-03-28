# python-stock-project

COP4930 Stocks Project
Team: Fernanda Rodriguez and Guillermo Villegas

Files:
	tickers.py: will produce ticker_filename file that holds the first n valid tickers from 
	url http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download
	* to run: python3 tickers.py number_of_tickers ticker_filename
 
	fetcher.py: this module updates current stock information for all tickers in ticker_filename every 
	minute and write the updates to info_filename (a .csv file) 
	* to run: python3 fetcher.py time_lim ticker_filename info_filename

	query.py:
	this module will take info_filename, time, and ticker to print details corresponding to a specific
	time and ticker to the terminal 
	* to run: python3 query.py -verbose -file info_filename -ticker ticker -time time
	(with time in format: HH:MM)
	
	* predictor.py:
	this module will use sklearn.linear regression to use linear regression to train the historical 
	data for a specific ticker stored in an information file and predict the result of a specified
	column for the next t minutes
	to run: python3 predictor.py ticker info_filename graph_filename col t
	
