import re
#hand=open('mbox-short.txt')
#for line in hand:
 #   line=line.rstrip()
  #  if re.search('^From:',line):
   #     print(line)
#x='my 2 favorite roll is 1602155 1602154'
#matches=re.findall(r'\d+',x)
#print(matches)
#x='From:using the:charecter'
#match=re.findall(r'^F.+:',x)
#match=re.findall(r'^F.+?:',x)
#print(match)
#x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#match=re.findall(r'\S+@\S+',x)
#print(match)
#with open('mbox-short.txt','r') as rf:
 #  text=rf.read()
  # match=re.findall(r'\S+@\S+',text)
  # match=re.findall(r'^From .*@([^ ]+)',text)
   #print(match)

#x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#match=re.findall(r'@([^ ]+)',x)
#match=re.findall(r'^From .*@([^ ]+)',x)
#print(match)
hand=open('mbox-short.txt')
num_list=[]
for line in hand:
   line=line.rstrip()
   result=re.findall(r'^X-DSPAM-Confidence:\s+([0-9.]+)',line)
   
   if len(result)!=1:
          continue
   num=float(result[0])
   num_list.append(num)
print('maximum:',max(num_list))