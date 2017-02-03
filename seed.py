# http://seed-db.com/accelerators

import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv
import re

today = str(datetime.datetime.now().date())

# //*[@id="5156331078025216"]/td[5]/span

# Create a list of dictionaries for JSON Object
response = []
accelerators = list()
total_exit_value = list()
total_funding_value = list()
city = list()
cohorts = list()

# //*[@id="accellist"]/tbody/tr[1]/td[2]/text()

# Scrape APNewsBriefs with requests
url = 'http://seed-db.com/accelerators'
page = requests.get(url)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soup = BeautifulSoup(page.content, 'lxml')

# anchor = soup.find_all('table')

for td in soup.find_all('td'):
    try:
        accelerators.append(td.find('strong').string)
    except:
        pass


for num in range(len(accelerators)):
    city.append(soup.find(text=accelerators[num]).findNext('td').contents[0])
    cohorts.append(city[num].findNext('td').string)
    total_exit_value.append(cohorts[num].findNext('td').find('span').string)
    total_funding_value.append(cohorts[num].findNext('td').findNext('td').find('span').string)

for num in range(len(accelerators)):
    print(city[num],cohorts[num],total_exit_value[num], total_funding_value[num])
    response.append({'Accelerators': accelerators[num], 'Cohorts': cohorts[num], 'Total Exit Value': total_exit_value[num], 'Total Funding Value': total_funding_value[num],
                })

# Write response to JSON file
postingsFile = today + '.seed-db.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'
# w for text wb for binary
with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
