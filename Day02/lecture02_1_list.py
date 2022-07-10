# #  변수는 변수명당 각각의 데이터를 담는다. 
# #  그러나 변수가 많아질수록 관리하기가 힘들기 때문에, 리스트 등장.
# a = "피카츄"
# b = "라이츄"
# c = "파이리"
# d = "꼬부기"
# print(a)
# print(b)
# print(c)
# print(d)


# # 하나의 변수로 여러개의 데이터를 담고 관리하기 위해 리스트를 사용
#리스트(문자열)
# list_poke = ["피카츄", "라이츄", "파이리", "꼬부기"]
# print(list_poke)
# print(list_poke[0], list_poke[2])


# # 리스트(숫자)
# numbers = [19, 48, 83, 100]
# print(type(numbers), numbers)
# print(type(numbers[0]), numbers[0])
# print(numbers[0] + numbers[3])


# # 리스트 숫자 + 문자
# list_mix = [1, 2, "피카츄", "라이츄"]
# print(list_mix[0], list_mix[2])


# # 리스트 리스트 + 숫자
# list_mix = [["피카츄", "라이츄"], 1, 2]
# print(list_mix[0][1])


# # range 함수로 리스트 값 초기화
# list_range = list(range(0, 11))  # 0 ~ 10
# list_range_02 = list(range(2, 101, 2))  
# print(list_range)
# print(list_range_02)


# # 리스트 인덱싱
# # 문자열 인덱싱과 같다.
# a = [10, 1, 8, 2, 5]
# slice_a = a[0:3]
# slice_b = a[:3]
# print(slice_a)
# print(slice_b)


# 2차원 리스트에서 인덱싱으로 값을 가져오는 방법
# list_even = [[2,4,6,8,10],[12,14,16,18,20],[22,24,26,28,30]]
# print(list_even[0][0])
# print(list_even[1][0])
# print(list_even[2][0])


#========================================================================
# #연습문제 인덱싱
# list_ex1 = ['a', 'b', 'c', [1, 2, 3]]
# print(type(list_ex1))

# number = list_ex1[3]
# print(number)

# print(number[0]+number[2])
# print(str(number[0])+ " 더하기 " + str(number[2]) + "는 "+ str(number[0]+number[2]) + "이다")
# print("%d 더하기 %d는 %d이다" %(number[0], number[2], number[0]+number[2]))
# print("{} 더하기 {}는 {}이다".format(number[0], number[2],number[0]+number[2]))
#========================================================================


#리스트의 슬라이싱
# list_poke =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# print(list_poke[1:2])
# print(list_poke[:2])
# print(list_poke[2:])
# print(list_poke[:])


#리스트더하기
# list_poke_01 =  ["피카츄", "라이츄"]
# list_poke_02 = ["파이리", "꼬부기"]
# list_poke_all = list_poke_01 + list_poke_02
# print(list_poke_all)


# #리스트 반복하기
# list_num =  [1, 2, 3, 4]
# list_result = list_num * 3;
# print(list_result)
# #자료의 크기(길이)를 구하는 내장함수
# print(len(list_result))


# #리스트값 수정하기
# list_num  = [1, 3, 5, 7, 9, 10]
# print('수정전 list_num :', list_num)
# list_num[2] = 4
# print('수정후 list_num :', list_num)
# list_num[1:5] = [10, 20, 30, 40]
# print(list_num)


# # 리스트 요소 개수(숫자) 파악하기
# list_num  = [1, 2, 3, 4, 5, 1, 2]
# print(list_num.count(1))
# # 리스트 요소 개수(문자) 파악하기
# list_num  = ['1', '2', '3', '4', '5', '1', '2']
# print(list_num.count('1'))


# # 리스트 값 삭제하기 : 빈리스트로 교체
# list_num = list(range(1, 11))
# print('list_num              :', list_num)
# list_num[0:1] = []
# print('list_num[0]번 제거 후 :', list_num)


# # del : 파이썬이 자체적으로 가지고 있는 문법
# del list_num[0:2]
# print(list_num)


