from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json

url = 'https://www.allrecipes.com/cuisine-a-z-6740455'
req = Request(url)
html_page = urlopen(req)
def extract_cuisines(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for div in soup.findAll('div', {'class': "alphabetical-list__group"}):
        for ul in div.findAll('ul', {"class": "loc link-list"}):
            for li in ul.findAll('li', {'class': "comp link-list__item"}):
                link = li.find('a')                
                links.append(link['href'])
    return links

links = extract_cuisines(html_page)
with open('listWorldCuisines', 'w') as file:
    json.dump({'url': url, 'links': links}, file)
