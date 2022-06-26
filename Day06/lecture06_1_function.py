#함수의 기본구조 def 함수명(매개변수)
# lista = [7,2,3,6]
# lista.sort()는 list.sort(lista)와 같다.
# print(lista)
# print(1+1)은 print(int.__add__(1, 2)) 와 같다.



# lista =  ['1', '2', '3', '4']
# print(lista.sort())
# print(lista.count('1'))



# #입력값,출력값이 있는 함수 기본 구조
# def plus(a, b):
#     result = a + b
#     return result   #result 없애고 a+b를 해도 무관

# plusvalue = plus(1,2)
# print(plusvalue)




# # 연습문제 1
# def mul (x,y) :
#     return x*y
# print(mul(2,3))




# 사용자 정의 함수 예제
# def circle_area(radius) :
#     result = radius**2 * 3.14
#     return result
# radius = float(input("반지름의 길이를 입력하세요. "))
# print(f"원의 넓이 : {circle_area(radius)}")



#입력값이 없는 함수 구조
# def hello():
#     return 'hello'
# print(hello())
#print(hello) 라고 했을때 hello의 값은 뭐지?




#입력값은 있지만 결과값이 없는 함수 구조
# def hello(name):
#     print(name, 'hello')

# print(hello("메가스터디"))




# #입력값과 결과값이 모두 없는 함수 구조
# def hello():
#     print('hello')
# hello()



# 결과값/출력값이 없는 함수 구조
# lista = [1,3,4,2]
# lista.sort()
# print(lista.sort())
# print(lista)




# #연습문제2-1
# def hello() :
#     print('hello python!')
# hello()


# #연습문제2-2
# def hello() :
#     return 'hello python!'
# print(hello())




# #연습문제3
# lst = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# #오름차순
# def func_up(lst) :
#     for a in range(0,len(lst)-1):
#         for b in range(a+1,len(lst)):
#             if lst[a] > lst[b]:
#                 # (lst[a], lst[b]) = (lst[b], lst[a])
#                 tmp = lst[a]
#                 lst[a] = lst[b]
#                 lst[b] = tmp
                
# print(type(lst))
# print(lst)
# func_up(lst)
# print(lst)




# 입력값이 몇개인지 모를때의 함수구조
# *args 매개변수 구조
# def plus(*args) :
#     print(type(args))
#     result = 0
#     for i in args:
#         result += i
#     return result
# print("시작")
# result = plus(1, 2, 3, 4, 5)
# print(result)



# # 입력값이 몇개인지 모를때의 함수구조2
# def names_func (name, *names) :
#     print(name)
#     print(names)
    
# names_func('서울시', '강남구', '메가스터디', '4층', 'python')




# # 입력값이 몇개인지 모를때의 함수구조3
# from statistics import mean, variance, stdev

# def statis_func (choice, *data) :
#     if (choice == 'avg') :
#         return mean(data)
#     elif (choice == 'var') :
#         return variance(data)
#     elif (choice == 'std') :
#         return stdev(data)
#     else :
#         return '오류, 재입력 요망'
    
# print('avg = ', statis_func('avg',1,2,3,4,5))
# print('var = ', statis_func('var',1,2,3,4,5))
# print('std = ', statis_func('std',1,2,3,4,5))




# # 연습문제 선택적 함수 만들기
# def cal(choice, num1, num2) :
#     if choice == '+' :
#         return num1 + num2
#     elif choice == '-' :
#         return num1 - num2
#     elif choice == '*' :
#         return num1 * num2
#     elif choice == '/':
#         return num1 / num2
#     else :
#         print("프로그램에 오류가 있어요 연산자를 다시 입력하세요")

# choice = input("어떤 연산을 하실껀가요? (+,-,*,/)\n")
# num1 = int(input("첫번째 정수를 입력하세요. "))
# num2 = int(input("두번째 정수를 입력하세요. "))
# result = cal(choice, num1, num2)
# print(f"{num1}과 {num2}의 {choice}연산결과는 {result}입니다.")