# # remove 인덱스 범위가 아닌 값으로 삭제시
# # 리스트 중 첫번째로 나오는 x 요소 제거
# list_num.remove(10)
# print(list_num)


# # append 함수: 리스트 마지막에 요소 추가
# # 리턴값이 없는 함수라는 것도 특이점.(대상 변수를 직점 바꿈)
# list_number = ["one", "two", "three", "four", "five"]
# list_number.append("six")
# print(list_number)
# list_number.append(['one', 'two', 'three'])
# print(list_number)

# list_test = list()
# list_test = []
# list_test.append("a")
# list_test.append("b")
# print(list_test)


# # insert 함수: 원하는 위치에 값 넣기
# print("### insert 함수")
# list_number = ["one", "two", "three", "four", "five"]
# list_number.insert(2,"2.5")
# print(list_number)
# list_number.insert(3,["3","4"])
# print(list_number)


# # insert 함수: 원하는 위치에 값 여러개 넣기
# print("### extend 함수")
# list_number.extend(["six", 7, "eight"])
# print(list_number)
# list_number[1:2] = [2, 3, 4, 5]
# print(list_number)


# # sort 함수 : 리스트 오름차순 정렬 >> 숫자는 낮은숫자부터, 문자는 ㄱㄴㄷㄹ abcd 순으로 정렬. 
# # 리턴값 없음(대상 변수를 직점 바꿈)
# list_name = ["박효신", "이수", "김범수", "나얼"]
# print(list_name.sort())
# print(list_name)
# print(list_name[0][0],list_name[1][0],list_name[2][0],list_name[3][0])


# # reverse 함수 : 리스트 자체를 뒤집기(순차 아님)
# list_name = ["박효신", "이수", "김범수", "나얼"]
# list_name.reverse()
# print(list_name)


#========================================================================
# # 연습문제 sort&reversed
# list_lang = ['banana', 'cat', 'egg', 'cat', 'apple', 'door']
# print(list_lang.sort())
# print(type(list_lang), list_lang)
# print(list_lang.reverse())
# print(type(list_lang), list_lang)

# # 연습문제 sort 옵션
# list_lang.sort(reverse=True)
# print(list_lang)
#========================================================================


# #index 함수(str과 같음) : 위치값 가져오기
# list_poke =  ["피카츄", "라이츄", "파이리", "꼬부기"]
# print(list_poke.index("꼬부기"))

# #index 함수 : 없는 값일때는 에러
# indexNum = list_poke.index("ㅌㅌㅌ")
# print(indexNum)


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


# # pop 함수: index번째에 있는 요소를 삭제하고 삭제된 값 반환 리스트 요소 꺼내기
# # 기본값은 마지막 인덱스
# list_poke = ["피카츄", "라이츄", "파이리", "꼬부기"]
# print(list_poke.pop())
# print(list_poke)
# list_poke.pop(1)
# print(list_poke)
# list_poke.pop(3) # 에러 유발

# # 추후 활용
# while list_poke :
#     print(list_poke.pop())


# #========================================================================
# # join함수
# a = ["life", "is", "too", "short"]
# print(type(a), a) 
# msg = ' '.join(a)
# print(type(msg), msg) 
# #========================================================================


# # split함수 복습(join과 반대)
# split_test = msg.split()
# print(type(split_test), split_test)


# # 키워드 in
# print("### 4. 어떤 값이 리스트에 포함되었는지 확인")
# if 5 in a:
#     print("들어있다")
# else:
#     print("들어있지 않다")


# # 리스트 연습문제
# lst = [10, 1, 5, 2]
# result = lst * 2
# print("단계 1", result)
# result.append(lst[0]*2)
# print("단계2 :", result)
# result2 = result[1:len(result):2]
# # result2 = result[1::2]
# print("단계3 :", result2)


#========================================================================
#리스트까지 배우면 할수 있는 연습문제 [1, 3, 5, 4, 2] - > [5, 4, 3, 2, 1]
# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a)
#========================================================================