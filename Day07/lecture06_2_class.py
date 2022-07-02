# 클래스의 기본 구조와 활용법
class Calculator:
    def __init__(self):
        self.result = 0
    def numSum(self, a):
        self.result += a
        # return self.result

acompany = Calculator()
acompany.numSum(10)
print(acompany.result)

#b사
bcompany = Calculator()
bcompany.numSum(20)
print(bcompany.result)
bcompany.numSum(20)
print(bcompany.result)
print(acompany.result)
lista = [acompany, bcompany]

##########################################################################################
#000000000000000000000000000000000000000000000000000000
# 누적이 안되는 함수예제
result = 0

def account(company, day, money) : 
    print(f"{company} 기업의 영업일수는 {day}이고 일수익은 {money}입니다. ")
    
    result = 0
    result += money
    return result

company = "mega"
day = 20
money = 100

result1 = account(company, day, money)
print(result1)

company1 = "mega1"
day1 = 21
money1 = 101
result2 = account(company1, day1, money1)
print(result2)


#1111111111111111111111111111111111111111111111111111111111
# #전부다 클래스야~
# print(type(3))
# type(3.1)
# type('3')
# type([])
# type(())



#22222222222222222222222222222222222222222222222222222222222
# class account :
#     pass

# a_account = account()
# print(type(a_account), id(a_account))
# b_account = account()
# print(type(b_account), id(b_account))



#3333333333333333333333333333333333333333333333333333333333
# class account :
#     def set_data (self, name, day, money) :
#         self.name = name
#         self.day = day
#         self.money = money
#         self.result = 0
        
#     def sumMoney(self) :
#         for i in range(self.day) : 
#             self.result += self.money
#         return self.result


    
# a_account = account()
# a_account.set_data('메가', 30, 100)

# print(a_account.__dict__)

# print(a_account.name)
# print(a_account.day)
# print(a_account.money)
# print(a_account.sumMoney())

#444444444444444444444444444444444444444444444444444444444
# b_account = account()
# b_account.set_data('삼성전자', 25, 200)
# print(b_account.name)
# print(b_account.day)
# print(b_account.money)
# print(b_account.sumMoney())














#이를 해결하기위해 global을 썻으나 중간의 결과값을 어딘가에서 사용하기 위해서는
#각기 다른 변수를 선언하고 그에 알맞게 할당하는 행위를 하면서 점차 관리 범위가 많아진다.
# result = 0
# def add(num) : 
#     global result
#     result += num
#     return result

# result1 = add(10)
# print(result1)
# result2 = add(result1)
# print(result2)



#그리하여 나온 개념이 클래스...
# class Calculator :
#     count = 0

#     def __init__(self) :
#         self.result = 0
    
#     def plus(self, num) :
#         self.result += num
#         return self.result

   
# cal_a = Calculator()
# cal_a.plus(100)
# cal_a.plus(100)
# print(cal_a.result)

# cal_b = Calculator()
# cal_b.plus(300)
# print(cal_b.result)




#클래스는 반복되는 변수 & 함수를 미리 정해 놓은 틀이자 설계도 이다.
#클래스가 왜 필요한가? 월매출을 계산 해주는 프로그램이 있다고 생각해보자. 
#이걸 A사에서 사용하고, B사에서도 사용한다고 생각하면...
############################### 1단계
#틀린 합계가 발생. 왜냐하면 사용주체별로 별도로 사용해야 하는 프로그램인데, 
#위와 같이 사용하면 누적이 되어 문제 발생.
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
# # day = 1
# # result = 0
# while day < 31 :
#     day += 1
#     print(f"b사의 일매출 {monthlySum(2000)}")
# print(f"b사의 월매출 {result}")



# 애써 바꾸면 이런식으로 할수는 있겠으나... 
# 누적된 값에 한번 더 더하기 연산을 하고 싶다면 어떻게 해야될까?
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

# 클래스를 선언하고 같은 작업을 해보자
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
# cal_a.setData(10, 30)
# aSum = cal_a.monthlySum()
# print(aSum)
# # print(cal_a.day)               # 이건 출력되고
# # print(cal_a.monthly_result)    # 이건 출력이 안돼 왜그럴까?

# #b사
# cal_b = Calculator()
# cal_b.setData(20, 30)
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




# #사칙연산 클래스 만들어보기.
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
# #     print("클래스 입니다.")

# class1 = Calculator(10,20) 
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

# class1 = Calculator(10,20) 
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




#클래스 연습 3
# class Rectangle :
#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height
    
#     def area(self) :
#         area = self.width * self.height
#         return area
    
#     def circum(self) :
#         circum = (self.width + self.height)*2
#         return  circum
    

# print("사각형의 넓이와 둘레를 계산하라.")
# w = int(input("가로 : " ))
# h = int(input("가로 : " ))

# rec = Rectangle(w, h)
# area = rec.area()
# print('='*20)
# print("넓이", area)

# circum = rec.circum()
# print("둘레 :", circum)
# print('='*20)




# #클래스의 상속 후 메서드를 추가해보자
# #클래스 상속, 오버라이딩 실습
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
# #     print("클래스 입니다.")


# class CalculatorA(Calculator):
#     def div(self):
#         result = self.first / self.second
#         return result

# classA = CalculatorA(20, 0)
# # print(classA.div())
# print(classA.add())
# print(classA.mul())




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
# # class Sword(Weapone):
# #     def __init__(self, power, level):
# #         self.power = power
# #         self.level = level

# # #Sword 클래스 정의 : Weapone 클래스 상속 후 생성자 상속 super()
# class Sword(Weapone):
#     def __init__(self, power, level):
#         super().__init__()
#         self.power = power
#         self.level = level

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
# class Calculator:
#     first_class = 20
#     # second = 30
#     # def __init__(self, first, second):
#     #     self.first = first
#     #     self.second = second
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
    
# class1 = Calculator()
# print(class1.first_class, "클래스1")
# Calculator.first_class = 100
# print(class1.first_class, "클래스1")
# class2 = Calculator()
# print(class2.first_class, "클래스2")
# print(class1.first_class, "클래스1")





#클래스변수 사용예쩨
# class cal :
#     result = 0
#     def __init__(self, num) :
#         self.num = num
#         cal.result += 1
    
#     def test (self) :
#         self.num += 100

# print(dir())
# print(cal.__dict__)

# cal_a = cal(10)
# print(cal_a.result)

# cal_b = cal(20)
# print(cal_b.result)
# print(cal_a.result)




# def add(x, y) :
#     result = x + y
#     return result
