from bs4 import BeautifulSoup
import json
from urllib.request import Request, urlopen
from tqdm import tqdm

def findAllImages(url):
    req = Request(url)
    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    skipped = []
    try:
        title = soup.title.string
    except:
        title = None
    
    div = soup.find('figure', {'id': 'figure-article_1-0'})
    if div != None:
        div2 = div.find('div', {'class': 'primary-image__media'})
        div3 = div2.find('div', {'class': 'img-placeholder'})
        img = div3.find('img')
        links.append(img['src'])
    
    div4 = soup.find('div', {'id': 'article__photo-ribbon_1-0'})
    if div4 != None:
        for a in div4.findAll('a', {'class': 'gallery-photos dialog-link mntl-text-link'}):
            div5 = a.find('div', {'class': 'img-placeholder'})
            img2 = div5.find('img')
            links.append(img2['data-src'])
    else:
        skipped.append(title)
    return links, skipped, title
def storeImageLinks(url):
    links, skipped, title = findAllImages(url)
    temp_dict = {'links': links, 'skipped': skipped, 'title': title}
    return temp_dict
