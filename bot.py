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

    data,sub = get_data(reddit,'investing')
    print_csv(data,sub, tick)

    #df = pd.read_csv('tickers_n.csv',index=False)
    #print(df)

def init_csv(filename):
    with open(filename, 'w', newline="") as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Date','Title','Selftext','Upvote','Upvote Ratio'])


def print_csv(data,sub,tick):

    for d in data:
        
        match = [x for x in tick if x in d.title]
        if match:

            if len(match) > 1:
                for comp in match:
                    filename =f"{sub}_{comp}_r.csv"

                    if os.path.isfile(f"datasets/{sub}/"+filename):
                        with open(f"datasets/{sub}/"+filename, 'a', newline="") as f:
                            thewriter = csv.writer(f)
                            thewriter.writerow([d.date,match, d.title,d.selftext, d.upvote, d.upvote_ratio])
                    else:
                        with open(f"datasets/{sub}/"+filename, 'w', newline="") as f:
                            thewriter = csv.writer(f)
                            thewriter.writerow(['Date','Tickers','Title','Selftext','Upvote','Upvote Ratio'])
                            thewriter.writerow([d.date,match, d.title,d.selftext, d.upvote, d.upvote_ratio])

            else:

                filename =f"{sub}_{match[0]}_r.csv"

                if os.path.isfile(f"datasets/{sub}/"+filename):
                    with open(f"datasets/{sub}/"+filename, 'a', newline="") as f:
                        thewriter = csv.writer(f)
                        thewriter.writerow([d.date,match, d.title,d.selftext, d.upvote, d.upvote_ratio])
                else:
                    with open(f"datasets/{sub}/"+filename, 'w', newline="") as f:
                        thewriter = csv.writer(f)
                        thewriter.writerow(['Date','Title','Selftext','Upvote','Upvote Ratio'])
                        thewriter.writerow([d.date,match, d.title,d.selftext, d.upvote, d.upvote_ratio])


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