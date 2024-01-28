# 1. 어떤기능을 하는 함수를 만들지 생각
# 2. 매개변수로 어떠한, 몇개의 값이 필요할지...
# 3. 함수를 호출한 곳으로 어떤 값을 돌려줘야 할지(return)
# 4. 구현

# # 기본구조
# def 함수명(매개변수) :
#     pass

# 숫자 두개를 매개변수로 전달하면 그 합을 돌려주는 함수
# a = 10
# b = 20
# result = a+b
# print(result) 

# def sum_num02(x, y) :
#     return x + y

# print(sum_num02(10, 20))


# def multi(x, y) :
#     return x*y

# print(multi(3,4))

# def squared(x) :
#     return x*x

# print(squared(5))

# def pow_mine(x, y) :
#     result = 1
#     for count in range(y) :
#         result *= x
#     return result
#     # return  x ** y

# print(pow_mine(4,3))

# # 홀짝 판별 함수
# def isEven(x) :
#     if x % 2 == 0 :
#         result = True
#     else :
#         result = False
#     return result

# print(isEven(9))
# r = float(input("반지름의 길이를 입력 : "))
# def circle_area(r) :
#     return print(r*r*3.14)
# print("원의넓이 :", circle_area(r))
r = 10

# def circle_area() :
#     return r*r*3.14

# print("원의넓이 :", circle_area())
# a = 2
# def sum(a):
#     a += 1
#     return a
# result = sum(a)
# print(result)
# print(a)


# result = 2
# def sum(a) :
#     global result
#     result = result + a
#     return result

# sum_result = sum(1)
# print(sum_result)

# result = 2
# def sum(a) :
#     result_sum = result + a
#     return result_sum

# sum_result = sum(1)
# print(sum_result)


# 입력값은 있지만 결과값은 없는 함수

# def hello(name):
#     print(name)

# hello("본인이름")


# def minus(x, y) :
#     print(x-y)

# print(minus(10,3))

# def divmod_mine(x,y) :
#     print((x//y, x%y))

# divmod_mine(10,3)

# def func_up(lst) :
#     for x in range(0, len(lst)-1) :
#         for y in range(x+1, len(lst)) :  
#             if lst[x] > lst[y] :
#                 lst[x],lst[y] = lst[y],lst[x]
#     print(lst)

# sample = [5, 1, 3, 7, 9, 2]
# func_up(sample)



# 매개변수는 없지만 결과값이 있는, 결과값이 없는 함수



# def warring01() :
#     print("1~2시 서버 업데이트!@#!#%!@#$")
# def warring02() :
#     print("1~2시 네트워크 작업중")
# def warring03() :
#     print("1~2시 서버 업데이트!@#!#%!@#$")
# def warring04() :
#     print("1~2시 서버 업데이트!@#!#%!@#$")


# def plus(*num) :
#     sum_result = 0
#     for x in num :
#         sum_result += x
#     return sum_result

# print(plus(1,2,3,4,5))
# print(plus(1,2,3))

# def cal(choice, *data) :
#     if choice == "+" :
#         print(sum(data))
#     else :
#         print("지원하지않는 연산입니다.")

# cal("+",1,2,3,4,5)
# cal("*",1,2,3,4,5)



# # 평균, 분산, 표준편차
# import statistics
# print(statistics.mean([1,2,3,4]))
# print(statistics.variance([1,2,3,4]))
# print(statistics.stdev([1,2,3,4]))

# import statistics
# def statistics_func(choice, *data) :
#     if choice == "평균" :
#         return statistics.mean(data)
#     elif choice == "분산" :
#         return statistics.variance(data)
#     elif choice == "표편" :
#         return statistics.stdev(data)
#     else :
#         return "에러"
#     retrun 0

# print(statistics_func("평균", 1,2,3,4))
# print(statistics_func("분산", 1,2,3,4))
# print(statistics_func("표편", 1,2,3,4))



# def sum(a, b):
#     result1 = a + b
#     result2 = a * b
#     result3 = a // b
#     return result1, result2, result3

# result = sum(1,2)
# print(result)



# 기본적으로는 덧셈 기능만 하는데 내가 옵션을 주면 다른 기능으로 바뀌는 계산

# def print(msg, end="\n", sep=" ") :



def sum(a,b,choice="+") :
    if choice == "+" :
        return a+b
    elif choice == "-" :
        return a-b
    else :
        pass

print(sum(1,2))
print(sum(1,2, choice="-"))