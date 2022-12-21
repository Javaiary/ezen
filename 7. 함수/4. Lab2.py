'''
    로또 예상번호 추출 프로그램을 구현하려고 합니다.
    다음 조건에 따라 프로그램을 완성해 보시오.
        1) 로또 번호를 6개를 생성한다
        2) 로또 번호는 1~45까지의 랜덤한 번호이다.
        3) 6개의 숫자 모두 중복이 없어야 한다.
        4) getRandomNumber() 함수를 사용해서 구현한다.

        출력 예) 1 8 11 13 26 42

        - 리스트, 반복문, 조건문
'''

import random
def getRandomNumber():
    number = random.randint(1,45)
    return number

lotto=[]
while len(lotto) < 6 :
    x= getRandomNumber()
    if x not in lotto:
        lotto.append(x)

lotto.sort()
for n in lotto:
    print(n, end=" ")

#-----------------------------------
print()
lotto_num =[]

count=0
while True:
    if count >5:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count+=1

lotto_num.sort()
for x in lotto_num:
    print(x, end=" ")