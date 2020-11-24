# filename: age-lottery.py
# Author name: Skanda Sastry
# Date: 11/23/2020
# Purpose: Parse a file containing NBA draft data and produce data visual-
# izations on the distribution of lottery pick age each year in the draft.


# number crunching/data representation tools
import pandas as pd
import numpy as np 


# pretty visualization creators
import seaborn as sns
import matplotlib.pyplot as plt

# to find date differences between draft date and birthdate to exactly
# calculate each player's age
import dateutil
from datetime import date, datetime

# need to divide by this to convert seconds to decimal years
YEAR_SECS = 3600 * 24 * 365


''' ------------------- DATA INPUT SECTION ----------------------------'''
# reads in draft data, focusing on lottery picks in prep-to-pro era
# if you would like to know how this csv was created, visit the 
# scrapers-pingers folder
drafts = pd.read_csv("../csvs/draft_data_api.csv")
pd.to_numeric(drafts["SEASON"])

# 1985 was the first year of the NBA draft lottery, picks 1-14 are considered
# "lottery picks" 
drafts = drafts.loc[(drafts["SEASON"] >= 1985)]
drafts = drafts.loc[(drafts["OVERALL_PICK"]) <= 14]

# reading in player birthday info
bdays = pd.read_csv("../csvs/birthdays-since-1985.csv", names=["Player_ID", "Birthday"])


# reads in the exact date of every draft
# if you would like to know how this csv was created, visit the scrapers-pingers 
# folder
draftDates = pd.read_csv("../csvs/draftYears.csv", names=["Year", "Date"])


''' ------------------- DATA PROCESSING SECTION ----------------------------'''
# dictionary relating draft year to exact draft date
dateMap = {}

# dictionary mapping player id to their birthdate
bdayMap = {}

# creating/populating each map
for index, row in draftDates.iterrows():
    dateMap[int(row["Year"])] = datetime.strptime(row["Date"], "%B %d, %Y")

for index, row in bdays.iterrows():
    
    if (type(row["Birthday"]) is str):
        bdayMap[row["Player_ID"]] = datetime.strptime(row["Birthday"], "%Y-%m-%dT%H:%M:%S")
    
    else:
        # for some reason the birthday doesn't show up for Len Bias
        # If anyone from the NBA league office is reading this, please fix
        # this error - not only is it a data governance/management error 
        # it is also a bit disrespectful of Bias' legacy.
        
        # Len Bias was born on 11/18/1963
        bdayMap[row["Player_ID"]] = datetime(1963, 11, 18)
        print(drafts.loc[drafts["PERSON_ID"] == row["Player_ID"]].values)


# Most important line of code here - this looks up the date of the draft
# in which a player was selected, and subtracts it by their birthdate, which
# it looks up by their player id. Then, converts that to years in output.
drafts["Age when Drafted"] = drafts.apply(
    lambda row: 
        (dateMap[row.SEASON] - bdayMap[row.PERSON_ID]).total_seconds()/YEAR_SECS, 
        axis=1)


    
''' ------------------- DATA VIZ SECTION ----------------------------'''
# Now that we have the ages of the players for each year, all we have to do 
# is plot their distributions. I used Seaborn to produce box and whisker plots.
f, ax = plt.subplots(figsize=(20, 8))

ax.set_title("NBA Draft Lottery Pick Age Distribution, 1985-2020 (Picks 1 - 14)", fontsize=16)
sns.boxplot(x="SEASON", y="Age when Drafted", data=drafts, ax=ax)
ax.set_xlabel("Season", fontweight="bold")
ax.set_ylabel("Prospect Age Distribution (yrs)", fontweight="bold")

# writes output image
f.savefig("../output-images/age_lottery_boxplot.jpg")


# plotting a lineplot of medians here
f2, ax2= plt.subplots(figsize=(20, 8))

# using list comprehension and np.percentile to produce median ages
ageMedians = [np.percentile(
    np.array(
        drafts.loc[drafts["SEASON"] == i]["Age when Drafted"].tolist()), 50) 
    for i in drafts["SEASON"].tolist()]

# plotting median ages using scatter and writing it out to disk
plt.plot(drafts["SEASON"].tolist(), ageMedians, linewidth=2, color="black", marker="o")
ax2.set_xlabel("Season", fontweight="bold")
ax2.set_ylim(18, 25)
ax2.set_ylabel("Median Age of Prospects (yrs)", fontweight="bold")
ax2.set_title("Median Age of NBA Lottery Picks in the Lottery Era (1985 - 2020)", fontsize=16)
f2.savefig("../output-images/age_lottery_lineplot.jpg")



