import json
from tqdm import tqdm
import recipesByNationality as rbn
import allImages as aI
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input json with nationality dictionary (assumes stored under links keywork)", required=True)
parser.add_argument("-o", "--output", help="output json to store recipe dictionaries", required=True)
args = parser.parse_args()

filePath = args.input

with open(filePath, 'r') as file:
    nationalityDict = json.load(file)

nationalityLinks = nationalityDict['links']

finalDictionary = {}

for link in tqdm(nationalityLinks, desc='Nationalities'):
    recipeDictionary = rbn.store_links(link)
    recipeLinks = recipeDictionary['links']
    finalDictionary[recipeDictionary['title']] = []
    for rlink in tqdm(recipeLinks, desc=f'Recipes'):
        imageDictionary = aI.storeImageLinks(rlink['recipe_link'])
        finalDictionary[recipeDictionary['title']].append(imageDictionary)

outPath = args.output

with open(outPath, 'w') as outFile:
    json.dump(finalDictionary, outFile)
