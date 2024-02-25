# 1~100까지의 범위에서 2의 배수만 출력하세요
# for x in range(1,101) :
#     if x % 2 == 0 : 
#         print(x, end=" ")

# for x in range(1,101) :
#     if x % 7 == 0 : 
#         print(x, end=" ")


# 1~100 사이에서 3의 배수이면서 2의 배수가 아닌 수를 출력하라
# 그 합을 역시 출력하라.
# for x in range(1,101) :
#     if x % 3 == 0 :
#         if x % 2 != 0 : 
#         # if x % 2 == 1 : 
#             print(x , end= " ")

# result = 0
# for x in range(1,101) :
#     if x % 3 == 0 and x % 2 != 0 : 
#         print(x , end= " ")
#         result += x
# print("\n누적합 :",result)

# # 1 ~ 100의 사이의 수중 7의 배수의 개수
# count = 0
# for x in range(1,101) :
#     if x % 7 == 0 :
#         count += 1
#         print(x, end=" ")
# print(f"\n7의 배수의 개수 : {count}")

# list_score = [90, 25, 67, 45, 80]
# count = 0
# for x in list_score :
#     count += 1
#     if x >= 60 :
#         # print(f"{list_score.index(x)+1}번 학생 {x}점으로 합격")
#         print(f"{count}번 학생 {x}점으로 합격")
#     else : 
#         print(f"{x}점으로 불합격")

# list_score = [90, 25, 67, 45, 80]
# for x in range(0, len(list_score)) :
#     if list_score[x] >= 60 :
#         print(f"{x+1}번 학생 {list_score[x]}점으로 합격")
#     else : 
#         print(f"{x+1}번 학생 {list_score[x]}점으로 불합격")


# # 약수 구하기
# num = 3
# for x in range(1,num+1) :
#     if num % x == 0 :
#         print(x)

# # coutinue
# for x in range(1,11) :
#     if x == 4 :
#         # continue
#         break
#     print(x, end=" ")


# list_blood_type = ['b', 'b', 'ab', 'a', 'b', 'a', 'b']

# for blood in list_blood_type :
#     if blood == "a" :
#         print("당첨")
#         break
#     else :
#         print("낙첨")
# print("이벤트 종료")

# own_list = []
# for x in range(1, 101) :
#     if x % 7 == 0 :
#         # 나의 리스트에 추가하는 작업
#         own_list.append(x)
# print(own_list)

# # 리스트 내포
# # [리스트 안에 문법작성을 허용]
# own_list = [x for x in range(1, 101) if x % 7 == 0]
# print(own_list)


# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a.intersection(b))

# a = [1,2,3,4]
# b = [3,4,5,6]

# inter_list = []
# for x in a :
#     for y in b :
#         if x == y :
#             inter_list.append(x)
# print(inter_list)

# # 운동시... 1세트 10회 2세트 10회 3세트 10회
# for x in range(1,4) :
#     print(f"======{x}세트 시작=======")
#     for y in range(1,11) :
#         print(f"{y}회 수행")

# for dan in range(2, 10) :
#     for y in range(1, 10) :
#         print(f"{dan}*{y}={dan*y}", end=" ")
#     print()


list_position = ['c.과장', 'b.부장', 'd.대리', 'a.사장', 'd.대리', 'c.과장']

# 중복되지 않은 직급 -> 형변환

# set타입의 특성 -> 순서가 없다, 중복 불가
# listToSet = set(list_position)
# print(listToSet)

# unique = list(set(list_position))
# unique.sort()
# print(unique)

# 반복문과 조건문을이용한 검출
unique = []
for x in list_position :
    if x not in unique :
        unique.append(x)
unique.sort()
print(unique)