import random
# while문

# while 조건식 :
    # 실행문
    # 증감식

# a = 1
# while a < 10 :
#     print("수행", a)
#     a += 1

# # 1~100까지 출력하세요
# num = 1
# while num <= 100 :
#     print(num, end=" ")
#     num += 1

# # 카운트 다운
# num = 5
# while num > 0 :
#     print("카운트다운",num)
#     # num = num - 1
#     num -= 1

# count = 1
# while count <= 10 :
#     print(f"푸쉬업 {count}회 수행")
#     if count == 5 :
#         print(f"{count}회 달성 축하드립니다.")
#     count += 1
# print("푸쉬업 종료")

# # 1~100까지의 합(while)
# num = 1
# result = 0
# while num <= 100 :
#     print(num, end=" ")
#     result += num
#     num += 1
# print()
# print(result)


# msg = '''1. Add
# 2. Del
# 3. List
# 4. Quit'''
# print(msg)

# select = -1
# while select != 4 : 
#     print(msg)
#     select = int(input("Enter Number : "))

# # 무한반복중에 어떠한 값이 들어오면 반복을 중지하세요
# while True :
#     print(msg)
#     select = int(input("Enter Number : "))
#     if select == 1 :
#         print("더하기 기능 실행")
#     elif select == 2 :
#         print("삭제 기능 실행")
#     elif select == 3 :
#         print("리스트 관련 기능 실행")
#     else :
#         print("종료")
#         break

# while True :
#     size = int(input("리스트의 크기를 할당하세요!"))
#     if size > 10 :
#         print("10이하의 값으로 재할당 하세요")
#     else :
#         break
# 입력한 사이즈로 구성된 리스트 만들기
# a = 0
# list_own = []
# while a < size :
    # print("출력")
    # 비어있는 리스트에 내가 입력한 값이 리스트 값으로 들어가면
    # data = int(input("리스트에 값을 할당해보세요 : "))
    # list_own.append(data)
    # list_own.append(int(input("리스트에 값을 할당해보세요 : ")))
    # 난수 입력
#     list_own.append(random.randint(1, 50))
#     a += 1
# print(list_own)

# # 난수를 발생시키기 위한 코드
# # 외장함수를 사용하겠다 라고 선언
# import random
# print(random.randint(1, 10))


# import random
# num_random = random.randint(1,10)
# print("난수 :",num_random)

# # 값이 일치하면 ‘성공’, 입력한 값이 난수보다 크면 ‘더 작은 값를 입력하세요‘ 난수보다 작으면 ‘더 큰 값을 입력하세요‘
# while True : 
#     guess_num = int(input("예상되는 값을 입력하세요! "))
#     if num_random == guess_num :
#         print("정답")
#         break
#     elif num_random > guess_num :
#         print("더 큰값을 입력해주세요")
#     else :
#         print("더 작은 값을 입력해주세요")


list_random = [57, 9, 27, 34, 58, 79, 61, 64, 15, 98]

# max_num = list_random[0]
# min_num = list_random[0]
# max_num = min_num = list_random[0]

# for x in list_random :
#     if max_num < x :
#         max_num = x
#     if min_num > x :
#         min_num = x
# print(f"최대값 : {max_num}, 최소값 = {min_num}")


list_sample = [5, 1, 3, 7, 2, 9]

for x in range(0, len(list_sample)-1) : # ~ 5
    for y in range(x+1, len(list_sample)) :
        if list_sample[x] > list_sample[y] :
            list_sample[x], list_sample[y] = list_sample[y],list_sample[x]
print(list_sample)