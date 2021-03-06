# 중첩 반복문: 반복문 안에 반복문
# 바깥 반복문: 천천히 돈다. ex) 세트    
# 안쪽 반복문: 빠르게 돈다. ex) 운동 횟수


# # 스쿼트 10회
# for i in range(1, 11):
#     print("스쿼트 %d회" % i)


# # 스쿼트 3세트 10회씩
# for i in range(1, 4):   # 1 ~ 3세트
#     for j in range(1, 11):   # 1 ~ 10회
#         print("%d세트:%d회차" % (i, j))


# # 이중 for문 예제 09(구구단 출력)
# for x in range(2,10) :
#     for y in range(1,10) :
#         print("{} * {} = {}".format(x, y, x*y))


# # 이중 for문 예제 09(구구단 출력 - 프린트문 조작을 통해 예쁘게 출력)
# for x in range(2,10) : 
#     print("")
#     for y in range(1,10) :
#         print(f"{x} * {y} = {x*y}", end=' ')


# # For문을 활용하여 리스트에 각종 값을 담기 01
# result = []
# for i in range(1, 101):
#     if i % 3 == 0 :
#         result.append(i)
# print(result)


# # For문을 활용하여 리스트에 각종 값을 담기 02
# result = list()
# for x in range(2,10) : 
#     for y in range(1,10) :
#         # result.append(f"{x}*{y}={x*y}")
#         result.append(x*y)
# print(result)


# # 제어문(반복문_for) list, set, dic 모두 이용한 마지막 for 예제
# # 각종 형 변환 활용가능
# list_position = ['c.과장', 'b.부장', 'd.대리', 'a.사장', 'd.대리', 'c.과장']
# set_position = set(list_position)
# set_to_list_position = list(set_position)
# set_to_list_position.sort()
# print(f"중복되지 않은 직급 : {set_to_list_position}")

# dic_position = {}
# for position1 in set_to_list_position:
#     count = 0
#     for position2 in list_position:
#         if position1 == position2:
#             count += 1
#     dic_position[position1] = count

# print(f"각 직급별 인원수 : {dic_position}")


# # [참고]for문 내부는 이런식으로 돌아간다...
# list_a = [1,2,3] 
# iter_test = iter(list_a)
# print(type(iter_test))
# print(next(iter_test))
# print(next(iter_test))
# print(next(iter_test))
# try :
#     print(next(iter_test))
# except :
#     print('더이상 없습니다')