# # # # 회사의 월수익을 계산해주는 프로그램

# # # # 1)회사의 정보를 출력하는 기능
# # # def print_company(name, money, day) :
# # #     print(f"[회사명] : {name}, [영업일수] : {day}, [일수익] : {money}")

# # # # 2)월수익을 계산해주는 기능
# # # def cal_monthly(money, day) :
# # #     # 영업일수 * 일수익
# # #     return money*day

# # # # 3)기존 계산된 월 수익에 추가 수입을 더해 최종 금액을 출력해주는 기능
# # # # 메가 전용 함수
# # # def bonus(add_money) :
# # #     global result
# # #     result += add_money
# # # # 이투스 전용 함수
# # # def bonus01(add_money) :
# # #     global result01
# # #     result01 += add_money

# # # # *전달정보 : 회사의 이름, 일수익, 영업일수
# # # name = "메가"
# # # money = 200
# # # day = 21
# # # print_company(name, money, day)
# # # result = cal_monthly(money, day)
# # # print("월수익 :", result)
# # # bonus(7777)
# # # print("보너스 추가된 월수익 :", result)

# # # ###################################################

# # # name01 = "이투스"
# # # money01 = 170
# # # day01 = 25
# # # print_company(name01, money01, day01)
# # # result01 = cal_monthly(money01, day01)
# # # print("월수익 :", result01)
# # # bonus01(7777)
# # # print("보너스 추가된 월수익 :", result01)



# # # # 위와 같은 기능을 하는 코드를 클래스화(객체지향)

# # 클래스 정의부
# class account :
#     # 생성자 메서드 역할
#     def __init__(self, name, money, day) :
#         self.name = name
#         self.money = money
#         self.day = day

#     # 1)회사의 정보를 출력하는 기능
#     def print_company(self) :
#         print(f"[회사명] : {self.name}, [영업일수] : {self.day}, [일수익] : {self.money}")

#     # 2)월수익을 계산해주는 기능
#     def cal_monthly(self) :
#         # 영업일수 * 일수익
#         self.result = self.money * self.day

#     # 3)기존 계산된 월 수익에 추가 수입을 더해 최종 금액을 출력해주는 기능
#     def bonus(self, add_money) :
#         self.result += add_money

# # 클래스 호출하는 방식 -> 인스턴스 생성 과정
# mega = account("메가", 200, 21)
# # mega.set_data(name, money, day)
# mega.print_company()
# mega.cal_monthly()
# mega.bonus(777)
# print(mega.result)








# # etus = account()
# # etus.set_data("이투스", 100, 25)
# # etus.print_company()

# # # etus.cal_monthly()
# # # etus.bonus(777)
# # # print(etus.result)








# # # class Sample :
# # #     def print(self) :
# # #         print(self, "self라는 변수의 의미")

# # # mega = Sample()
# # # print(mega, "mega 인스턴스")
# # # mega.print()


# # # sam = Sample()
# # # print(sam, "sam 인스턴스")
# # # sam.print()





# # class Calculator :
# #     # __init__의 목적
# #     # def __init__(self) :
# #     #     pass
# #     def __init__(self, name, day, money) :
# #         self.name = name
# #         self.day = day
# #         self.money = money
    
# # c1 = Calculator("메가", 21, 200)
# # print(c1.name)
# # print(c1.day)
# # print(c1.money)
# # c2 = Calculator()


# class Cal :
#     def __init__(self, num01, num02) :
#         self.num01 = num01
#         self.num02 = num02
    
#     def add(self) :
#         return self.num01 + self.num02

#     def sub(self) :
#         self.result = self.num01 - self.num02

# c1 = Cal(10,20)
# print(c1.add()) # 덧셈결과
# c1.sub() # 뺄셈결과
# # 뺄셈 결과출력
# print(c1.result)

# c1.mul() # 곱셈결과



# Ractangle 클래스를 구현하라
# 생성자 : width(가로), height(세로) 인스턴스 변수 초기화
# area 메서드 : 가로 * 세로 
# circum 메서드 : (가로 + 세로) * 2


# class Ractangle :
#     def __init__(self, w, h) :
#         self.width = w
#         self.height = h
    
#     def area(self) :
#         # return w*h
#         return self.width * self.height

#     def circum(self) :
#         self.result = 2*(self.width + self.height)

# r1 = Ractangle(3,4)
# print(r1.area())

# r1.circum()
# print(r1.result)

# ##상속##
# #부모 클래스
# class Parent_cal :
#     def add(self) :
#         print("더하기 기능입니다")

# #L2 자식 클래스
# class Child_class(Parent_cal) :
#     def sub(self) :
#         print("빼기 기능입니다")
    
# # L3 자식 클래스
# class Child02_class(Child_class) :
#     def sub(self) :
#         print("L3 자식 클래스에서 재구현 해놓은 빼기 기능입니다")

# c2 = Child02_class()
# c2.sub()


class Cal :
    def __init__(self, x, y) :
        self.x = x 
        self.y = y
        self.result = 0

    def div(self) :
        self.result = self.x / self.y

# c1 = Cal(10,2)
# c1.div()
# print(c1.result)

class child(Cal) :
    def div(self) :
        if  self.y == 0 :
            print("0으로 나눌수 없습니다")
        else :
            self.result = self.x / self.y
c2 = child(10,0)
c2.div()
print(c2.result)

