from bs4 import BeautifulSoup
import json
from urllib.request import Request, urlopen
from tqdm import tqdm

def findAllImages(url):
    req = Request(url)
    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    links = []
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
        for a in tqdm(div4.findAll('a', {'class': 'gallery-photos dialog-link mntl-text-link'}), desc='Accessing link of many links...'):
            div5 = a.find('div', {'class': 'img-placeholder'})
            img2 = div5.find('img')
            links.append(img2['data-src'])
    else:
        print('skipped')
    return links, title
def storeImageLinks(fileWithURLs, name):
    listRecipeImages = []
    with open(fileWithURLs, 'r') as file:
        dictionary = json.load(file)
    urls = dictionary['links']
    for url in tqdm(urls, desc='Accessing url...'):
        links, title = findAllImages(url['recipe_link'])
        temp_dict = {'links': links, 'title': title, 'url': url['recipe_link']}
        listRecipeImages.append(temp_dict)
    with open(f'{name}.json', 'w') as file2:
        json.dump({'links': listRecipeImages, 'url': dictionary['url'], 'title': dictionary['title']}, file2)

storeImageLinks("./amishRecipes.json", "amishCuisineImageLinks")
