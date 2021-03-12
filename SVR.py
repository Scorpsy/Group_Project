#!/usr/bin/env python3
from sklearn.svm import SVR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main() -> None:

    df = pd.read_csv("fb_data.csv")
    #print(df.tail())

    df = df[2189:2208]
    print(df)


    days = list()
    adj_close_prices = list()

    df_days = df.loc[:, 'Date']
    df_adj_close = df.loc[:, 'Close']

    for day in df_days:
        days.append([int(day.split('-')[2])]  )

    for close in df_adj_close:
        adj_close_prices.append( float(close))

    #print(days)
    #print(adj_close_prices)


    lin_svr = SVR(kernel = 'linear', C=1000.0)
    lin_svr.fit(days,adj_close_prices)

    pol_svr = SVR(kernel = 'poly', C=1000.0, degree=2)
    pol_svr.fit(days,adj_close_prices)

    rbf_svr = SVR(kernel = 'rbf', C=1000.0, gamma = 0.15)
    rbf_svr.fit(days,adj_close_prices)

    plt.figure(figsize=(16,8))
    plt.scatter(days, adj_close_prices, color = 'red', label = 'Data')
    plt.plot(days, rbf_svr.predict(days),color='green',label = 'RBF Model')
    plt.plot(days, pol_svr.predict(days),color='orange',label = 'Polynomial Model')
    plt.plot(days, lin_svr.predict(days),color='blue',label = 'Linear Model')

    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()