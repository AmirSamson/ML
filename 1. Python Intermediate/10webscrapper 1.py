
# the beautiful soup package:::::   ```` python -m pip install beautifulsoup4 ````

import requests
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/"
response = requests.get(url)
html = response.content 
# print(html)
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_="btn-md mb-1.5 mr-[6px] flex items-center w-fit float-left btn-secondary")

for a_tag in a_tags:
    print(a_tag.get_text())

####### Challenge:
    # use map to extract all the titles:

titles = list(map(lambda a_tag: a_tag.get_text() , a_tags))
print(titles)