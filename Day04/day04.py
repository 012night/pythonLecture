# #For문 예제를 통한 이해1(문자열)
# str1 = 'for 반복문 연습'
# for i in str1 :
#     print(i)



# #For문 예제를 통한 이해2(리스트)
# list_cookies = ['새우깡', '홈런볼', '초코파이']
# for cookie in list_cookies :
#     print(cookie)



# #for문 기본 예제1
# list_num = ['one', 'two', 'three']
# for a in list_num:
#     print(type(a))
#     print(a)



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
# for (a, b) in tupleList:
#     print(a + b)



#긴 범위를 쉽게 작성할수 있게 도와주는 range함수
# for num in range(1, 101): #슬라이싱 범위와 같은 개념
    # print(num)
    # print(num, end=' ')



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



#break문 기본 이해
# for num in range(1,11) : 
#     if num == 4 :
#         print(f"숫자 {num}이 나와 종료합니다.")
#         break
#     print(f"숫자 {num}")
# print("프로그램을 종료합니다.")



#continue문 기본 이해
# for num in range(1,11) : 
#     if num == 4 :
#         continue
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



#60점 이상인 학생들의 합격 문구 출력 예시(continue)
# score = [66, 72, 45, 89, 31]

# for i in range(len(score)) :
#     if score[i] < 60 :
#         continue
    
    # print(f"{i+1}번 학생 {score[i]}점으로 합격입니다.")




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