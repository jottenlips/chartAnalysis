# http://www.espn.com/nhl/statistics
# //*[@id="my-players-table"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/a
# //*[@id="my-players-table"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/a
from lxml import html
import requests
import json
# from bs4 import BeautifulSoup
# players/a/alstowa01.shtml?redir


# //*[@id="my-players-table"]/div[1]/div[1]/div[2]/table/tbody

# //*[@id="my-players-table"]/div[1]/div[2]/div/table/tbody
# //*[@id="my-players-table"]/div[1]
# //*[@id="my-players-table"]/div[1]/div[3]/div/table/tbody


# page = requests.get('http://www.espn.com/nhl/statistics')
# tree = html.fromstring(page.content)
# cleanLink = list()
# response = []
#
# linkTitles = tree.xpath('//*/div[@class="mod-content"]//*/a/text()')
# links = tree.xpath('//*/div[@class="mod-content"]//*/a/@href')
# print(links)



page = requests.get('http://www.espn.com/nhl/stats/dailyleaders')
tree = html.fromstring(page.content)
cleanLink = list()
response = []

linkTitles = tree.xpath('//*[@id="my-players-table"]/div[1]/div[1]/table[2]//*/td[2]/a/text()')
links = tree.xpath('//*[@id="my-players-table"]/div[1]/div[1]/table[2]//*/td[2]/a/@href')
print(linkTitles, len(links))


# with open("baseball-reference.json", 'wb') as outfile:
# 	json.dump(response, outfile, indent=4)
# outfile.close()

	# print(page.content)
