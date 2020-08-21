import re
hand=open('actual.txt')
sum=0
final_result=[]
for line in hand:
    line=line.rstrip()
    result=re.findall(r'[0-9]+',line)
    for i in result:
        if len(i)!=0:
            final_result.append(i)
for j in final_result:
    sum+=(int(j))
print(sum)