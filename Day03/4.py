# # 선언
# num = int(input("10보다 작은 수 입력 : "))

# if num < 10 :
#     print(f"10보다 작은수 {num}입력 완료")


# 본인의 몸무게를 입력 하고 조건에 맞게끔 결과가 나오는 코드

# weight = int(input("본인의 몸무게 입력 : "))

# if weight <= 60 :
#     print("야식 가능")

# if weight > 60 :
#     print("다이어트 하세요")


# id = input("아이디 입력 : ")

# if id == "mega" :
#     print("id 확인 완료")
# if id != "mega" :
#     print("id 오류")

# # if - else
# id = input("아이디 입력 : ")
# if id == "mega" :
#     print("id 확인 완료")
# else :
#     print("id 오류")

# 돈이 만원 이상 있으면 택시를 타고 없으면 걸어라

# money = int(input("얼마 있나요? : "))
# if (30000 < money) :
#     print("택시")
# else :
#     print("걷는다")

# a = 2
# b = 2

# if a > b :
#     print(a)
# if a < b :
#     print(b)

# if a > b :
#     print(a)
# else :
#     print(b)

# weight = 111
# fee = weight//10*10000

# if weight < 10 :
#     print("무료")
# else :
#     print(f"수수료 {fee} 있음")


# 돈이 만원 이상 있으면 택시를 타고 없으면 걸어라

# money = int(input("얼마 있나요? : "))
# if (money > 10000) :
#     print("택시")
#     talk = input("기사님과 대화하시겠습니까? (Yes or No) : ")
#     if talk.upper() == "YES" :
#         print("대화한다")
#     else : 
#         print("이어폰을 꼽는다")
# else :
#     print("걷는다")


# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = int(input("숫자입력 : "))

# if num in num_list :
#     print(f"입력하신 숫자는 num_list[{num_list.index(num)}]에 존재합니다.")
# else :
#     print(f"해당값{num}은 리스트에 포함되지 않았습니다")
    
# # 논리연산자(and, or, not) 결과
# # a = 1>10
# a = True
# b = True
# c = False

# # and -> 두개의 연산결과가 모두 참일경우 참을 반환
# print(a and b)
# print(a and c)

# # or -> 두개 연산결과 중 하나만 참이어도 참을 반환
# print(a or b)
# print(a or c)

# print(not c)


# # 10보다 크고 19보다 작다
# num = 15
# print(10 <= num and num < 20) 
# print(10 <= num < 20) 


# num = 31
# a,b = divmod(num,2)
# print(b)

# # if num%2 != 1 :
# if result[1] != 1 :
#     print("짝수입니다")
# else : 
#     print("홀수입니다")


# 방법 1
# num = int(input("수 입력 : "))
# q = num // 10
# r = num % 10

# if num % (q+r) == 0 :
#     print("하샤드 수")
# else :  
#     print("하샤드 수 아님")

# # 방법 2
# num = input("수 입력 : ")
# if int(num) % (int(num[0])+int(num[1])) == 0 :
#     print("하샤드 수")
# else :  
#     print("하샤드 수 아님")


num = input("수 입력 : ")
result = 0
for x in num :
    result += int(x)

if int(num) % result == 0 :
    print("하샤드 수")
else :  
    print("하샤드 수 아님")