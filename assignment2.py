from urllib import request
import urllib.parse
import urllib.error
import json
api_key=False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
params={}
address=input('enter address:')
params['address']=address
if api_key is not False: 
    params['key'] = api_key
url=serviceurl+urllib.parse.urlencode(params)
print('retriving url:',url)
uo=request.urlopen(url)
data=uo.read().decode()
print('retrieved',len(data),'charecters')
try:
    js=json.loads(data)
except:
    js=None
print(data)
placeId = js['results'][0]['place_id']
print('Place id', placeId)