#키워드 파라미터(키와 value를 받아 dic 형태로 값을 받는 방법)
# def dic(**kwargs) :
#     print(kwargs)

# dic(a=1, b='파이썬')




# #2개 이상의 리턴값이 있을경우
# def sum(a, b):
#     result1 = a + b
#     result2 = a * b
#     result3 = a // b
#     return result1, result2, result3
# result = sum(1,2)
# print(result)

# result1, result2, result3 = sum(1,2)
# print(result1)
# print(result2)
# print(result3)




#return의 또다른 용도
# def speak(msg) :
#     if msg == "종료" :
#         return
#         print("{msg}를 입력하셨습니다,")
#     else :
#         print(msg)

# speak(input("메시지를 입력하세요 :"))



#default값 미리 세팅하기
# def sum(a, b, test=True):
#     if(test) :
#         result = a + b
#         return result
#     else :
#         result1 = a + b
#         result2 = a * b
#         result3 = a // b
#         return result1, result2, result3

# # result = sum(b=2, a=1, test=False)
# # result = sum(1,2, False)
# result = sum(1,2)
# print(result)




#함수의 매개변수의 순서를 맞춰야 하는가? 안맞춰도 되는 방법은?
# def whoareyou(name, age, gender):
#     print("제 이름은 %s 이고 나이는 %d 살, 그리고 성별은 %s 입니다." %(name, age, gender))
# whoareyou(age=19, name='홍길동', gender= '남자')
# whoareyou(19,'홍길동',  '남자')




#lamda 함수의 사용
# def add(a, b):
#     return a+b

# add = lambda a, b: a+b
# print(add(1,2))




# #람다를 왜 사용하느냐? list같은 형태로 담는 등, 자유도가 높다.
# add_mul_List = [lambda a, b: a+b, lambda a, b : a*b]
# print(add_mul_List[0](1,2))
# print(add_mul_List[1](3,4))

# lst = []
# lst.append(add_mul_List[0](1,2))
# lst.append(add_mul_List[1](3,4))
# print(lst)




# #지역변수와 전역변수 란 무엇인가
# #지역변수의 예 : 함수안의 변수 a 
# #전역변수의 예 : 함수밖의 a
# a = 2
# def sum(a):
#     a = a + 1
#     return a
# result = sum(a)
# print(result)
# print(a)



#아래 코드에서 result값은 어디에 정의 되어 있는가?
#함수 내에서 result를 선언하는과정에서 할당이 안된 result 값을 참조하는 상황이 발생
# result = 2
# def sum(a) :
#     # result = 1
#     result = result + a
#     return result
# sumvalue = sum(1)
# print(sumvalue)



# 위가 헷갈리는가? 이것과 같은 이치
# a = a+1
# print(a)



#새로운 지역변수 선언을 하는데 전역변수의 값을 가져와 사용하는것은 괜찮다.
# result = 2
# def sum(a) :
#     # result = 1
#     result_func = result + a
#     return result_func
# sumvalue = sum(1)
# print(sumvalue)




#함수안에서의 변수들은 함수가 호출이 끝나면 사라진다.  메모리 호출 구조를 보면 더 편하다
#https://pythontutor.com/live.html#mode=edit 참고
#모든 변수는 메모리에 담긴다. 그러나 메모리의 어떤 영역에 담기느냐에 따라, 그 효력 범위가 달라진다.
#파이썬의 메모리 구조 참고 http://www.tcpschool.com/c/c_memory_structure


#그렇다면 파이썬에서는 왜 지역변수를 함수호출이 끝나면 사라지도록 설계 하였을까? 파이썬 뿐만아니라 대부분의 프로그램에서
#예를 들어 아래 프로그램에서 add는 여러번 사용이 가능하다.
#아래와 같은 프로그램에서 add의 결과값이 누적이 된다면 말이 되겠는가?
# result = 0

# def add(a, b):
#     result = a + b
#     return result

# a_workday = 10
# a_money = 0
# cash = 10000
# card = 10000
# if a_workday >= 10:
#     a_money = add(cash,  card)

