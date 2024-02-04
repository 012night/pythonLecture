# while True : 
#     try :
#         num01 = int(input("분자 입력 : "))
#         num02 = int(input("분모 입력 : "))
#         print("결과 :", num01/num02)
#     except ValueError as ve:
#         print(f"[{ve}] : 에러 발생 재입력 요망")
#     except ZeroDivisionError as zde :
#         print(f"[{zde}] : 0으로 나눌수 없습니다.")
#     else :
#         print("정상 수행되었습니다. 에러X")
#         break
#     finally :
#         print("에러 유무와 관계없이 수행 됩니다.")

class Parent :
    def speak(self) :
        print("상속 후 오버라이딩 하여 사용 하세요")
        raise Exception


class Mine(Parent) :
    def speak(self) :
        print("오버라이딩 하여 사용중입니다.")

m1 = Mine()
m1.speak()