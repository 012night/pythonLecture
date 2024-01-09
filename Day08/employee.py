# import employee_parent
from employee_parent import Employee

# Employee를 상속받아 Permanent(정규직) 클래스 구현
class Permanent(Employee) :
    def __init__(self, name, emptype, money, bouns) :
        # 부모의 생성자 이용, super()
        super().__init__(name, emptype)
        self.pay = money + bouns
    
    def print_profile(self) :
        # 부모의 print_profile를 super()를 사용해 활용하면서 오버라이딩
        super().print_profile()
        print(f"급여 : {self.pay}")
        
# Employee를 상속받아 Temporary(비정규직) 클래스 구현
class Temporary(Employee) :
    def __init__(self, name, emptype, time, t_money) :
        # 부모의 생성자 이용, super()
        super().__init__(name, emptype)
        self.pay = time * t_money
    
    def print_profile(self) :
        # 부모의 print_profile를 super()를 사용해 활용하면서 오버라이딩
        super().print_profile()
        print(f"급여 : {self.pay}")

# emptype 입력값을 정확하게 받을때까지 요청
while True :
    emptype = input("고용형태 선택(정규직<P>, 비정규직<T>) : ")
    if emptype == 'p' or emptype == 'P' or emptype == 't' or emptype == 'T' :
        break
    else :
        print('지원하지 않는 고용형태입니다. 입력을 다시하세요! ')
        continue 

# emptype 조건에 따라 다른 클래스를 이용하여 객체 생성
if emptype == 'p' or emptype == 'P' :
    name = input("이름 : ")
    emptype = '정규직'
    while True :
        # ValueError 처리
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
        # ValueError 처리
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