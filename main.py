#Stocks and Bonds Report - Final Portfolio
#8/20/23
#Laura Walker

from datetime import date, datetime
from prettytable import PrettyTable
import datetime
import csv
import sys
import sqlite3
from sqlite3 import Error
import week4Assignment
import candlestickGraph
import graph


class Customer:
    def __init__ (this, customerID, name, address, city, state, phoneNumber):
        this.customerID = customerID
        this.name = name
        this.address = address
        this.city = city
        this.state = state
        this.phoneNumber = phoneNumber
        this.stocks = []
        this.bonds = []

    def add_stock_to_portfolio(this, purchaseNumber, stockName, numberOfStocks, purchasePrice, currentPrice, purchaseDate):
        stock = Stocks (purchaseNumber, stockName, numberOfStocks, purchasePrice, currentPrice, purchaseDate)
        this.stocks.append(stock)

    def add_bond_to_portfolio(this, purchaseNumber, stockName, numberOfStocks, purchasePrice, currentPrice, purchaseDate, coupon, bondYield):
        bond = Bonds (purchaseNumber, stockName, numberOfStocks, purchasePrice, currentPrice, purchaseDate, coupon, bondYield)
        this.bonds.append(bond)

class Stocks:
    type = 'stock'
    def __init__ (this, purchaseNumber, stockName, numberOfStocks, purchasePrice, currentPrice, purchaseDate):
        this.purchaseID = purchaseNumber
        this.stockName = stockName
        this.numberOfStocks = numberOfStocks
        this.purchasePrice = purchasePrice
        this.currentPrice = currentPrice
        this.purchaseDate = purchaseDate

    def calculateEarnings(currentPrice, purchasePrice, numberOfStocks):
        earnings = (currentPrice - purchasePrice) * numberOfStocks
        return earnings

    def yearlyEarnings (currentPrice, purchasePrice, purchaseDate):
        yearlyPercentage = (((currentPrice-purchasePrice)/purchasePrice)/((today - purchaseDate).days/365))*100
        return yearlyPercentage

class Bonds(Stocks):
    type = 'bond'
    def __init__ (this, purchaseNumber, stockName, numberOfStocks, purchasePrice, currentPrice, purchaseDate, coupon, bondYield):
        super().__init__(purchaseNumber, stockName, numberOfStocks, purchasePrice, currentPrice, purchaseDate)
        this.coupon = coupon
        this.bondYield = bondYield

def display_portfolio(self):
    myTable = PrettyTable()
    myTable.field_names = ["PO No.", "Symbol", "Purchase Date", "No. of Shares", "Purchase Price", "Current Value", "Coupon", "Yield", "Customer Number"]
    myTable.add_rows(portfolios[0:])
    print(myTable)
        
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('portfolio.db')
    except Error as e:
        print(e)
    return connection    
    
