#집합은 중복이 허용되지 않고, 순서가 없다.
#집합의 표현방식 set(리스트)
# s1 = set([1,2,3])
# s2= {1,2,3}
# s3 = set('test')
# print(s1)


# #집합을 어떨때 활용을 하는가?
# lista = [1,1,2,3,3,4]
# #위 리스트 중복을 제거하라.
# s1 = set(lista)
# listb = list(set(lista))
# print(s1)
# print(listb)

#교집합 >> 직접 구현하려면 엄청나게 어려운 로직을 간단하게 기능제공
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# s3 = s1 & s2
# s4 = s1.intersection(s2)
# print(s3)
# lista = list(s1)
# listb = list(s2)
# listc = []
# inta = 0
# for a in lista:
#     for b in listb:
#         if(a == b):
#             listc.append(a)
#             inta = inta+1
#
# print(listc)

#합집합
# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}
# s3 = s1 | s2
# s4 = s1.union(s2)
# print(s3)


#차집합
# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}
# s3 = s1 - s2
# s4 = s1.difference(s2)
# print(s3)


#값추가 >> 리턴은 없고, s1이 변화함에 유의.
# s1 = {1,2,3,4,5,6}
# s1.add(7)
# print(s1)


#값추가 여러개
# s1 = {1,2,3,4,5,6}
# s1.update({7, 8, 9})
# print(s1)


#값 삭제
s1 = {1,2,3,4,5,6}
s1.remove(1)
print(s1)