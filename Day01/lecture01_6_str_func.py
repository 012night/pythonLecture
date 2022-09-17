# ============================================================================
# 함수란 무엇인가? (추후 배울 내용이므로 참고만)
# 프로그램속 작은 프로그램, 많은 기본 프로그램이 파이썬에 내장되어 있고, 그것을 내장함수라고 부르고, 가끔은 library라고 표현하기도 한다.
# def count (word, key) :
#     count = 0
#     for i in word :
#         if i == key :
#             count += 1
#     return count

# print(count('bbbc', 'd'))
# ============================================================================


# ============================================================================
# # 1.문자열 개수 세기(count)
# a = "python"
# countNum = a.count('o')
# print(type(countNum))
# print(countNum)
# ============================================================================


# ============================================================================
# # 2.문자열 위치 확인하기(find)
# a = "python"
# findNum = a.find('o')
# print(findNum)
# ============================================================================


# ============================================================================
# # 2-1.찾는 값이 없을 경우 -1 return(반환)
# a = "hobby"
# findNum = a.find('x')
# print(findNum)

# # 에러발생
# indexNum = a.index('x')
# print(indexNum)
# ============================================================================


# ============================================================================
# # 여러개를 찾고자 할때 enumerate 함수 사용법... 아직은 이르지만 알고만 있자...
# text = "hobby"
# print("Original list : " + text)
# res_list = [i for i, value in enumerate(text) if value == 'b']
# print("New indices list : " + str(res_list))
# ============================================================================


# ============================================================================
# # 3.소문자 <> 대문자 변경
# a = 'hi'
# print(a.upper())
# print('upper() 함수 사용후', a)

# a = 'HI'
# print(a.lower())
# print('lower() 함수 사용후', a)
# ============================================================================

    
# ============================================================================
# # 4.양쪽공백 지우기
# a = ' hi python '
# print(a)
# print("rstrip() 사용 후 :", a.rstrip())
# print("lstrip() 사용 후 :", a.lstrip())
# print(" strip() 사용 후 :", a.strip())
# ============================================================================


# ============================================================================
# # 5.문자열 바꾸기
# a = 'I studied python'
# print(a.replace('python', 'java'))
# print(type(a), a)
# print("함수 사용 후 a변수 :", a)
# ============================================================================


# ============================================================================
# # 문자열까지 배우면 할수 있는 [연습문제] // replace 사용하여 문자열 a:b:c:d -> a-b-c-d
# a = "a:b:c:d"
# print(a.replace(":","-").upper())
# print(a.replace(":","-").upper().find("C"))
# ============================================================================


# ============================================================================
# # 6.문자열 나누기(공백으로 나누기)
# a = 'I studied python'
# b = a.split()
# print(type(b), b)
# ============================================================================


# ============================================================================
# # 6-1.문자열 나누기(특정문자열로 나누기)
# a = 'I:studied:python'
# b = a.split(':')
# print(type(b), b)
# ============================================================================


# ============================================================================
# # 연습문제(숫자형)
# x = 2
# y= 2.5 * x**2 + 3.3 * x + 6
# print("2차 방정식의 결과 :", y)
# ============================================================================

