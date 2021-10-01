import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr ' )
# 아래 빈 칸('')을 채워보세요
# 아래 코드에 빈 칸을 채워서 순위 / 곡 제목 / 가수를 스크래핑해 출력하면 됩니다.
# rank = soup.select_one('trs'.text)
for i in trs:
    rank = i.select_one('td.number').text[0:2].strip()
    title = i.select_one('a.title.ellipsis').text.strip()
    singer =i.select_one('a.artist.ellipsis').text
    print(rank, title, singer)

#순위 tr > td.number
#제목 tr > td.info > a.title.ellipsis
#가수 tr > td.info > a.artist.ellipsis


# # 아래 빈 칸('')을 채워보세요
# for tr in trs:
#     rank = tr.select_one('').text[0:2].strip()
#     title = tr.select_one('').text.strip()
#     artist = tr.select_one('').text
#     print(rank, title, artist)






# # movies = soup.select('#old_content > table > tbody > tr')
# movies = soup.select('#old_content > table > tbody > tr')
# # for i in moives:
# for i in movies:
#     a_tag = i.select_one('td.title > div > a')
#     if a_tag is not None:
#         # a의 text를 찍어본다.
#         print(a_tag.text)
