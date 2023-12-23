import random
# 반복문 2
# while 조건식 :
#     실행문

# a = 10
# while a > 5 :
#     print("출력", a)
#     a -= 1

# #3번 반복하는 문장(hello 세번 출력 - while 사용)
# num = 0
# while num < 3 :
#     print("hello")
#     num += 1

# # 카운트다운 5 ~ 1
# x = 5
# while x > 0 :
#     print(f"카운트다운 {x}")
#     x -= 1

# x = 0
# while x < 10 :
#     x += 1
#     print(f"푸쉬업 {x}회 수행")

# print("끝")

# num = 0
# sum_result = 0
# while num < 100 :
#     num += 1
#     sum_result += num
# print(f"합계 : {sum_result}")

msg = '''
1. Add
2. Del
3. List
4. Quit'''

# number = 0
# while number != 4 :
#     print(msg)
#     number = int(input("Enter Number : "))

# while True :
#     print(msg)
#     number = int(input("Enter Number : "))
#     if number == 4 :
#         break

# 10이하의 크기로 리스트를 지정
# size = 0
# while size < 10 : 
#     size = int(input("리스트의 사이즈를 구하세요 : "))
# import random

# while True : 
#     size = int(input("리스트의 사이즈를 구하세요 : "))
#     if size <= 10 : 
#         break
#     else :
#         print("10 이하의 값으로 사이즈를 할당해주세요")

# # for문 처리(랜덤함수 사용)
# list_result = []
# for x in range(0,size) :
#     list_result.append(random.randint(1,10))
# print(list_result)

# # for문 처리
# list_result = []
# for x in range(0,size) :
#     list_result.append(int(input("입력하세요 ")))
# print(list_result)
        
# 지정한 사이즈 만큼 리스트의 값을 불러 새로운 리스트로 만드는..
# while문 처리
# differ = 0
# list_result = []
# while differ < size :
#     differ += 1
#     # number = int(input("입력하세요 "))
#     # list_result.append(number)
#     list_result.append(int(input("입력하세요 ")))
# print(list_result)



# # 난수발생(랜덤한 수)
# # 외장함수 선언방법
# import random

# random_nubmer = random.randint(1,10) 
# print(random_nubmer)

# import random
# num_random = random.randint(1,10) 

# while True :
#     guess_num = int(input("값을 맞춰보세요! : "))
#     if guess_num == num_random :
#         print("정답")
#         break
#     elif guess_num < num_random :
#         print("더 큰값을 입력하세요~")
#     else :
#         print("더 작은값을 입력하세요~")

# num_random = [57, 9, 27, 34, 58, 79, 61, 64, 15, 98]

# num_random = []
# for x in range(0,10) :
#     if x not in num_random :
#         num_random.append(random.randint(1,10))
# print(num_random)

# # min_num = num_random[0]
# max_num = min_num = num_random[0]
# for x in num_random :
#     #최대값 구하기
#     if max_num < x :
#         max_num = x
#     #최소값 구하기
#     if min_num > x :
#         min_num = x
# print(f"최대값 : {max_num}")
# print(f"최소값 : {min_num}")