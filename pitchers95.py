from lxml import html
import requests
import json
# from bs4 import BeautifulSoup

def getThosePitchers(the_year):
	page = requests.get('http://www.baseball-reference.com/leagues/MLB/'+str(the_year)+'-rookies.shtml#pitch')
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
		team = tree.xpath('//*/td[2]/a/text()')[0]
		# //*[@id="pitching_standard.1995.clone"]/td[2]/a
		# //*[@id="pitching_standard.1995.clone"]/td[2]/a
		try:
			playerName = str(tree.xpath('//*[@id="meta"]/div[2]/h1/text()'));
			so = str(tree.xpath('//*[@data-stat="SO"]/text()')[1]);
			ip = tree.xpath('//*[@data-stat="IP"]/text()')[1];
			print(playerName, so, ip, team)
			response.append({'Player' : playerName, 'SO' : so, "IP" : ip, "Team":team})
			with open(str(the_year)+"pitcherStats.json", 'w') as outfile:
				json.dump(response, outfile, indent=4)
			outfile.close();
		except:
			continue

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

def main():
	for i in range(22):
		try:
			getThosePitchers(1993-i)
		except:
			continue
main()
