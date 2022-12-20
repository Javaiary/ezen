# 비만도 계산기를  만들어 보시오.

'''
예시)

    BMI 계산기 입니다.
    신장: (입력)
    몸무게: (입력)
    BMI:

'''

print("BMI 계산기 입니다.")
height = float(input("신장(m) : "))
weight = float(input("몸무게(kg) : "))
print("BMI : ", weight/(height**2))