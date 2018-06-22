############
## Calculate the Sharpe Ratio for a simple buy and hold strategy
############
import pandas as pdr
import math

def main():
	symbol = 'AAPL'
	data = read_data(symbol)
	SharpeRatio = calculate_SR(data) 
	print SharpeRatio

def read_data(symbol):
	### read Adjusted Close Price into dataframe
	data = pdr.read_csv('data/{}.csv'.format(symbol))
	return data

def calculate_SR(data):
	adjClose = data['Adj Close']
	dailyReturn = adjClose.pct_change()
	excessiveReturn = dailyReturn - .04/len(dailyReturn)
	SharpeRatio = math.sqrt(len(dailyReturn))*excessiveReturn.mean()/excessiveReturn.std()
	return SharpeRatio


if __name__ == '__main__':
	main()