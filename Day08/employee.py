# import employee_parent
from employee_parent import Employee

class Permanent(Employee) :
    def __init__(self, name, emptype, money, bonus):
        super().__init__(name, emptype)
        self.money = money
        self.bonus = bonus
        self.pay = money + bonus
    
    def print_profile(self):
        super().print_profile()
        print(f"급여 : {self.pay}")

# class Temporary(Employee) :
#     pass


# 무조건 P 또는 T만 받게 할거야... 정확한 값을 받을때까지...
while True :
    emptype = input("고용형태 입력(정규직<P>, 비정규직<t>) : ").upper()
    if emptype == "T" or emptype == "P" :
    # if emptype in ["p", "P", "t", "T"] :
        break
    else :
        print("지원하지 않는 고용 형태입니다.")

if emptype == "P" :
    name = input("이름 : ")
    emptype = "정규직"
    while True :
        try : 
            money = int(input("기본급 : "))
            bonus = int(input("보너스 : "))
            break
        except ValueError :
            print("숫자 입력 요망!")
    
    p1 = Permanent(name, emptype, money, bonus)
    p1.print_profile()


else :
    pass