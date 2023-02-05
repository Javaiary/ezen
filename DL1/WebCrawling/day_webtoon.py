from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = 'https://comic.naver.com/webtoon/weekday'

# url 페이지에 접속하여 데이터를 가져옴
response = urlopen(myurl)
print(type(response))

# BeautifulSoup()을 이용해서 데이터를 파싱
soup = BeautifulSoup(response, 'html.parser')

# BeautifulSOup 객체를 들여쓰기 형태로 출력
# print(soup.prettify())

title =soup.find("title").string
print(title)
