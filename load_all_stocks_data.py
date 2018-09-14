import fix_yahoo_finance as fyf
import pandas_datareader.data as pdr 
import pandas as pd 

fyf.pdr_override()

def load_company_list(filename):
	company = pd.read_csv(filename)
	return company

def read_data(symbol):
	return



def main():
	company_list = load_company_list('nyse.csv')['Symbol'].tolist()
	for symbol in company_list:
		data = pdr.get_data_yahoo(symbol, start='2000-01-01')
		print 'finish {}'.format(symbol)	

if __name__ == '__main__':
	main()
