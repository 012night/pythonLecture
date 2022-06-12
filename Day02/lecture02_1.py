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
# print(lista[0], lista[2])


#리스트 숫자
# lista = [1, 2, 3, 4]
# print(lista[0])
# print(lista[0] + lista[3])


# #리스트 숫자 + 문자
# lista = [1, 2, "피카츄", "라이츄"]
# print(lista[0])


# #리스트 리스트+숫자
# lista = [["피카츄", "라이츄"], 1, 2]
# print(lista[0][0])



#========================================================================
#연습문제 인덱싱
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



# #리스트의 슬라이싱
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# print(lista[1:2])
# print(lista[:2])
# print(lista[2:])
# print(lista[:])


# #리스트더하기
# lista =  ["피카츄", "라이츄"]
# print(lista)
# listb = ["파이리", "꼬부기"]
# print(listb)
# listc = lista + listb
# print(listc)


# #리스트 반복하기
# lista =  [1, 2, 3, 4]
# listb = lista * 3;
# print(listb)
# print(len(listb))


# #리스트값 수정하기
# lista  = [1, 3, 5, 7, 9, 10]
# print('수정전 lista :', lista)
# lista[2] = 4
# print('수정후 lista :', lista)

# lista  = [1, 3, 5, 7, 9, 10]
# lista[1:5] = [2,3,4,5]
# print(lista)


# #리스트 요소 개수 파악하기
# lista  = [1, 2, 3, 4, 5, 6, 1, 2, 1]
# print(lista.count(1))



# #리스트 값 삭제하기 >> 빈리스트로 교체
# lista = ["피카츄", "라이츄", "파이리", "꼬부기"]
# lista[0:1] =[]
# print('[1]번 값 지운 후 lista', lista)
# del lista[0:2]
# print(lista)

# # 인덱스가 아닌 값으로 삭제시
# lista.remove("피카츄")
# print(lista)



#리스트에 요소추가 >> append >>맨뒤에 추가. 
#리턴값이 없는 함수라는 것도 특이점.(대상 변수를 직점 바꿈)
# lista = ["피카츄", "라이츄", "파이리", "꼬부기"]
# lista.append("버터풀")
# print(lista)
# lista.append([1,2,3])
# print(lista)
# lista.insert(2,"버터풀2")
# print(lista)
# lista.insert(3,("나이스","파이썬"))
# print(lista)
# lista.extend(["야도란", 2, "asd"])
# print(lista)
# lista[1:2] = ['라이츄', '라이츄2', '라이츄3', '라이츄4']
# print(lista)



##리스트 정렬 >> sort >> 숫자는 낮은숫자부터, 문자는 ㄱㄴㄷㄹ abcd 순으로 정렬. 
# 리턴값 없음(대상 변수를 직점 바꿈)
# lista = ["피카츄", "라이츄", "파이리", "꼬부기"]
# print(lista.sort())
# print(lista)



#리스트 뒤집기 >> reverse >> 뒤에서부터 순서변경, 
# 리턴값 없음.(대상 변수를 직점 바꿈)
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# lista.reverse()
# print(lista)



#========================================================================
#연습문제 sort
# list_lang = ['p', 'y', 't', 'h', 'o', 'n']
# print(type(list_lang))

# print(list_lang.sort())
# print(list_lang)
# print(list_lang.reverse())
# print(list_lang)
#========================================================================



# #리스트 인덱싱을 통한 위치값 가져오기
# lista =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# indexNum = lista.index("꼬부기")
# print(indexNum)
# print(lista.index("꼬부기"))



# #지금 단계에서 할순 없지만 여러개의 인덱스를 가져오는 방법
# test_list = [1, 3, 4, 3, 6, 7]
# print("Original list : " + str(test_list))

# index_list = []
# for i, value in enumerate(test_list) :
#     if value == 3 :
#         print(i, value)
#         index_list.append(i)
# print(index_list)


# #위 코드를 리스트 내포 방법으로...
# index_list = [(i,value) for i, value in enumerate(test_list) if value == 3]
# print("New indices list : " + str(index_list))


# stra = "Courage is very important. Like a muscle, it is strengthened by use."
# indexNum2 = stra.index("b")
# print(indexNum2)
# print(stra.find("ㅋ"))
# print(stra.index("ㅋ"))




# #리스트 요소 꺼내기 (pop) >> 마지막 요소 꺼내는 
# lista = ["피카츄", "라이츄", "파이리", "꼬부기"]
# lista.pop(3)
# print(lista)
# lista.pop(3) # 에러 유발



#========================================================================
#리스트까지 배우면 할수 있는 연습문제 [1, 3, 5, 4, 2] - > [5, 4, 3, 2, 1]
# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a)
#========================================================================



#========================================================================
# join함수
# a = ["life", "is", "too", "short"]
# print(type(a)) 
# msg = ' '.join(a)
# print(type(msg)) 
# print(msg)
#========================================================================


    
#리스트 연습문제
# lst = [10, 1, 5,2]
# result = lst * 2
# print("단계 1", result)
# result.append(lst[0]*2)
# print("단계2 :", result)
# result2 = result[1:len(result):2]
# # result2 = result[1::2]
# print("단계3 :", result2)