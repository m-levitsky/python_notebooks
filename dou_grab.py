from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = None

cat_url = input('Enter category (e.g. Python) or skip to view all: ')
if len(cat_url) < 1: url = "https://jobs.dou.ua/vacancies/"
else:
    srv_url = "https://jobs.dou.ua/vacancies/?category="
    url = srv_url+cat_url

search = input('Search for (e.g. Junior): ')
if len(search) < 1: search = ''

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

links = list()
positions = list()
companies = list()

for tag in tags:
    link = tag.get('href', None)

    if re.search("vacancies/[0-9+]", link):
        links.append(link)
        positions.append(tag.text)
        nlink = link.split("/")
        companies.append(nlink[4])

count = len(links)
success = False
res_count = 0

for i in range(count):
    if search in positions[i]:
        print("\n\n", positions[i], "at", companies[i])
        print(links[i])
        success = True
        res_count += 1


if not success: print("Nothing was found")
else: print("\n\nFound", res_count, "vacancies")
