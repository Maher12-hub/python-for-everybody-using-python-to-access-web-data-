#from urllib import request
#import urllib.parsecls
#x=request.urlopen('https://www.google.com')
#print(x.read())
#from urllib import request
#import urllib.parse
#url='http://pythonprogramming.net'
#values={'q':'Tutorial+Series+Matched'}
#data=urllib.parse.urlencode(values)
#data=data.encode('utf-8')
#req=urllib.request.Request(url,data)
#resp=urllib.request.urlopen(req)
#respdata=resp.read()
#print(respdata)

#import urllib.request
#x=urllib.request.urlopen('http://www.google.com')
#print(x.read())


import urllib.request
import urllib.parse
import re
url='http://pythonprogramming.net'
value={'q':'Practical+Machine+Learning+Tutorial+with+Python+Introduction'}
data=urllib.parse.urlencode(value)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
respdata=resp.read()
# <li><a class="grey-text text-lighten-3" href="https://instagram.com/sentdex">Instagram</a></li>
result=re.findall(r'<li><a class=(.*?) href=(.*?)>.*?</a></li>',str(respdata),flags=re.S)
print(result[0])
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0
'''
from urllib import request
import urllib.parse
try:
    url='https://www.google.com/search?q=test'
    headers={}
    headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
    req=request.Request(url,headers=headers)
    res=request.urlopen(req)
    respdata=res.read()
    html_data_sunny=open('html_data_sunny.txt','w')
    html_data_sunny.write(str(respdata))
    html_data_sunny.close()
except Exception as e:
    print(str(e))
'''

