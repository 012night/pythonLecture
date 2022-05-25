# # 예외 처리, try except 기본 구조 구문
# while True:
#     first = input("분자를 입력하세요.")
#     second = input("분모를 입력하세요")
#     try:
#         print(first / second)
#     except:
#         print("오류입니다.")


# # 예외 처리, try except 구조 발전
# while True:
#     try:
#         first = int(input("분자를 입력하세요."))
#         second = int(input("분모를 입력하세요"))
#     except ValueError as ve:
#         print(ve,"숫자를 입력해주세요.")
#         continue
#     try:
#         result = (first / second)
#     except ZeroDivisionError as ze:
#         print(ze, ": 0으로 나누지 말아주세요.")
#     except Exception as e:
#         print("오류입니다.")
#     else:
#         print("나눗셈 값 입니다.", result)
#     finally:
#         print("결과를 확인하세요")



# 에러 강제를 통해 상속을 유도 한다.
# class Bird:
#     def fly(self):
#         print("상속을 받아서 사용하시오.")
#         raise Exception

# class Eagle(Bird):
#     print("독수리 입니다.")
#     def fly(self):
#         print("빠르게 다닙니다.")

# eagle1 = Eagle()
# eagle1.fly()