import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

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
    doc = {
        'rank': rank,
        'title': title,
        'singer': singer  # DB에는 숫자처럼 생긴 문자열 형태로 저장됩니다.
    }
    db.musics.insert_one(doc)