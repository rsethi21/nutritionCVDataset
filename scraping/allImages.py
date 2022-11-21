from bs4 import BeautifulSoup
import json
from urllib.request import Request, urlopen

def findAllImages(url):
    req = Request(url)
    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    title = soup.title.string    
    div = soup.find('figure', {'id': 'figure-article_1-0'})
    div2 = div.find('div', {'class': 'primary-image__media'})
    div3 = div2.find('div', {'class': 'img-placeholder'})
    img = div3.find('img')
    links.append(img['src'])
    
    div4 = soup.find('div', {'class': 'comp total-photos28 article__photo-ribbon mntl-block'})
    for a in div4.findAll('a', {'class': 'gallery-photos dialog-link mntl-text-link'}):
        div5 = a.find('div', {'class': 'img-placeholder'})
        img2 = div5.find('img')
        links.append(img2['data-src'])
    return links, title
def storeImageLinks(url, name):
    url = url
    links, title = findAllImages(url)
    with open(f'{name}.json', 'w') as file:
        json.dump({'url': url, 'links': links, 'title': title}, file)

storeImageLinks("https://www.allrecipes.com/recipe/13743/pennsylvania-dutch-pickled-beets-and-eggs/", "exampleAmishCuisine")
