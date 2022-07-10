# # set은 중복이 허용되지 않고, 순서가 없다.
# # set의 초기화 하는 방법 set(리스트)
# set_01 = set([1,2,3,2,1])
# set_02= {1,2,3,2,1}
# print(type(set_01), set_01)
# print(type(set_02), set_02)

# set_03 = set('hello')
# print(type(set_03), set_03)

# list_04 = list(set_03)
# list_04.sort()
# print(type(list_04), list_04)
# print(list_04[0])


# #집합을 어떨때 활용을 하는가?
# list_num = [1,1,2,3,3,4]
# # 위 리스트 중복을 제거하라.
# s1 = set(list_num)
# print(s1)
# print("="*25)


# # 집합을 리스트로 바꾸고 reverse를 이용해 역순으로...
# listb = list(s1)
# print(listb)
# print("="*25)
# listb.sort(reverse=True)
# print(listb)


# # 합집합
# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}
# print("합집합 1: ", s1 | s2)
# result_union = s1.union(s2)
# print("합집합 2: ", result_union)



# #교집합 >> 직접 구현하려면 엄청나게 어려운 로직을 간단하게 기능제공
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# print("교집합 1: ", s1 & s2)
# result_intersection = s1.intersection(s2)
# print("교집합 2: ", result_intersection)



############## 교집합의 원리 리스트 변환(for문 이용) ############## 
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# lista = list(s1)
# listb = list(s2)
# listc = []
# inta = 0
# for a in lista:
#     for b in listb:
#         if(a == b):
#             listc.append(a)
#             # inta = inta+1
# print(listc)


# ############## 교집합의 원리 셋으로 수행(for문 이용) ############## 
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# s3 = set()
# inta = 0
# for a in s1:
#     for b in s2:
#         if(a == b):
#             s3.add(a)
#             # inta = inta+1
# print(s3)


# #차집합
# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}
# print("차집합 1:", s1 - s2)
# result_s3 = s1.difference(s2)
# result_s4 = s2.difference(s1)
# print(result_s3)
# print(result_s4)


# # add 함수 : 값 한 개 추가하기, 리턴 없고, s1이 변화함에 유의.
# s1 = {1,2,3,4,5,6}
# s1.add(7)
# print(s1)


# # update 함수 : 값 여러개 추가하기
# s1 = {1,2,3,4,5,6}
# s1.update({7, 8, 9})
# s1.update([1, 10, 19])
# print(s1)


# #값 삭제
# s1 = {1,2,3,4,5,6,'a'}
# print("제거전", s1)

# s1.remove('a')
# print("제거후", s1)

# print(s1.discard('a'))    # 없는 값 삭제 시 None
# s1.remove('a')            # 없는 값 삭제 시 에러
# print(s1)


# 연습문제
#===========================================================================
# photo = {'정준하', '정형돈', '황광희', '노홍철', '전진', '길성준'}
# dance = {'박명수', '전진', '유재석', '하하', '정형돈'}
# band = {'전진', '민경훈', "길성준", '황광희'}

# # 1. 3개의 동아리 중 하나 이상 가입된 사람들의 전체 명단을 중복 없이 출력하세요.
# print("3개의 동아리 중 하나 이상 가입된 사람:", photo | dance | band)

# # 2. 댄스동아리에만 가입한 사람
# print("댄스동아리에만 가입한 사람", dance - photo - band)

# # 3. 3개의 동아리에 모두 가입된 사람
# print("3개의 동아리에 모두 가입된 사람", dance & photo & band)

# # 4. 2개의 동아리에 모두 가입된 사람
# s1 = photo.intersection(dance)
# s2 = photo.intersection(band)
# s3 = dance.intersection(band)

# print("2개의 동아리에 가입된 사람", (s1 | s2 | s3) - (dance & photo & band))
#===========================================================================