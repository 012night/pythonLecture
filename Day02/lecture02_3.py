#딕셔너리란 key+value로 이루어진 사전적 구조의 자료구조를 말함.
#딕셔너리의 기본 구조 a = {key:value}, 리스트는 a = [value], 튜플은 a=(value)
#딕셔너리의 기본호출은 a[key], 또다른 방식은 get 함수 사용 >> 리스트, 튜플에는 있을 수 없는 함수.

# dic1 = {'이름':'홍길동', '나이':25, '성별':'여'}
# print(dic1['이름'])
# print(dic1.get('이름'))

# #딕셔너리 쌍 추가하기 dic[key] = value 방식으로 추가.
# dic1['신분'] = '학생'
# print(dic1)
#
# #딕셔너리 쌍 삭제하기 del dic[key]방식으로 삭제.
# del dic1['이름']
# print(dic1)

#딕셔너리 만들때 주의사항
#key가 겹치면 안된다. >> 겹칠 경우 나중에 선언한 key:value가 최종값이 됨.
# dic1 = {'a':1, 'b':2, 'a':3}
# print(dic1)

# #딕셔너리 key리스트, value리스트 뽑아내기(많이 쓰이는 함수)
# dic1 = {'a':1, 'b':2, 'c':3}
# print(dic1.keys())
# print(dic1.values())

#딕셔너리를 튜플형태의 리스트로 담기 >> .items() >> key, value를 세트로 묶어 처리해야 하는 경우 >> dic1자체를 바꾸지는 않음.

# dic1 = {'a':1, 'b':2, 'c':3}
# print(dic1.items())
# print(dic1)

# for k, v in dic1.items():
#     print('키는 :' + k + ' 밸류는 :' + str(v))

# #딕셔너리 Key, Value 쌍 얻기(item) Key:Value 쌍 지우기(clear) >> dic1자체를 바꿈.
# dic1 = {'a':1, 'b':2, 'c':3}
# print(dic1.items())
# print(dic1.clear())
# print(dic1.items())


# #딕셔너리 활용, 리턴은 bool형
# dic1 = {'a':1, 'b':2, 'c':3}
# print('a' in dic1)
# print('d' in dic1)