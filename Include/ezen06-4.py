# ezen06-4
'''
    5) 딕셔너리(Dictionary) 자료형
        - {key1 : Value1, Key2: Value2, Key3: Value3,...}
        - {'name': 'Jack', 'age' : 52}  자료형이 달라도 가능
        - stu = {'name' : ['Susan', 'Jack', 'Mitch', 'William'], 'age':[19,52,32,33]}
'''

stu = {'name' : ['Susan', 'Jack', 'Mitch', 'William'], 'age':[19,52,32,33]}
print(stu)
print(type(stu))
print(type(stu['name']))
print(type(stu['name'][1]))
print(stu['name'][1][0])

stu['math'] =[50,100,70,80]
print(stu)

del stu['math']
print(stu)

for key, value in stu.items():
    print(key, value)