# import employee_parent
from employee_parent import Employee

# class Permanent(employee_parent.Employee) :
class Permanent(Employee) :
    def __init__(self, name, emptype, money, bouns) :
        super().__init__(name, emptype)
        self.pay = money + bouns
    
    def print_profile(self) :
        super().print_profile()
        print(f"급여 : {self.pay}")

# class Temporary(employee_parent.Employee) :
class Temporary(Employee) :
    pass


# p1 = Permanent(1,2,3,4)
# p1.print_profile()
while True :
    choice = input("고용형태 선택(정규직<P>, 비정규직<T>) : ").upper()
    if choice == "P" or choice == "T" :
        break
    else :
        print("다시 입력하세요 :")

if choice == "P" :
    name = input("이름 입력 : ")
    choice = "정규직"
    while True :
        try :
            money = int(input("기본급 : "))
            bonus = int(input("보너스 : "))
            break
        except ValueError as ve :
            print(f"[{ve}], 문자입력 불가!")

    p1 = Permanent(name,choice,money,bonus)
    p1.print_profile()
# else :
#     name = input("이름 입력 : ")
#     choice = "비정규직"
#     while True :
#         try :
#             time = int(input("시급 : "))
#             t_money = int(input("시간 : "))
#             break
#         except ValueError as ve :
#             print(f"[{ve}], 문자입력 불가!")

#     t1 = Temporary(name,choice,time,t_money)
#     t1.print_profile()
