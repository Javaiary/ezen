'''
    동백이는 교환학생 점순이와 친해지게 되었습니다.
    영어를 잘 하지 못하는 점순이에게 한국어를 가르쳐 주기 위해
    한국어 연습 프로그램을 만들게 되었습니다.
        - 연습할 한국어가 담긴 리스트를 만든다.
        - 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
        - 프로그램 사용자가 단어를 그대로 입력하고
        - 맞추면 다음 단어를 가져온다.      // 틀리면 프로그램 종료.

        Let's Learning Korean
        사랑해
        사랑해
        귀엽다
        귀엽다
        고마워
        고마워
        행복해
        햄복해
        --TheEnd--
'''

list = ["사랑해", "귀엽다", "고마워", "행복해"]

print("Let's Learning Korean")
for i in list:
    x = input(i)
    if x != i:
        print("--TheEnd--")
        break
#--------------틀려도 계속 진행--------------------

word_list = ["사랑해", "귀엽다", "고마워", "행복해"]
print("Let's Learning Korean")
correct=0
for word in word_list:
    print(word)
    data = input()
    if data == word:
        correct += 1


print("전체 문제 개수 : ",len(word_list),"개")
print("맞힌 문제 개수 :",correct,"개")
print("맞힌 문제 개수 :",len(word_list)-correct,"개")
# 전체 문제 개수 : 4개 len(word_list)
# 맞힌 문제 개수 : 2개 correct:
# 틀린 문제 개수 : 2개 incorrect:
