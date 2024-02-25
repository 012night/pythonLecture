# for A[B영역의 데이터를 담을수 있는 변수] in B[반복가능한 데이터] : 
# msg = "for 반복문"
# for word in msg :
#     print(word)

# list_name = ["김", "이", "박", "최"]
# for name in list_name :
#     print(name)

# list_num = [1,2,3,4,5]
# for x in list_num :
#     print(x)

# tuple_list = [(1,2), (3,4), (5,6)]
# for x,y in tuple_list : # (1,2)
#     print(x, y)


#1~100까지 출력하세요
# for x in [1,2,3,4,5] :
#     print(x)

# for x in range(1,11) :
#     print(x)


# print함수의 특성
# # 1) 띄어쓰기(sep)
# print("나","는","피", "곤",sep="#")

# # 2) 개행(end)
# print(1,end=" ")
# print(2,end=" ")
# print(3)

# for x in range(1,11) :
#     # print(x, end=" ")
#     print("실행")

# 1~100까지의 누적합을 구하시오
# list_num = [1,2,3,4,5]

# result = 0
# for x in range(1,101) :
#     # result 라는 변수에 각각의 x값을 더해서 담아두면...
#     result += x
# print(result)

# dan = int(input("원하는 단수입력 : "))
# for x in range(1, 10) :
#     print(f"{dan}*{x}={dan*x}")

# 최고값과 최저값을 제외한 평균을 구하시오
# score = [10,8,9,4,6,7,9]
# score.sort()
# del score[0] #최저값
# del score[-1] #최고값
# del score[len(score)-1] #최고값
# del score[6] #최고값
# # print(sum(score))
# result = 0
# for x in score :
#     result += x
# print("누적합 :",result)
# print("평균 :",result/len(score))

# score = [10,8,9,4,6,7,9]
# print(max(score))
# print(min(score))