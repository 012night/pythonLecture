#클래스의 기본 구조와 활용법
# class Calculator:
#     def __init__(self):
#         self.result = 0
#     def lumSum(self, a):
#         self.result += a
#         return self.result
#
# acompany = Calculator()
# aSum = acompany.lumSum(10)
# print(aSum)

# #b사
# bcompany = Calculator()
# bSum = bcompany.lumSum(20)
# print(bSum)
# bSum = bcompany.lumSum(20)
# print(bSum)




#클래스는 반복되는 변수 & 함수를 미리 정해 놓은 틀이자 설계도 이다.
#클래스가 왜 필요한가? 월매출을 계산 해주는 프로그램이 있다고 생각해보자. 
#이걸 A사에서 사용하고, B사에서도 사용한다고 생각하면...
# result = 0
# def monthlySum(a):
#     global result
#     result += a
#     return result

# #a사
# day = 1
# while day < 31 :
#     day += 1
#     print(f"a사의 일매출 {monthlySum(1000)}")
# print(f"a사의 월매출 {result}")

# #b사
# while day < 31 :
#     day += 1
#     print(f"b사의 일매출 {monthlySum(2000)}")
# print(f"b사의 월매출 {result}")

#틀린 합계가 발생. 왜냐하면 사용주체별로 별도로 사용해야 하는 프로그램인데, 
#위와 같이 사용하면 누적이 되어 문제 발생.





#애써 바꾸면 이런식으로 할수는 있겠으나... 누적된 값에 한번 더 더하기 연산을 하고 싶다면 어떻게 해야될까?
# def monthlySum(a, day):
#     result = 0
#     while day < 31 :
#         result += a
#         day += 1
#     return result

# #a사
# print(f"a사의 일매출 {monthlySum(1000, 1)}")

# #b사
# print(f"b사의 일매출 {monthlySum(2000, 1)}")




#이를 해결하기 위해 클래스가 등장. 
# 붕어빵틀만 제공하고 각각 필요한 붕어빵을 그때 그때 만들어 쓰는것.



##클래스를 선언하고 같은 작업을 해보자
# class Calculator :
#     def setData(self, money, day) :
#         self.money = money
#         self.day = day
        
#     def monthlySum(self) :
#         monthly_result = 0
#         num = 0
#         while num < self.day :
#             num += 1
#             monthly_result += self.money
#         return monthly_result

# #a사
# cal_a = Calculator()
# aSum = cal_a.setData(10, 30)
# aSum = cal_a.monthlySum()
# print(aSum)
# # print(cal_a.day)               # 이건 출력되고
# # print(cal_a.monthly_result)    # 이건 출력이 안돼 왜그럴까?

# #b사
# cal_b = Calculator()
# bSum = cal_b.setData(20, 30)
# bSum = cal_b.monthlySum()
# print(bSum)




#클래스에 생성자로 변수를 초기화 해보자
# class Calculator :
#     def __init__(self, money, day) :
#         self.money = money
#         self.day = day
        
#     def monthlySum(self) :
#         monthly_result = 0
#         num = 0
#         while num < self.day :
#             num += 1
#             monthly_result += self.money
#         return monthly_result

# #a사
# cal_a = Calculator(10,30)
# aSum = cal_a.monthlySum()
# print(aSum)

# #b사
# cal_b = Calculator(20,30)
# bSum = cal_b.monthlySum()
# print(bSum)




#사칙연산 클래스 만들어보기.
# class Calculator:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result

#     def mul(self):
#         result = self.first * self.second
#         return result

#     print("클래스 입니다.")

# class1 = Calculator(10,20)  #클래스를 객체화 하면 바로 프린트문이 바로 실행된다. 코드의 흐름 및 순서를 생각해보자
# class1.setdata(30, 40)      # 오류가 난다 왜? init이 가장 먼저 도니깐
# result = class1.add()
# print(result)               #class1.result? 로 받아올순 없을까? 시도해보자





# #리턴값이 없는 함수라면 이렇게 접근 해야겠지?
# class Calculator:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#         self.result = 0

#     def add(self):
#         self.result = self.first + self.second

#     print("클래스 입니다.")

# class1 = Calculator(10,20)  #클래스를 객체화 하면 바로 프린트문이 바로 실행된다. 코드의 흐름 및 순서를 생각해보자
# result = class1.add()
# print(result)               #값이 있니?
# print(class1.result)        #이렇게 해보자~




#클래스 연습 2
# class Calculator :
#     def __init__(self) :
#         self.result = 0
    
#     def sum(self, startNum) :
#         self.result += startNum


# sumA = Calculator()

# endNum = int(input("몇까지 더하실껀가요? : "))
# startNum = 0

# while startNum < endNum :
#     startNum += 1
#     sumA.sum(startNum)

# print(sumA.result)





# #클래스의 상속 후 메서드를 추가해보자
# #클래스 상속, 오버라이딩 실습
# class Calculator :
#     def __init__(self, first, second) :
#         self.result = 0
#         self.first = first
#         self.second = second
    
#     def sum(self, startNum) :
#         self.result += startNum


# class CalculatorA(Calculator):
#     def div(self):
#         result = self.first / self.second
#         return result

# classA = CalculatorA(20, 0)
# # print(classA.div())




# #상속을 받은 후 수정을 해볼까?
# class CalculatorB(CalculatorA):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             result = self.first / self.second
#         return result
# classB = CalculatorB(20,0)
# print(classB.div())




# #super()
# #Weapone 클래스 정의
# class Weapone:
#     def __init__(self):
#         self.what = "무기"
#         self.type = "근거리"
#     print("나는 무기 클래스다!")

# # Sword 클래스 정의 : Weapone 클래스 상속
# class Sword(Weapone):
#     def __init__(self, power, level):
#         self.power = power
#         self.level = level

# # #Sword 클래스 정의 : Weapone 클래스 상속 후 생성자 상속 super()
# # class Sword(Weapone):
# #     def __init__(self, power, level):
# #         super().__init__()
# #         self.power = power
# #         self.level = level

# #Sword 속성(power,level) 및 부모 클래스 Weapon 의 속성 불러오기(what, type)
#     def info(self):
#         print("공격력 : ",self.power)
#         print("필요레벨 : ",self.level)
#         print("무기종류 : ", self.what)
#         print("공격타입 : ", self.type)
# #Sword 클래스 객체 short_sword 선언
# short_sword = Sword(10, 20)
# short_sword.info()





#클래스변수와 인스턴스 변수
class Calculator:
    first_class = 20
    # second = 30
    # def __init__(self, first, second):
    #     self.first = first
    #     self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    print("클래스 입니다.")
    
class1 = Calculator()
Calculator.first_class = 100
print(class1.first_class, "클래스1")
class2 = Calculator()
print(class2.first_class, "클래스2")


# def add(x, y) :
#     result = x + y
#     return result
