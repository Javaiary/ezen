# 주석(comments) // 실행 ctrl + shift + f10
# 숫자형 - 숫자 데이터, 정수형, 실수형
#       - "(큰 따옴표) 또는 '(작은 따옴표)로 문자열의 시작과 끝을 나타냄
#       - ' " " '
#       - " ' ' "
#       """
#           여러 줄에 걸쳐 문자열 표현 가능
#       """
#       - indexing & slicing string

# 불린형 - 참 또는 거짓
# None == null
#       - 아무런 값을 갖지 않을 때 사용
#         해당 변수가 초기값을 갖지 않게 하여 생성할 때 사용
#           - 문자열의 각 문자는 순서가 있음
#           - 이 때 각 문자열의 순서를 인덱스라고 함.
#           - 첫 번째 시작 문자의 순서는 0으로 시작 ( not 1)
#           - -1 인덱스 : 가장 마지막 인덱스, -2 : 마지막에서 두 번째 인덱스를 의미
#           - 문자열 slicing
#               - 인덱스가 하나의 문자만을 추출함
#               - slicing은 부분 문자열을 추출함
#               - [시작 : 끝]에 해당하는 부분 문자열을 추출함
#           - 문자열 함수
#               -


'''
print()
    - , 로 여러 변수를 나열하면 한 줄로 출력
    - 기본적으론느 한 칸 띄어쓰기 후 출력
'''


print(1, 3, 0, -1, sep=" ")
print(1.1, 3.1, 0, -1.4)
print("침묵은 과학입니다.")
print('현대 침묵의 경이로움')
print('"노이즈 캔슬링"')
print("'주변소리듣기'")
print(True)

a= 10
b = 11.4
print(a, b, 10, 100, sep = '*', end='||')
print(a, b)

print(type(a))
print(type(b))

c= None
print(c)

d='''
    hello
        ezen
    '''
e = """
    hello
    world!
"""
print(d)
print(e)

f='hello world'
print(f[10])
print(f[0])
print(f[-1])     #뒤에서부터 인덱싱
print(f[-11])
#print(f[11])   # 범위를 넘어갈 경우 에러 발생
print(f[0:11])
print(f[0:1])
print(f[:5])
print(f[3:])
print(f[:])

print(f.upper())
print(f.replace('h', 'j'))

temperature = 15.5
prob = 50.0

g= '오늘 기온 {}도 이고, 비 올 확률은 {}% 입니다. '.format(temperature,prob)
print(g)

