from urllib import request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
html=request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html').read()
soup=BeautifulSoup(html,'html.parser')
li=[]
li1=[]
li2=[]
li3=[]
li4=[]
for link in soup.find_all('a'):
        li.append(link.get('href'))
a=li[2]
print('retriving:',a)
html=request.urlopen(a).read()
soup=BeautifulSoup(html,'html.parser')
for link in soup.find_all('a'):
        li1.append(link.get('href'))
b=li1[2]
print('retriving:',b)
html=request.urlopen(b).read()
soup=BeautifulSoup(html,'html.parser')
for link in soup.find_all('a'):
        li2.append(link.get('href'))
c=li2[2]
print('retriving:',c)
html=request.urlopen(c).read()
soup=BeautifulSoup(html,'html.parser')

for link in soup.find_all('a'):
        li3.append(link.get('href'))
d=li3[2]
print('retriving:',d)
