import xml.etree.ElementTree as ET
from urllib import request
xml=request.urlopen('http://py4e-data.dr-chuck.net/comments_834591.xml').read()
tree=ET.fromstring(xml)
sum=0
for item in tree.findall('comments/comment'):
        num=item.find('count').text
        num=int(num)
        sum+=num
print(sum)