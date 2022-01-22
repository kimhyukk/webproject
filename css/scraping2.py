# https://movie.naver.com/movie/bi/mi/point.naver?code=187320

import urllib.request
from bs4 import BeautifulSoup

url=urllib.request.urlopen("https://movie.naver.com/movie/bi/mi/point.naver?code=187320")

# soup=BeautifulSoup(url,'html.parser')
#
# for i in range(10):
#     print(soup.select("#_filtered_ment_1"))



#
#
# <a id="pagerTagAnchor1" href="/movie/bi/mi/pointWriteFormList.naver?code=187320&amp;type=after&amp;isActualPointWriteExecute=false&amp;isMileageSubscriptionAlready=false&amp;isMileageSubscriptionReject=false&amp;page=1" onclick="parent.clickcr(this, 'ara.page', '', '', event);"><span class="on">1</span></a>
#
# < a
# id = "pagerTagAnchor2"
# href = "/movie/bi/mi/pointWriteFormList.naver?code=187320&amp;type=after&amp;isActualPointWriteExecute=false&amp;isMileageSubscriptionAlready=false&amp;isMileageSubscriptionReject=false&amp;page=2"
# onclick = "parent.clickcr(this, 'ara.page', '', '', event);" > < span > 2 < / span > < / a >

import requests
# res=requests.get("http://www.google.com")
# print(res) #200 == 정상
# soup=BeautifulSoup(res.content,'html.parser')
# # print(soup)
# r1=soup.find('strong')
# print(r1)

url_pre="https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=187320&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="

id_pre = '_filtered_ment_'
id_list = []
final_data=[]
for page in range(10):
    print(page+1,"페이지\n")
    site=url_pre+str(page+1)
    res=requests.get(site)
    soup=BeautifulSoup(res.content,'html.parser')
    # for i in range(10):
    #     print(soup.select("div.star_score")[i].text)
    scores=soup.find_all("div","star_score")
    score_list=[]
    for i in scores:
        score_list.append(i.get_text())
    # print(score_list)

    for i in range(10):
        id=id_pre+str(i)
        id_list.append(id)

    mydata=[]
    for i in id_list:
        mydata.append(soup.find("span",id=i).get_text())

    for score, line in zip(score_list, mydata):
        final_data.append([score.strip(),line.strip()])

# print(final_data)

import pandas as pd

print(pd.DataFrame(final_data))

