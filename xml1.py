import xml.etree.ElementTree as ET

data='''
<person> 
     <name>chuck</name>
     <phone type='intl'>+123744848 </phone>
     <email hide='yes'/>




</person>



'''
tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('phone:',tree.find('phone').text)
print('attr:',tree.find('email').get('hide'))