# #For문 예제를 통한 이해1(문자열)
# str1 = 'for 반복문 연습'
# for i in str1 :
#     print(i)



# #For문 예제를 통한 이해2(리스트)
# list_cookies = ['새우깡', '홈런볼', '초코파이']
# for cookie in list_cookies :
#     print(cookie)



# list_a = [1,2,3] 
# iter_test = iter(list_a)
# print(type(iter_test))
# print(next(iter_test))
# print(next(iter_test))
# print(next(iter_test))
# try :
#     print(next(iter_test))
# except :
#     print('더이상 없습니다')




# #변수의 범위? 영향력
# a=0
# for a in [1,2,3] :
#     print(a)
#     a=0
#     print(a)




# #for문 기본 예제1
# list_num = ['one', 'two', 3]
# for a in list_num:
#     print(type(a), a)



##for문 예제2
# lista = [90, 25, 67, 45, 80]
# no = 0

# for a in lista :
#     no += 1
#     if a >= 60 :
#         print("{}번 학생 {}점으로 합격입니다".format(no, a))
#     else :
#         print("{}번 학생 {}점으로 불합격입니다".format(no, a))



#튜플로 구성된 리스트
# tupleList = [(1, 2), (3, 4), (5, 6)]
# for a, b in tupleList:
#     print(a + b)



#긴 범위를 쉽게 작성할수 있게 도와주는 range함수
# for num in range(1, 101): #슬라이싱 범위와 같은 개념
#     print(num)
#     # print(num, end=' ')



# #for문 range 예제
# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)



# #for문 range를 다르게 작성
# sum = 0
# for num in range(101) : 
#     sum += num
# print(sum)



#continue문 기본 이해
# for num in range(1,11) : 
#     if num == 4 :
#         continue
#     print(f"숫자 {num}")
# print("프로그램을 종료합니다.")


# for num in range(1,11) : 
#     print(f"숫자 {num}")
#     # continue
#     break
#     print("컨티뉴 다음 문장입니다")
# print("프로그램을 종료합니다.")
    



#break문 기본 이해
# for num in range(1,11) : 
#     if num == 4 :
#         print(f"숫자 {num}이 나와 종료합니다.")
#         break
#     print(f"숫자 {num}")
# print("프로그램을 종료합니다.")



##for문과 continue
# lista = [90, 25, 67, 45, 80]
# no = 0
# for a in lista:
#     no += 1
#     if a < 60:
#         continue
#     print("%s번 학생 %s점으로 합격입니다." %(no,a))



# #60점 이상인 학생들의 합격 문구 출력 예시(continue)
# score = [66, 72, 45, 89, 31]

# for i in range(len(score)) :
#     if score[i] < 60 :
#         continue
#     print(f"{i+1}번 학생 {score[i]}점으로 합격입니다.")




# ##for문과 break >> 가장 먼저 뽑힌 a형 고객을 찾는다. >> 선착순 1명만 찾는다고 한다고 할때
# lista = ['b', 'b', 'ab', 'a', 'b', 'b']
# seq = 0

# for blood in lista :
#     seq += 1
#     if blood == 'a' :
#         print("{}번 고객님 {}형이시군요. 당첨되셨습니다.".format(seq, blood))
#         break
#     else :
#         print("{}번 고객님{}형이시군요. 불발입니다.".format(seq, blood))



#연습문제 : 3의 배수이며 2의 배수가 아닌 값 찾기
#1~100사이에서 3의 배수이면서 2의 배수가 아닌 수를 한줄에 출력하고, 누적합을 출력.

# num_list = range(1,101)
# sum = 0

# for num in num_list :
#     if num % 3 ==0 and num % 2 != 0 :
#         print(num, end=' ')
#         sum += num
#     else :
#         pass
# print(f"\n누적합은 {sum} 입니다.")



#range 함수를 이용한 리스트 만들기
# list = list(range(1,11))


#리스트 내포 변형 전
#1~100까지의 숫자중에 3의 배수를 리스트에 담은 후 해당 리스트를 print 하여라.
# list_result = []
# for num in range(1, 101) :
#     if num % 3 == 0 :
#         list_result.append(num)
# print(list_result)



#리스트 내포 변형 후
# #1~100까지의 숫자중에 3의 배수를 리스트에 담은 후 해당 리스트를 print 하여라
# list_result = [num for num in range(1, 101) if num % 3 == 0]
# print(list_result)



#이중 포문을 활용한 구구단 출력
# for x in range(2,10) :
#     for y in range(1,10) :
#         print("{} * {} = {}".format(x, y, x*y))




#이중 포문을 활용한 구구단 출력(좀 예쁘게 출력)
# for x in range(2,10) : 
#     print("")
#     for y in range(1,10) :
#         print(f"{x} * {y} = {x*y}", end=' ')



# # 제어문(반복문_for) list, set, dic 모두 이용한 마지막 for 예제
# # 각종 형 변환 활용가능
# list_position = ['과장', '부장', '대리', '사장', '대리', '과장']
# set_position = set(list_position)
# set_to_list_position = list(set_position)
# set_to_list_position.sort(reverse=True)
# print(f"중복되지 않은 직급 : {set_to_list_position}")

# dic_position = {}
# for position1 in set_to_list_position:
#     count = 0
#     for position2 in list_position:
#         if position1 == position2:
#             count += 1
#     dic_position[position1] = count

# print(f"각 직급별 인원수 : {dic_position}")