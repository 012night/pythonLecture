# msg = "반복문 연습"
# for word in msg :
#     print(word)


# list_cookies = ["홈런볼", "쿠쿠다스", "새우깡"]
# # print(list_cookies)
# for name in list_cookies :
#     print(name)

# list_num = [1,2,"3"]
# for x in list_num :
#     print(type(x), x)

# for a,b in [(1,2), (3,4), (5,6)] :
#     print(a, b)


# for num in [1,2,3,4,5,6,7,8,9,10] :
#     print(num)

# for num in range(1, 1001) :
#     print(num)

# for num in range(100) :
#     print(num)

# print함수 특성
# # 개행
# print(1, end=" ")
# print(2, end=" ")
# print(3)

# 구분자 , 
# print("메"+"가"+"스"+"터"+"디")
# print("메","가","스","터","디", sep="")

# for num in range(1,101) :
#     print(num, end=" ")

# for num in range(5,0,-1) :
#     print(num, end=" ")


# range(1,101)

# num_list = [1,2,3,4,5]
# print(sum(range(1,101)))

# # 1부터 100까지의 합을 구하세요
# sum_result = 0
# for num in range(1,101) :
#     # sum_result에다 num 변수가 가르키는 데이터를 누적해서 더하는 작업
#     sum_result = sum_result + num
#     # sum_result += num
# print(sum_result)

# dan = int(input("단수 입력 : "))

# for x in range(1,10) :
#     print(f"{dan} * {x} = {dan*x}")


# # 반복의 횟수를 제어하는 반복문
# count = int(input("반복 횟수 입력 : "))
# for x in range(1,count+1) :
#     print(x)

# for x in [1,2,3] :
#     print("반복")

# # 1~10까지 누적합을 계산하는 코드
# result = 0
# for x in range(1,11) :
#     result += x 
# print(result/len(range(1,11)))


# score = [6,10,7,7,8,9,4]
# score.sort()
# print("정렬 후",score)
# del score[0]
# del score[-1]
# # del score[len(score)-1]
# print("삭제 후 :", score)

# score_result = 0
# for x in score :
#     score_result += x
# print("평균 :",score_result/len(score))