# # 예외 처리, try except 기본 구조 구문
# while True:
#     try :
#         first = int(input("분자를 입력하세요 : "))
#         second = int(input("분모를 입력하세요 : "))
#         print(first / second)
#         break
#     except :
#         print("오류입니다.")


# 연습문제
# 현재 이 코드는 오류가 난다. 이를 예외처리를 통해 처리하라
# print('프로그램 시작!')
# x = [10, 30, 25.2, 'num', 14, 51]

# for i in x :
#     print(i)
#     y = pow(i,2)
#     print(f'대상 = {i}, 제곱값 = {y}')

# print('프로그램 종료!')


# print('프로그램 시작!')
# x = [10, 30, 25.2, 'num', 14, 51]

# for i in x :
#     try :
#         print(f"======={i}=======")
#         y = pow(i,2)
#         print(f'대상 = {i}, 제곱값 = {y}')
#     except TypeError as err:
#         print(f'{err}, {i}는 숫자가 아닙니다.')

# print('프로그램 종료!')



# 예외 처리, try except 구조 발전
# while True:
#     try:
#         first = int(input("분자를 입력하세요 : "))
#         second = int(input("분모를 입력하세요 : "))
#     except ValueError as ve:
#         print(ve,"숫자를 입력해주세요.")
#         continue
#     try:
#         result = (first / second)
#     except ZeroDivisionError as ze:
#         print(ze, ": 0으로 나누지 말아주세요.")
#         break
#     except Exception as e:
#         print("오류입니다.")
#     else:
#         print("나눗셈 값 입니다.", result)
#     finally:
#         print("결과를 확인하세요")



# 에러 강제를 통해 상속을 유도 한다.
# class Bird:
#     def fly(self):
#         print("상속 후 꼭 오버라이딩 하여 사용하시오.")
#         raise Exception

# class Eagle(Bird):
#     print("독수리 입니다.")
#     # def fly(self):
#     #     print("빠르게 다닙니다.")

# eagle1 = Eagle()
# eagle1.fly()