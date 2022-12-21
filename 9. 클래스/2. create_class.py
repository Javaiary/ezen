class Monster:
    def say(self):
        print("안녕하세요. 난 몬스터야~!")

mob = Monster()
mob.say()

a= 10
print (type(a))

b= "문자열객체"
print(type(b))
print(b.__dir__())