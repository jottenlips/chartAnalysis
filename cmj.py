# https://www.cmj.com/category/charts/
# https://www.cmj.com/cmj-year-end-charts-2016-radio-200/
from lxml import html
import requests
from bs4 import BeautifulSoup
import datetime
import json

today = str(datetime.datetime.now()).split(' ')


page = requests.get('https://www.cmj.com/category/charts/')
tree = html.fromstring(page.content)
links = tree.xpath('//span/a/@href')
# categories = tree.xpath('//span[@class="field-content"]/a/text()')
print(links)

page = requests.get('https://www.cmj.com/cmj-year-end-charts-2016-radio-200/')
tree = html.fromstring(page.content)
links = tree.xpath('*//td/')
print(links)