try:

    investor = Customer(customerID = "1", name = "Bob Smith", address = "123 Main St", city = "City", state = "State", phoneNumber = "123-456-7890")
    
    listOfStocks = "..\Data\Lesson6_Data_Stocks.csv"
    listOfBonds = "..\Data\Lesson6_Data_Bonds.csv"
    listOfCustomers = "..\Data\Lesson6_Data_Customers.csv"
    
    #initializing portfolios
    portfolios = []
    customers = []

    #sets purchase ID at 0
    purchaseID = 000
    customerID = 000
                        
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS PORTFOLIO")
    sql_create_portfolio_table = """CREATE TABLE IF NOT EXISTS portfolio (
           purchaseID PRIMARY KEY,
           symbol NOT NULL,
           numberOfStocks NOT NULL,
           purchasePrice NOT NULL,
           currentPrice NOT NULL,
           purchaseDate NOT NULL,
           coupon,
           bondYield,
           customer_ID);"""
                   
    cursor.execute("DROP TABLE IF EXISTS CUSTOMER")
    sql_create_customer_table = """CREATE TABLE IF NOT EXISTS customer (
            customer_ID text NOT NULL,
            name text NOT NULL,
            address text NOT NULL,
            city text NOT NULL,
            state text NOT NULL,
            phone text NOT NULL,
            purchaseID,
            FOREIGN KEY (purchaseID) REFERENCES portfolio(purchaseID));"""
    
    cursor.execute(sql_create_portfolio_table)
    cursor.execute(sql_create_customer_table)
    
    customerNumber = 1
    name = investor.name
    address = investor.address
    city = investor.city
    state = investor.state
    phone = investor.phoneNumber
    customer=[customerNumber, name, address, city, state, phone]
    customers.append(investor)
    cursor.execute ("INSERT INTO customer (customer_ID, name, address, city, state, phone) VALUES (?, ?, ?, ?, ?, ? )", (customer[0], customer[1], customer[2], customer[3], customer[4], customer[5]))
    investor_id = cursor.lastrowid   

    
    # reading csv file
    with open(listOfStocks, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        # extracting each data row one by one
        for row in csvreader:
            purchaseID = purchaseID+1
            purchaseNumber = "PN""{:05d}".format(purchaseID)
            symbol = (row[0])
            numberOfStocks = (row[1])
            purchasePrice = (row[2])
            currentPrice = (row[3])
            purchaseDate = (row[4])
            customer_ID = (row[5])
            customerNumber =  "CN"+(customer_ID)
            investor.add_stock_to_portfolio(purchaseNumber, symbol, numberOfStocks, purchasePrice, currentPrice, purchaseDate)
            stock=[purchaseNumber, symbol, numberOfStocks, purchasePrice, currentPrice, purchaseDate, 0, 0, customerNumber]
            portfolios.append(stock)
            cursor.execute ("INSERT INTO portfolio (purchaseID, symbol, numberOfStocks, purchasePrice, currentPrice, purchaseDate, coupon, bondYield, customer_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (stock[0], stock[1], stock[2], stock[3], stock[4], stock[5], stock[6], stock[7], stock[8]))   
            purchaseID = cursor.lastrowid
            cursor.execute("UPDATE customer SET purchaseID = ? WHERE customer_ID = ?", (purchaseNumber,investor_id))
   
    with open(listOfBonds, 'r') as csvfile:
         # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting field names through first row
        fields = next(csvreader)
        # extracting each data row one by one
        for row in csvreader:
            purchaseID = purchaseID+1
            purchaseNumber = "PN""{:05d}".format(purchaseID)
            symbol = row[0]
            numberOfStocks = (row[1])
            purchasePrice = (row[2])
            currentPrice = (row[3])
            purchaseDate = (row[4])
            coupon = (row[5])
            bondYield = (row[6])
            customer_ID = (row[7])
            customerNumber = "CN"+(customer_ID)
            investor.add_bond_to_portfolio(purchaseNumber, symbol, numberOfStocks, purchasePrice, currentPrice, purchaseDate, coupon, bondYield)
            bond=[purchaseNumber, symbol, numberOfStocks, purchasePrice, currentPrice, purchaseDate, coupon, bondYield, customerNumber]
            portfolios.append(bond)
            cursor.execute ("INSERT INTO portfolio (purchaseID, symbol, numberOfStocks, purchasePrice, currentPrice, purchaseDate, coupon, bondYield, customer_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (bond[0], bond[1], bond[2], bond[3], bond[4], bond[5], bond[6], bond[7], bond[8]))   
            purchaseID = cursor.lastrowid
            cursor.execute("UPDATE customer SET purchaseID = ? WHERE customer_ID = ?", (purchaseNumber,investor_id))

            #sets the table to be print out to a file instead of the command prompt window


    original_stdout = sys.stdout
    with open('..\Output\output.txt', 'w') as file:
        sys.stdout = file
        display_portfolio(portfolios)       
    today = date.today()
    
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
