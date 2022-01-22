import urllib.request
from bs4 import BeautifulSoup

dg=urllib.request.urlopen("https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC")

dgs=BeautifulSoup(dg,'html.parser')
#
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li:nth-child(1)").string)
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li:nth-child(2)").string)
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li:nth-child(3)").string)
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li:nth-child(6)").string)
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li:nth-child(4) > a").string)
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li:nth-child(5) > a:nth-child(1)").string)
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li:nth-child(7) > a").string)

#
# ddd=dgs.select("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li")
# for i in ddd:
#     book=i.get_text()
#     # num=int(str(book).index("》"))+1
#     print(book)


#
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(54) > li:nth-child(1) > a").string,"졸업")
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(54) > li:nth-child(2)").string,"수료")
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(54) > li:nth-child(3) > a:nth-child(3)").string,"수료")
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(54) > li:nth-child(4) > a").string,"졸업")
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(54) > li:nth-child(5) > a").string,"학사")
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(54) > li:nth-child(6) > a:nth-child(2)",).string,"중퇴")
# print(dgs.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(54) > li:nth-child(7) > a:nth-child(2)").string,"제적")

# poet="https://ko.wikipedia.org/wiki/%ED%95%98%EB%8A%98%EA%B3%BC_%EB%B0%94%EB%9E%8C%EA%B3%BC_%EB%B3%84%EA%B3%BC_%EC%8B%9C"
#
# poet=urllib.request.urlopen("https://ko.wikipedia.org/wiki/%ED%95%98%EB%8A%98%EA%B3%BC_%EB%B0%94%EB%9E%8C%EA%B3%BC_%EB%B3%84%EA%B3%BC_%EC%8B%9C")
# pt=BeautifulSoup(poet,'html.parser')
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(1) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(2) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(3) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(4) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(5) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(6) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(7) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(8) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(9) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(10) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(11) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(12) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(13) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(14) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(15) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(16) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(17) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(18) > a").string)
# print(pt.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(9) > li:nth-child(19) > a").string)
#
# #한줄요약
# for i in range(0,19):
#     print(pt.select("a.extiw")[i].string)
#
# #한줄요약
# for i in range(10):
#     print(dgs.select("#mw-content-text > div.mw-parser-output > ul:nth-child(54) > li > a")[i].string)
#
# #한줄요약실패
# for i in range(4):
#     print(dgs.select("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li > a")[i].string)
#






#
# king = urllib.request.urlopen("https://movie.daum.net/moviedb/main?movieId=118715")
#
# # km=BeautifulSoup(king,'html.parser')
# #
# # print(km.select_one("#mainContent > div > div.box_basic > div.info_detail > div.detail_cont > div:nth-child(2) > dl:nth-child(1) > dd").text)
# url="https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC"
# res=urllib.request.urlopen(url)
# contents=BeautifulSoup(res, 'html.parser')
# books=contents.select("#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li")
#
# print("윤동주 작품목록: ")
# for i in books:
#     book=i.get_text()
#     num=int(str(book).index("》"))+1
#     print(book[:num])
#
#     edu = contents.select("#mw-content-text > div.mw-parser-output > ul:nth-child(54) > li")
#     print("윤동주 학력: ")
#     for i in edu:
#         print(i.get_text())


url="https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC"
res=urllib.request.urlopen(url)
data=res.read()
data=data.decode('utf-8')
soup = BeautifulSoup(data,'html.parser')

for i in range(1,8):
    booktitle="#mw-content-text > div.mw-parser-output > ul:nth-child(49) > li:nth-child("+str(i)+")"
    print(soup.select_one(booktitle).text)