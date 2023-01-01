import pandas as pd

agg_prd_pd = pd.DataFrame({
    'L' : [5141, 5365, 5084],
    'M' : [4968, 4977, 4915],
    'S' : [5012,4991, 5029],
    'XL' : [5071, 4976, 5023],
    'XS' : [5195, 4954, 5088]
}, index =['Jacket', 'Shirt', 'Trousers'])

print(agg_prd_pd)

'''
    1. 데이터 삭제 : drop()
        - 필요없는 데이터를 삭제
        - 행(index), 열(column) 단위로 삭제
    2. 중복 데이터 삭제 : 
        - duplicated() : 데이터 중복 여부를 true,false로 반환
                        keep: 중복이 있다면 처음과 마지막 값 중 어떤것을 중복이라고 판단
        - drop_duplicates() : 중복된 데이터를 삭제
                        keep: 중복이 있다면 처음과 마지막 값 중 어떤것을 삭제
'''


df = pd.DataFrame({
    'SIZE' : ['L','L', 'M', 'S', 'XS'],
    'product_type':['Jacket', 'Shirt', 'Trousers', 'Jacket', 'Shirt'],
    'color': ['red', 'black', 'black', 'red', 'blue'],
    'quantity': [5,15,10,20,15]

})
print(df)
df.drop(['color'], axis =1)
print(df)       # 원본 데이터가 바뀌는 것은 아님

print()
print(df.drop(['color', 'quantity'], axis = 1))

print()
print(df.drop(['SIZE', 'product_type'], axis=1))

print()
# print(df.drop(['SIZE', 'product_type'])) 열단위 삭제할 때에는 반드시 axis 값이 필요함.
print(df)
print()
print(df.drop([0], axis=0))     # 행 삭제
print()
print(df.drop([0]))             # 행단위 삭제할 때에는 axis 값 여부가 중요하지 않음
print()
print(df.drop([1,4]))           # 행 2개 삭제

print("---------------------------------------------")
print(df)
print()
print(df.duplicated(['product_type'], keep='first'))        #후자를 중복으로 인식
print(df.duplicated(['product_type'], keep='last'))         #전자를 중복으로 인식

print()
print(df.drop_duplicates(['product_type'], keep='first'))   #중복된 후자 삭제
print(df.drop_duplicates(['product_type'], keep='last'))    #중복된 전자 삭제



