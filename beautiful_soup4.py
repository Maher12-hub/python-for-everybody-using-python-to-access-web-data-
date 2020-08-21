from bs4 import BeautifulSoup
import requests
from urllib import request
'''
with open('simple.html','r') as rf:
    soup=BeautifulSoup(rf,'lxml')

#match=soup.title
#match=soup.title.text
#match=soup.div
#match=soup.find('div',class_='footer')
article=soup.find('div',class_='article')
headlines=article.h2.a.text
#print(headlines)
#print(article)
summary=article.p.text
print(summary)
'''
'''
for article in soup.find_all('div',class_='article'):
    headlines=article.h2.a.text
    print(headlines)

    summary=article.p.text
    print(summary)
    print('\n')
'''
text=request.urlopen('https://coreyms.com/')
with open('corey.html','w') as wf:
    for line in text:
        wf.write(line.decode())
with open('corey.html','r') as rf:
        soup=BeautifulSoup(rf,'lxml')
article=soup.find('article')
#print(article.prettify())
'''
headline=article.h2.a.text
print(headline)
'''
'''
link=article.find('span',class_='entry-comments-link')
link_match=link.a
print(link_match)
'''
'''
summary=article.find('div',class_='entry-content')
summary_match=summary.p.text
print(summary_match)
'''
'''
vid_src=article.find('iframe',class_='youtube-player')['src']

vid_id=vid_src.split('/')[4]
vid_id=vid_id.split('?')[0]
yt_link=f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
'''
#print(article.prettify())
for article in soup.find_all('article'):
    headline=article.h2.a.text
    print(headline)

    summary=article.find('div',class_='entry-content').p.text
    print(summary)

    try:
       vid_src=article.find('iframe',class_='youtube-player')['src']
       vid_id=vid_src.split('/')[4]
       vid_id=vid_id.split('?')[0]
       yt_link=f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link=None
    print(yt_link)
    print('\n')

