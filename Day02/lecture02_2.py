# # #튜플 선언
# a  = ( )    # 빈값
# print(type(a), a)
# a  = (1, )   # 숫자
# print(type(a), a)
# a  = ('python', 'is', 'fun')   # 문자
# print(type(a), a)
# a  = 1, 2, 'python'   # 숫자 + 문자
# print(type(a), a)
# a  = (1, 2, ('python', 'is', 'fun'))   # 숫자 + 리스트
# print(type(a), a)



#튜플 값 삭제시 >> 에러발생
# t1 = (1, 2, 'a', 'b')
# del t1[0]

# #튜플 값 변경시 >> 에러발생
# t1 = (1, 2, 'a', 'b')
# t1[3] = 'c'


# #튜플 값 인덱싱, 슬라이싱
# t1 = (1, 2, 'a', 'b')
# print(t1[3])
# print(t1[0:3])
# print(t1)


# #튜플의 더하기, 곱하기 >> 
# 새로운 튜플을 만들어 낸 것이지 기존의 튜플은 변하지 않는다.
# t1 = (1,2, 'a', 'b')
# t2 = (3,4, 'c', 'd')
# print(t1+t2)
# print(t1*2)