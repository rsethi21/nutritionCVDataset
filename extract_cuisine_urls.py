from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request('https://www.allrecipes.com/cuisine-a-z-6740455')
html_page = urlopen(req)
def extract_cuisines(html, max_count):
    soup = BeautifulSoup(html, 'html.parser')
    count = 0
    links = []
    for div in soup.findAll('div', {'class': "alphabetical-list__group"}):
        print('accessed div')
        for ul in div.findAll('ul', {"class": "loc link-list"}):
            print('accessed ul')
            for li in ul.findAll('li', {'class': "comp link-list__item"}):
                print('accessed li')
                link = li.find('a')                
                links.append(link['href'])
                count+=1
                if count == max_count:
                    return links
    return links

links = extract_cuisines(html_page, 1)
print(links)

