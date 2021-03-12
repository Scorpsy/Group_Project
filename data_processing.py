#!/usr/bin/env python3
import yfinance as yf
import pandas as pd
import numpy as np


def main() -> None:

    googl = yf.Ticker('FB')
    fb_df = googl.history(period='max')

    fb_df = rolling_aves2(fb_df)

    fb_df = date_time_prep(fb_df)
    fb_df.to_csv('fb_data.csv')

    #fb_df = future_close_setup(fb_df, 5)
    #print(fb_df.head())


def rolling_aves(stock_df):

    # Generate columns for 5 day means using pandas rolling  
    stock_df['5 Day Open Mean'] = stock_df['Open'].rolling(5, min_periods=1).mean()
    stock_df['5 Day High Mean'] = stock_df['High'].rolling(5,min_periods=1).mean()
    stock_df['5 Day Low Mean'] = stock_df['Low'].rolling(5, min_periods=1).mean()
    stock_df['5 Day Close Mean'] = stock_df['Close'].rolling(5, min_periods=1).mean()
    stock_df['5 Day Volume Mean'] = stock_df['Volume'].rolling(5,min_periods=1).mean()
    
    # Produce columns for 5 day var using rolling 
    stock_df['5 Day Open Var'] = stock_df['Open'].rolling(5, min_periods=1).var(ddof=0)
     # could also try "...var(ddof=0).interpolate(limit_direction ='backward')" if you dont want to pad with zeroes
    stock_df['5 Day High Var'] = stock_df['High'].rolling(5, min_periods=1).var(ddof=0)
    stock_df['5 Day Low Var'] = stock_df['Low'].rolling(5, min_periods=1).var(ddof=0)
    stock_df['5 Day Close Var'] = stock_df['Close'].rolling(5, min_periods=1).var(ddof=0)
    stock_df['5 Day Volume Var'] = stock_df['Volume'].rolling(5, min_periods=1).var(ddof=0)
    
    # Create 10 day means
    stock_df['10 Day Open Mean'] = stock_df['Open'].rolling(10, min_periods=1).mean()
    stock_df['10 Day High Mean'] = stock_df['High'].rolling(10, min_periods=1).mean()
    stock_df['10 Day Low Mean'] = stock_df['Low'].rolling(10, min_periods=1).mean()
    stock_df['10 Day Close Mean'] = stock_df['Close'].rolling(10, min_periods=1).mean()
    stock_df['10 Day Volume Mean'] = stock_df['Volume'].rolling(10, min_periods=1).mean()
    
    # produce 10 day var columns
    stock_df['10 Day Open Var'] = stock_df['Open'].rolling(10, min_periods=1).var(ddof=0)
    stock_df['10 Day High Var'] = stock_df['High'].rolling(10, min_periods=1).var(ddof=0)
    stock_df['10 Day Low Var'] = stock_df['Low'].rolling(10, min_periods=1).var(ddof=0)
    stock_df['10 Day Close Var'] = stock_df['Close'].rolling(10, min_periods=1).var(ddof=0)
    stock_df['10 Day Volume Var'] = stock_df['Volume'].rolling(10, min_periods=1).var(ddof=0)
    
    # Produce 20 day mean columns
    stock_df['20 Day Open Mean'] = stock_df['Open'].rolling(20, min_periods=1).mean()
    stock_df['20 Day High Mean'] = stock_df['High'].rolling(20, min_periods=1).mean()
    stock_df['20 Day Low Mean'] = stock_df['Low'].rolling(20, min_periods=1).mean()
    stock_df['20 Day Close Mean'] = stock_df['Close'].rolling(20, min_periods=1).mean()
    stock_df['20 Day Volume Mean'] = stock_df['Volume'].rolling(20, min_periods=1).mean()
    
    # Produce columns for 20 day var
    stock_df['20 Day Open Var'] = stock_df['Open'].rolling(20, min_periods=1).var(ddof=0)
    stock_df['20 Day High Var'] = stock_df['High'].rolling(20, min_periods=1).var(ddof=0)
    stock_df['20 Day Low Var'] = stock_df['Low'].rolling(20, min_periods=1).var(ddof=0)
    stock_df['20 Day Close Var'] = stock_df['Close'].rolling(20, min_periods=1).var(ddof=0)
    stock_df['20 Day Volume Var'] = stock_df['Volume'].rolling(20, min_periods=1).var(ddof=0)
    
    return stock_df

