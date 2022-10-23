# =====================================================================
# dict란 key와 value로 이루어진 사전적 구조의 자료구조를 말함.
# dict의 기본 구조 a = {key:value}, 리스트는 a = [value], 튜플은 a = (value)
# key로 value를 찾는 구조
# key는 중복이 되지 않는다.
# =====================================================================

# =====================================================================
# # dict 생성
# dict_profile = {'name':'메가스터디', 'address':'강남', 'type':"IT", 'floor':4}
# print(type(dict_profile), dict_profile)
# print(dict_profile['name'])
# # 없는 키로 검색하면 에러 발생
# # print(dict_profile['name1']) 
# =====================================================================

# =====================================================================
# # 추가 : 변수명[key] = value 방식으로 추가. 
# dict_profile['phone']='010-0000-1111'
# print(dict_profile)

# dict_profile['employee']=100
# print(dict_profile)

# dict_profile['x월 휴강'] = [30, 31]
# print(dict_profile)
# =====================================================================

# =====================================================================
# # 수정 : dict에 중복되는 키를 넣으면 수정과 같다
# dict_profile['phone'] = '010-1234-5678'
# print(dict_profile)
# =====================================================================

# =====================================================================
# # 삭제1 : del dic[key]방식으로 삭제
# del dict_profile['address']
# print(dict_profile)
# =====================================================================

# =====================================================================
# # 삭제2 변수명.pop(key)방식으로 삭제
# print(dict_profile.pop('floor'))
# print(dict_profile)
# =====================================================================

# =====================================================================
# # 모두 삭제하기
# dict_profile.clear()
# print(dict_profile)
# =====================================================================

# =====================================================================
# # 확장
# dic1 = {'a':3, 'b':2, 'c':3}
# dic2 = {'a':2, 'd':4, 'e':5}
# print(dic1, dic2)
# # dic1.update(dic2)
# dic2.update(dic1)
# print(dic2)
# =====================================================================

# =====================================================================
# # 딕셔너리 초기 생성시 주의사항
# # key가 겹치면 나중에 선언한 key:value가 최종값이 됨.
# dic1 = {'a':1, 'b':2, 'a':3}
# print(dic1)   
# =====================================================================

# =====================================================================
# # key를 통해 값 얻기 01 : 기본호출은 변수명[key], 
# dict_profile = {'이름':'홍길동', '나이':25, '성별':'남'}
# # 변수명['성격'] 시 키가 없으면 에러메시지 발생
# # print(dict_profile['성격'])
# print(dict_profile['나이'])
# =====================================================================

# =====================================================================
# # key를 통해 값 얻기 02 : get 함수 사용
# # dict_profile.get 없는 키 조회 시 에러가 아닌 None 발생
# print(dict_profile.get('성격'))
# print(dict_profile.get('성격','성격이라는 key가 없습니다'))
# =====================================================================

# =====================================================================
# # keys 함수: key 리스트 생성 
# dict_01 = {'a':1, 'b':2, 'c':3}
# print(type(dict_01.keys()), dict_01.keys())
# keys_to_list = list(dict_01.keys())
# print(keys_to_list.pop())
# print(dict_01.get(keys_to_list[0]))
# =====================================================================

# =====================================================================
# # values 함수: value리스트 생성(많이 쓰이는 함수)
# print(type(dict_01.values()), dict_01.values())
# values_to_list = list(dict_01.values())
# print(values_to_list.pop())
# print(dict_01.get(values_to_list[0]))
# =====================================================================

# =====================================================================
# # key, value 쌍을 tuple형태의 list로 묶기 >> 
# # items() 함수 : key, value를 세트로 묶어 처리해야 하는 경우 
# dic1 = {'a':1, 'b':2, 'c':3}
# print(type(dic1), dic1)
# print(type(dic1.items()), dic1.items())
# a = dic1.items()
# # print(list(a)[0])
# =====================================================================

# =====================================================================
# # 딕셔너리 Key, Value, items를 활용한 반복문 미리 맛보기 
# for k in dic1.keys() :
#     print(f"현재 key들은 다음과 같습니다.{k}")    
# for k, v in dic1.items():
#     print(f'key : {k}, value : {v}')
# =====================================================================

# =====================================================================
# # 딕셔너리 활용, 리턴은 bool형 if문과 in 활용 맛보기
# dict_profile = {'name':'메가스터디', 'address':'강남', 'type':"IT", 'floor':4}
# print('name' in dict_profile)
# print('강남' in dict_profile)

# dict_profile = {'name':'메가스터디', 'address':'강남', 'type':"IT", 'floor':4}
# if 'name' in dict_profile :
#     print(dict_profile['name'])
# =====================================================================

# =====================================================================
# # 연습문제
# books_dict = {'말 그릇':'김윤나', '마음의 미래':'미치오 카쿠',
#               '메모의 마법':'마에다 유지', '시간은 흐르지 않는다':'카를로 로벨리',
#               '평행우주':'미치오 카쿠'}

# # 1. 책 '시간은 흐르지 않는다'의 저자는 누구인지 출력하세요.
# print(books_dict['시간은 흐르지 않는다'])
# print(books_dict.get('시간은 흐르지 않는다'))

# # 2.
# # 책: 코스모스, 저자: 칼 세이건
# # 책: 해변의 카프카, 저자: 무라카미 하루키
# books_dict['코스모스'] = '칼 세이건'
# books_dict['해변의 카프카'] = '무라카미 하루키'
# print(books_dict)

# # 3. 책 이름 출력
# print(list(books_dict.keys()))

# # 4. 책 저자 출력
# print(set(books_dict.values()))
# =====================================================================


