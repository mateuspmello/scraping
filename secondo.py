from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find_all(['span'],{'class':'green'})

# for name in nameList:
#     print(name.get_text())

#busca dentro da tabela apenas os filhos e não os descendentes (tras o titulo)
for child in bs.find('table', {'id':'giftList'}):
    print(child)

#busca sem o titulo
for sibiling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibiling)