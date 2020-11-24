# filename: scraper.py
# Author name: Skanda Sastry
# Date: 11/23/2020
# Purpose: Scrape wikipedia for the exact date of each year's NBA draft. The
# purpose of this is to calculate the exact age of each pick based on their
# birthdates.

# api GET tool, beautiful soup for the scraping/html parsing
import requests
from bs4 import BeautifulSoup

# writing output to csvs folder for input data.
import csv

# So we don't have to hardcode values. We are focusing on the lottery era.
START_DATE = 1985
END_DATE = 2020

# finding exact date for each draft year
with open("../csvs/draftYears.csv", "w", newline='') as myFile:
    myWriter = csv.writer(myFile)
    
    # focusing on only the Lottery Era (1985 to 2020) - could do something
    # different instead of hardcoding this value.
    for i in range(START_DATE, END_DATE + 1):
        reqString = "https://en.wikipedia.org/wiki/" + str(i) + "_NBA_draft"
    
        res = requests.get(reqString)
        
        # parses the string to find the wikipedia table that tells us
        # the date.
        if (res.status_code == 200):
            soup = BeautifulSoup(res.content, 'html.parser')
            
            bodyInfo = soup.find(id="bodyContent").find("table", {"class": "infobox"})
            
                
            cells = bodyInfo.findAll('td')    
    
            cells = [i.text for i in cells]
    
            date_suspect = [s for s in cells if (", " + str(i)) in s][0]
            
            myWriter.writerow([i, date_suspect])
            
            # progress report to keep yourself from going insane, prints
            # after each year has been finished
            print("Finished: ", i)
            

        
        
