# def plus(x, y) : # x=1, y=2
#     # result = x + y
#     return x + y
# print(plus(1,2))

# def multi(x, y) :
#     return x*y
# print(multi(3,4))

# def squared(x) :
#     return x**2
# print(squared(5))


# print(pow(3,4))
# def pow_sample(x, y) :
#     return x**y
# print(pow_sample(3,4))

# def is_even(x) : # x = 3
#     if x % 2 == 0 :
#         result = True
#     else :
#         result = False
#     return result

# print(is_even(3))



# def circle_area(r) : # r = radius
#     return r*r*3.14

# radius = int(input("반지름의 길이를 입력하세요. : "))
# print(circle_area(radius))


# def sum(a) :
#     a += 1
#     return a

# a = 1
# result = sum(a)

# print(result)
# print(a)

# ========================================
# def sum(a) :
#     global result
#     result = result + a
#     return result

# result = 2
# sum_result = sum(1)
# print(sum_result)
# print(result)
# ========================================
# def sum(a) :
#     result_func = result + a
#     return result_func

# result = 2
# sum_result = sum(1)
# print(sum_result)


# def hello(name) :
#     print(name, 'hello')

# hello("메가result스터디")

# def minus(x,y) :
#     result = x-y
#     print(result)

# minus(5,3)

# print(divmod(10,3))

# def divmod_02(x, y) :
#     return (x//y, x%y)
# print(divmod_02(10,3)) # (3, 1)

# def divmod_02(x, y) :
#     print((x//y, x%y))
# divmod_02(10,3) # (3, 1)



# def func_up(a) : # a = lst
#     for x in range(0, len(a)-1) :
#         for y in range(x+1, len(a)) :
#             if a[x] > a[y] : 
#                 a[x],a[y] = a[y],a[x]
#     print(a)


# lst = [5, 1, 3, 7, 2, 9]
# func_up(lst)

# def hello() :
#     return "hello python!"
# print(hello())


# def hello() :
#     print("hello python!")
# hello()


# def warning_01 () :
#     print("10:00~11:00 서버 점검 시간입니다.")
# def warning_02 () :
#     print("12:00~13:00 서버 점검 시간입니다.")
# def warning_03 () :
#     print("13:00~14:00 서버 점검 시간입니다.")
# def warning_04 () :
#     print("15:00~16:00 서버 점검 시간입니다.")
    
# def msg_01 () :
#     print("누를수 없는 버튼입니다")
    
# def num_plus(*num) :
#     result_sum = 0
#     for x in num :
#         result_sum += x
#     return result_sum

# print(num_plus(1,2,3,4,5))
# print(num_plus(1,2,3,4))
# print(num_plus(1,2,3))


# def get_average(*scores) :
#     result = 0
#     for score in scores :
#         result += score
#     return result / len(scores)

# print(get_average(10,20,30,40))
# print(get_average(10,20,30,40,100))


# def names_func(choice, *names) : #name = "서울시" names = 나머지 데이터가 다 들어가
#     if choice == "+" :
#         pass
#     elif choice == "-" :
#         pass

# names_func("+", 1,2,3,4,5,6)
# names_func("-", 1,2,3,4,5,6)
# names_func("*", 1,2,3,4,5,6)



# 평균, 분산, 표준편차를 위한 함수, 모듈페이지 statistic 
# import statistics
# from statistics import mean, variance, stdev

# def stat_func(select, *data) :
#     if select == "평균" :
#         # return statistics.mean(data)
#         return mean(data)
#     elif select == "분산" :
#         # return statistics.variance(data)
#         return variance(data)
#     elif select == "표편" :
#         # return statistics.stdev(data)
#         return stdev(data)
#     else :
#         return "지원하지 않는 계산"

# print(stat_func("평균",1,2,3,4,5))
# print(stat_func("분산",1,2,3,4,5))
# print(stat_func("표편",1,2,3,4,5))


# def cal (choice, num1, num2) : #choice = c, num1= n1, num2=n2
#     if choice == "+" :
#         print(num1 + num2)
#     elif choice == "-" :
#         print(num1 - num2)
#     else :
#         print("지원하지 않는 수식입니다.")
        
# c = input("어떤 연산을 하실껀가요? (+,-,*,/) : ")
# n1 = int(input("첫번째 정수 입력 : "))
# n2 = int(input("두번째 정수 입력 : "))

# cal(c, n1, n2)

# def cal (a,b) :
#     r1 = a+b
#     r2 = a-b
#     r3 = a*b
#     return r1, r2, r3

# print(cal(1,2))


# def speak(msg) :
#     if msg == "종료" :
#         return
#         print(msg)
#     else :
#         print(msg)

# speak("안녕")
# speak("종료")



# print("안녕", "안녕", sep="#", end="//")
# print("안녕", "안녕", sep="#", end="//")


#기본적으로는 +연산만 출력, 내가 False 라는 인자를 넣으면 +, -, * 연산 결과가 다 오게.

# def cal (x, y, choice = True) :
#     if choice :
#         print(x+y)
#     else :
#         print(x+y, x-y, x*y)

# cal(1,2) # 3
# cal(1,2,False) # 3, -1, 2


# def print_profile(name, age, gender) :
#     print(f"나의 이름은 {name}이고 나이는 {age}, 성별은 {gender}입니다.")
#     pass

# # print_profile("메가", 20, "남")
# print_profile(age= 20, name= "메가", gender ="남")


# def plus(x,y) :
#     return x+y

# plus = lambda x,y : x+y
# print(plus(1,3))

# cal_list = [lambda x,y : x+y, lambda x,y : x-y]
# print(cal_list[0](1,2))
# print(cal_list[1](1,2))



# def starCount() :
#     layer = int(input("layer : "))
#     sum_result = 0
#     for x in range(1, layer+1) :
#         print((x)*"*")
#         sum_result += x
#     print(sum_result)

# starCount()