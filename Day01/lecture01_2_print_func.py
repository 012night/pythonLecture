# 주석(#)이란 파이썬의 인터프리터가 인식하지 못하도록 하는 기호, 단축키는 Ctrl+/
# 개발자가 보기 위한 설명. 프로그램 수행시 해석되지 않는 코드


# 함수 - 어떠한 기능을 실행시키기 위해서 미리 정의한 코드의 집합체...
# print - python에서의 표준 출력 명령(함수)
# ()안에 출력시키고자 하는 내용을 적으면 된다...
print(3+5)
print("Hello python!")
print('Hello python!')
print("Hello python!",12345)

print(10)
print(12.364)


# 파이썬에서는 함수의 옵션이 존재한다..
# end
# - 출력할때 가장 끝에 자동으로 삽입되는 문자를 지정하는 옵션
# - 디폴트값으로 \n으로 지정되어 있다...
print(1, end="******")
print(2)


# sep
# - 데이터들을 출력할때 중간중간 삽입되는 문자를 지정하는 옵션
# - 디폴트값으로 Space로 지정이 되어 있다..
print(1,2,3,4,5,6)
print(1,2,3,4,5,6,sep=" ")
print(1,2,3,4,5,6,sep="\n")
print(1,2,3,4,5,6,sep=":")



# 문자나 문자열
# - 문자나 문자열을 데이터로써 구분하기위해 '' or ""를 통해서 구분짓는다...
# - python은 문자나 문자열을 별도로 구분하지 않는다...
# - C계열과 JAVA는 문자는 '' , 문자열은 ""로 구분한다..
print('print')
print("print")

# print를 통해서 여러개의 데이터를 출력하는 법....
# , - 구분점
print(10,12.34,'T',"Hello")




#1.변수에 대해 알아보자.
# 정수형 변수(Integer)
a = 10    # a변수에 정수 10이라는 값을 넣는다, 할당한다, 초기화 한다.
print(a)

#변수에 담긴 값을 재할당, 변경한다, 초기화 한다.
a = 20
print(a)

#2.변수 자료형 출력
#변수의 자료형을 출력한다. 결과 : 숫자 >> 정수(int)
print(type(a))
#실수의 자료형을 출력한다. 결과 : 숫자 >> 실수(float)
a = 2.1
print(type(a))