#  변수는 변수명당 각각의 데이터를 담는다. 
#  그러나 변수가 많아질수록 관리하기가 힘들기 때문에, 리스트 등장.
# a = "피카츄"
# b = "라이츄"
# c = "파이리"
# d = "꼬부기"
# print(d)

# #하나의 변수로 여러개의 데이터를 담고 관리.


# lista = ["피카츄", "라이츄", "파이리", "꼬부기"]
# print(lista)
# print(lista[0])


# #리스트 숫자
# lista = [1, 2, 3, 4]
# print(lista[0])
# print(lista[0]+lista[3])


# #리스트 숫자+문자
# lista = [1, 2, "피카츄", "라이츄"]
# print(lista[0])


# #리스트 리스트+숫자
# lista = [["피카츄", "라이츄"], 1, 2]
# print(lista[0][0])


# #리스트의 슬라이싱
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# print(lista[1:2])
# print(lista[:2])
# print(lista[2:])


# #리스트더하기
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# print(lista)
# listb = [1,2,3,4,5]
# print(listb)
# listc = lista + listb
# print(listc)


# #리스트 반복하기
# lista =  [1, 2, 3, 4]
# listb = lista * 3;
# print(listb)
# print(len(listb))


# #리스트값 수정하기 >> 1개값 바꿀땐 1개변수로, 여러값 바꿀떈 다른 리스트로 교체
# lista  = [ 1, 3, 5, 7, 9, 10]
# lista[2] = 4
# print(lista)
# lista  = [ 1, 3, 5, 7, 9, 10]
# lista[1:5] = [2,3,4,5]
# print(lista)


# #리스트 값 삭제하기 >> 빈리스트로 교체
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# lista[0:1] =[]
# del lista[0:2]
# print(lista)
# lista[0:2] = []
# print(lista)
#인덱스가 아닌 값으로 삭제시
# lista.remove("피카츄")

#리스트에 요소추가 >> append >>맨뒤에 추가. 
#리턴값이 없는 함수라는 것도 특이점.(대상 변수를 직점 바꿈)
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# lista.append("버터풀")
# lista.append([1,2,3])
# lista.insert(2,"버터풀2")
# lista.insert(3,("나이스","파이썬"))
# lista.extend(["야도란", 2, "asd"])
# print(lista)


# #리스트 정렬 >> sort >> 숫자는 낮은숫자부터, 문자는 ㄱㄴㄷㄹ abcd 순으로 정렬. 
# 리턴값 없음.(대상 변수를 직점 바꿈)
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# lista.sort()
# print(lista)


# #리스트 뒤집기 >> reverse >> 뒤에서부터 순서변경, 
# 리턴값 없음.(대상 변수를 직점 바꿈)
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# lista.reverse()
# print(lista)


# 리턴값 있음. (대상 변수를 직점 바꾸지 않음.)
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# indexNum = lista.index("꼬부기")
# print(indexNum)
# print(lista.index("꼬부기"))
# stra = "Courage is very important. Like a muscle, it is strengthened by use."
# indexNum2 = stra.index("b")
# print(indexNum2)
# print(stra.find("ㅋ"))
# print(stra.index("ㅋ"))

# #리스트 요소 꺼내기 (pop) >> 마지막 요소 꺼내는 
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# lista.pop(3)
# print(lista)
# lista.pop(3) -> 에러 유발

# lista =  ["1", "2", "3", "4", "1", "1", "3"]
# countNum = lista.count("1")
# print(countNum)


#========================================================================
#연습문제 1
# list_ex1 = ['a', 'b', 'c', [1, 2, 3]]
# print(type(list_ex1))

# number = list_ex1[3]
# print(number)

# print(number[0])

# print(number[0]+number[2])
# print(str(number[0])+ " 더하기 " + str(number[2]) + "는 "+ str(number[0]+number[2]) + "이다")
# print("%d 더하기 %d는 %d이다" %(number[0], number[2], number[0]+number[2]))
# print("{} 더하기 {}는 {}이다".format(number[0], number[2],number[0]+number[2]))
#========================================================================

#========================================================================
#연습문제 2
# list_lang = ['p', 'y', 't', 'h', 'o', 'n']
# print(type(list_lang))

# print(list_lang.sort())
# print(list_lang)
# print(list_lang.reverse())
# print(list_lang)
#========================================================================

#========================================================================
#리스트까지 배우면 할수 있는 연습문제 6번 [1, 3, 5, 4, 2] - > [5, 4, 3, 2, 1]
# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a)
#========================================================================


#========================================================================
#리스트까지 배우면 할수 있는 연습문제 7번
# a = ["life", "is", "too", "short"]
# print(type(a)) 
# msg = ' '.join(a)
# print(type(msg)) 
# print(msg)
#========================================================================