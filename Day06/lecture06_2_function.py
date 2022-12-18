# ============================================================================
# # 2개 이상의 리턴값이 있을경우(두수를 input값으로 전달하여 두수의 합,차,곱을 리턴해주는 함수라면...)
# def cal(a, b):
#     result1 = a + b
#     result2 = a - b
#     result3 = a * b
#     return result1, result2, result3

# result = cal(1,2)
# print(result)

# plus_result = result[0]
# print(plus_result)

# result1, result2, result3 = cal(1,2)
# print(result1)
# print(result2)
# print(result3)
# ============================================================================


# ============================================================================
# # 리턴값이 두개인 튜플관련 예제
# def sum_limit_100(n):
#     sum = 0
#     last_num = 0
#     for i in range(1, n + 1):
#         sum += i
#         last_num = i

#         if sum > 100:
#             break
#     return sum, last_num

# n = int(input("수를 입력하세요"))
# s, last_num = sum_limit_100(n)
# print("합은 %d이고 마지막으로 더해진 수는 %d이다." % (s, last_num))
# print("합은 %d이고 마지막으로 더해진 수는 %d이다." % sum_limit_100(n))
# ============================================================================


# ============================================================================
# return의 또다른 용도(함수의 종료)
# def speak(msg) :
#     if msg == "종료" :
#         return
#         print("{msg}를 입력하셨습니다,")
#     else :
#         print(msg,"라고 입력하셨네요?")

# while True :
#     msg = input("메시지를 입력하세요 :")
#     speak(msg)
#     if msg == "종료" :
#         break
# ============================================================================


# ============================================================================
# # default값 미리 세팅하기
# def cal(a, b, choice="All"):
#     if choice == "All" :
#         result1 = a + b
#         result2 = a - b
#         result3 = a * b
#         result4 = a // b
#         return result1, result2, result3, result4
#     elif choice == "+" :
#         result = a + b
#         return result
#     else :
#         pass
    
# result = cal(1,2)
# # result = cal(1,2, choice="+")
# # result = cal(1,2, False)
# print(result)
# ============================================================================


# ============================================================================
# # 함수의 매개변수의 순서를 맞춰야 하는가? 안맞춰도 되는 방법은?
# def whoareyou(name, age, gender):
#     print("제 이름은 %s 이고 나이는 %d 살, 그리고 성별은 %s 입니다." %(name, age, gender))
# whoareyou(age=19, name='홍길동', gender= '남자')
# whoareyou(19,'홍길동',  '남자')
# ============================================================================


# ============================================================================
# # lambda 함수의 사용
# def add(a, b):
#     return a + b

# add = lambda a, b : a + b
# print(add(1,2))
# ============================================================================


# ============================================================================
# # lamda를 사용하는 이유. list같은 형태로 담는 등, 자유도가 높다.
# add_mul_List = [lambda a, b: a+b, lambda a, b : a*b]
# print(add_mul_List[0](1,2))
# print(add_mul_List[1](3,4))

# lst = []
# lst.append(add_mul_List[0](1,2))
# lst.append(add_mul_List[1](3,4))
# print(lst)
# ============================================================================


# ============================================================================
# # 지역변수와 전역변수 란 무엇인가
# # 지역변수의 예 : 함수안의 변수
# # 전역변수의 예 : 함수밖의 변수
# a = 2
# def sum(a):
#     a = a + 1
#     return a

# result = sum(a)
# print(result)
# print(a)
# ============================================================================


# ============================================================================
# # 아래 코드에서 result값은 어디에 정의 되어 있는가?
# # 함수 내에서 result를 선언하는 과정에서 정의되지 않은 result 값을 참조하는 상황이 발생
# result = 2
# def sum(a) :
#     # result = 1
#     result = result + a
#     return result
# sumvalue = sum(1)
# print(sumvalue)
# ============================================================================


# ============================================================================
# 위가 헷갈리는가? 이것과 같은 이치
# a = a+1
# print(a)
# ============================================================================


# ============================================================================
# # 새로운 지역변수 선언을 하는데 전역변수의 값을 가져와 사용하는것은 괜찮다.
# result = 2
# def sum(a) :
#     # result = 1
#     result_func = result + a
#     return result_func
# sumvalue = sum(1)
# print(sumvalue)
# ============================================================================


# ============================================================================
# # 함수안에서의 변수들은 함수가 호출이 끝나면 사라진다. 메모리 호출 구조를 보면 더 편하다
# # https://pythontutor.com/live.html#mode=edit 참고
# # 모든 변수는 메모리에 담긴다. 그러나 메모리의 어떤 영역에 담기느냐에 따라, 그 효력 범위가 달라진다.
# # 파이썬의 메모리 구조 참고 http://www.tcpschool.com/c/c_memory_structure
# ============================================================================


# ============================================================================
# # 전역 변수에 영향을 주고 담아두고 싶으면 아래 2가지 방법을 써야 한다.
# # 전역변수 a에 영향을 줄 수 있는 방법 01 
# # 전역변수 a에 다시 할당/초기화 한다.
# a = 2
# print(a)
# def sum(a):
#     a += 1
#     return a
# a = sum(a)
# print(a)
# ============================================================================


# ============================================================================
# # 전역변수 a에 영향을 줄 수 있는 방법 02 
# # global 키워드 선언
# result = 2
# def sum(a):
#     global result
#     result += a
#     # return result
# sumvalue = sum(1)
# print(sumvalue)
# print(result)
# ============================================================================


# ============================================================================
# # 그런데 특이한 자료 구조가 있다. list를 생각해보자.
# # 아래와 같은 자료구조의 특성을 보면 이해할 수 있다.
# # 함수도 메모리에 주소가 할당되어 저장되지만, 함수 내의 지역변수는 스택에 저장되어 휘발되도록 한다.
# # 그에 반해 list의 append는 object로서 heap 메모리라는 휘발되지 않는 공간에 변수값을 추가 하는 것므로 날아가지 않는다.
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
# ============================================================================


# ============================================================================
# mutable immutable
# 위에서 말한 일반적인 자료형들은 모두 함수를 통해서 전역변수를 변화 시킬수 없는 불변의 값이다. 즉  immutable 하다.
# 그러나 리스트, 집합과 같은 자료형은 함수내에서도 특정 함수를 통해 해당 값을 변화시킬 수 있는, mutable한 자료형이 되는 것이다.
# ============================================================================


# ============================================================================
# # 연습문제 04
# # list의 index를 직접 구현, 그러나 리스트가 find를 자체 내장하고 있지 않기 때문에, 
# # lst.find(6)의 형태로 사용불가.

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
# ============================================================================


# ============================================================================
# # 연습문제 05
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
# ============================================================================


# ============================================================================
# 연습문제 06 이전
# def count_num(x) :
#     if x == 0 :
#         return 0
#     else :
#         count_num(x-1)
#         print(x)

# print('x=5',  count_num(5))
# ============================================================================


# ============================================================================
# # 연습문제 06
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
# ============================================================================


# ============================================================================
# # 키워드 파라미터(키와 value를 받아 dic 형태로 값을 받는 방법)
# def dic(**kwargs) :
#     print(kwargs)
# dic(a=1, b='파이썬')
# ============================================================================


# ============================================================================
# list_num = [7,2,3,6]
# list_num.sort() #는 list.sort(list_num)와 같다.
# print(list_num)
# print(1+1) #은 print(int.__add__(1, 2)) 와 같다.
# ============================================================================

# list_num = [7,2,3,6]
# list_num.sort()
# # list.sort(list_num)
# print(list_num)
# # list_num.sort()