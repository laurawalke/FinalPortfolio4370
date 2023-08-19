#Developed by: Laura Walker
#7/9/23
#Simple Stock Program to calculate Earnings/Loss on list of stocks using dictionaries functions split into new file

from datetime import date
import datetime
import currentEarnings

stockPortfolio = {}

#Dictionary Definition
stockPortfolio = {1: {'customerName': 'Bob Smith', 'stockName': 'Google', 'numberOfStocks': 25 ,
                        'purchasePrice': 772.88, 'currentPrice': 941.53, 'purchaseDate': date(2017,8,1)}}
                 
stockPortfolio[2] = {'customerName': 'Bob Smith', 'stockName': 'MSFT  ', 'numberOfStocks': 85 ,
                        'purchasePrice': 56.60, 'currentPrice': 73.04, 'purchaseDate': date(2017,8,1)}                 

stockPortfolio[3] = {'customerName': 'Bob Smith', 'stockName': 'RDS-A ', 'numberOfStocks': 400,
                        'purchasePrice': 49.58, 'currentPrice': 55.74, 'purchaseDate': date(2017,8,1)}     

stockPortfolio[4] = {'customerName': 'Bob Smith', 'stockName': 'AIG   ', 'numberOfStocks': 235,
                        'purchasePrice': 54.21, 'currentPrice': 65.27, 'purchaseDate': date(2017,8,1)}  
                        
stockPortfolio[5] = {'customerName': 'Bob Smith', 'stockName': 'FB    ', 'numberOfStocks': 130,
                        'purchasePrice': 124.31, 'currentPrice': 175.45, 'purchaseDate': date(2017,8,1)}

stockPortfolio[6] = {'customerName': 'Bob Smith', 'stockName': 'M     ', 'numberOfStocks': 425,
                        'purchasePrice': 30.30, 'currentPrice': 23.98, 'purchaseDate': date(2018,1,10)}

stockPortfolio[7] = {'customerName': 'Bob Smith', 'stockName': 'F     ', 'numberOfStocks': 85,
                        'purchasePrice': 12.58, 'currentPrice': 10.95, 'purchaseDate': date(2018,2,17)}

stockPortfolio[8] = {'customerName': 'Bob Smith', 'stockName': 'IBM   ', 'numberOfStocks': 80,
                        'purchasePrice': 150.37, 'currentPrice': 145.30, 'purchaseDate': date(2018,5,12)}

#Print list of stocks
print('Stock Symbol','|', 'Purchase Date','|', ' No. Shares','   |', 'Purchase Price','|', 'Current Value')
print('-'*80)

for key in stockPortfolio:
        print (stockPortfolio[key]['stockName'], '\t'*2, stockPortfolio[key]['purchaseDate'], '\t',
               stockPortfolio[key]['numberOfStocks'],  '\t'*2, '{0:6.2f}'.format(stockPortfolio[key]['purchasePrice']),
               '\t', '{0:6.2f}'.format(stockPortfolio[key]['currentPrice']))
        print('-'*80)   

#Print earnings
if stockPortfolio[key]['customerName'] == 'Bob Smith':
        print(f'') #print a blank line
        print(f'Summary of stock for: Bob Smith.') #print users name
        print('----------------------------------------------------------------')
        print('Stock','   |   ', 'Share #','   |', ' Earnings/Loss', '   |', ' Yearly Earnings/Loss')
        print('----------------------------------------------------------------')
    
#Print Report Output
for key in stockPortfolio:
        print (stockPortfolio[key]['stockName'], '\t'*2, '{0:4}'.format(stockPortfolio[key]['numberOfStocks']),
                '\t'*2,'{0:8.2f}'.format(currentEarnings.calculateCurrentEarnings(stockPortfolio,key)),
               '\t', '{0:8.2f}'.format(currentEarnings.calculateYearlyEarnings(stockPortfolio,key)))


