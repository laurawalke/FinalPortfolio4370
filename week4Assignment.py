import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
import sqlite3
from sqlite3 import Error

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('..\Output\portfolio.db')
    except Error as e:
        print(e)
    return connection

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
    file_path = '..\Data\AllStocks.json'

    columns = []
    column = []
    #with open(file_path) as json_file:
    data_set = json.load(open('..\Data\AllStocks.json'))
    for row in data_set:
        column = list(row.keys())
        for col in column:
            if col not in columns:
                columns.append(col)

    value = []
    values = []
    for data in data_set:
        for i in columns:
            value.append(str(dict(data).get(i)))
        values.append(list(value))
        value.clear()

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS PORTFOLIO_PRICE_HISTORY")
    sql_create_portfolio_price_history_table = """CREATE TABLE IF NOT EXISTS portfolio_price_history (
           symbol NOT NULL,
           date DATE NOT NULL,
           open NOT NULL,
           high,
           low,
           close,
           volume);"""

    cursor.execute(sql_create_portfolio_price_history_table)

    cursor.executemany ("INSERT INTO portfolio_price_history VALUES (?, ?, ?, ?, ?, ?, ?)", values)

    try:
        connection.commit()
    except Error as e:
        print (e)

    connection.close()
        
#file not found error handling
except FileNotFoundError:
    print ("The specified file does not exist")

#type error handling
except TypeError:
    print ("Error type wrong")
   
