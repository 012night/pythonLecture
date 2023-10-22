# a = 1 
# if a < 10 :
#     pass
# else :
#     print('???')


# if - elif

# a = 10

# if a >= 10:
#     print("10보다 크거나 같습니다")
# if a >= 5:
#     print("5보다 큽니다")
# if a >= 1:
#     print("1보다 큽니다")


# a = 10
# if a >= 10 :
#     print("10보다 크거나 같습니다")
# elif a >= 5:
#     print("5보다 큽니다")
# else :
#     print("1보다 큽니다")



# 1. 보유액이 10000원 이상이면 택시를 타시오
# 2. 보유액이 10000원 미만 2000원 이상이면 킥보드를 타시오
# 3. 보유액이 2000원 미만 1000원 이상이면 버스를 타시오
# # 4. 그것도 아니면 걸어가시오

# money = 2000

# if money >= 10000 :
#     print("택시")
# # elif money < 10000 and money > 2000 :
# elif 2000 <= money < 10000 :
#     print("킥보드")
# elif 1000 <= money < 2000 :
#     print("버스")
# else :
#     print("걷는다")


# score = float(input("점수 입력 하세요 : "))

# if score >= 4.5 :
#     # print("A+")
#     grade = "A+"
# elif 3.5 < score :
#     # print("B+")
#     grade = "B+"
# elif 2.5 < score :
#     # print("C+")
#     grade = "C+"
# elif 1.5 < score :
#     # print("D+")
#     grade = "D+"
# else : 
#     # print("F")
#     grade = "F"

# print(f"당신의 학점은 {grade}입니다")


# 조건부 표현식

# score = 85
# if score >= 90 :
#     print("합격")
# else :
#     print("불합격")

# score = 85
# # 조건이 참인경우 수행될 코드 if score >= 90 else 조건이 거짓인 경우 수행될 코드  
# print("합격") if score >= 90 else print("불합격")
