from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json


def extract_cuisines(url):
    req = Request(url)
    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    # links = []
    # for div in soup.findAll('div', {'class': "alphabetical-list__group"}):
    #     for ul in div.findAll('ul', {"class": "loc link-list"}):
    #         for li in ul.findAll('li', {'class': "comp link-list__item"}):
    #             link = li.find('a')
    #             links.append(link['href'])
    return None # links
def store_links(url, name):
    links = extract_cuisines(url)
    with open(f'{name}.json', 'w') as file:
        json.dump({'url': url, 'links': links}, file)

extract_cuisines("https://www.allrecipes.com/recipes/732/us-recipes/amish-and-mennonite/")
