#while문의 기본구조는 
# while 조건문 : 
#   실행문
#   증감문
# 의 구조로서 while안의 조건문이 True인한 계속 반복된다.


# # while문 예제를 통한 이해1
# count = 1
# while count < 5 :
#     print(count)
#     count += 1


# # "안녕" 3번 쓰기 while 반복문
# num = 0  # 카운팅 변수
# while num < 3:     # 0 1 2  => 3번
#     print("안녕", num)
#     num += 1   # 복합 대입 연산자 num = num + 1 


# # 5 ~ 1 : 5번
# num = 5
# while num >= 1:
#     print("hello world", num)
#     num -= 1


# # while문 예제 01
# pushUp = 0

# while pushUp < 10:
#     pushUp += 1 #뒤와 같이 표현도 가능. pushUp = pushUp +1
#     print("푸쉬업 %s회 수행했습니다" % pushUp)
#     if pushUp == 10:
#         print("오늘 운동을 끝마칩니다.")


# 변수 초기화 선언을 내부에 하면 1씩 증가가 아닌 그냥 0만 출력되는 무한 루프를 돌게된다.
# while True :
#     a = 0
#     print(a)
#     a += 1


# # 무한루프
# while True:
#     print("무한루프")


# # 0은 거짓(False)   0이 아닌 수는 (True)
# while 1:
#     print("1 무한루프")



# # 1~100까지의 합(for문과 range함수 사용했을때...) for문에서 본 코드와 같아
# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)


# # while문 예제 02(1~100까지의 합)
# sum = 0
# num = 0
# while num < 100 :
#     num += 1
#     sum += num
# print(f"합산 결과는 다음과 같습니다. {sum}")


# # while문 예제03(문자열 다루기)
# number = 0
# msg = '''    1. Add
#     2. Del
#     3. List
#     4. Quit'''

# while number != 4 :
#     print(msg)
#     number = int(input("Enter Number : "))
# print("종료되었습니다.")


# # 무한 루프를 통해서 반복적으로 수를 입력을 받고 원하는 값이 입력 되었을때 반복문을 빠져 나오는 코드
# while True:
#     number = int(input("수를 입력하세요:"))
#     if number == 0 :
#         print("끝")
#         break


# # while문 예제04(나만의 리스트 만들기)
# while True :
#     listNum = int(input("리스트의 크기를 정하세요!"))
#     if listNum < 10 :
#         break
#     print("리스트의 크기를 10 이하로 다시 할당하세요!")

# a = 0
# result = []
# while a < listNum :
#     result.append(input("리스트에 값을 할당해 보세요! "))
#     a += 1
#     result_len = len(result)

# print(f"크기{result_len}의 리스트 {result}가 할당 되었어요")


# # while문 예제04(나만의 리스트 만들기) 또다른 풀이(랜덤함수 사용)
# import random
# listNum = int(input("리스트의 크기를 입력하세요"))
# a = 0
# lst =[]
# while a < listNum:
#     lst.append(random.randint(1, 10))
#     a += 1
# print(lst)


# # while문 예제05(break)
# sum = 0
# num = 0
# while True :
#     num += 1
#     sum += num
#     if num  == 100 : 
#         print(f"1부터 {num}까지의 덧셈 종료")
#         break
# print(f"결과 : {sum}")


# # while문 예제06(break)
# # 기본 while문 
# pushUp = 0
# while pushUp < 10:
#     pushUp += 1 
#     print("푸쉬업 %s회 수행했습니다" % pushUp)
# print("오늘 운동을 끝마칩니다.")

# # break 사용 
# pushUp = 0
# while True:
#     pushUp += 1
#     print("푸쉬업 %s회 수행했습니다" % pushUp)
#     if pushUp == 10:
#         print("오늘 운동을 끝마칩니다.")
#         break


# # while문 예제07(continue)
# number = 0
# while number < 100:
#     number = number +1
#     if number % 2 == 0:
#         continue
#     print(number, end=" ")


# # while문 예제08(continue - break)(푸쉬업)
# pushUp = 1

# while True:
#     if pushUp <= 10:
#         print("푸쉬업 %s회 수행했습니다" % pushUp)
#         pushUp += 1  # 뒤와 같이 표현도 가능. pushUp = pushUp +1
#         continue
#     print("오늘 운동을 끝마칩니다.")
#     break


# # while문 Final test01
# import random
# num_random = random.randint(1,5)
# while True :
#     guess_num = int(input("값을 맞춰보세요.(1~10중 하나를 적으세요) "))
#     if guess_num == num_random :
#         print("정답입니다.")
#         break
#     elif guess_num < num_random :
#         print("입력하신 값보다 더 큰값이에요~")
#     else :
#         print("입력하신 값보다 더 작은 값이에요~")


# # while문 Final test02
# msg = '''비 갠 뒤에 비애 대신 a happy end 
# 비스듬히 씩 비웃듯 칠색 무늬의 무지개 
# 철없이 철 지나 철들지 못해 (still)'''
# # msg_list = msg.split(" ")
# msg_list = msg.replace("\n","").split(" ")
# print(msg_list)
# num = 0
# print(len(msg_list))
# while num < len(msg_list) :
#     print(msg_list[num])
#     num += 1

# print("단어 개수 : ", num)