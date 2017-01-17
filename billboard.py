from lxml import html
import requests
from bs4 import BeautifulSoup
import datetime
import json


today = str(datetime.datetime.now()).split(' ')


page = requests.get('http://www.billboard.com/charts/')
tree = html.fromstring(page.content)
links = tree.xpath('//span[@class="field-content"]/a/@href')
categories = tree.xpath('//span[@class="field-content"]/a/text()')
print links, categories

for count in range(len(links)):
	print today
	page = requests.get('http://www.billboard.com'+links[count])
	tree = html.fromstring(page.content)
	soup = BeautifulSoup(page.content, 'html.parser')
	# songs = soup.find_all('h2')
	songs = zip(tree.xpath('//h2[@class="chart-row__song"]/text()'), tree.xpath('//span[@class="chart-row__current-week"]/text()'))
	print categories[count] + "\n"   , songs  ,  "\n"  + "\n"
	# with open(page, 'wb') as outfile:
	#     json.dump(songs, outfile)


	# print(page.content)
