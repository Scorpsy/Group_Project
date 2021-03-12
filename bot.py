#!/usr/bin/env python3
import praw
import os
import time
import csv
import datetime as dt
import pandas as pd
from classes import Posts
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
          

    data = get_data(reddit,'investing','TSLA','all')

    print_csv('investing_TSLA.csv',data)

    df = pd.read_csv('investing_TSLA.csv')
    print(df)


def get_data(reddit, sub, ticker, time_frame):
    stock = reddit.subreddit(sub)
    data = []

    stock_search = stock.search(query=ticker, time_filter = time_frame, limit=None)
    for submission in stock_search:
        if not submission.stickied:
            time = submission.created_utc
            utc_time = get_date(time)

            post = Posts(submission.title,utc_time,submission.ups,submission.upvote_ratio)

            data.append(post)

    return data

def print_csv(filename: str, data):
    with open(filename, 'w', newline="") as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Date','Title','Upvote','Upvote Ratio'])

        for d in data:
            thewriter.writerow([d.date, d.title, d.upvote, d.upvote_ratio])


def get_date(created):
    return dt.datetime.fromtimestamp(created)

if __name__ == "__main__":
    main()