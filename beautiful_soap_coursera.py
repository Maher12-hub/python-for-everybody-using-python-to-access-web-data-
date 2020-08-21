from urllib import request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
url='http://www.dr-chuck.com/page1.html'
html=request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))