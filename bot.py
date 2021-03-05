#!/usr/bin/env python3
import praw
import os
import time
import datetime as dt
from os.path import join,dirname
from dotenv import load_dotenv


def main() -> None:

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    reddit = praw.Reddit(client_id = os.getenv('client_id'),
                        client_secret =  os.getenv('client_secret'),
                        username =  os.getenv('username'),
                        password = os.getenv('password'),
                        user_agent = os.getenv('user_agent'))

    investing = reddit.subreddit('investing')
    hot_investing = investing.hot(limit=5)

    print("r/investin on TSLA\n")
    investing_search = investing.search(query='TSLA', time_filter = 'all')
    #print(size(investing_search))
    for submission in investing_search:
        if not submission.stickied:
            time = submission.created_utc
            utc_time = get_date(time)

            print(utc_time)
            print(submission.title)
            #print(submission.ups)
            #print(submission.downs)



    print("r/investin on MSFT\n")
    investing_search = investing.search(query='MSFT', time_filter = 'all', limit = 5)
    #print(size(investing_search))
    for submission in investing_search:
        if not submission.stickied:
            time = submission.created_utc
            utc_time = get_date(time)

            print(utc_time)
            print(submission.title)
            print(submission.ups)
            print(submission.upvote_ratio)


    print("r/investin on GOOGL\n")
    investing_search = investing.search(query='GOOGL', time_filter = 'all', limit = 5)
    #print(size(investing_search))
    for submission in investing_search:
        if not submission.stickied:
            time = submission.created_utc
            utc_time = get_date(time)

            print(utc_time)
            print(submission.title)





    print("\n")

    print("Investing Subreddit\n")

    #for submission in hot_investing:
    #    if not submission.stickied:
    #        print('Title: {}'.format(submission.title))

    stocks = reddit.subreddit('stocks')
    hot_stocks = stocks.hot(limit=5)

    #print("\n")

    #print("r/stocks on MSFT\n")
    
    #stocks_search = stocks.search(query = 'MSFT', time_filter = 'week')
    #for submission in stocks_search:
    #    if not submission.stickied:
    #        time = submission.created_utc
    #        utc_time = get_date(time)

    #        print(utc_time)
    #        print(submission.title)

    #print("\n")

    #print("Stocks Subreddit\n")

    #for submission in hot_stocks:
    #    if not submission.stickied:
    #        print('Title: {}'.format(submission.title))
    

def get_date(created):
    return dt.datetime.fromtimestamp(created)

if __name__ == "__main__":
    main()