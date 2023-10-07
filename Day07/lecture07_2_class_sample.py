# =======================================================================================
# # 클래스 만들기
# # 설계도
# class Cellphone:
#     # 생성자: 객체가 처음 만들어질 때 불려지는 특수한 메소드(method)
#     serial = 99999
#     def __init__(self):
#         # 속성: 필드, 멤버변수
#         self.maker = 'samsung'
#         self.model = '21s-plus'
#         self.color = 'black'
#         self.price = 830000
#         Cellphone.serial += 1

#     # 행위: 메소드(method)
#     def camera(self):
#         print("카메라 찰칵")

#     def call(self):
#         print("전화하기")

#     def introduce(self):
#         print("제조사는 %s이며 모델명 %s고 가격은 %d, 시리얼은 %d입니다."
#               % (self.maker, self.model, self.price, Cellphone.serial))

# # 인스턴스 화 => 객체(Object), Cellphone의 instance
# sample = Cellphone()
# # 타입 확인
# print(type(sample))

# # 값 넣기
# sample.maker = "apple"
# sample.color = "gold"
# sample.price = 1200000
# sample.model = 'iphone11pro'

# # 값 출력하기
# print(sample.maker)
# print(sample.model)
# print(sample.price)
# print(sample.color)
# print(sample.serial)

# # method 호출하기
# sample.call()
# sample.camera()
# sample.introduce()

# # 100개를 생산하기
# cellphones = []
# for i in range(100):
#     cellphones.append(Cellphone())
#     cellphones[i].introduce()
# =======================================================================================


# =======================================================================================
# # 사람을 클래스(객체)화 해보는 예제
# class Person:
#     # 1. 속성: 필드
#     def __init__(self, name='김엘지', birth='20000101', gender='여자'):
#         self.name = name
#         self.birth = birth   # 생년월일
#         self.gender = gender

#     # 2. 행위: 메소드
#     def greet(self):
#         print("안녕하세요, 인사하는 기능의 메서드 입니다")

#     def walk(self):
#         print("걷는다~ 걷는 기능의 메서드 입니다")

#     def introduce(self):
#         print("제 이름은 %s이고 성별은 %s입니다." % (self.name, self.gender))

#     def age(self):
#         yyyy = self.birth[:4]  # "20000101"
#         age = 2021 - int(yyyy) + 1
#         return age

# # instance 화 => 객체 만들기
# p1 = Person()
# p1.greet()
# p1.walk()
# p1.introduce()
# print("나이는 %d세입니다" % p1.age())

# p2 = Person("박삼성", "19801231", "남자")
# p2.introduce()
# print("나이는 %d세입니다" % p2.age())
# =======================================================================================


# =======================================================================================
# # 클래스 연습 01
# # 사칙연산 클래스 만들어보기.
# class Calculator:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#         print("생성자 매소드입니다. 인스턴스 생성시 자동으로 실행되는 메소드에요")

#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result

#     def mul(self):
#         result = self.first * self.second
#         return result
#     print("클래스 입니다. 프로그램 실행시 수행되요")

# cal_01 = Calculator(10,20)
# cal_01.setdata(30, 40)
# print("add() 메소드 수행 결과 : ",cal_01.add())
# # print(cal_01.result)        # cal_01.result? 로 받아올순 없을까? 시도해보자
# =======================================================================================


# =======================================================================================
# # 리턴값이 없는 함수라면 이렇게 접근 해야겠지?
# class Calculator:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#         self.result = 0

#     def add(self):
#         self.result = self.first + self.second

# cal_01 = Calculator(10,20) 
# result = cal_01.add()
# print(result)               # 값이 있니?
# print(cal_01.result)        # 이렇게 해보자~
# =======================================================================================


# =======================================================================================
# # 클래스 연습 02
# class Calculator :
#     def __init__(self) :
#         self.result = 0
    
#     def sum(self, startNum, endNum) :
#         while startNum <= endNum :
#             self.result += startNum
#             startNum += 1

