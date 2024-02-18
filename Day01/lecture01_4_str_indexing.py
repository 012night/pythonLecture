# # 1.문자열 자료형은 "" '' """ ''' 의 형태

# a = "Hello World"
# print(a)
# # Python's fun은 어떻게 출력?
# a = "python's fun"
# print(a)

# # 2.여러줄로 이루어진 문자열 : \n
# a = "Life is too short, \nYou need python "
# print(a)
# # 더 편한 방법
# a = """
# Life is too short,

# test

# You need python """
# print(a)


# # 3.문자열 자료형은 str
# print(type(a))


# # 4.제어문자(이스케이프 시퀀스 , 이스케이프 문자) , 서식문자
# # - 콘솔에서 특수한 기능을 하는 문자들, 약 30가지정도 된다...
# # - 문자열에서 실행 시키고자 하는 위치에 \를 적고 뒤에
# #   기능에 맞는 문자를 적으면 된다..

# # \n (New Line , Line Feed) - Enter
# # - 커서를 다음줄로 이동시키는 제어문자...
# print("이름 : 김메가\n전화번호 : 010-1234-5678")


# # \t (Tab) - Tab
# #  - 커서를 Tab크기만큼 이동시키는 제어문자...
# print("이름\t : 김메가\n전화번호 : 010-1234-5678")


# # \r(Carriage Return) - 커서를 줄의 처음으로 이동시키는 제어문자
# # \b(Back Space) - 커서를 왼쪽으로 한칸 이동시키는 제어문자...
# print("abcdefg\b\b\b\b",end=" ")
# print("abcdefg\rABC")
# print("abcdefg\b\b\b")


# #문자열에서 특수한 기능을 하는 문자들을 출력할때는
# # \뒤에 적어주어야 한다...
# # C:\김메가\Python\WorkSpace\test
# print("C:\김메가\Python\WorkSpace\test")
# print("C:\김메가\Python\WorkSpace\\test")


# # "" , ''
# print("\"HI\"")
# print('"HI"')
# print("'HI'")
# print('\'HI\'')


# # """, '''
# print('''   이름:김메가
#    전화번호:010-1234-5678
#    주소:서울시 강남구
# ''')


#5.문자열 더하고 곱하기
# a = "Python "
# b = "is fun"
# print(a+b)
# a = '='
# print(a*20)


# #print함수 예쁘게 꾸미기
# print("\t#### 회비 정보 ####")
# print("="*40)
# print("이름\t나이\t전화번호\t회비")
# print("="*40)
# print("김범수\t38\t010-1111-1111\t\\20,000")
# print("나  얼\t24\t010-1234-5678\t\\30,000")
# print("박효신\t25\t010-2525-2345\t\\50,000")
# print("-"*40)
# print("총합계\t\t\t\t\\100,000")
# print("="*40)


#6.문자열 인덱싱, 모든 인덱싱은 0부터 시작
# a = "Python is fun"
# print(a[-1])
# print(a[13])


#7.문자열 슬라이싱, [x:y] x이상 y미만
# a = "Python is fun"
# print(a[:6])
# print(a[6:])
# print(a[::3])
# print(a[::-1])


a = "20221225Christmas"
date = a[:8]
# print(type(date))
day = a[8:]
# print(type(day))

print(date + "은 " + day + "입니다")


print("{}은 {}입니다".format(date, day))
print(f"{date}은 {day}입니다")
