# 6. 다음 문자열에서 '-'을 제거 후 출력하시오.
phoneNumber = "010-5555-9999"

phoneNum =[]
for x in range(0,13):
    if phoneNumber[x] != "-":
        phoneNum.append(phoneNumber[x])
        print(phoneNumber[x],end="")


