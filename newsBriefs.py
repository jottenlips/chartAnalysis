# http://hosted.ap.org/dynamic/fronts/HOME?SITE=AP&SECTION=HOME
from lxml import html
import requests
from bs4 import BeautifulSoup
import datetime
import json



#Using lxml
page = requests.get('http://hosted.ap.org/dynamic/fronts/HOME?SITE=AP&SECTION=HOME')
tree = html.fromstring(page.content)
links = tree.xpath('//span/a[@class="ap-newsbriefitem-a"]/@href')
titles = tree.xpath('//span/a[@class="ap-newsbriefitem-a"]/text()')
briefs = tree.xpath('//span[@class="topheadlinebody"]/text()')

print(links,"\n" ,titles, "\n", briefs)


# BeautifulSoup way

urlRequest = 'http://hosted.ap.org/dynamic/fronts/HOME?SITE=AP&SECTION=HOME'
page = requests.get(urlRequest)
soup = BeautifulSoup(page.content,'lxml')
position = soup.find("div", class_="ap-newsbriefitem")
headline = position.find('a').string
brief = position.find('span',class_="topheadlinebody").string
apOffice = brief.split(' (AP) ')[0]
fullStory = 'hosted.ap.org' + position.find('a').get("href")
# ctime = fullStory.split("CTIME=")[1]
# links = soup.find_all('a',class_="ap-newsbriefitem-a").get("href")

print("--------acree-----------\n",headline,brief,apOffice,fullStory)
