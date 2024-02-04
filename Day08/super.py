class Profile :
    def __init__(self) :
        self.position = "사원"
        self.type = "개발자"
    
class New(Profile) :
    def __init__(self, money):
        # self.position = "사원"
        # self.type = "개발자"
        super().__init__()
        self.money = money
    
    def print_profile(self) :
        print(f"직급은 {self.position}, 역할은 {self.type} 그리고 원급은 {self.money}") 

if __name__ == "__main__" :
    n1 = New(300)
    n1.print_profile()




