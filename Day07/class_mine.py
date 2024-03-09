# # # # 객체지향(class)을 사용하지 않고 하나의 프로그램을 만든다.
# # # # 회계관리 프로그램
# # # # 회사의 정보(기업이름, 영업일수, 일수익, 보너스 등)을 받아 처리하고 결과를 돌려주는...

# # # # 기능 1) 회사의 정보를 출력(리턴X)
# # # def print_profile(name, day, money) : # name = c_name ....
# # #     print(f"{name}기업의 영업일수는 {day}이고 일수익은 {money}입니다.")

# # # # 기능 2) 월수익을 계산(리턴O)
# # # def cal_monthly(day, money) :
# # #     return day * money

# # # # 기능 3) 보너스 금액을 합산하여 총 수익을 계산(메가스터디 전용)
# # # def bonus(b_money) :
# # #     # 기 계산된 월수익에 보너스를 합하여 리턴
# # #     global result_monthly_money
# # #     result_monthly_money += b_money

# # # # 기능 3) 보너스 금액을 합산하여 총 수익을 계산(타기업 전용)
# # # def bonus01(b_money) :
# # #     # 기 계산된 월수익에 보너스를 합하여 리턴
# # #     global result_monthly_money01
# # #     result_monthly_money01 += b_money

# # # # 데이터 할당 #1    
# # # c_name = "메가스터디"
# # # c_day = 23
# # # c_money = 300

# # # # print_profile() 호출부(기업이름, 영업일수, 일수익)
# # # print_profile(c_name, c_day, c_money)

# # # # cal_monthly() 호출부
# # # result_monthly_money = cal_monthly(c_day, c_money)
# # # print("보너스 합산 전 :", result_monthly_money)

# # # # bonus() 호출부
# # # bonus(1111)
# # # print("보너스 합산 후 :", result_monthly_money)

# # # # =================================================
# # # # 두번째 기업에 대한 호출
# # # # 데이터 할당 #2
# # # c_name01 = "삼성전자"
# # # c_day01 = 20
# # # c_money01 = 500

# # # print_profile(c_name01, c_day01, c_money01)
# # # result_monthly_money01 = cal_monthly(c_day01, c_money01)
# # # print(result_monthly_money01)
# # # bonus01(3333)
# # # print("보너스 합산 후 :", result_monthly_money01)


# # # -> 위 프로그램을 객체지향화(class) 해서 프로그래밍
# # # 클래스 선언부

# class Account :
#     # 생성자 메서드
#     def __init__(self, c_name, c_day, c_money) :
#         self.c_name = c_name
#         self.c_day = c_day
#         self.c_money = c_money

#     # # 메소드1) 데이터 셋팅
#     # def set_data(self, c_name, c_day, c_money) :
#     #     self.c_name = c_name
#     #     self.c_day = c_day
#     #     self.c_money = c_money

# #     # 메소드2) 회사의 정보를 출력(리턴X)
# #     def print_profile(self) :
# #         print(f"{self.c_name}기업의 영업일수는 {self.c_day}이고 일수익은 {self.c_money}입니다.")

# #     # 메소드3) 월수익을 계산(리턴O)
# #     def cal_monthly(self) :
# #         self.result_monthly_money = self.c_day * self.c_money
# #         return self.result_monthly_money

# #     # 메소드4) 보너스 금액을 합산하여 총 수익을 계산(메가스터디 전용)
# #     def bonus(self, b_money) :
# #         self.result_monthly_money += b_money

# # # 클래스 호출부(객체 생성) - 기업 1
# # a1 = Account("메가스터디", 23, 300)
# # # a1.set_data("메가스터디", 23, 300)
# # a1.print_profile()
# # a1.cal_monthly()
# # print("보너스 추가 전 월수익 :", a1.result_monthly_money)
# # a1.bonus(1111)
# # print("보너스 추가 후 월수익 :", a1.result_monthly_money)

