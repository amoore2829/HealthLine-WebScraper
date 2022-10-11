#Web scraper that takes the article titles from healthline.com/sleep and prints them out

import requests 
from bs4 import BeautifulSoup as bs

url = 'https://www.healthline.com/sleep/routines'
req = requests.get(url)

soup = bs(req.text, 'html.parser')
title = soup.find_all('a', {'data-testid':'title-link'})

for t in title:
    print(t.getText())

