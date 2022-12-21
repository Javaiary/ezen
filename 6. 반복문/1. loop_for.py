'''
    for 변수 in 시퀀스 자료 :
        명령문
    예) for a in [1,2,3,4]
        print(a)

    * 순서가 있는 자료형
    - 리스트, 문자열, range객체, 튜플, 딕셔너리

    *range(10) : 0~9까지 숫자를 포함하는 range 객체를 생성해 줌
 '''

#리스트 사용
champions = ["티모","이즈리얼","레오나","리신","쉬바나"]

for champion in champions:
    print("선택한 챔피언은 ", champion, "입니다.", sep='')

#문자열 사용
message ="나는 할 수 있어! 화이팅 힘내 뭐해"
for word in message:
    print(word)

#range 객체 사용
x= range(10)

for i in x:
    print(i)

# range(시작, 끝 +1, 단계)
for i in range(1,10,2):
    print(i)