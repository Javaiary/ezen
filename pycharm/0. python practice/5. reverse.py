# 5. 다음 문자열을 거꾸로 출력하시오.
string = "strawberry"

print(len(string))

print(string[-10])

for x in range(-1, -11, -1):
   print(string[x], end="")

print()
#-----------------------
strawberry = list(string)
print(strawberry)

#strawberry[0], strawberry[-1] = strawberry[-1], strawberry[0]
#print(strawberry[0], strawberry[-1])

for x in range(0,5):
    y= 9-x
    strawberry[x], strawberry[y] = strawberry[y], strawberry[x]
    print(strawberry[x], strawberry[y])

for x in range(0,10):
    print(strawberry[x], end="")


