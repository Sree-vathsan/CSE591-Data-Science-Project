import urllib

months = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z'] 
for year in range(2000,1984,-1):
	for month in months:
		#filename = 'FUTURE_CL' + month + str(year) + '.csv'
		filename = 'CME-GC' + month + str(year) + '.csv'
		#url = 'https://www.quandl.com/api/v1/datasets/OFDP/FUTURE_CL' + month + str(year) + '.csv?collapse=monthly'
		url = 'https://www.quandl.com/api/v1/datasets/CME/GC' + month + str(year) + '.csv?&auth_token=x8qkg4WAXwcJmaxx_s_u&collapse=monthly'
		print("Downloading " + url + " to " + filename + " ...")
		urllib.urlretrieve(url,filename)
		print("Done!")

#GOLD
#APRIL: https://www.quandl.com/api/v1/datasets/CME/GCJ2014.csv?&collapse=monthly
#MAY: https://www.quandl.com/api/v1/datasets/CME/GCK2014.csv?&collapse=monthly
#NOVEMBER: https://www.quandl.com/api/v1/datasets/CME/GCX2014.csv?collapse=monthly

#x8qkg4WAXwcJmaxx_s_u	