def rolling_aves2(stock_df):
    stock_df.dropna(inplace=True)
    stock_df['Mt'] = (stock_df['High'] + stock_df['Low'] + stock_df['Close']) / 3
    stock_df['Price Change'] = (stock_df['Close'] - stock_df['Close'].shift(1, fill_value=0)) / stock_df['Close'].shift(
        1, fill_value=1)

    # Generate columns for 5 day means using pandas rolling
    stock_df['5 Day Open Mean'] = stock_df['Open'].rolling(5, min_periods=1).mean()
    stock_df['5 Day High Mean'] = stock_df['High'].rolling(5, min_periods=1).mean()
    stock_df['5 Day Low Mean'] = stock_df['Low'].rolling(5, min_periods=1).mean()
    stock_df['5 Day Close Mean'] = stock_df['Close'].rolling(5, min_periods=1).mean()
    stock_df['5 Day Volume Mean'] = stock_df['Volume'].rolling(5, min_periods=1).mean()

    # Produce columns for 5 day var using rolling
    stock_df['5 Day Open Var'] = stock_df['Open'].rolling(5, min_periods=1).var(ddof=0)
    # could also try "...var(ddof=0).interpolate(limit_direction ='backward')" if you dont want to pad with zeroes
    stock_df['5 Day High Var'] = stock_df['High'].rolling(5, min_periods=1).var(ddof=0)
    stock_df['5 Day Low Var'] = stock_df['Low'].rolling(5, min_periods=1).var(ddof=0)
    stock_df['5 Day Close Var'] = stock_df['Close'].rolling(5, min_periods=1).var(ddof=0)
    stock_df['5 Day Volume Var'] = stock_df['Volume'].rolling(5, min_periods=1).var(ddof=0)

    stock_df['5 Day High'] = stock_df['High'].rolling(5, min_periods=1).max()
    stock_df['5 Day Low'] = stock_df['Low'].rolling(5, min_periods=1).min()

    # 5 Day SMt & Dt --->>> This is used for advanced analytics
    stock_df['5 Day SMt'] = stock_df['Mt'].rolling(5, min_periods=1).mean()
    stock_df['5 Day Dt'] = stock_df['Mt'].rolling(5, min_periods=1).std(ddof=0)

    # Create 10 day means
    stock_df['10 Day Open Mean'] = stock_df['Open'].rolling(10, min_periods=1).mean()
    stock_df['10 Day High Mean'] = stock_df['High'].rolling(10, min_periods=1).mean()
    stock_df['10 Day Low Mean'] = stock_df['Low'].rolling(10, min_periods=1).mean()
    stock_df['10 Day Close Mean'] = stock_df['Close'].rolling(10, min_periods=1).mean()
    stock_df['10 Day Volume Mean'] = stock_df['Volume'].rolling(10, min_periods=1).mean()

    # produce 10 day var columns
    stock_df['10 Day Open Var'] = stock_df['Open'].rolling(10, min_periods=1).var(ddof=0)
    stock_df['10 Day High Var'] = stock_df['High'].rolling(10, min_periods=1).var(ddof=0)
    stock_df['10 Day Low Var'] = stock_df['Low'].rolling(10, min_periods=1).var(ddof=0)
    stock_df['10 Day Close Var'] = stock_df['Close'].rolling(10, min_periods=1).var(ddof=0)
    stock_df['10 Day Volume Var'] = stock_df['Volume'].rolling(10, min_periods=1).var(ddof=0)

    stock_df['10 Day High'] = stock_df['High'].rolling(10, min_periods=1).max()
    stock_df['10 Day Low'] = stock_df['Low'].rolling(10, min_periods=1).min()

    # 10 Day SMt & Dt --->>> This is used for advanced analytics
    stock_df['10 Day SMt'] = stock_df['Mt'].rolling(10, min_periods=1).mean()
    stock_df['10 Day Dt'] = stock_df['Mt'].rolling(10, min_periods=1).std(ddof=0)

    # Produce 20 day mean columns
    stock_df['20 Day Open Mean'] = stock_df['Open'].rolling(20, min_periods=1).mean()
    stock_df['20 Day High Mean'] = stock_df['High'].rolling(20, min_periods=1).mean()
    stock_df['20 Day Low Mean'] = stock_df['Low'].rolling(20, min_periods=1).mean()
    stock_df['20 Day Close Mean'] = stock_df['Close'].rolling(20, min_periods=1).mean()
    stock_df['20 Day Volume Mean'] = stock_df['Volume'].rolling(20, min_periods=1).mean()

    # Produce columns for 20 day var
    stock_df['20 Day Open Var'] = stock_df['Open'].rolling(20, min_periods=1).var(ddof=0)
    stock_df['20 Day High Var'] = stock_df['High'].rolling(20, min_periods=1).var(ddof=0)
    stock_df['20 Day Low Var'] = stock_df['Low'].rolling(20, min_periods=1).var(ddof=0)
    stock_df['20 Day Close Var'] = stock_df['Close'].rolling(20, min_periods=1).var(ddof=0)
    stock_df['20 Day Volume Var'] = stock_df['Volume'].rolling(20, min_periods=1).var(ddof=0)

    stock_df['20 Day High'] = stock_df['High'].rolling(20, min_periods=1).max()
    stock_df['20 Day Low'] = stock_df['Low'].rolling(20, min_periods=1).min()

    # 10 Day SMt & Dt --->>> This is used for advanced analytics
    stock_df['20 Day SMt'] = stock_df['Mt'].rolling(20, min_periods=1).mean()
    stock_df['20 Day Dt'] = stock_df['Mt'].rolling(20, min_periods=1).std(ddof=0)

    ###############################################################
    ###############  Advanced Analytics ###########################
    ###############################################################

    # Weighted Moving Averages
    stock_df['5 Day Weighted Close Ave'] = stock_df['Close'].ewm(span=5).mean()

    stock_df['10 Day Weighted Close Ave'] = stock_df['Close'].ewm(span=10).mean()

    stock_df['20 Day Weighted Close Ave'] = stock_df['Close'].ewm(span=20).mean()

    # Momentum
    stock_df['5 Day Momentum'] = stock_df['Close'] - stock_df['Close'].shift(5, fill_value=0)
    stock_df['10 Day Momentum'] = stock_df['Close'] - stock_df['Close'].shift(10, fill_value=0)
    stock_df['20 Day Momentum'] = stock_df['Close'] - stock_df['Close'].shift(20, fill_value=0)

    # Stochasitc K%
    stock_df['5 Day Stochastic K'] = 100 * (stock_df['Close'] - stock_df['5 Day Low']) \
                                     / (stock_df['5 Day High'] - stock_df['5 Day Low'])
    stock_df['10 Day Stochastic K'] = 100 * (stock_df['Close'] - stock_df['10 Day Low']) \
                                      / (stock_df['10 Day High'] - stock_df['10 Day Low'])
    stock_df['20 Day Stochastic K'] = 100 * (stock_df['Close'] - stock_df['20 Day Low']) \
                                      / (stock_df['20 Day High'] - stock_df['20 Day Low'])

    # Stochastic D%
    stock_df['5 Day Stochastic K'] = stock_df['5 Day Stochastic K'].rolling(5, min_periods=1).mean()
    stock_df['10 Day Stochastic K'] = stock_df['10 Day Stochastic K'].rolling(5, min_periods=1).mean()
    stock_df['20 Day Stochastic K'] = stock_df['20 Day Stochastic K'].rolling(5, min_periods=1).mean()

    # Relative Strength Index (RSI)
    stock_df['5 Day RSI'] = 100 - 100 / (1 + stock_df['Price Change'].rolling(5, min_periods=1).mean())
    stock_df['10 Day RSI'] = 100 - 100 / (1 + stock_df['Price Change'].rolling(10, min_periods=1).mean())
    stock_df['20 Day RSI'] = 100 - 100 / (1 + stock_df['Price Change'].rolling(20, min_periods=1).mean())

    # Signal

    # Larry Williams
    stock_df['Larry Williams R 5 Day'] = 100 * (stock_df['5 Day High'] - stock_df['Close']) \
                                         / (stock_df['5 Day High'] - stock_df['5 Day Low'])
    stock_df['Larry Williams R 10 Day'] = 100 * (stock_df['10 Day High'] - stock_df['Close']) \
                                          / (stock_df['10 Day High'] - stock_df['10 Day Low'])
    stock_df['Larry Williams R 20 Day'] = 100 * (stock_df['20 Day High'] - stock_df['Close']) \
                                          / (stock_df['20 Day High'] - stock_df['20 Day Low'])

    # Accumulation/Distribution Oscillator
    stock_df['AD Oscillator'] = (stock_df['High'] - stock_df['Close']) / (stock_df['High'] - stock_df['Low'])
    stock_df.loc[stock_df['AD Oscillator'] < 0, 'AD Oscillator'] = 0
    stock_df.loc[stock_df['AD Oscillator'] > 1, 'AD Oscillator'] = 1


    # CCI (Commodity Channel Index)
    stock_df['5 Day CCI'] = (stock_df['Mt'] - stock_df['5 Day SMt']) / (0.015 * stock_df['5 Day Dt'])
    stock_df['10 Day CCI'] = (stock_df['Mt'] - stock_df['10 Day SMt']) / (0.015 * stock_df['10 Day Dt'])
    stock_df['20 Day CCI'] = (stock_df['Mt'] - stock_df['20 Day SMt']) / (0.015 * stock_df['20 Day Dt'])

    stock_df['5 Day CCI'].fillna(0, inplace=True)
    stock_df['10 Day CCI'].fillna(0, inplace=True)
    stock_df['20 Day CCI'].fillna(0, inplace=True)
    stock_df['AD Oscillator'].fillna(0, inplace=True)

    return stock_df

def date_time_prep(stock_df):
  # Makes columns for day/month/year from datetime index
  stock_df['Day'] = stock_df.index.day
  stock_df['Month'] = stock_df.index.month
  stock_df['Year'] = stock_df.index.year

  # Calculates the number of days since IPO
  stock_df['Days From IPO'] = (stock_df.index - stock_df.index[0]).days

  return stock_df

def future_close_setup(stock_df, days=1):
  #This function adds a second closing column and moves it up the number of rows
  # needed to predict that many days ahead
  stock_df['Close in ' + str(days) + ' Days'] = stock_df['Close']
  stock_df['Close in ' + str(days) + ' Days'] = stock_df['Close in ' + str(days) + ' Days'].shift(-days)
  return stock_df



if __name__ == "__main__":
    main()