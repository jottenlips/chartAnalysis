from lxml import html
import requests
import json
import os
# from bs4 import BeautifulSoup
# players/a/alstowa01.shtml?redir

#
# //*[@id="my-players-table"]/div[1]/div[1]/div[2]/table/tbody
#
# //*[@id="my-players-table"]/div[1]/div[2]/div/table/tbody
# //*[@id="my-players-table"]/div[1]
# //*[@id="my-players-table"]/div[1]/div[3]/div/table/tbody

# //*[@id="my-players-table"]/div[1]/div[1]/div[2]/table

# http://www.hockey-reference.com/friv/dailyleaders.fcgi?month=3&day=6&year=2017

#
fileNames = []
i = 0;
date = []
dates = []
for file in os.listdir('json'):
    fileNames.append('/Users/johnottenlips/chartAnalysis/json/'+file)
    numOfDays = len(fileNames)
    date = fileNames[i].split("/json/")[1].split("-")
    start_year = date[0]
    start_month = date[1]
    start_day = date[2].split(".")[0]
    i += 1
    date = [start_year,start_month,start_day]
    dates.append(date)
    print(date)
    # print(start_year, start_month, start_day)
# print(dates)


# //*[@id="skaters"]/tbody/tr[1]/td[10]
# //*[@id="skaters"]/tbody/tr[1]/td[3]/a
# //*[@id="skaters"]/tbody/tr[1]/td[23]



response = []
for i in range(len(dates)):
    url = "http://www.hockey-reference.com/friv/dailyleaders.fcgi?month="+dates[i][1]+"&day="+dates[i][2]+"&year="+dates[i][0]
    page = requests.get(url)
    tree = html.fromstring(page.content)
    names = tree.xpath('//*[@id="skaters"]/tbody/tr/td[1]/a/text()')
    team = tree.xpath('//*[@id="skaters"]/tbody/tr/td[3]/a/text()')
    points = tree.xpath('//*[@id="skaters"]/tbody/tr/td[10]/text()')
    toi = tree.xpath('//*[@id="skaters"]/tbody/tr/td[23]/text()')
    print(url)
    playersOnPage = []
    for j in range(len(names)):
        playerDataObj = {"name": names[j], "team": team[j], "points":points[j],"toi":toi[j],"Date Pulled":dates[i][0]+"-"+dates[i][1]+"-"+dates[i][2]}
        playersOnPage.append(playerDataObj)
    response.append(playersOnPage)
    print(response[i])

for i in range(len(response)):
    with open("/Users/johnottenlips/chartAnalysis/nhlLeadersJSON/"+dates[i][0]+"-"+dates[i][1]+"-"+dates[i][2]+".nhlLeaders", 'w') as outfile:
        json.dump(response[i], outfile, sort_keys=True, indent=2)
    outfile.close()


#
# links = tree.xpath('//*[@id="my-players-table"]/div[1]/div[1]/div[2]/table//*/td/a/@href')
# cleanLinks = links[2:-1]
# print(cleanLinks)
#
# for link in cleanLinks:


# page = requests.get('http://www.espn.com/nhl/stats/dailyleaders')
# tree = html.fromstring(page.content)
# cleanLink = list()
# response = []
#
# linkTitles = tree.xpath('//*[@id="my-players-table"]/div[1]/div[1]/table[2]//*/td[2]/a/text()')
# links = tree.xpath('//*[@id="my-players-table"]/div[1]/div[1]/table[2]//*/td[2]/a/@href')
# print(linkTitles, len(links))
#

# with open("baseball-reference.json", 'wb') as outfile:
# 	json.dump(response, outfile, indent=4)
# outfile.close()

	# print(page.content)
