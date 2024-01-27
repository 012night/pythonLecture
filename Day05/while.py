# # a = 0
# # while a < 10 :
# #     a += 1
# #     print(a)

# # 1~10 찍어내는 반복문
# # # for문
# # for x in range(1,11) :
# #     print(x, end=" ")

# # # while문
# # x = 0
# # while x < 10 :
# #     x += 1
# #     print(x, end=" ")

# # result = 0
# # for x in range(1, 101) :
# #     result += x
# # print(result)

# # x = 0
# # result = 0

# # while x < 100 :
# #     x += 1
# #     result += x
# # print(result)

# msg = '''
# 1. Add
# 2. Del
# 3. List
# 4. Quit'''

# # select = 9999
# # while select != 4 :
# #     print(msg)
# #     select = int(input("입력하세요 : "))

# # while True :
# #     print(msg)
# #     select = int(input("입력하세요 : "))
# #     if select == 4 :
# #         break

# # size = int(input("리스트의 사이즈를 정하세요 : "))
# # while size > 10 :
# #     print("10이하의 값으로 설정하세요!")
# #     size = int(input("리스트의 사이즈를 정하세요 : "))


# # # 무한반복중 특수 조건일시 반복종료
# # while True :
# #     size = int(input("리스트의 사이즈를 정하세요 : "))
# #     if size <= 10 :
# #         break
# #     else :
# #         print("10이하의 값으로 설정하세요!")

# # num = 0
# # result = []
# # while num < size :
# #     num += 1
# #     item = int(input("리스트에 넣을 값을 입력하세요"))
# #     result.append(item)
# # print(result)
        
# # result = []    
# # for x in range(size) :
# #     item = int(input("리스트에 넣을 값을 입력하세요"))
# #     result.append(item)
# # print(result)

# # num = 0
# # while num < 100 :
# #     num += 1
# #     if num % 2 == 0 :
# #         continue
# #     print(num, end= " ")


# # # 외장함수 사용법
# # import random
# # print(random.randint(1,10))

# # from random import randint
# # print(randint(1,10))


# # import random

# # while True :
# #     size = int(input("리스트의 사이즈를 정하세요 : "))
# #     if size <= 10 :
# #         break
# #     else :
# #         print("10이하의 값으로 설정하세요!")

# # num = 0
# # result = []
# # while num < size :
# #     num += 1
# #     # item = int(input("리스트에 넣을 값을 입력하세요"))
# #     item = random.randint(1,100)
# #     result.append(item)
# # print(result)

# # 1~10 사이의 난수 하나를 발생시켜 변수에 담고, 예상되는 숫자를 입력하여 맞추는 프로그램을 작성하라. 
# # 값이 일치하면 ‘성공’, 입력한 값이 난수보다 크면 ‘더 작은 값를 입력하세요‘ 
# # 난수보다 작으면 ‘더 큰 값을 입력하세요‘ 라고 출력하라.

# import random
# num_random = random.randint(1,10)
# while True : 
#     print("정답 :", num_random)

#     guess_num = int(input("숫자 입력하세요! :"))
#     if num_random == guess_num :
#         print("정답")
#         break
#     elif num_random < guess_num :
#         print("더 작은값을 입력하세요!")
#     else :
#         print("더 큰값을 입력하세요!")

# import random
# sample = []
# for x in range(1, 11) :
#     sample.append(random.randint(1,100))
# print(sample)

sample = [57, 9, 27, 34, 58, 79, 61, 64, 15, 98]

# max_num = sample[0]
# min_num = sample[0]
max_num = min_num = sample[0]

for x in sample :
    if max_num < x :
        max_num = x
    
    if min_num > x :
        min_num = x

print("최대값 :",max_num)
print("최소값 :",min_num)

