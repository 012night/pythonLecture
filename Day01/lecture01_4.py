#1.문자열 자료형은 "" '' """ ''' 의 형태

# a = "Hello World"
# print(a)
#Python's fun은 어떻게 출력?
# a = "python's fun"
# print(a)

#2.여러줄로 이루어진 문자열 : \n
# a = "Life is too short, \nYou need python "
# print(a)
#더 편한 방법
# a = """
# Life is too short,
#
# test
#
# You need python """
# print(a)


#3.문자열 자료형은 str
# print(type(a))

#4.문자열 더하고 곱하기
# a = "Python "
# b = "is fun"
# print(a+b)

# a = '='
# print(a*20)


#5.문자열 인덱싱, 모든 인덱싱은 0부터 시작
# a = "Python is fun"
# print(a[-1])
# print(a[13])

#6.문자열 슬라이싱, [x:y] x이상 y미만
# a = "Python is fun"
# print(a[:6])
# print(a[6:])
# print(a[::3])
# print(a[::-1])


# a = "20220505children’s_day"

# date = a[:8]
# print(type(date))
# day = a[8:]
# print(type(day))

# print("금일 " + date + "은 " + day + "입니다")
# print("금일 {}은 {}입니다".format(date, day))
# print(f"금일 {}은 {}입니다".format(date, day))
