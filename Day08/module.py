# 1) 에러정보 출력하는 함수
def print_error() :
    print("현재 시스템 사용 불가입니다. 11~13시까지 서버 패치 작업중...")

# 2) Cal 클래스
class Cal :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.result = 0
    
    def add(self) :
        self.result = self.x + self.y
    
    def sub(self) :
        self.result = self.x - self.y


# c1 = Cal(1,2)
# c1.add()
# print(c1.result)

if __name__ == '__main__' :
    print_error()
