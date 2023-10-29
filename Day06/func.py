# 1. 어떤 역할을 하는 함수를 만들것인가

# # 기본구조
# def 함수명(매개변수) :
#     실행문(로직)
#     return 함수를 호출한 곳을호 돌려주기 위한 결과


# # 두개의 정수를 받아 덧셈의 결과를 돌려주는 기능
# def sum_num2(x, y) :
#     result = x + y
#     # print(result)
#     return result

# a = sum_num2(10, 11)
# print(a)



# def multi_num2(x, y) :
#     result = x * y
#     return result
# print(multi_num2(2,5))


# print(pow(2,3))


# def squared(num) :
#     return num * num
# print(squared(3))


# def squared_ver02(x, y) :
#     result = 1
#     for count in range(y) :
#         result *= x
#     return result

# print(squared_ver02(3,4))


# def is_even(check) :
#     # if check % 2 == 0 :
#     #     # return True
#     #     result = True
#     # else :
#     #     # return False
#     #     result = False
#     # return result
    
#     result = check % 2 == 0
#     return result
    

# print(is_even(5))


# def circle_area(r) : # r = radius
#     result = r * r * 3.14
#     return result

# radius = float(input("반지름의 길이를 입력하세요. : "))
# print(circle_area(radius))


# # # 주어진 문장 내 단어의 개수를 구해주는 함수
# def w_count(text) : # text = msg
#     return len(text.split())

# msg = "i like python"
# print(w_count(msg))

# def sum(a) :
#     a = a + 1
#     return a
# a = 1
# result = sum(a)
# print(result)



# # 안되는 상황
# def sum(a) :
#     global result
#     result = result + a
#     return result
# result = 2
# sum_result = sum(1)
# print(sum_result)


# # 되는 상황
# def sum(a) :
#     result02 = result + a 
#     return result02
# result = 2
# sum_result = sum(1)
# print(sum_result)

# def hello(word) :
#     print(word, "hello")

# print(hello("이름"))


# def minus(x, y) :
#     print(x-y)

# minus(10, 3)

# 두수를 입력 받아 몫과 나머지를 출력하는 함수를 만들라.
# (리턴값은 없다.)

# def divmod_mine(x, y) :
#     q = x // y
#     r = x % y
#     print((q,r))

# def divmod_mine(x, y) :
#     q = x // y
#     r = x % y
#     return q,r

# x,y = divmod_mine(10,3)
# print(x)

# def func_up (kkk) :
#     for a in range(0,len(kkk)-1):
#         for b in range(a+1,len(kkk)):
#             if kkk[a] > kkk[b]:
#                 kkk[a], kkk[b] = kkk[b], kkk[a]

# lst = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# func_up(lst)
# print(lst)


# def warrning01() :
#     return "01~02까지 서버 점검입니다."
# def warrning02() :
#     return "02~03까지 서버 점검입니다."
# def warrning03() :
#     return "03~04까지 서버 점검입니다."
# def warrning04() :
#     return "04~05까지 서버 점검입니다."
# def warrning05() :
#     print("04~05까지 서버 점검입니다.")

# print(warrning01())
# warrning05()

# # 사용자의 입력값이 몇개인지 정의 할수 없을때...
# def num_sum(*data) : # data = (1,2,3), data = (7,8,9,10)
#     sum_result = 0
#     for x in data :
#         sum_result += x
#     return sum_result

# print(num_sum(1,2,3))
# print(num_sum(7,8,9,10))


# def get_average_many(*data) : # data = (1,2,3), data = (7,8,9,10)
#     sum_result = 0
#     for x in data :
#         sum_result += x
#     return sum_result/len(data)

# result = get_average_many(1,20,8,50)
# print("평균", result)



# def names_func (name, *names) :
#        print(name)
#        print(names)

# names_func('서울시', '강남구', '메가스터디', '4층', 'python')



# 하나의 함수로 여러 기능을 하게끔 하는...
# 외장함수 이용 평균, 분산, 표준편차를 사용
# 첫번째 매개변수로 저 세가지중 하나를 던져주면 그 기능을 하는 함수를 구현
# import statistics

# def statis_func(choice, *data) :
#     if choice == "평균" :
#         print(statistics.mean(data))
#     elif choice == "분산" : 
#         print(statistics.variance(data))
#     elif choice == "표편" : 
#         print(statistics.stdev(data))
#     else :
#         print("지원하지 않는 기능 입니다.")

# statis_func("평균",1,2,3,4,5)
# statis_func("분산",1,2,3,4,5)
# statis_func("표편",1,2,3,4,5)


# # 통계 외장함수 사용
# import statistics
# data = [1,2,3,4,5]
# # 평균
# print(statistics.mean(data))
# # 분산
# print(statistics.variance(data))
# # 표준편차
# print(statistics.stdev(data))


# def cal(x,y,z) :
#     if x == "+" :
#         print(y+z)
#     elif x == "-" :
#         print(y-z)
#     else :
#         print("지원하지 않습니다.")

# choice = input("어떤 연산을 하실껀가요? (+,-,*,/)")
# num01 = int(input("첫번째 정수를 입력하세요."))
# num02 = int(input("두번째 정수를 입력하세요."))
# cal(choice, num01, num02)





# def sum(a, b):
#     result1 = a + b
#     result2 = a * b
#     result3 = a // b
#     return result1, result2, result3


# # 기본적으로는 덧셈 기능을 하는 함수, 내가 False라는 인자를 던지면 -로 바뀌는 기능을 하는 함수
# def cal(x,y,select=True) :
#     if select :
#         print(x+y)
#     else :
#         print(x-y)

# cal(10,11) # 21(덧셈)
# cal(10,11,select =False) # -1(뺄셈)


# def print_profile(name, age, gender) :
#     print(f"이름은 {name}이며 나이는 {age}, 성별은 {gender}입니다.")

# print_profile("김메가", 39, "남")
# print_profile(age=39, name= "김메가", gender= "남")


# # def add(a,b):
# #     return a+b

# # #위 함수를 람다식을 이용해서 작성
# # add = lambda x,y : x+y
# # print(add(1,2))

# list_calFunc = [lambda x,y : x+y, lambda x,y : x-y, lambda x,y : x*y, lambda x,y : x/y]
# print(list_calFunc[0](1,2))
# print(list_calFunc[1](1,2))
# print(list_calFunc[2](1,2))



# layer = int(input("층수 입력"))
# sum_result = 0
# for x in range(1,layer+1) :
#     print(x*"*")
#     sum_result += x
# print("총합 :", sum_result)