# sumA = Calculator()
# startNum = int(input("시작값 : "))
# endNum = int(input("종료값 "))
# sumA.sum(startNum, endNum)
# print(sumA.result)
# =======================================================================================


# =======================================================================================
# # 클래스 연습 03
# class Rectangle :
#     def __init__(self, width, height) :
#         self.width = width
#         self.height = height
    
#     def area(self) :
#         area = self.width * self.height
#         return area
    
#     def circum(self) :
#         circum = (self.width + self.height)*2
#         return  circum
    

# print("사각형의 넓이와 둘레를 계산하라.")
# w = int(input("가로 : " ))
# h = int(input("가로 : " ))

# rec = Rectangle(w, h)
# area = rec.area()
# print('='*20)
# print("넓이 :", area)

# circum = rec.circum()
# print("둘레 :", circum)
# print('='*20)
# =======================================================================================


# =======================================================================================
# class Product:
#     def __init__(self, name, price, expired_date):
#         # 속성: 필드(field)
#         # 이름: 새우깡
#         # 가격: 1300
#         # 유통기한: 2025-03-02
#         self.name = name
#         self.price = price
#         self.expired_date = expired_date

#     # 행위: 메소드(함수)
#     def price_of_count(self, count):
#         print("제품 %d개의 가격은: %d" % (count, count * self.price))

#     def sale_status(self):
#         today = "2021-01-01"
#         if today <= self.expired_date:
#             return "판매 가능 상품"
#         else:
#             return "판매 불가 상품"

# # instance화 => 객체, instance
# p1 = Product("새우깡", 1300, "2025-03-02")
# print("이름:", p1.name)
# print("가격:", p1.price)
# print("유통기한:", p1.expired_date)

# p1.price_of_count(5)   # 5개의 가격
# p1.price_of_count(13)  # 13개의 가격
# print(p1.sale_status())
# =======================================================================================


# =======================================================================================
# # 클래스의 상속 후 메서드를 추가해보자
# # 클래스 상속, 오버라이딩 실습
# class Calculator:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result

#     def mul(self):
#         result = self.first * self.second
#         return result
# # Calculator클래스(부모)를 상속받은 Calculator_child클래스(자식)
# class Calculator_child(Calculator):
#     def div(self):
#         result = self.first / self.second
#         return result

# cal_parent = Calculator(20, 3)
# print(cal_parent.add())

# # 생성자도 같이 상속된다.
# cal_child = Calculator_child(20, 3)
# print(cal_child.mul())
# print(cal_child.div())
# =======================================================================================


# =======================================================================================
# # 상속을 받은 후 수정을 해볼까?
# class Calculator_child_change(Calculator_child):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             result = self.first / self.second
#         return result
# cal_child_change = Calculator_child_change(20,0)
# print(cal_child_change.div())
# =======================================================================================

# =======================================================================================
# # super()
# # Weapone 클래스 정의
class Weapone:
    def __init__(self, what, type):
        self.what = what
        self.type = type
    print("나는 무기 클래스다!")

# Sword 클래스 정의 : Weapone 클래스 상속
# class Sword(Weapone):
#     def __init__(self, power, level):
#         self.power = power
#         self.level = level

# Sword 클래스 정의 : Weapone 클래스 상속 후 생성자 상속 super()
class Sword(Weapone):
    def __init__(self, what,  type, power, level):
        super().__init__(what,type)
        self.power = power
        self.level = level

# Sword 속성(power,level) 및 부모 클래스 Weapon 의 속성 불러오기(what, type)
    def info(self):
        print("무기종류 :", self.what)
        print("공격타입 :", self.type)
        print("공 격 력 :", self.power)
        print("레    벨 :", self.level)

# Sword 클래스 객체 short_sword 선언
short_sword = Sword("123", "234", 10, 20)
short_sword.info()
# =======================================================================================

def add_sample(x, y) :
    return x+y