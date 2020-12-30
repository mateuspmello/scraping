from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())
allExtLinks = set()
allIntLinks = set()

#obtem uma lista de todos os lunks internos encontrados em uma página
def getInternalLinks(bs, includeUrl):
    includeUrl = f'{urlparse(includeUrl).scheme}://{urlparse(includeUrl).netloc}'
    internalLinks = []
    #Encontra todos os links que começam com "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    #Encontra todos os links que começam com "http" e que não contenham o URL atual
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking arounf the site for one')
        domain = f'{urlparse(startingPage).scheme}://{urlparse(startingPage).netloc}'
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print(f"Random external link is {externalLink}")
    followExternalOnly(externalLink)

# followExternalOnly('http://google.com')

def getAllExternalLinks(siteUrl):

    html = urlopen(siteUrl)
    domain = f'{urlparse(siteUrl).scheme}://{urlparse(siteUrl).netloc}'
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
        
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            print(link)

# allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://google.com')
    
 
# print(allExtLinks)
