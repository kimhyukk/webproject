#키워드입력(input)->뉴스기사검색(크롤링)->파일 저장


# 그냥 오미크론 검색 https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%AF%B8%ED%81%AC%EB%A1%A0

# 뉴스에서 오미크론 검색 https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%98%A4%EB%AF%B8%ED%81%AC%EB%A1%A0

# 오미크론 검색 후 뉴스 클릭 https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%98%A4%EB%AF%B8%ED%81%AC%EB%A1%A0

from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re #regular expression; 정규표현식
date=str(datetime.now())

date=date[:date.rfind(":")].replace(" ","_")
date=date.replace(":","시")+"분"
print(date)

query=input("네이버 뉴스 검색어를 입력하세요:")

news_num=int(input("뉴스 몇개를 가져올까요? 개수를 입력하세요: "))
#query=까지 일치 이후 검색어로 변함
news_url="https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}"
req=requests.get(news_url.format(query))
# print(req.text) #text=한글로출력,  contents=16진수값출력
soup=BeautifulSoup(req.text,'html.parser')
#ul태그에 class가 news_list



news_dict={}
idx=0


while idx<news_num:
    table = soup.find('ul', {'class': 'list_news'})
    # table에서 뉴스기사 추출 : li태그 id 가 sp_nws로 시작
    # soup.find_all('li',{id:'sp_nws'})
    #정규표현식 사용하면 쉬움 re.complile
    li_list=table.find_all("li",{"id":re.compile("sp_nws.*")})
    #sp_nws.*은 sp_nws로 시작하면 모두 검색조건을 만족함

    # print(li_list)
    #뉴스 제목 본문 url위치 : div태그 class가 news_area
    area_list=[li.find("div",{'class':'news_area'}) for li in li_list]
    #뉴스제목 : a태그 class가 new_tit
    a_list=[area.find('a',{'class':'news_tit'}) for area in area_list]
    # print(a_list[0])
    #href, title 속성값을 출력하세요
    # #a_list[0].attrs [attrs=속성값 입력하면 그냥나옴]
    # print(a_list[0].attrs)
    # print(a_list[0].attrs['href'])
    # print(a_list[0].attrs) #{'속성명':'속성값',...}
    # print("뉴스 기사 주소 : ", a_list[0].attrs['href'])
    # print("뉴스 기사 제목 : ", a_list[0].attrs['title'])
    for n in a_list[ :news_num]:
        news_dict[idx]={'url':n.attrs['href'],'title':n.attrs['title']}
        idx+=1
print(news_dict)

df=pd.DataFrame(news_dict).T
fn='네이버뉴스_{}_{}.xlsx'.format(query, date)
df.to_excel(fn)

    #
    # print(str(a_list[0])[str(a_list[0]).find('href='):str(a_list[0]).find('onclick')])
    # print(str(a_list[0])[str(a_list[0]).find('title='):str(a_list[0]).find("'>")])






























