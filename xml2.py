import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
tree=ET.fromstring(input)
for item in tree.findall('users/user'):
    print('Name:',item.find('name').text)
    print('id:',item.find('id').text)
    print('x:',item.get('x'))
    print('\n')
