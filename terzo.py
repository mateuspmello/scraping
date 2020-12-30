from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

#obtendo apenas links do texto
def getLinks(link):
    html = urlopen(f"https://en.wikipedia.org{link}")
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all(
        'a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = []
# links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    getLinks(newArticle)
         

#obtendo links não repetidos
pages = set()
def getLinksNaoRepetidos(link):
    global pages
    html = urlopen(f"https://en.wikipedia.org{link}")
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

# getLinksNaoRepetidos('')

#obtendo titulo e primeiro paragrafo
pgs = set()
def getTitleFirstParagraph(link):
    html = urlopen(f"https://en.wikipedia.org{link}")
    bs = BeautifulSoup(html, 'html.parser')
    print(bs.h1.get_text())
    firstP = bs.find_all('p')
    print(firstP[1].get_text())

    for link in bs.find_all('a', href=re.compile('^(/wiki)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pgs:
                newLink = link.attrs['href']
                pgs.add(newLink)
                getTitleFirstParagraph(newLink)

getTitleFirstParagraph('/wiki/Florianopolis')         