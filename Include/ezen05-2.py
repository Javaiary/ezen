# ezen05-2
'''
    참/거짓 자료형
        - 거짓(False) : 0, 비어있는 리스트/튜플/ 사전, None 등
        - 참(True) : 이외에 실제 의미 있는 값들

        - 7 -> 참
          1 -> 참
          0 -> 거짓
          "hello world" -> 참
          "" -> 거짓
          [1,2,3] -> 참
          [] -> 거짓
          () -> 거짓
'''
print(bool(7))
print(bool(1))
print(bool(0))
print(bool("hello world"))
print(bool(""))
print(bool([1,2,3]))
print(bool([]))
print(bool(()))

'''
    반복문
        for 원소 in 시퀀스데이터:
            원소를 처리하는 코드
'''

for x in [1,2,3,4,5,6,7,8,9]: 
    print(x)

print()
result=0
for i in range(1,51): # 1부터 50까지
    result+=i
print(result)

# 1부터 50까지의 수 중에서 10의 배수만 더하는 프로그램을 작성하시오.
result=0
for i in range(1,51):
    if( i % 10 == 0 ):
        result+=i
print(result)

# enumerate()
name_list = ['이순신', '손흥민', '이도']
for i, element in enumerate(name_list) :
    print(i, element)

print()
# 구구단
for i in range(1, 10) :
    for j in range(1, 10):
        print(i ,"X", j ,"=", i*j)

'''
    리스트 2 개가 있습니다.
    리스트의 중앙값을 출력하는 코드를 작성하시오.
    단, 중앙값은 리스트가 홀수개의 숫자에 대해서는 크기 순서대로 가장 가운데 있는 값이다.
    리스트가 짝수개의 숫자에 대해서는 가장 가운데 있는 두 숫자의 평균이다.
'''
num1 =[10,100,24,5,11,55]
num2 = [3,2,677,99,11,6,1001]

num1.sort()
num2.sort()
print(num1)
print(num2)

num1len=len(num1)
num2len=len(num2)

print(num1[(num1len//2)])
if num1len % 2 != 0 :
    print("num1의 중앙값: ", num1[(num1len//2)])
else:
    print("num1의 중앙값: ", (num1[num1len//2-1]+ num1[num1len//2])/2 )

if num2len % 2 != 0 :
    print("num2의 중앙값: ", num2[(num2len//2)])
else:
    print("num2의 중앙값: ", (num2[num2len//2-1]+ num2[num2len//2])/2 )

