import json
from urllib import request
import urllib.parse
import urllib.error
serviceurl='https://maps.googleapis.com/maps/api/geocode/json?'
key='&key=AIzaSyBUW_7ZtfCeyayLotkY0CAYYKJORiTkrks'
while True:
    address=input('enter location:')
    if len(address)<1:
        break
    url=serviceurl+urllib.parse.urlencode({'address':address})+key
    print('retrieving:',url)
    uo=request.urlopen(url)
    data=uo.read().decode()
    print(data)
    try:
        js=json.loads(data)
    except:
        js=None
    if not js or js['status']!='ok' or 'status' not in js:
        print('failed to retireve:')
        continue
    