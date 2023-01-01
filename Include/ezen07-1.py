# ezen07
'''
    1. 함수 정의
    def function_name(parameter):
        code

    2. 함수 호출
    function_name()    
'''

def hello(world):
    print("Hello, ", world)

hello("Trip")

print()

# 함수2
def hello_return(world):
    value = "Hello, " + str(world)
    return value

str = hello_return("Cruise!")
print(str)

# 함수3 (다중리턴)
def func_mul(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 5
    return y1, y2, y3

val1, val2, val3 = func_mul(3)
print(val1, val2, val3)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 5
    return (y1, y2, y3)

tuple = func_mul2(4)
print(tuple, type(tuple), list(tuple))

# 리스트 리턴
def func_mul3(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 5
    return [y1, y2, y3]

lis = func_mul3(6)
print(type(lis), lis)

# 딕셔너리 리턴
def func_mul4(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 5
    return {'re1':y1,'re2': y2,'re3' : y3}

dic = func_mul4(5)
print(type(dic), dic, dic.get('re2'), dic.items(), dic.keys(), dic.values())

print()
# 함수4 (*args, **kwargs)

# *args
def args_func(*args) : # 매개변수명 자유롭게 변경 가능
    for i, v in enumerate(args):
        print('{}'.format(i), v, end=' ')

args_func('home')
print()
args_func('home', 'seoul')
print()
args_func('home', 'seoul', 'korea')

# **kwargs
def args_func2(**kwargs):   # 매개변수명 자유롭게 변경 가능
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v], end =" ")
print()
args_func2(name1='lee')
print()
args_func2(name1='lee',name2='Kem')
print()
args_func2(name1='lee',name2='Kem', name3 = 'park')

print()
# 함수5 - 전체 혼합
def func_ezen(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)

func_ezen(1,2)
print()
func_ezen(1,2,3,4)

func_ezen(10, 20, 'snow', 'snow2', 'snow2', age=30, age2= 31, age3 = 40)

# 함수 6 - 중첩함수
def nested_function(num):
    def func_in_func(num):
        print(num)
        return num+10

    print("In func")
    func_in_func(num + 100)
    print(func_in_func(num + 100))

# func_in_func(1) : 내부 중첩함수 직접 호출은 불가
nested_function(1)

# 함수7 - hint
def tot_length(word: str, num: int) -> int:
    return len(word) * num

print("hint func" , tot_length("Heavy snow falls in Seoul",10))




