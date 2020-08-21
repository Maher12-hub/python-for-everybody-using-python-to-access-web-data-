import json
from urllib import request
import urllib.parse
import urllib.error
url='http://py4e-data.dr-chuck.net/comments_834592.json'
uo=request.urlopen(url)
data=uo.read()
js=json.loads(data)
sum=0
for item in js['comments']:
   count=item['count']
   sum+=int(count)
print(sum)