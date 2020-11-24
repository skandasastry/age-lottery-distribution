# filename: api-pinger.py
# Author name: Skanda Sastry
# Date: 11/23/2020
# Purpose: Send requests to the NBA stats API in order to get the entire 
# draft pick history as well as each draft pick's birthday. API calls will have the data 
# written to a csv, which we will then use for subsequent data input. This is 
# to be less wasteful about API calls in case there is a limit.


# API calling with NBA API and using Pandas to represent the data.
import pandas as pd
from nba_api.stats.endpoints import drafthistory, commonplayerinfo 

# to write output data to disk
import csv

# to sleep after each request (in a loop) so the API wont get overloaded
import time


# Draft pick history
drafts = drafthistory.DraftHistory().get_data_frames()[0]
drafts.to_csv("../csvs/draft_data_api.csv")

# only focusing on lottery picks so we will slice down the data frame to 
# save some time.

pd.to_numeric(drafts["SEASON"])
drafts = drafts.loc[(drafts["SEASON"] >= 1985)]
drafts = drafts.loc[(drafts["OVERALL_PICK"]) <= 14]

# finding player birthdays
bdays = {}


# Pings the NBA stats API to find each draft pick's birthdate.
with open("../csvs/birthdays-since-1985.csv", "w", newline = '') as infile:
    
    myWriter = csv.writer(infile)
    for i in drafts["PERSON_ID"].tolist():
        
        bday = commonplayerinfo.CommonPlayerInfo(i).get_data_frames()[0]["BIRTHDATE"].values.tolist()[0]
        bdays[i] = bday
        myWriter.writerow([i, bday])
        
        # Need to do this so API doesn't lock us out for doing too many calls 
        # at once. 
        time.sleep(2)