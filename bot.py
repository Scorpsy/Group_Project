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


    tick = []

    with open("tickers_n.csv") as csvfile:
        tickers = csv.reader(csvfile)
        for row in tickers: 
            tick.append(row[0])

    print(tick)

    #data,sub = get_data(reddit,'investing')
    #data_p = data_processing(data,sub)
    #init_csv('investing_FB_r.csv')
    #print_csv(data,sub)

    #df = pd.read_csv('tickers_n.csv',index=False)
    #print(df)

def init_csv(filename):
    with open(filename, 'w', newline="") as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Date','Title','Selftext','Upvote','Upvote Ratio'])


def print_csv(data,sub):

    for d in data:
        
        if 'TSLA' in d.title:
            filename = f"{sub}_TSLA_r.csv"
            with open(filename, 'a', newline="") as f:
                thewriter = csv.writer(f)
                thewriter.writerow([d.date, d.title,d.selftext, d.upvote, d.upvote_ratio])

        elif 'MSFT' in d.title:
            filename = f"{sub}_MSFT_r.csv"
            with open(filename, 'a', newline="") as f:
                thewriter = csv.writer(f)
                thewriter.writerow([d.date, d.title,d.selftext, d.upvote, d.upvote_ratio])

        elif 'GOOG' in d.title:
            filename = f"{sub}_GOOG_r.csv"
            with open(filename, 'a', newline="") as f:
                thewriter = csv.writer(f)
                thewriter.writerow([d.date, d.title,d.selftext, d.upvote, d.upvote_ratio])

        elif 'AAPL' in d.title:
            filename = f"{sub}_AAPL_r.csv"
            with open(filename, 'a', newline="") as f:
                thewriter = csv.writer(f)
                thewriter.writerow([d.date, d.title,d.selftext, d.upvote, d.upvote_ratio])

        elif 'AMZN' in d.title:
            filename = f"{sub}_AMZN_r.csv"
            with open(filename, 'a', newline="") as f:
                thewriter = csv.writer(f)
                thewriter.writerow([d.date, d.title,d.selftext, d.upvote, d.upvote_ratio])

        elif 'FB' in d.title:
            filename = f"{sub}_FB_r.csv"
            with open(filename, 'a', newline="") as f:
                thewriter = csv.writer(f)
                thewriter.writerow([d.date, d.title,d.selftext, d.upvote, d.upvote_ratio])



def data_processing(data,tickers):
    data_p = []
    for d in data:
        if any(word in d.title for word in tickers):
            data_p.append(d)

    return data_p

def get_data(reddit, sub):
    stock = reddit.subreddit(sub).new()

    data = []

    for submission in stock:
        if not submission.stickied:
            time = submission.created_utc
            utc_time = get_date(time)

            todays_d = dt.date.today()

            #if utc_time.date() == todays_d:
            post = Posts(submission.title,submission.selftext,utc_time,submission.ups,submission.upvote_ratio)
            data.append(post)

    return data,sub


def get_date(created):
    return dt.datetime.fromtimestamp(created)

if __name__ == "__main__":
    main()