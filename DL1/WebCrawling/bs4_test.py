from bs4 import BeautifulSoup

html = open("fruits.html", "r", encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")
body = soup.select_one("body")     # 객체.select_one(<선택자>) : CSS 선택자로 요소 하나를
ptag = body.find('p')                     # 객체.find(tag[, attributes]: tag라는 태그 중 조건에 맞는 1번째 태그를 찾아줌
print('1번째 p태그 : ', ptag)
print('1번째 p태그 : ', ptag['class'])

ptag['class'][1]= 'white'
print('1번째 p태그 : ', ptag['class'])

ptag['id'] ='apple'
print('1번째 p태그의 id속성 :', ptag['id'])

print()
body_tag =soup.find('body')
print(body_tag)

print()
idx = 0
# 객체.childern : 해당 태그의 하위 태그들을 리스트 목록으로 반환함
print('chilern 속성으로 하위 항목 보기')
for child in body_tag.children:
    idx += 1
    print(str(idx) + ' 번째 요소 : ', child)

print()
mydiv = soup.find("div")
print(mydiv)

print()
# 객체.parent : 해당 객체의 부모 요소를 찾아 줌
print('div 태그의 부모 태그는?')
print(mydiv.parent)

print()
# 객체.find_parents() : 현재 태그의 상위에 있는 모든 태그를 찾아줌
print('mytag 태그의 모든 상위 부모 태그들의 이름: ')
parents = mydiv.find_parents()
for p in parents:
    print(p.name)