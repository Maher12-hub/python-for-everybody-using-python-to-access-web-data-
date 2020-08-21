import json
input='''[
    {
       "name":"Maher",
       "id":"1602155"
    },
    {
        "name":"Nitu",
        "id":"1602156"
    }
    ]'''
info=json.loads(input)
for item in info:
    print('Name',item['name'])
    print('id',item['id'])
    print('\n')