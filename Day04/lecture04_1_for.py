# # For문 예제를 통한 이해1(문자열)
# str1 = 'for 반복문 연습'
# for i in str1 :
#     print(i)


# # For문 예제를 통한 이해2(리스트)
# list_cookies = ['새우깡', '홈런볼', '초코파이']
# for cookie in list_cookies :
#     print(cookie)


# # 변수의 범위? 영향력 이해
# a = 0
# for a in [1,2,3] :
#     print(a)
#     a = 0
#     print(a)
# print(a)


# # for문 예제 01(list)
# list_num = ['one', 'two', 3]
# for a in list_num:
#     print(type(a), a)


# # 튜플로 구성된 리스트
# tupleList = [(1, 2), (3, 4), (5, 6)]
# for a, b in tupleList:
#     print(a + b)


# # 긴 범위를 쉽게 작성할 수 있게 도와주는 range함수
# for num in range(1, 101): #슬라이싱 범위와 같은 개념
#     print(num)
#     # print(num, end=' ')


# # For문 예제를 통한 이해(range01)
# for num in range(101) :   # 0 ~ 100
#     print(num)
# print("=" * 50)


# # For문 예제를 통한 이해(range03)
# for i in range(5, 0, -1):   # 5 4 3 2 1 0
#     print(i)


# # 반복할 횟수만큼 돌기
# count = int(input("반복할 횟수를 입력하세요:"))   # 3
# for i in range(count):  # 0 1 2 => 3번
#     print(i, end=' ')
# print()
# print("끝")


# # for문 예제 02(추가적인 변수 사용법)
# sum = 0
# for i in range(1, 101):
# # for num in range(101) :
#     sum = sum + i
# print(sum)


# # for문 예제 03(구구단)
# number = int(input("단수를 입력하세요:"))
# for i in range(1, 10):  # 1 2 3 4 5 6 7 8 9
#     print(f"{number} X {i} = {number * i}")



# # for문 예제 04(and 활용)
# # 1~100사이에서 3의 배수이면서 2의 배수가 아닌 수를 한줄에 출력하고, 누적합을 출력.
# num_list = range(1,101)
# sum = 0

# for num in num_list :
#     if num % 3 ==0 and num % 2 != 0 :
#         print(num, end=' ')
#         sum += num
#     else :
#         pass
# print(f"\n누적합은 {sum} 입니다.")





# # [1 2 3 4 5 6 7 8 9] 리스트 완성하기
# ========================================================================
# a = [4, 3, 5, 7, 9, 2, 1]   # 6, 8
# a.sort()     # [1, 2, 3, 4, 5, 7, 9]

# for i in range(9):   # 0 1 2 3 4 5 6 7 8
#     if a[i] != i + 1:
#         a.insert(i, i + 1)
# print(a)
# ========================================================================




# # 최고점과 최저점을 제외하고 평균을 구하시오
# ========================================================================
# scores = [8, 7, 8, 8, 9, 4, 6, 8, 10, 8]

# scores.sort()
# del scores[0]   # 최저점 
# del scores[len(scores) - 1] # 최고점

# sum = 0
# for score in scores:
#     sum += score

# print("최고점과 최저점을 제외한 평균 점수는 %g입니다." % (sum / len(scores)))
# ========================================================================