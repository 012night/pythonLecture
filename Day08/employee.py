# import employee_parent
# import sys
# print(sys.path)
# sys.path.append('C:\chicoding\Day08')
from employee_parent import Employee

class Permanent(Employee) :
    def __init__(self, name, emptype, money, bouns) :
        super().__init__(name, emptype)
        self.pay = money + bouns
    
    def print_profile(self) :
        super().print_profile()
        print(f"급여 : {self.pay}")
        
        
class Temporary(Employee) :
    def __init__(self, name, emptype, time, t_money) :
        super().__init__(name, emptype)
        self.pay = time * t_money
    
    def print_profile(self) :
        super().print_profile()
        print(f"급여 : {self.pay}")



while True :
    emptype = input("고용형태 선택(정규직<P>, 비정규직<T>) : ")
    if emptype == 'p' or emptype == 'P' or emptype == 't' or emptype == 'T' :
        break
    else :
        print('지원하지 않는 고용형태입니다. 입력을 다시하세요! ')
        continue 


if emptype == 'p' or emptype == 'P' :
    name = input("이름 : ")
    emptype = '정규직'
    while True :
        try :
            money = int(input("기본급 : "))
            bouns = int(input("보너스 : "))
            break
        except ValueError :
            print("숫자가 아닌것 같은데요?")
    p = Permanent(name, emptype, money, bouns)
    p.print_profile()
        
elif emptype == 't' or emptype == 'T' :
    name = input("이름 : ")
    emptype = '비정규직'
    while True :
        try :
            time = int(input("작업시간 : "))
            t_money = int(input("시급 : "))
            break
        except ValueError :
            print("숫자가 아닙니다. 정확하게 다시 입력하세요!")
    t = Temporary(name, emptype, time, t_money)
    t.print_profile()
else :
    print('=' * 30)
    print('입력오류')




# import sys
# print(sys.path)
# import bank.deposit.deposit

# bank.deposit.deposit.deposit()

