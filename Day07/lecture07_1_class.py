# =======================================================================================
# # 클래스를 사용하지 않고 회계관리 프로그램을 만든다면...
# result = 0
# def account(company, day, money) : 
#     print(f"{company} 기업의 영업일수는 {day}이고 일수익은 {money}입니다. ")
    
#     global result
#     result += money*day
#     return result

# company = "mega"
# day = 20
# money = 100

# monthly_money = account(company, day, money)
# print(monthly_money)

# # # 새로운 회사가 사용을 요청한다면... 변수가 증가...
# # # 지금은 하나의 회사가 추가 되었으나 수십~ 수백개의 회사가 요청한다면...
# company1 = "mega1"
# day1 = 21
# money1 = 101

# monthly_money2 = account(company1, day1, money1)
# print(monthly_money2)
# =======================================================================================


# =======================================================================================
# # 이와같은 방법으로 변수 관리를 할수도 있겠지만... 이는 객체지향과는 거리가 멀다...
# list_cName = ["mega1", "mega2", "mega3"]
# list_day = ["day1", "day2", "day3"]
# list_money = ["money1", "money2", "money3"]
# =======================================================================================


# =======================================================================================
# # 전부다 클래스
# print(type(3))
# print(type(3.1))
# print(type('3'))
# print(type([]))
# print(type(()))
# =======================================================================================


# =======================================================================================
# # 클래의 기본 구조
# class account :
#     pass

# company_A = account()
# print(type(company_A), id(company_A))
# company_B = account()
# print(type(company_B), id(company_B))
# =======================================================================================


# =======================================================================================
# # 클래스 구성 하나하나 천천히
# class account :
#     # 변수를 할당하는 역할을 하는 메소드(함수)
#     def set_data (self, name, day, money) :
#         self.name = name
#         self.day = day
#         self.money = money
#         self.result = 0
#     # 인스턴스 변수를 이용해 월수익을 계산하는 역할을 하는 메소드(함수)    
#     def sumMoney(self) :
#         for i in range(self.day) : 
#             self.result += self.money
#         return self.result
#     # 월수익에 보너스를 추가하여 누적시키는 역할을 하는 메소드(함수)
#     def bonus_add(self, bouns) :
#         self.result += bouns

# # account클래스를 이용해 company_A인스턴스(객체)를 생성
# company_A = account()
# company_A.set_data('mega', 20, 100)
# # print(company_A.__dict__,'네임 스페이스')
# print("="*25)
# print("상호명   :", company_A.name)
# print("영업일수 :", company_A.day)
# print("일수익   :", company_A.money)
# print("월수익   :", company_A.sumMoney())

# # 기존 result에 bouns를 추가 누적 시키는 역할
# company_A.bonus_add(1000)
# print("보너스 추가된 금액 : ",company_A.result)
# # print(company_A.bonus)                # 해당 변수는 인스턴스 변수가 아닌 매개 변수로 함수 종료후 사라짐 출력X
# print("="*25)

# # # account클래스를 이용해 company_B인스턴스(객체)를 생성
# company_B = account()
# company_B.set_data('samsung', 22, 300)
# print("상호명   :", company_B.name)
# print("영업일수 :", company_B.day)
# print("일수익   :", company_B.money)
# print("월수익   :", company_B.sumMoney())
# print("="*25)
# =======================================================================================


# =======================================================================================
# # 지금까지 배운 내용을 정리해보면 파이썬의 클래스를 이용하면 프로그래머가 원하는 새로운 타입을 만들 수 있다.
# # 생성된 타입은 변수에 데이터를 할당하고 그 데이터를 처리하는 메서드(함수)로 구성돼 있다.
# =======================================================================================


# =======================================================================================
# # 함수를 이용해 하나의 값을 누적해서 이를 해결하기 위해 global//재할당 방법을 사용했으나
# result = 0
# def add(num) : 
#     global result
#     result += num
#     return result
# print(result)
# add(10)
# add(10)
# print(result)
# =======================================================================================


# =======================================================================================
# # 클래스를 사용한다면 아래와 같이 사용가능하다
# class Calculator :
#     # 클래스 변수 사용을 통한 채번/넘버링
#     count = 0
#     def __init__(self) :
#         self.result = 0
    
#     def plus(self, num) :
#         Calculator.count += 1
#         self.result += num
#         return self.result

# cal_a = Calculator()
# cal_a.plus(100)
# print("Plus 함수 수행횟수 : ", cal_a.count)
# cal_a.plus(100)
# print("Plus 함수 수행횟수 : ", cal_a.count)
# print(cal_a.result)

