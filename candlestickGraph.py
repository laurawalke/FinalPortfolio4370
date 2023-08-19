#Stocks and Bonds Report - Importing data from CSV to SQLite
#7/26/23
#Laura Walker

import csv
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime
    
try:

    AIG = "..\Data\AIG.csv"
    df = pd.read_csv(AIG)
    figAIG = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    figAIG.update_layout(title_text='Stock Name: AIG')
    figAIG.show()

    F = "..\Data\F.csv"
    df = pd.read_csv(F)
    figF = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    figF.update_layout(title_text='Stock Name: F')
    figF.show()

    FB = "..\Data\FB.csv"
    df = pd.read_csv(FB)
    figFB = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    figFB.update_layout(title_text='Stock Name: FB')
    figFB.show()

    GOOG = "..\Data\GOOG.csv"
    df = pd.read_csv(GOOG)
    figGOOG = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    figGOOG.update_layout(title_text='Stock Name: GOOG')
    figGOOG.show()

    IBM = "..\Data\IBM.csv"
    df = pd.read_csv(IBM)
    figIBM = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    figIBM.update_layout(title_text='Stock Name: IBM')
    figIBM.show()

    M = "..\Data\M.csv"
    df = pd.read_csv(M)
    figM = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    figM.update_layout(title_text='Stock Name: M')
    figM.show()

    MSFT = "..\Data\MSFT.csv"
    df = pd.read_csv(MSFT)
    figMSFT = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    figMSFT.update_layout(title_text='Stock Name: MSFT')
    figMSFT.show()

    RDSA = "..\Data\RDS-A.csv"
    df = pd.read_csv(RDSA)
    figRDSA = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    figRDSA.update_layout(title_text='Stock Name: RDS-A')
    figRDSA.show()

    SPY = "..\Data\SPY.csv"
    df = pd.read_csv(SPY)
    figSPY = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
    figSPY.update_layout(title_text='Stock Name: SPY')
    figSPY.show()
#file not found error handling
except FileNotFoundError:
    print ("The specified file does not exist")

#type error handling
except TypeError:
    print ("Error type wrong")