# # # 클래스 호출부(객체 생성) - 기업 2
# # a2 = Account("LG", 21, 450)
# # # a2.set_data("LG", 21, 450)
# # a2.print_profile()
# # a2.cal_monthly()
# # print("보너스 추가 전 월수익 :", a2.result_monthly_money)
# # a2.bonus(2222)
# # print("보너스 추가 후 월수익 :", a2.result_monthly_money)

# # class Test :
# #     def __init__(self, c_name) :
# #         self.c_name = c_name

# # t1 = Test("메가스터디")
# # print(t1.c_name)


# # # 누적 계산기
# # class Cal :
# #     def __init__(self):
# #         self.result = 0
# #         print("self의 의미 :",self)
    
# #     def add(self, num) :
# #         self.result += num

# # c1 = Cal()
# # print("인스턴스 주소 :",c1)


# # class Sample :
# #     count = 0 # 클래스 변수
# #     def __init__(self, num) :
# #         self.unique_num = num # 인스턴스 변수
# #         Sample.count += 1

# # s1 = Sample(10)
# # print(s1.unique_num)
# # print(s1.count)

# # s2 = Sample(20)
# # print(s2.unique_num)
# # print(s1.count)
# # print(s2.count)

# # class Calculator :
# #     def __init__(self, x, y) :
# #         self.x = x
# #         self.y = y
# #         self.result = 0
    
# #     def add(self) :
# #         return self.x + self.y
    
# #     def sub(self) :
# #         self.result = self.x - self.y

# # cal_01 = Calculator(10, 20)
# # result = cal_01.add()
# # print(result)

# # cal_01.sub()
# # print(cal_01.result)


# # Ractangle 클래스를 구현하라
# # 생성자 : width(가로), height(세로) 인스턴스 변수 초기화
# # area 메서드 : 가로 * 세로 
# # circum 메서드 : (가로 + 세로) * 2

# # class Ractangle :
# #     # 데이터 셋팅
# #     def __init__(self, x, y) :
# #         self.x = x
# #         self.y = y
# #         self.result01 = 0
# #         self.result02 = 0
    
# #     # 넓이 구하는 기능
# #     def area(self) :
# #         self.result01 = self.x * self.y
   
# #     # 둘레 구하는 기능
# #     def circum(self) :
# #         self.result02 = (self.x + self.y)*2

# # # 객체 생성 하면서 데이터 세팅
# # r1 = Ractangle(3, 4)
# # r1.area()
# # print(r1.result01)
# # r1.circum()
# # print(r1.result02)
        

# class Parent_cal :
#     def add(self) :
#         print("더하기 기능 수행")

# # 상속
# class My_cal(Parent_cal) :
#     def __init__(self, x, y) :
#         self.x = x
#         self.y = y
#         self.result = 0

#     def sub(self) :
#         self.result = self.x - self.y

#     def div(self) :
#         self.result = self.x / self.y
    
# # # 메서드 오버라이딩(상속 받은 부모의 것을 수정하여 사용)
# # m1 = My_cal(1,2)
# # m1.div()
# # print(m1.result)

# # class child_cal(My_cal) :
# #     def div(self) :
# #         if self.y == 0 :
# #             print("0으로 나눌수 없습니다")
# #         else :
# #             super().div()
# #             # self.result = self.x / self.y
        
# # c1 = child_cal(1,0)
# # c1.sub()
# # print(c1.result)
# # c1.div()
# # print(c1.result)


# # 무기 클래스(검, 단도, 망치, 창 등등)
# class Weapon :
#     def __init__(self) :
#         self.what = "무기"
#         self.type = "근거리"
    
# class Sword(Weapon) :
#     def __init__(self) :
#         super().__init__()
#         self.power = 10
#         self.level = 5

# if __name__ == "__main__" :
#     s1 = Sword()
#     print(s1.what)
#     print(s1.type)
#     print(s1.power)
#     print(s1.level)

# print("__name__ :",__name__)