from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def get_title(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'lxml')
        title = bs.body.h1
        return title
    except AttributeError as e:
        return None
    except HTTPError as e:
        return None
    except URLError as e:
        return None


titulo = get_title('http://pythonscraping.com/pages/page1.html')
if titulo == None:
    print('Title not found')
else:
    print(titulo)