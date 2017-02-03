from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
import json
import csv

# Create dict for JSON Object
response = []

# Prepare for parsing APNewsBriefs with BeautifulSoup after Scraping with Selenium
browser = webdriver.Chrome()

urlAPNewsBriefs = 'http://hosted.ap.org/dynamic/fronts/HOME?SITE=AP&SECTION=HOME'
pageAPNewsBriefs = browser.get(urlAPNewsBriefs)
soupAPNewsBriefs = BeautifulSoup(browser.page_source, 'lxml')

# browser.quit()

# Parse APNewsBriefs urlbrowser.page_source
today = str(datetime.datetime.now().date())
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
postingsFile = '/Users/johnottenlips/' + today + '.APNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()

# Write response to CSV file
keys = response[0].keys()
with open(today + '.APNewsBriefs.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(response)
