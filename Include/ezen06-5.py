# ezen06-5
'''
    6) Dataframe
        - index 행
        - columns 열
        - 데이터 선택(slicing)
            - 데이터 위치를 활용한 데이터 가공 : loc(), iloc()
        - 데이터 삭제(drop)
            - 필요 없는 데이터 삭제
            - 행 (index), 열(column) 단위로 삭제 
'''
import pandas as pd
df = pd.DataFrame()
print(type(df))

stu_list=[['Susan', 'Jack', 'Mitch', 'William'],[19,15,16,17]]
print(stu_list)

df = pd.DataFrame(stu_list)
print(df)

df = df.T
print(df)

print()

columns_name = ['name', 'age']
df.columns = columns_name
print(df)

'''
    "I am quitting this exam."
    "This is the quickest approach I ever seen."
    "The king should make quick decision."
    
    문장을 입력하다가 'q'라고 작성을 하였습니다. 
    원래는 'w'를 작성해야 했습니다.

    주어진 문장들을 모두 맞게 변경하시오.(replace())
    "I am wuitting this exam."
    "This is the wuickest approach I ever seen."
    "The king should make wuick decision."
'''
# 리스트, for문, q -> w, print

str_list = [    "I am quitting this exam.",
    "This is the quickest approach I ever seen.",
    "The king should make quick decision."]
for sentence in str_list:
    print(sentence.replace('q','w'))

for x in range(len(str_list)) :
    str_list[x]=str_list[x].replace('q','w')
    print(str_list[x])



# 주어진 문장들에 대해서 몇 개의 단어가 있는지 출력하시오. (split())
# 5
# 8
# 6

for x in range(len(str_list)):
    print(len(str_list[x].split()))

'''
    차범근 축구감독이 미래 축구 꿈나무를 선발하여 축구부를 만듭니다.
    키가 175cm이상인 사람들을 뽑아서 축구부를 결성합니다.
    soccer_team이라는 빈 리스트를 작성하여, 축구부가 될 사람들의 이름만 추가하는 코드를 작성해 보시오.
'''
꿈나무후보 = {"이순신":146, "이도" :160, "유성룡": 167, "정철": 175.3, "이황":207 }
soccer_team = []
for key, val in 꿈나무후보.items():
    if val >=175:
        soccer_team.append(key)

print(soccer_team)

soccer_team2 = [name for name, height in 꿈나무후보.items() if height >=175]
print(soccer_team2)

# 구구단 출력 (for문)