# cal_b = Calculator()
# cal_b.plus(300)
# print("Plus 함수 수행횟수 : ", cal_b.count)
# print(cal_b.result)
# =======================================================================================


# =======================================================================================
# # 클래스에 생성자로 변수를 초기화 해보자
# # 생성자 테스트
# class test_init :
#     def __init__(self) :
#         print("생성자 입니다.")

# test_print = test_init()
# =======================================================================================


# =======================================================================================
# # 앞선 코드 중 set_data 메소드를 __init__메소드로 변형
# class account :
#     # 변수를 할당하는 역할을 하는 메소드(함수)
#     def __init__(self, name, day, money) :
#         self.name = name
#         self.day = day
#         self.money = money
#         self.result = 0
#     # 인스턴스 변수를 이용해 월수익을 계산하는 역할을 하는 메소드(함수)    
#     def sumMoney(self) :
#         for i in range(self.day) : 
#             self.result += self.money
#         return self.result
#     # 월수익에 보너스를 추가하여 누적시키는 역할을 하는 메소드(함수)
#     def bonus_add(self, bouns) :
#         self.result += bouns

# # account클래스를 이용해 company_A인스턴스(객체)를 생성
# company_A = account('mega', 20, 100)
# # company_A.set_data('mega', 20, 100)
# print(company_A.__dict__,'네임 스페이스')
# print("="*25)
# print("상호명   :", company_A.name)
# print("영업일수 :", company_A.day)
# print("일수익   :", company_A.money)
# print("월수익   :", company_A.sumMoney())

# # 기존 result에 bouns를 추가 누적 시키는 역할
# company_A.bonus_add(1000)
# print("보너스 추가된 금액 : ",company_A.result)
# # print(company_A.bonus)                        # 해당 변수는 인스턴스 변수가 아닌 매개 변수로 함수 종료후 사라짐 출력X
# print("="*25)

# # account클래스를 이용해 company_B인스턴스(객체)를 생성
# company_B = account('samsung', 22, 300)
# # company_B.set_data('samsung', 22, 300)
# print("상호명   :", company_B.name)
# print("영업일수 :", company_B.day)
# print("일수익   :", company_B.money)
# print("월수익   :", company_B.sumMoney())
# print("="*25)
# =======================================================================================


# =======================================================================================
# # 메서드의 첫 번째 인자는 항상 self여야 한다고 했습니다.
# # 하지만 메서드의 첫 번째 인자가 항상 self여야 한다는 것은 사실 틀린 말입니다. 
# # 이번 절에서는 파이썬 클래스에서 self의 정체를 확실히 이해하자

# # func1() 메서드의 첫 번째 인자가 self가 아님에도 클래스를 정의할 때 
# # 에러가 발생하지 않는다는 점입니다.
# class Foo:
#     def func1():
#         print("function 1")
#     def func2(self):
#         print(id(self), self)
#         print("function 2")


# f = Foo()
# print(id(f), f)
# f.func2()
# # f.func1()
# Foo.func1()
# =======================================================================================


# =======================================================================================
# # 클래스변수와 인스턴스 변수
# class Account:
#     num_accounts = 0
#     def __init__(self, name):
#             self.name = name
#             Account.num_accounts += 1
            
# print(Account.num_accounts)
# # print(Account.name)
# test_A = Account ('CHI1')
# print(test_A.num_accounts, test_A.name)
# test_B = Account ('CHI2')
# print(test_B.num_accounts, test_B.name)
# test_A.num_accounts = 100
# test_c = Account ('CHI3')
# print(test_c.num_accounts, test_c.name)
# test_d = Account ('CHI4')
# print(test_d.num_accounts, test_d.name, test_d.__dict__)
# print(test_A.num_accounts, test_A.name, test_A.__dict__)
# print(test_B.num_accounts)
# =======================================================================================


# =======================================================================================
# # 클래스변수와 인스턴스 변수
# class Calculator:
#     cal_number = 0
#     def __init__(self, first, second):
#         Calculator.cal_number += 1
#         self.first = first
#         self.second = second
    
#     def add(self):
#         result = self.first + self.second
#         return result

#     def mul(self):
#         result = self.first * self.second
#         return result
#     print("클래스 입니다.")
    
# cal_01 = Calculator(30, 40)
# print(cal_01.cal_number, "cal_01")
# Calculator.cal_number = 100
# cal_02 = Calculator(30, 40)
# print(cal_02.cal_number, "cal_02")
# print(cal_01.cal_number, "cal_01")
# =======================================================================================