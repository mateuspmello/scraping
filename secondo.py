from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find_all(['span'],{'class':'green'})

for name in nameList:
    print(name.get_text())

#busca dentro da tabela apenas os filhos e não os descendentes
for child in bs.find('table', {'id':'giftList'}):
    print(child)

