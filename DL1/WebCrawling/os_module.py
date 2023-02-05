'''
    * os 모듈과 예외 처리
        - os.mkdir (폴더)
        - os.path.join() : str1과 str2의 문자열을 연결하여 파일이나 폴더에 대한
                           전체 경로를 생성해 줌
    * 예외 처리
        - try:  예외 발생 가능성이 있는 코드
          except: 예외 발생시 처리할 내용
          finally: 예외 여부와 관계 없이 항상 실행될 내용
'''
import os
myfolder='c:\\Users\\Administrator\\Desktop'

newpath = os.path.join(myfolder, 'Cruz')

try:
    os.mkdir(path=newpath)
    for idx in range(1,11):
        newfile = os.path.join(newpath,'bluefolder' +str(idx).zfill(2))
        os.mkdir(path=newfile)
except FileExistsError:
    print("디렉터리가 이미 존재합니다.")

print('finished')