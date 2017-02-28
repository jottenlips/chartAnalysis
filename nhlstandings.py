# http://www.cbssports.com/nhl/standings

import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv
import re

today = str(datetime.datetime.now().date())

# //*[@id="5156331078025216"]/td[5]/span

# ATLANTIC DIVISION	W	L	OT	PTS	ROW	GF	GA	HOME	ROAD	L10	STREAK

# Create a list of dictionaries for JSON Object
response = []
teams = list()
w = list()
l = list()
ot = list()
pts = list()
regovertimewins = list()
gf = list()
ga = list()
home = list()
road = list()
L10 = list()
streak = list()

# //*[@id="accellist"]/tbody/tr[1]/td[2]/text()

# Scrape APNewsBriefs with requests
url = 'http://www.cbssports.com/nhl/standings'
page = requests.get(url)

# Prepare for parsing APNewsBriefs with BeautifulSoup
soup = BeautifulSoup(page.content, 'lxml')

# anchor = soup.find_all('table')
# //*[@id="sortableContent"]/table[1]/tbody/tr[2]/td[11]/nobr

for tr in soup.find_all('tr'):
    try:
        team = tr.find('td')
        teams.append(team.string)
        win = team.findNext('td').string
        w.append(win)
        loss = win.findNext('td')
        l.append(loss.string)
        overtime = loss.findNext('td')
        ot.append(overtime.string)
        points = overtime.findNext('td')
        pts.append(points.string)
        regulationOvertimeWins = points.findNext('td')
        regovertimewins.append(regulationOvertimeWins.string)
        gfs = regulationOvertimeWins.findNext('td')
        gf.append(gfs.string)
        gas = gfs.findNext('td')
        ga.append(gas.string)
        homes = gas.findNext('td')
        home.append(homes.string)
        roads = homes.findNext('td')
        road.append(roads.string)
        L10s = roads.findNext('td')
        L10.append(L10s.string)
        streaks = L10s.findNext('td')
        streak.append(streaks.string)
    except:
        pass
# print(teams)
# print(w)
# print(l)
# print(ot)
# print(pts)
# print(regovertimewins)
# print(gf)
# print(ga)
# print(home)
# print(road)
# print(L10)
# print(streak)
postingsFile = today + '.nhlstandings.json'

# teams = list()
# w = list()
# l = list()
# ot = list()
# pts = list()
# regovertimewins = list()
# gf = list()
# ga = list()
# home = list()
# road = list()
# L10 = list()
# streak = list()

for num in range(len(teams)):
    response.append({'Team': teams[num], 'Win': w[num], 'Loss': l[num], 'Over Time': ot[num],
                    'Points': pts[num], 'Regulation Overtime Wins': regovertimewins[num],'GF': gf[num],
                     'GA': ga[num], 'Home': home[num], 'Road': road[num], 'L10': L10[num], 'Streak': streak[num], 'Date Pulled': today, 'Source': url})


#Write response to JSON file in another location

with open("/Users/johnottenlips/chartAnalysis/json/"+postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
