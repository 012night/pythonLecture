# # 0.숫자의 사칙연산

# # 1.덧셈 : +
# a = 3
# b = 4
# print(a+b)


# # 2.뺄셈 : -
# print(a-b)


# # 3.곱셈 : *, 제곱 : **
# print(a*b)
# print(a**b)

# # 4.나눗셈 : /, 나머지 : %, 몫 : //
# print(a/b)
# print(a//b)
# print(a%b)


# # 5. 몫과 나머지를 모두 구할수 있는 함수
# m,n = divmod(a,b)
# print(m,n)


# # 6. 변수에 값을 담아 연산하기
# # 산술 연산
# noodle_cup = 850
# print("육개장 가격:", noodle_cup)

# # 육개장 3개의 가격 계산
# sum = noodle_cup * 3
# print("육개장 3개의 가격:", sum)

# # 가격 상승
# noodle_cup = noodle_cup + 100
# print("가격 상승 후 육개장 가격:", noodle_cup)
# print("육개장 3개의 가격:", noodle_cup * 3)

# # 변수 여러개
# # 육개장 하나의 가격은 OO원 이고, 육개장 3개의 가격은 OO원 입니다.
# print('육개장 하나의 가격은', noodle_cup, "원 이고, 육개장 3개의 가격은",
#       noodle_cup * 3, "원 입니다.")

# # 10,000원으로 육개장 3개를 산 후 거스름돈 구하기
# money = 10000
# change = money - sum
# print("거스름돈:", change)

# # 5,000원으로 육개장 몇 개를 살 수 있고, 거스름돈은 얼마나 남는가?
# money = 5000
# buy_noodle_cup = money / noodle_cup
# print('살 수 있는 개수:', buy_noodle_cup)   # 소수로 나온다.

# buy_noodle_cup = money // noodle_cup
# print("살 수 있는 개수:", buy_noodle_cup)   # 몫만 구한다.

# change = money % noodle_cup    # 나머지를 구한다.
# print("거스름돈:", change)



# # 컴퓨터에서 사용되는 진법
# #                               C언어          Python
# # 2진수     0,1                 X              0b10 
# # 8진수     0 ~ 7               010            0o10
# # 10진수    0 ~ 9               10             10 
# # 16진수    0 ~ 9 , A ~ F       0x10           0x10


# # 컴퓨터는 기계어를 사용하기 때문에 
# # 정수는 2진수로 변환되어 저장된다...
# # 출력형식은 기본 10진법으로 출력한다...
# print(0b10)
# print(0o10)
# print(10)
# print(0x10)


# #진법변환 함수
# # bin - 2진수 변환 함수
# # oct - 8진수 변환 함수
# # hex - 16진수 변환 함수
print(hex(65))
print(hex(0b101010101))
print(oct(8))
print(bin(15))