# Scrapers and API Pingers

These were the files used to create the datasets in the ``csvs/`` directory. Brief description of each of them:

### api-pinger.py
Sends requests to stats.nba.com, uses the NBA API developed by Swar Patel. Pings the API first for 
a draft pick history dataset, turns that into ``draft_data_api.csv`` so we can limit API calls and simply
read the constant data from a csv.

Then, pings the API once for each player to find their birthdays. In order to limit the time it takes for this to run,
I slice the draft info dataFrame to only include lottery picks from 1985-2020 (which is the scope of our study).
Writes the birthday data to a CSV as well as it loops through the draft info dataframe.

### scraper.py

Scrapes the Wikipedia page for each NBA draft (starting from the 1985 NBA draft, which had the first lottery ever. Small trivia factoid - first ever No. 1 pick in the lottery era was Patrick Ewing).
Finds the dates for each year, draft year, writes them to a csv. These, along with player birthdate info, will be used later to calculate each player's age in seconds to be as precise as possible.
