# misc_pitching

from lxml import html
import requests
import json
# from bs4 import BeautifulSoup
# players/a/alstowa01.shtml?redir


page = requests.get('http://www.baseball-reference.com/leagues/MLB/1995-rookies.shtml#pitch')
tree = html.fromstring(page.content)
cleanLink = list()
response = []


links = tree.xpath('//*[@id="misc_pitching"]/tbody/tr/td/a/@href')
print(links)
for link in links:
    cleanLink.append(link)

print(cleanLink)

for count in range(len(cleanLink)):
	page = requests.get('http://www.baseball-reference.com/'+cleanLink[count])
	tree = html.fromstring(page.content)
	playerName = str(tree.xpath('//*[@id="player_name"]/text()')); so = str(tree.xpath('//*[@id="pitching_standard.1995"]/td[22]/text()')); ip = str(tree.xpath('//*[@id="pitching_standard.1995"]/td[15]/text()')); print(playerName, so, ip); response.append({'Player' : playerName, 'SO' : so, "IP" : ip})

with open("pitcherStats.json", 'w') as outfile:
	json.dump(response, outfile, indent=4)
outfile.close()
