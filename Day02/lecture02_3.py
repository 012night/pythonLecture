#딕셔너리란 key+value로 이루어진 사전적 구조의 자료구조를 말함.
#딕셔너리의 기본 구조 a = {key:value}, 리스트는 a = [value], 튜플은 a = (value)


# #딕셔너리 생성
dic_profile = {'name':'메가스터디', 'address':'강남', 'floor':4}
# print(type(dic_profile), dic_profile)
# print(dic_profile['name'])


# #딕셔너리 추가 변수명[key] = value 방식으로 추가. 
# dic_profile['phone']='010-0000-1111'
# print(dic_profile)


# #수정
# dic_profile['phone'] = '010-1234-5678'
# print(dic_profile)


# #딕셔너리 삭제하기1 del dic[key]방식으로 삭제
# del dic_profile['address']
# print(dic_profile)


# #딕셔너리 삭제하기2 변수명.pop(key)방식으로 삭제
# print(dic_profile.pop('floor'))
# print(dic_profile)


# #딕셔너리 모두 삭제하기
# dic_profile.clear()
# print(dic_profile)


# #딕셔너리 확장하기
# dic1 = {'a':3, 'b':2, 'c':3}
# dic2 = {'a':2, 'd':4, 'e':5}
# print(dic1, dic2)
# dic1.update(dic2)
# print(dic1)



# #딕셔너리 key값 확인 하여 bool형으로 결과 받기
# print('name' in dic_profile)
# dic_profile = {'name':'메가스터디', 'age':30, 'address':'강남'}
# if 'name' in dic_profile :
#     print(dic_profile['name'])



# 딕셔너리 생성시 주의사항
# key가 겹치면 안된다. >> 겹칠 경우 나중에 선언한 key:value가 최종값이 됨.
# dic1 = {'a':1, 'b':2, 'a':3}
# print(dic1)   



# #딕셔너리의 기본호출은 변수명[key], 
# #또다른 방식은 get 함수 사용 >> 리스트, 튜플에는 있을 수 없는 함수.
# dic1 = {'이름':'홍길동', '나이':25, '성별':'여'}
# # 변수명['성격'] 시 키가 없으면 에러메시지 발생
# print(dic1['성격'])



# # dic1.get 사용시 에러가 아닌 none 발생
# print(dic1.get('성격'))
# print(dic1.get('성격','이름이라는 key가 없습니다'))



#딕셔너리 key리스트, value리스트 뽑아내기(많이 쓰이는 함수)
dic1 = {'a':1, 'b':2, 'c':3}
print(type(dic1.keys()), dic1.keys())
print(type(dic1.values()), dic1.values())
a_list = list(dic1.keys())


# # 딕셔너리를 튜플형태의 리스트로 담기 >> 
# # .items() >> key, value를 세트로 묶어 처리해야 하는 경우 >> 
# dic1 = {'a':1, 'b':2, 'c':3}
# print(type(dic1), dic1)
# print(type(dic1.items()), dic1.items())



# # Key:Value 쌍 지우기(clear)
# dic1 = {'a':1, 'b':2, 'c':3}
# print(dic1.items())
# dic1.clear()
# print(dic1.items())


# # 딕셔너리 Key, Value, items를 활용한 반복문 미리 맛보기 
# for k in dic1.keys() :
#     print("현재 key들은 다음과 같습니다.{}".format(k))
#     # print(f"현재 key들은 다음과 같습니다.{k}")    
# for k, v in dic1.items():
#     print(f'키는 : {k}, 밸류는 : {v}')


# #딕셔너리 활용, 리턴은 bool형
# dic1 = {'a':1, 'b':2, 'c':3}
# print('a' in dic1)
# print('d' in dic1)