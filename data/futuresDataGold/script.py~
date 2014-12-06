import urllib

months = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z'] 
for year in range(2014,2009,-1):
	for month in months:
		#filename = 'FUTURE_CL' + month + str(year) + '.csv'
		filename = 'FUTURE_GC' + month + str(year) + '.csv'
		#url = 'https://www.quandl.com/api/v1/datasets/OFDP/FUTURE_CL' + month + str(year) + '.csv?collapse=monthly'
		url = 'https://www.quandl.com/api/v1/datasets/OFDP/FUTURE_GC' + month + str(year) + '.csv?collapse=monthly'
		print("Downloading " + url + " to " + filename + " ...")
		urllib.urlretrieve(url,filename)
		print("Done!")
