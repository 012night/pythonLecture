# 반복문과 조건문의 조합

#1~100 사이의 수 중에서 3의 배수만 출력하세요
# for x in range(1,101) :
#     if x % 3 == 0 :
#         print(x, end=" ")

# for x in range(3, 101, 3) :
#     print(x, end=" ")

# # 1~100 사이의 수 중에서 9의 배수의 개수
# count = 0
# for x in range(1,101) :
#     if x % 9 == 0 :
#         print(x, end=" ")
#         count += 1
# # print()
# print(f"\n{count}")

# result = 0
# for x in range(1,101) :
#     # if x % 3 == 0 :
#     #     if x % 2 == 1 :
#     if x % 3 == 0 and x % 2 == 1 :
#         result += x
# print(result)


# list_score = [90, 25, 67, 45, 80]
# no = 0
# for score in list_score :
#     # no = list_score.index(score)+1 # 함수 사용 : 점수가 위치한 인덱스 번호
#     no += 1 # 변수 사용
#     if score >= 60 :
#         print(f"{no}번 학생 {score}점으로 합격")
#     else :
#         print(f"{no}번 학생 {score}점으로 불합격")


# num = int(input("정수 하나 입력 : ")) # 8
# for x in range(1, num+1) :
#     if num % x == 0 :
#         print(x, end=" ")


# for x in range(1, 11):
#     if x == 4 : 
#         # continue
#         break
#     print(x) 


# list_blood_type = ['b', 'b', 'ab', 'a', 'b', 'a', 'b']

# for blood in list_blood_type :
#     if blood == "a" :
#         print("당첨입니다.")
#         break
#     else : 
#         print("불발입니다.")


# 로직을 통해 가공된 데이터를 리스트화 

# list_sample = []
# result = 0

# for x in range(1,101) :
#     if x % 3 == 0 and x % 2 == 1 :
#         list_sample.append(x)
# print(list_sample)

# list_sample = [x for x in range(1,101) if x % 3 == 0 and x % 2 == 1]
# print(list_sample)

# 1세트 10회 2세트 10회 3세트 10회

# for y in range(1,4) :
#     print(f"{y}set 시작")
#     for x in range(1,11) :
#         print(f"{x}회 수행")

# l1 = [1,2,3,4,5]
# l2 = [3,4,5,6,7]
# list_sample = []

# for x in l1 :
#     for y in l2 :
#         if x == y :
#             list_sample.append(x)

# print("교집합 :",list_sample)

for x in range(2,10) :
    for y in range(1,10) :
        print(f"{x}*{y}={x*y}", end=" ")
    print()