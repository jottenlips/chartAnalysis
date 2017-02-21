from lxml import html
import requests
import json
# from bs4 import BeautifulSoup
# players/a/alstowa01.shtml?redir


page = requests.get('http://www.baseball-reference.com/managers/')
tree = html.fromstring(page.content)
cleanLink = list()
response = []


links = tree.xpath('//*[@id="manager_register"]/tbody/tr/td/a/@href')
for link in links:
	if 'managers' not in str(link):
		cleanLink.append(link)

print(cleanLink)

for count in range(len(cleanLink)):
	allstar = bool

	page = requests.get('http://www.baseball-reference.com/'+cleanLink[count])
	tree = html.fromstring(page.content)
	playerName = str(tree.xpath('//*[@id="player_name"]/text()'))
	print(playerName)
	if "All-Star Games" in page.content:
		allstar = True
	else:
		allstar = False

	response.append({'Player' : playerName, 'AllStar' : allstar})


with open("baseball-reference.json", 'wb') as outfile:
	json.dump(response, outfile, indent=4)
outfile.close()

	# print(page.content)
