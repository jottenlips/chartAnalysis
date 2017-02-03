import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape APNewsBriefs with requests
urlAPNewsBriefs = 'http://hosted.ap.org/dynamic/fronts/HOME?SITE=AP&SECTION=HOME'
pageAPNewsBriefs = requests.get(urlAPNewsBriefs)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soupAPNewsBriefs = BeautifulSoup(pageAPNewsBriefs.content, 'lxml')

# Parse APNewsBriefs url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'
for position in soupAPNewsBriefs.find_all('div', class_='ap-newsbriefitem'):
    headline = position.find('a').string
    brief = position.find('span', class_='topheadlinebody').string
    apOffice = brief.split(' (AP)')[0]
    fullStory = 'http://hosted.ap.org/' + position.find('a').get('href')
    ctime = fullStory.split('CTIME=')[1]


    # Make changes to response for APNewsBriefs
    response.append({'Headline': headline, 'Brief': brief, 'AP_Office': apOffice, 'Full_Story': fullStory,
                    'CTIME': ctime})

# Write response to JSON file
postingsFile = today + '.APNewsBriefs.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'
# w for text wb for binary
with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
