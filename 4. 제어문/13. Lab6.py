'''
    if
    if-else
    if-elif
    if-elif-else

    규황이는 강의를 8시간동안 들으니, 배가 너무 고파 저녁을 먹기로 하였습니다.
    규황이가 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력해주는 프로그램을 작성해 보시오.

    조건 ) 20000원 이상 : 치킨, 10000원 이상 : 떡볶이, 3000원 이상: 편의점 김밥, 그 외 : 굶어요

'''

balance = int(input("현재 소지 금액(원) ="))
if balance >= 20000 :
    print("치킨")
elif balance >= 10000:
    print("떡볶이")
elif balance >=3000:
    print("편의점 김밥")
else:
    print("이규황 그지")