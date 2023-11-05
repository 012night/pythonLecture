class Employee :
    def __init__(self, name, emptype) :
        self.name = name
        self.emptype = emptype
        
    def print_profile(self) :
        print("="*30)
        print("이름 : {}".format(self.name))
        print("고용형태 : {}".format(self.emptype))