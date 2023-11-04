# # 회계관리 프로그램(하나의 기업이 아닌 여러 기업을 관장)
# # 기능 - 함수()
# # 1) 대상 회사의 정보 출력(이름?, 영업일수?, 일수익은 얼마인지?)
# def print_profile(name, day, money) :
#     print(f"회사의 이름은 {name}, 영업일수는 {day}이며 일수익은 {money}입니다")

# # 2) 월수익 계산(로직)
# def cal_monthly(day, money) :
#     return money * day
# # 3) 계산된 월수익에 추가 보너스?가 누적해서 더해지는...
# # def bonus(result, add_money) :
# #     return result + add_money
# def bonus(add_money) :
#     global result
#     result += add_money

# def bonus02(add_money) :
#     global result02
#     result02 += add_money


# name = "메가"
# day = 21
# money = 300
# print_profile(name, day, money)
# result = cal_monthly(day, money)
# print(f"월수익 : {result}")
# bonus(1111)
# print(f"보너스 추가된 월수익 : {result}")

# name02 = "이투스"
# day02 = 23
# money02 = 280
# print_profile(name02, day02, money02)
# result02 = cal_monthly(day02, money02)
# print(f"월수익 : {result02}")
# bonus02(2222)
# print(f"보너스 추가된 월수익 : {result02}")






# # 클래스를 이용해서 위 코드를 객체지향화 하는 작업
# # class 템플릿으로대표되는 이름(첫글자가 대문자) :
# class Account :
#     # 데이터 세팅작업을 대체할 생성자 메서드
#     def __init__(self, name, day, money) :
#         self.name = name
#         self.day = day
#         self.money = money
#         self.result = 0

#     # # 데이터 셋팅작업, 변수 초기화
#     # def set_data(self, name, day, money) :
#     #     self.name = name
#     #     self.day = day
#     #     self.money = money
#     #     self.result = 0
#     # 1)
#     def print_profile(self) :
#         print(f"회사의 이름은 {self.name}, 영업일수는 {self.day}이며 일수익은 {self.money}입니다")
#     # 2) 월수익 계산(로직)
#     def cal_monthly(self) :
#         # return self.money * self.day
#         self.result = self.money * self.day
#     # 3)
#     def bonus(self, bonus_money) :
#         # global result
#         # result += add_money
#         # 계산된 월수익 + bonus_money
#         self.result += bonus_money
# a = Account("메가", 21, 300)
# # a.set_data("메가", 21, 300)
# a.print_profile()
# a.cal_monthly()
# print("월수익 :",a.result)
# a.bonus(1111)
# print("보너스 추가된 월수익 :",a.result)

# b = Account()
# b.set_data("맥아", 23, 280)
# b.print_profile()
# b.cal_monthly()
# print("월수익 :",b.result)
# b.bonus(1111)
# print("보너스 추가된 월수익 :",b.result)



# # 생성자
# class Test :
#     def __init__(self, aaa) :
#         print(f"{aaa}")

# t1 = Test(111)


# # self의 의미
# class Test :
#     def __init__(self) :
#         print(f"self의 주소 : {self}")

# t1 = Test()
# print("t1인스턴스의 주소 :",t1)
# t2 = Test()
# print("t1인스턴스의 주소 :",t2)


# class Test :
#     no = 0
#     def __init__(self, sample) :
#         self.sample = sample
#         Test.no += 1

# t1 = Test(10)
# print(t1.sample)
# print(Test.no)

# t2 = Test(20)
# print(t2.sample)
# print(Test.no)


# class Calculator :
#     def __init__(self, x, y) :
#         self.x = x
#         self.y = y
#         self.result = 0
    
#     def add(self) :
#         self.result = self.x + self.y
    
#     def sub(self) :
#         self.result = self.x - self.y
#         print(self.result)

#     def mul(self) :
#         self.result = self.x * self.y
#         return self.result

# c1 = Calculator(10, 20)
# # 1)
# c1.add()
# print(c1.result)
# # 2)
# c1.sub()
# # 3)
# print(c1.mul())


# c2 = Calculator(20,30)
# c2.add()
# print(c2.result)



# #클래스(Calculator)의 생성자 메서드를 통해 인스턴스 변수 result를 0으로 초기화 하라
# class Calculator :
#     def __init__(self) :
#         # self.x = x
#         # self.y = y
#         self.result = 0
    
#     def sum(self, startNum, endNum) :
#         while startNum <= endNum :
#             self.result += startNum
#             startNum += 1
#         print(self.result)

# c1 = Calculator()
# c1.sum(1,10)


# class Calculator :
#     def __init__(self, x, y) :
#         self.x = x
#         self.y = y
#         self.result = 0
    
#     def sum(self) :
#         while self.x <= self.y :
#             self.result += self.x
#             self.x += 1
#         print(self.result)

# c1 = Calculator(1,10)
# c1.sum()


# class Ractangle :
#     def __init__(self, width, height) :
#         # self.width = 0
#         # self.height = 0
#         self.width = width
#         self.height = height

#     def area (self) :
#         self.result = self.width * self.height

# w = int(input("가로 : "))
# h = int(input("세로 : "))
# r1 = Ractangle(w, h)
# r1.area()
# print(r1.result)


# # 상속
# class Calculator_parent :
#     def __init__(self,x,y) :
#         self.x = x
#         self.y = y

#     def add(self) :
#         print(self.x+self.y)

#     def sub(self) :
#         print(self.x-self.y)

# class Calculator_child(Calculator_parent) :
#     def mul(self) :
#         print(self.x*self.y)

# class Calculator_child02(Calculator_child) :
#     def div(self) :
#         print(self.x/self.y)


# class New(Calculator_child02) :
#     def div(self) :
#         if self.y == 0 :
#             print("0으로 나눌수없습니다")
#         else : 
#             print(self.x/self.y)

# n1 = New(10,0)
# n1.div()

# ch = Calculator_child(20,30)
# ch.mul()
# c1 = Calculator_parent(10,20)
# c1.add()
# c1.sub()


class Weapon :
    def __init__(self) :
        self.what = "무기"
        self.type = "근거리"


class Sword(Weapon) :
    def __init__(self) :
        # super()의 역할 : 부모의 메서드를 참조
        super().__init__()
        self.power = 20
        self.level = 10
    
s1 = Sword()
print(s1.what)
# w1 = Weapon()
# print(w1.type)
# print(w1.what)