# b_workday = 20
# b_money = 0
# cash = 30000
# card = 30000
# if b_workday >= 20:
#     companymoney = add(cash,  card)
# print(a_money)
# print(b_money)






# 담아두고 싶으면 아래 2가지 방법을 써야 한다.
# a에 영향을 줄 수 있는 방법 1 
# 1.a에 다시 담아둔다.
# a = 2
# def sum(a):
#     a += 1
#     return a
# a = sum(a)
# print(a)
# print(a)



# a에 영향을 줄 수 있는 방법 2 
# 2.global 선언
# result = 2
# def sum(a):
#     global result
#     result += a
#     return result
# sumvalue = sum(1)
# print(sumvalue)




#그런데 특이한 자료 구조가 있다. list를 생각해보자. 어찌된일일까?
#아래와 같은 자료구조의 특성을 보면 이해할 수 있다.
#함수도 메모리에 주소가 할당되어 저장되지만, 함수 내의 지역변수는 스택에 저장되어 휘발되도록 한다.
#그에 반해 list의 append는 object로서 heap 메모리라는 휘발되지 않는 공간에 변수값을 추가 하는 것므로 날아가지 않는다.
# b = (2,3,4)
# print("리스트 b의 id ", id(b))
# b = (1,2)
# def test(b):
#     b = (1,2)
# test(b)
# print("리스트 b는?", b)

# a=1
# print("a의 id ", id(a))
# a=2
# print("a의 id ", (id(a)))
# b = [2,3,4]
# print("리스트 b의 id ", id(b))
# def test(b):
#     b = b.append(1)
# test(b)
# print("리스트 b의 id ", id(b))
# print("리스트 b의 [2]의 id ", id(b[2]))
# print("리스트 b의 [1]의 id ", id(b[1]))
# print("함수 test의 id ", id(test))


#mutable immutable
#위에서 말한 일반적인 자료형들은 모두 함수를 통해서 전역변수를 변화 시킬수 없는 불변의 값이다. 즉  immutable 하다.
#그러나 리스트, 집합과 같은 자료형은 함수내에서도 특정 함수를 통해 해당 값을 변화시킬 수 있는, mutable한 자료형이 되는 것이다.





#연습문제4
#list의 index를 직접 구현, 그러나 리스트가 find를 자체 내장하고 있지 않기 때문에, 
#lst.find(6)의 형태로 사용불가.

# lst = [1, 4, 6]
# print(lst.index(6))

# def find(self, any):
#     print(type(self), self)
#     a = 0
#     while a < len(self):
#         if any == self[a]:
#             return a
#         a += 1

# print(find(lst, 6))




# #연습문제5
# def starCount (layer) :
#     layer_count = 0
#     star_count = 0
    
#     while layer_count < layer :
#         layer_count += 1
#         print('*'*layer_count)
#         star_count += layer_count
        
#     return star_count

# layer = int(input('layer : '))
# print(f'별의 개수 : {starCount(layer)}') 




# 연습문제 6 이전
# def count_num(x) :
#     if x == 0 :
#         return 0
#     else :
#         count_num(x-1)
#         print(x)

# print('x=5',  count_num(5))



# #연습문제6
# def factorial_func (x) :
#     if x == 1 :
#         print(x, end = ' ')
#         return 1
#     else :
#         result = x * factorial_func(x-1)
#         print(x, end = ' ')
#         return result
        
# result_factorial = factorial_func(4)
# print(f'팩토리얼 결과 : {result_factorial}') 




# #알고리즘
# #파이썬에서 가능한 오름차순 정렬 코드
# list_num = [5, 1, 3, 7, 2, 9]
# print(f"초기 리스트 : {list_num}")
# rotate = len(list_num)

# for i in range(0, rotate-1) :
#     for j in range(i+1, rotate) :
#         if list_num[i] > list_num[j] :
#             list_num[i], list_num[j] = list_num[j], list_num[i]
            

#     print(f"{i+1}번째 정렬 : {list_num}")




# help(len)
# import builtins
# import statistics

# # dataset = range(1,6)
# # print(max(dataset))
# # print(statistics.mean(dataset))


# print(dir(builtins))