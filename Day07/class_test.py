# # 회계관리 프로그램
# # 기능 1) 고객사의 정보를 받아서 회사의 정보를 출력해주는 기능
# #        고객사 정보(회사이름, 영업일수, 일수익)
# def print_profile(name, day, dailyMoney) :
#     print(f"고객사의 회사명은 {name}이고 영업일수는 {day}이며 일수익은 {dailyMoney}입니다.")

# # 기능 2) 월수익을 계산해서 돌려주거나 출력하는 기능
# def cal_money(day, dailyMoney) :
#     return day*dailyMoney

# # 기능 3) 계산된 월 수익에 보너스를 추가해서 돌려주는 기능
# def add_bonus(bonus) :
#     global monthlyMoney
#     monthlyMoney = monthlyMoney + bonus

# def add_bonus_01(bonus) :
#     global monthlyMoney_01
#     monthlyMoney_01 = monthlyMoney_01 + bonus

# name_01 = "이투스"
# day_01 = 23
# dailyMoney_01 = 180
# print_profile(name_01, day_01, dailyMoney_01)
# monthlyMoney_01 = cal_money(day_01, dailyMoney_01)
# print("월수익 : ", monthlyMoney_01)
# add_bonus_01(1111)
# print("보너스 추가된 월수익 : ", monthlyMoney_01)

# name = "메가"
# day = 21
# dailyMoney = 200
# print_profile(name, day, dailyMoney)
# monthlyMoney = cal_money(day, dailyMoney)
# print("월수익 : ", monthlyMoney)
# add_bonus(3333)
# print("보너스 추가된 월수익 : ", monthlyMoney)



# 회계관리 프로그램
# 기능 1) 고객사의 정보를 받아서 회사의 정보를 출력해주는 기능
#        고객사 정보(회사이름, 영업일수, 일수익)
# 기능 2) 월수익을 계산해서 돌려주거나 출력하는 기능
# 기능 3) 계산된 월 수익에 보너스를 추가해서 돌려주는 기능

# # 클래스 선언
# class Account :
#     # 데이터 셋팅 기능
#     def __init__(self, name, day, dailyMoney) :
#         self.name = name
#         self.day = day
#         self.dailyMoney = dailyMoney
#         self.result = 0
    
#     def print_profile(self) :
#         print(f"고객사의 회사명은 {self.name}이고 영업일수는 {self.day}이며 일수익은 {self.dailyMoney}입니다.")

#     def cal_money(self) :
#         self.result = self.day*self.dailyMoney

#     def add_bonus(self, bonus) :
#         self.result += bonus

# a2 = Account("이투스", 23, 180)
# a2.print_profile()
# print("월수익 계산 전 :",a2.result)
# a2.cal_money()
# print("월수익 계산 후 :",a2.result)
# a2.add_bonus(11111)
# print("보너스 추가 후 :",a2.result)


# # 객체 생성
# a1 = Account()
# # 객체 생성 후 메서드 호출
# name = "메가"
# day = 21
# dailyMoney = 200
# a1.set_data(name, day, dailyMoney)
# a1.print_profile()
# print("월수익 계산 전 :",a1.result)
# a1.cal_money()
# print("월수익 계산 후 :",a1.result)
# a1.add_bonus(3333)
# print("보너스 추가 후 :",a1.result)


# class Cal :
#     def __init__(self, check) :
#         print("실행되었습니다", check)

# c1 = Cal(1)


# class Sample :
#     def __init__(self) :
#         print("self의 의미 :", self)
# s1 = Sample()
# print("s1객체의 주소 :",hex(id(s1)))

# s2 = Sample()
# print("s2객체의 주소 :",hex(id(s2)))


# # 통장 개설
# class Sample :
#     # 클래스 변수
#     count = 0
#     def __init__(self, name) :
#         # 인스턴스 변수
#         self.name = name
#         Sample.count += 1

# s1 = Sample("이름1")
# print(s1.name)
# print("s1객체로 본 count", s1.count)
# s2 = Sample("이름2")
# print(s2.name)
# print("s2객체로 본 count", s2.count)
# print("s1객체로 다시 확인 해 본 count", s1.count)


# class Calculator :
#     def __init__(self, x, y) :
#         self.x = x
#         self.y = y
#         self.result = 0
    
#     def add(self):
#         return self.x + self.y
    
#     def sub(self) :
#         self.result = self.x - self.y

# cal_01 = Calculator(10, 20)
# result = cal_01.add()
# print("합계 :",result)

# cal_01.sub()
# print(cal_01.result)


# class Calculator :
#     def __init__(self) :
#         self.result = 0
    
#     def add(self, x):
#         self.result += x

# c1 = Calculator()
# c1.add(10)
# c1.add(20)
# c1.add(30)

# c2 = Calculator()
# c2.add(1)
# c2.add(2)
# c2.add(3)

# c1.add(30)
# print("c1의 계산값-진행중", c1.result)
# print("c2의 계산값-진행중", c2.result)


# class Ractangle :
#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height
    
#     def area(self) :
#         self.result = self.width * self.height

# width = 3
# height = 4

# r1 = Ractangle(width, height)
# r1.area()
# print(r1.result)


class calParent :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.result = 0

    def add(self) :
        self.result = self.x + self.y

class calChild(calParent) :
    def sub(self) :
        self.result = self.x - self.y
    
    def div(self) :
        self.result = self.x / self.y

class calChild_02(calChild) :
    def div(self) :
        if self.y == 0 :
            print("0으로 나눌수 없습니다")
        else : 
            # 이 기능은 부모의 코드로 대체 하고 싶은..
            super().div()
            # self.result = self.x / self.y

ch02 = calChild_02(10,1)
ch02.div()
print(ch02.result)

