class Employee :
    def __init__(self, name, emptype) :
        self.name = name
        self.emptype = emptype

    def print_profile(self) :
        print(f"이름 : {self.name}")
        # if self.emptype == "P"
        print(f"고용형태 : {self.emptype}")

if __name__ == "__main__" :
    e1 =Employee(1,2)
    e1.print_profile()