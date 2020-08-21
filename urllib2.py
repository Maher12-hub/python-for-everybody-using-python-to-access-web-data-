from urllib import request
import re
'''
x=request.urlopen('http://data.pr4e.org/romeo.txt')
count={}
for line in x:
    words=line.decode().split()
    for word in words:
        if word not in count.keys():
            count[word]=0
        count[word]+=1
print(count)
'''
x=request.urlopen('http://www.dr-chuck.com/page1.html')
'''
for line in x:
    print(line.decode().strip())
'''


with open('html.txt','w') as wf:
    for line in x:
        wf.write(line.decode().strip())
file=open('html.txt','r')
text=file.read()
result=re.findall(r'<a href=(.*?)>',text)
print(result[0])

