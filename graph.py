import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
import sqlite3
from sqlite3 import Error

class StocksWorth:
    def __init__ (this, stockName):
        this.stockName = stockName
        this.numberOfStocks = []
        this.stockPriceList = []
        this.stockDate = []

    def add_stock(self, price, date):
        """Add information to the class"""
        self.stockPriceList.append(price)
        self.stockDate.append(date)

    def add_stock_purchased(self, numberOfStocks, symbol):
        """Add information to the class"""
        self.numberOfStocks.append(numberOfStocks)
        self.symbol.append(symbol)
        
class Bonds(StocksWorth):
    type = 'bond'
    def __init__ (this, purchaseID, stockName, numberOfStocks, purchasePrice, currentPrice, purchaseDate, coupon, bondYield):
        super().__init__(purchaseID, stockName, numberOfStocks, purchasePrice, currentPrice, purchaseDate)
        this.coupon = coupon
        this.bondYield = bondYield
try:
    portfoliosHistory = {}
    numberOfShares = []
          
    file_path = '..\Data\AllStocks.json'

    with open(file_path) as json_file:
        data_set = json.load(json_file)

    for row in data_set: 
        if row['Symbol'] not in portfoliosHistory:
                newStock = StocksWorth(row['Symbol'])
                print (row['Symbol'] + " added to your portfolio")
                portfoliosHistory[row['Symbol']] = newStock
                if row['Symbol'] == 'GOOG':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*125, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'MSTF':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*85, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'RDS-A':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*400, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'FB':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*150, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'M':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*425, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'F':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*85, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'IBM':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*80, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'AIG':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*235, datetime.strptime(row['Date'], '%d-%b-%y'))
                
        else:
                if row['Symbol'] == 'GOOG':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*125, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'MSTF':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*85, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'RDS-A':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*400, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'FB':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*150, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'M':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*425, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'F':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*85, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'IBM':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*80, datetime.strptime(row['Date'], '%d-%b-%y'))
                if row['Symbol'] == 'AIG':
                    portfoliosHistory[row['Symbol']].add_stock(row['Close']*235, datetime.strptime(row['Date'], '%d-%b-%y'))

    

        

    for row in portfoliosHistory:
        stocks = (portfoliosHistory[row].stockPriceList)
        dates = matplotlib.dates.date2num(portfoliosHistory[row].stockDate)
        name = portfoliosHistory[row].stockName
        plt.plot_date(dates, stocks, linestyle='solid', marker=" ", label = name)
    plt.savefig('..\Output\simplePlot.png')
    plt.legend()
    plt.show()


except FileNotFoundError:
    print ("The specified file does not exist")

#type error handling
except TypeError:
    print ("Error type wrong")
   
