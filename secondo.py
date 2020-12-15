from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find_all(['span'],{'class':'green'})

title = bs.find_all(class_='text', id="title")

# for name in nameList:
    # print(name.get_text())


for t in title:
    print(t)
