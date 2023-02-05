'''
    * 크롤링
        1) urllib 라이브러리 이용한 웹 페이지 크롤링
            - urllib.request 모듈
            - urlopen() : 네트워크를 통해 원격 객체를 읽고 메모리에 올리는 역할 수행

'''
import urllib.request       # 라이브러리 읽어들임

#url과 저장 경로 지정하기
url = "https://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg"
savename = "urldownload_webtoon02.png"

# urlopen() 함수 이용하여 다운로드
result = urllib.request.urlopen(url)
# read() 함수 이용해 바이너리 형식으로 변경함
data = result.read()
print('type() : ', type(data))

# 파일로 저장하기
with open(savename, mode="wb") as f:        # 자동 close 됨
    f.write(data)
    print(savename + '파일로 저장되었습니다.')

print('웹에 있는 이미지'+url+'를', end='')
print(savename,"파일로 저장하였습니다.")
