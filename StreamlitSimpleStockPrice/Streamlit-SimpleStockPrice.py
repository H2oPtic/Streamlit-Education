import yfinance as yf
import streamlit as st
import pandas as pd

#Streamlit "write" command lets you add text, 1-# = H1 size(Markdown style)
st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume for: 
""" ) 


#Assigning a variable to hold ticker symbol
tickerSymbol = 'TSLA'

#Assigning a variable to hold yFinance ticker data
tickerData = yf.Ticker(tickerSymbol)

#Assigning a Pandas DataFrame with historical data from yfinance
tickerDf = tickerData.history(period=max, start='2015-05-01', end='2021-05-01')

#Printing 2 charts to Streamlit page(Closing prices, Volume)
st.write("""
## Closing Price
""")

#Streamlit line chart command takes in closing price of ticker DataFrame
st.line_chart(tickerDf.Close)

#Streamlit "write" command lets you add text, 1-# = H1 size(Markdown style)
st.write("""
## Volume
""")

#Streamlit line chart command takes in volume of ticker DataFrame
st.line_chart(tickerDf.Volume)