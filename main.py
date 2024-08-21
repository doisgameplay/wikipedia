import requests
from bs4 import BeautifulSoup



def getLinksFromPage(url) ->list:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    rawTexts = soup.find_all('p')
    links = []
    
    for paragraph in rawTexts:
        paragraphLinks = paragraph.find_all('a', href = True)
        for link in paragraphLinks:
            if '/wiki/' == link['href'][:6]:
                links.append(link['href'])
    
    return links 
    

def getLinksFromLayer(currentLayer, objective) ->dict :
    newLayer = {}
    for path,links in currentLayer.items():
       for url in links:
        link = 'https://en.wikipedia.org' + url
        newWay = url.split('/')[-1]
        if newWay == objective:
            print(f'\n\n{path} | {newWay}') 
            return None
        newLayer[f'{path} | {newWay}'] = getLinksFromPage(link)
        print(f'\n{path} | {newWay}')

    getLinksFromLayer(newLayer, objective)
    return newLayer   


def central(firstUrl, objective):
    currentLayer = {}
    currentLayer[firstUrl.split('/')[-1]] = getLinksFromPage(firstUrl)
    
    currentLayer = getLinksFromLayer(currentLayer, objective)

    
    

url = "https://en.wikipedia.org/wiki/Advanced_Tactical_Fighter"

central(url, 'Jet_aircraft')
