# ========================================================================
# # and 기본 예제 >> 좌항과 우항 모두 True 일때 True
# a = True
# b = False
# if a and b :
#     print("참입니다.")
# else :
#     print("거짓입니다.")
# ========================================================================

# ========================================================================
# # or 기본 예제 >> 좌항과 우항 하나라도 True 일때 True
# a = True
# b = False
# if a or b :
#     print("참입니다.")
# else :
#     print("거짓입니다.")
# ========================================================================

# ========================================================================
# # not A : A가 참인 경우, not A는 False
# a = True
# if not a:
#     print("참입니다.")
# else:
#     print("거짓입니다.")
# ========================================================================

# ========================================================================
# # in, not in : a가 변수 이고, b가 리스트 일 경우, a가 b에 속하면 True
# a = 1
# b = [1,2,3]
# if a in b:
#     print("a는 b에 속한다")
# else:
#     print("a는 b에 속하지 않는다")
# ========================================================================

# ========================================================================
# # and, or 실습
# number = int(input("숫자를 입력하세요:"))
# # 10 <= number <= 20
# # AND , OR , NOT
# if 10 <= number <= 20:
#     print("%d가 10 이상이고 20이하이다." % number)
# if 10 <= number and number <= 20:
#     print("%d가 10 이상이고 20이하이다." % number)

# # number < 10 또는 number > 20
# if number < 10 or number > 20:
#     print(f"{number}가 10보다 작거나 20보다 크다.")
# ========================================================================

# ========================================================================
# # 두수를 입력받아 비교 후 and, or 연산 예제
# weight, walk = input("몸무게와 걸은 수를 입력하세요:").split()
# weight = int(weight)
# walk = int(walk)
# # 만약에 걸은 수가 10000보를 초과하면서 몸무게가 70키로 이하이면 "야식"
# if walk > 10000 and weight <= 70:
#     print("둘 다 만족하니 야식")

# # 만약에 걸은 수가 10000보를 초과했거나 몸무게가 70키로 이하이면 "야식"
# if walk > 10000 or weight <= 70:
#     print("하나라도 만족하니 야식")
# ========================================================================

# ========================================================================
# # 연습문제06 : range, in, index 활용
# num_list = [1,2,3,4,5,6,7,8,9,10]
# # num_list = list(range(1,11))

# print(num_list)
# a = int(input("숫자 하나를 입력하세요 "))
# if a in num_list :
#     print(f"입력하신 숫자는 num_list[{num_list.index(a)}]에 존재합니다.")
# else :
#     print(f"입력하신 숫자 {a}은 리스트에 포함되지 않았습니다")
# ========================================================================

# ========================================================================
# 연습문제07 ~ 08 : if_else(and, or 이해)
# money = int(input("얼마 있으신가요? "))
# hungry = input("배고프세요? ('예' 또는 '아니오'로 대답)")
# if money >= 10000 and hungry == "예" : 
#     print("저녁을 사먹으시오")
# else :
#     print("집에 가시오")
# ========================================================================
a="예"
b="예1"
print(a==b)
# ========================================================================
# # 연습문제09 : 홀수 짝수 구분 // 알고리즘의 시작
# num = int(input("정수를 입력하세요. "))
# if num % 2 == 0 :
#     print(f"정수 {num}는 짝수입니다")
# else :
#     print(f"정수 {num}는 홀수입니다")
# ========================================================================

# ========================================================================
# # 연습문제10 : 하샤드 수 문제
# # 예를 들어 18의 자릿수 합은 1 + 8 = 9이고, 18은 9로 나누어 떨어지므로 하샤드 수.
# num = int(input("자연수 하나를 입력하세요:"))
# q = num // 10  # 십의 자리
# r = num % 10   # 일의 자리
# # q + r 더한 것을 num 나눠보고 0으로 떨어지면 하샤드 수
# if num % (q + r) == 0:
#     print("%d은 하샤드 수 입니다." % num)
# else :
#     print("%d는 하샤드 수가 아닙니다." % num)
# ========================================================================

# ========================================================================
# # 세자리수 이상이라면...
# num = input("자연수 하나를 입력하세요:")
# result = 0

# for x in num :
#     result += int(x)
# print(result)

# if int(num) % result == 0:
#     print(f"{num}은 하샤드 수 입니다.")
# else :
#     print(f"{num}는 하샤드 수가 아닙니다.")
# ========================================================================

# ========================================================================
# # pass의 활용, 기본 문구 구성, 추후 클래스 및 함수(메서드에서 활용)
# option = ['money', 'smartphone', 'card']
# my_item = 'money'
# if my_item in option:
#     pass
# else:
#     print("돈 되는걸 꺼내시오")
# ========================================================================