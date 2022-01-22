



"https://ssl.pstatic.net/sstatic/search/nlogo/20220119214419.png"



import urllib.request #모듈 읽어오기
url="https://ssl.pstatic.net/sstatic/search/nlogo/20220119214419.png"


#이미지를 다운로드 받아 16진수 형태로 출력
# res=urllib.request.urlopen(url)
# data=res.read()
# print(data)




# urllib.request.urlretrieve(url,"mynaver.png") #이미지 저장
# print("저장되었습니다")



#url로부터 이미지를 다운로드받아 이미지 형태로 출력
# res=urllib.request.urlopen(url)
# img=res.read()
# with open("mynaver2.png", mode="wb") as f:
#     f.write(img)
#     print("저장되었습니다")
#
#
#
# import urllib.parse
# import urllib.request
# #스크래핑 대상이 1개라면 아래와 같이 full address를 기술
# # url="https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
#
# print(urllib.parse.urlencode({"stnId":"108"}))
# #urlencode : 딕셔너리 형태로 구성된 데이터를 키 = 값 형태로 변환
#
# #스크래핑 대상이 여러개라면 아래와 같이 url에 여러개의 주소를 인코딩한 값을 결합하여 반복적으로 주소 생성
# url="https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# params=urllib.parse.urlencode({"stnId":"108"})
# url=url+"?"+params
#
# res=urllib.request.urlopen(url)
# data=res.read()
# data=data.decode('utf-8')
# #print(data)
#
#
#
# #스크래핑 된 결과로 부터 분석 대상 데이터를 추출
# #html, xml 형식의 데이터는 BeautifulSoup 도구를 이용하여 분석함
#
# from bs4 import BeautifulSoup
#
# soup=BeautifulSoup(data,'html.parser')
# print(soup)
# print(soup.find("title").string)
# print(soup.find("wf").string)
# res=soup.find_all("wf")
#
# print(len(res))
#
# for i in range(len(res)):
#     print(res[i].string)
#     print("===")
#
# for i in res:
#     print(i.string)
#     print("===")

from bs4 import BeautifulSoup
url="https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
import urllib.parse
import urllib.request
# res=urllib.request.urlopen(url)
# data=res.read()
# soup=BeautifulSoup(data,'html.parser')
# print(soup)


#
# html = """
# <html><body>
#   <ul>
#     <li><a href="http://www.naver.com">naver</a></li>
#     <li><a href="http://www.daum.net">daum</a></li>
#   </ul>
# </body></html>
# """
#
# soup=BeautifulSoup(html,'html.parser')
# links=soup.find_all('a')
# for a in links:
#     print(a.attrs['href'])
#     print(a.string)


from bs4 import BeautifulSoup

f=open("fruit_vegetables.html",encoding='utf-8')
# print(f.read())
soup=BeautifulSoup(f,'html.parser')
# print(soup.select_one('li').string)
# print(soup.find('li').string)
# print(soup.select_one("#ve-list > li[data-lo='us']").string)
#
# print(soup.select("#ve-list > li.black")[0].string)
# print(soup.select("#ve-list > li[data-lo='ko']")[1].string)
#
# print(soup.select("#ve-list > li.black[data-lo='us']")[0].string)
#
# print(soup.select("#main-goods"))
# print(soup.select(".purple"))
#
#
dic={'class':'black','data-lo':'us'}
# print(soup.find('li', dic).string)

print(soup.find(id="ve-list").find("li", dic))

html = """
<html><body>
<div id="meigen">
  <h1>위키북스 도서</h1>
  <ul class="items">
    <li>유니티 게임 이펙트 입문</li>
    <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
    <li>모던 웹사이트 디자인의 정석</li>
  </ul>
</div>
</body></html>
"""

soup=BeautifulSoup(html,'html.parser')

print(soup.select("li")[0].string)
print(soup.select_one("#meigen > ul.items > li").string)


html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p id='title'>웹 페이지를 분석하는 것</p>
  <p id='body'>원하는 부분을 추출하는 것</p>
</body></html>
"""

# soup=BeautifulSoup(html,'html.parser')
# # print(soup.html.body.p.next_sibling.next_sibling) #.next_sibling 한번하면 엔터를 인식함
# print(soup.find(id='title'))
#
# url="https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%ED%99%98%EC%9C%A8"
# import urllib.request
# res=urllib.request.urlopen(url)
#
# soup=BeautifulSoup(res,'html.parser')
# print(soup.select_one("#_cs_foreigninfo > div > div.api_cs_wrap > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.up > strong").string)

#_cs_foreigninfo > div > div.api_cs_wrap > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.up > strong


import urllib.request
from bs4 import BeautifulSoup

f=open("books.html", encoding='utf-8')
soup=BeautifulSoup(f,'html.parser')
print(soup.select_one("#nu").string)
print(soup.select("li")[3].string)
print(soup.select_one("#bible > li[id='nu']").string)
print(soup.html.body.ul.li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string)
print(soup.find(id="nu").string)
