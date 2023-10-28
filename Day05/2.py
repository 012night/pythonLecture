import random
# a = 11
# while a > 10 :
#     print("반복문 실행중", a)
#     a -= 1


# # 5회 반복하는 반복문
# a = 1
# while a <= 5 :
#     print(a)
#     a += 1


# pushUp = 0
# while pushUp < 10 :
#     pushUp += 1
#     print(f"푸쉬업 {pushUp}회 수행")
# print("끝")

# a = 0
# sum_result = 0
# while a < 100 :
#     a += 1
#     sum_result += a
# print(sum_result)


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




import random

while True :
    size = int(input("리스트의 크기를 정하세요 : "))
    # if size > 10 :
    #     print("10보다 작은 값을 입력하세요")
    #     continue
    # break
    if size <= 10 :
        break
    print("10보다 작은 값을 입력하세요")

list_result = []
# for x in range(1,size+1) :
#     data = int(input("리스트에 값을 할당하세요! : "))
#     list_result.append(data)
# print(list_result)

a = 0
while a < size :
    # data = int(input("리스트에 값을 할당하세요! : "))
    # list_result.append(int(input("리스트에 값을 할당하세요! : ")))
    list_result.append(random.randint(1,10))
    a += 1
print(list_result)


