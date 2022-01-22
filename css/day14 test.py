#https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=bts

from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
date=str(datetime.now())

date=date[:date.rfind(":")].replace(" ","_")
date=date.replace(":","시")+"분"

url="https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={}"
search=input("검색어:")
req=requests.get(url.format(search))
news_num=input("기사갯수:")
soup=BeautifulSoup(req.text,'html.parser')

list=soup.find_all('a',{'class':"news_tit"})
idx=0
dic={}
for i in list[:int(news_num)]:
    dic[idx]={'url':i.attrs['href'],'title':i.attrs['title']}
    idx+=1

df=pd.DataFrame(dic).T
fn='네이버뉴스_{}_{}.xlsx'.format(search, date)
df.to_excel(fn)


search=input("검색어:")
url2="https://kin.naver.com/search/list.naver?query={}"
res=requests.get(url2.format(search))
soup=BeautifulSoup(res.text,'html.parser')
title_list=soup.find_all('a',{'class':"_nclicks:kin.txt _searchListTitleAnchor"})
title=[]
for i in range(10):
    title.append(title_list[i].text)
print(title)

import urllib

url="https://music.bugs.co.kr/chart/track/week/total"
res=urllib.request.urlopen(url)
soup=BeautifulSoup(res,'html.parser')
table=soup.find('table',{'class':'list trackList byChart'})
title=table.find_all('p',{'class':'title'})
artist=table.find_all('p',{'class':'artist'})
b=[]
c=[]
for i in range(len(artist)):
    c.append(artist[int(i)].a.attrs['title'])

for i in range(len(title)):
    b.append(title[int(i)].a.attrs['title'])

d={x:y for x,y in zip(b[:10],c[:10])}

print(d)


