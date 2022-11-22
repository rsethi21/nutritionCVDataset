from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json


def extract_cuisines(url):
    req = Request(url)
    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    title = soup.title.string
    count = 0
    for a in soup.findAll('a', {'class': "comp mntl-card-list-items mntl-document-card mntl-card card card--no-image"}):
        recipe_link = a['href']
        div1 = a.find('div', {'class': 'loc card__top'})
        div2 = div1.find('div', {'class': "card__media mntl-universal-image card__media universal-image__container"})
        div3 = div2.find('div', {'class': "img-placeholder"})
        img = div3.find('img', {'class': 'lazyload card__img universal-image__image'})
        img_link = img['data-src']
        links.append({'recipe_link': recipe_link, 'image_link': img_link})
        count += 1
    print(count)
    return links, title

def store_links(url):
    links, title = extract_cuisines(url)
    return {'url': url, 'links': links, 'title': title}