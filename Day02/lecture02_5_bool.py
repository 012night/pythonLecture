# # 불형 : boolean 자료형의 줄임말
# # 불형의 type 프린트
# a = True;
# print(type(a), a)

# compare_num = 1<3
# print(type(compare_num), compare_num)

# a = True
# b = True
# c = False

# print(a and b)
# print(a or c)
# print(not a and c)


# # 파이썬 불형의 특징
# a = "hello"
# if a:
#     print(a)


# # not 예제
# a = 3
# b = 4
# print(a == b)


# # if와 비교연산자를 활용한 기본 예제    
# a = 3
# if a == 3:
#     print(a)
    

# # if문과 in을 이용한 조건 
# a = [1,2,3,4]
# if 1 in a :
#     print(a.pop())
#     print(a)


# # while문 맛보기 예제 a가 False가 될때까지
# a = [1,2,3,4]
# while a :
#     print(a.pop())


# # while의 무한루프 예제    
# while a==3:
# 	print(a)
# 	# a += 1


# #딕셔너리 key값 확인 하여 bool형으로 결과 받기
# dic_profile = {'name':'메가스터디', 'age':30, 'address':'강남'}
# if 'name' in dic_profile :
#     print(dic_profile['name'])



##############삼항 연산자는 나중에...##############

#None이란 값이 없는 것. None 또한 False
# dic1 = {"이름": '몽키D루피', "나이":3}
# print(dic1.get("학교"))
# if dic1.get("학교"):
#     print("학교는 False 입니다.")
# if dic1.get("이름"):
#     print("이름은 True 입니다.")