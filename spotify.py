import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []
songs = list()
artist = list()
chartNumbers = list()
streams = list()



# Scrape APNewsBriefs with requests
url = 'https://spotifycharts.com/regional/us/daily/latest'
page = requests.get(url)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soup = BeautifulSoup(page.content, 'lxml')



for data in soup.find_all('td', class_='chart-table-track'):
    songs.append(data.find('strong').string)
    artist.append(data.find('span').string.split("by ")[1])

for data in soup.find_all('td', class_="chart-table-streams"):
    streams.append(data.string)

for data in soup.find_all('td', class_="chart-table-position"):
    chartNumbers.append(data.string)
print(songs[0],artist[0])


for i in range(len(chartNumbers)):
    response.append({'Song': songs[i], 'Artist': artist[i], 'Steams': streams[i], 'Chart Number': chartNumbers[i]})

# Write response to JSON file
postingsFile = today + '.spotify.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'
# w for text wb for binary
with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
