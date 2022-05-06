#0.함수란 무엇인가? (추후 배울 내용이므로 참고만)
#프로그램속 작은 프로그램, 많은 기본 프로그램이 파이썬에 내장되어 있고, 그것을 내장함수라고 부르고, 가끔은 library라고 표현하기도 한다.
# a = "hobby"
# def countCharacter(character):
#     count = 0
#     characterList = list(character)
#     for c in characterList:
#         if(c == 'b'):
#            count = count +1
#     return count
# print(countCharacter(a))


# def count (word) :
#     count = 0
#     for i in word :
#         if i == 'b' :
#             count += 1
#     return count
# print(count('bb'))


#1.문자열 개수 세기(count)
# a = "hobby"
# countNum = a.count('o')
# print(countNum)


#2.문자열 위치 확인하기(find)
# a = "python"
# findNum = a.find('o')
# print(findNum)


#2-1.찾는 값이 없을 경우 -1 return(반환)
# a = "hobby"
# findNum = a.find('x')
# print(findNum)


#4.소문자 <> 대문자 변경
# a = 'hi'
# print(a.upper())
# a = 'HI'
# print(a.lower())

    
#5.양쪽공백 지우기
# a = ' hi python '
# print(a.strip())


#6.문자열 바꾸기
# a = 'I studied python'
# print(a.replace('python', 'java'))
# print(type(a))


#7.문자열 나누기
#공백으로 나누기
# a = 'I studied python'
# b = a.split()
# print(b)


#특정문자열로 나누기
# a = 'I:studied:python'
# b = a.split(':')
# print(b)