def add(a, b):
    result = a + b
    return result


class Calculator :
    def __init__(self, first_num, second_num) :
        self.result = 0
        self.first_num = first_num
        self.second_num = second_num
    
    def sum(self) :
        self.result += self.first_num + self.second_num


#모듈 자체의 이름을 내부적으로 main이라 칭한다
#다른 파일에서 불러 사용할때는 안나오고 자체적으로 만 나오게 하는 조건문이다,
if __name__ == '__main__' :
    print('모듈페이지 입니다~')
