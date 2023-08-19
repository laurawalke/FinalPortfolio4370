#Developed by: Laura Walker
#7/9/23
#Calculate the current earnings for the stock based on the (current price - purchase price) * number of stocks

from datetime import date
import numbers

#Determine difference in dates
def numOfDays(date1, date2):
    return (date2-date1).days

#Calculating Loss/Gain
def calculateCurrentEarnings(stockPortfolio,key):
    finalPrice = {}
    finalPrice [key] = ((stockPortfolio[key]['currentPrice'] - stockPortfolio[key]['purchasePrice']) * stockPortfolio[key]['numberOfStocks'])
    return(finalPrice[key])        

#Calculate Percentage Yeild/Loss
def calculatePercentageEarnings(stockPortfolio,key):
    finalPercent = {}
    finalPercent[key] = ((stockPortfolio[key]['currentPrice'] - stockPortfolio[key]['purchasePrice'])/stockPortfolio[key]['purchasePrice'] * 100)
    return(finalPercent[key])    

#Calculate Yearly Earnings/Loss Rate
def calculateYearlyEarnings(stockPortfolio,key):   
    yearlyEarnings = {}
    date2 = date.today()
    date1 = (stockPortfolio[key]['purchaseDate'])
    yearlyEarnings[key] = (((((stockPortfolio[key]['currentPrice']-(stockPortfolio[key]['purchasePrice']))/(stockPortfolio[key]['purchasePrice'])/
                                  (numOfDays(date1,date2))))))*100
    return yearlyEarnings[key]

#Determine which stock earned the most
def calculateHighestEarningStock(finalPrice):
    #Determine max earning stock   
    for key in finalPrice:
        maxEarningIndex = (max(finalPrice, key=finalPrice.get))

    maxEarning = finalPrice[maxEarningIndex]

    highestEarningCompany = stockPortfolio[maxEarningIndex]

    if maxEarning > 0:
        print ('The stock with the highest increase in value in your portfolio on a per-share basis is: ', highestEarningCompany['stockName'])
    elif maxEarning < 0:
        print ('The stock with least decrease in value in your portfolio on a per-share basis is: ', highestEarningCompany['stockName'])


    
