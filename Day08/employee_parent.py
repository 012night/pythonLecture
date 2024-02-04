# 해당 클래스는 이름(name), 고용타입(emptype)을 매개변수로 받아 초기화 하며 print_profile이라는 메서드로 이름, 고용형태를 그대로 출력해준다.
class Employee :
    def __init__(self, name, emptype) :
        self.name = name
        self.emptype = emptype

    def print_profile(self) :
        print(f"이름 : {self.name}")
        print(f"고용형태 : {self.emptype}")

if __name__ == "__main__" :
    e1 = Employee("김메가", "비정규직")
    e1.print_profile()