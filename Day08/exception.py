# while True :
#     try : 
#         num01 = int(input("분자 입력 : "))
#         num02 = int(input("분모 입력 : "))
#         print(num01/num02)
#     # #모든 에러를 다 잡아...
#     # except :
#     #     print("어떠한 오류 발생")
#     except ValueError as ve:
#         print(f"[{ve}], 정수를 입력하셔야 합니다.")
#     except ZeroDivisionError as zde:
#         print(f"[{zde}],0으로 나눗셈 불가 합니다.")
#     # 에러가 발생하지 않았을 때 수행되는 코드
#     else :
#         print("에러가 발생하지 않았습니다.")
#         break
#     # 에러가 발생하건 하지 않건 수행되는 코드
#     finally :
#         print("수행1111111111111111111111")



# # x = [10, 30, 25.2, 'num', 14, 51] 
# # for item in x :
# #     try :
# #         print(item**2)
# #     except :
# #         print("제곱할 수 없습니다")

# 부모클래스
class Animal :
    def move(self) :
        print("오버라이딩 하여 사용하길 원합니다.")
        raise Exception


class Tiger(Animal) :
    def move(self) :
        print("오버라이딩 사용합니다.")
      

t1 = Tiger()
t1.move()