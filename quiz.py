import re
text='<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
result=re.findall(r'href="(.+)"',text)
#print(result[0])
print(ord('*'))