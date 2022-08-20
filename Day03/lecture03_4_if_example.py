# 1. 두 점수를 입력 받고, 평균이 70점 이상이면 합격 그렇지 않으면 불합격을 출력하세요.
score1, score2 = input("두 점수를 입력하세요:").split()
score1 = int(score1)
score2 = int(score2)
average = (score1 + score2) / 2

if average >= 70:
    print("합격입니다.")
else:
    print("불합격입니다.")

# 2. 세 개의 정수를 입력 받아서 가장 큰 값을 출력하세요.
a, b, c = input("3개의 수를 입력하세요:").split()
a = int(a)
b = int(b)
c = int(c)

max = a
if max < b:
    max = b
if max < c:
    max = c
print(max)

# 3.
# 평균이 60점 이상이면 합격
#   한과목이라도 50점 이하면 무조건 과락
# 평균 60점 미만이면 불합격
score1 = int(input("점수1:"))
score2 = int(input("점수2:"))
average = (score1 + score2) / 2
if average < 60:
    print("불합격")
else:
    if score1 <= 50 or score2 <= 50:
        print("과락")
    else:
        print("합격")

# 4로 나누어 떨어지는 연도는 윤년이다.
# 100으로 나누어 떨어지는 연도는 윤년이 아니다.
# 400으로 나누어 떨어지는 연도는 무조건 윤년이다.
year = int(input("연도를 입력하세요:"))
# 1. 무식하게 푸는 방법
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("윤년")
        else:
            print("평년")
    else:
        print("윤년")
else:
    print("평년")

# 2.
# 4로 나누어 떨어지는 연도는 윤년이다.
#   100으로 나누어 떨어지는 연도는 윤년이 아니다.
# 400으로 나누어 떨어지는 연도는 무조건 윤년이다.
if year % 400 == 0:
    print("윤년")
elif year % 100 == 0:
    print("평년")
elif year % 4 == 0:
    print("윤년")
else:
    print("평년")

# 4로 나누어 떨어지는 연도는 윤년이다.
# 100으로 나누어 떨어지지 않는 연도는 윤년이다.
#  => 4로 나누어 떨어지는 연도 그리고 100으로 나누어 떨어지지 않는 연도 윤년
#     또는
#     400으로 나누어 떨어지는 연도는 무조건 윤년이다.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("윤년")
else:
    print("평년")

condition1 = year % 4 == 0 and year % 100 != 0
condition2 = year % 400 == 0
if condition1 or condition2:
    print("윤년")
else:
    print("평년")

# 5.
# 도 : 1개가 뒤집어진 상태
# 개 : 2개가 뒤집어진 상태
# 걸 : 3개가 뒤집어진 상태
# 윷 : 4개가 뒤집어진 상태
# 모 : 하나도 뒤집어지지 않은 상태
st1, st2, st3, st4 = input("윷 상태를 입력:").split()
st1 = int(st1)
st2 = int(st2)
st3 = int(st3)
st4 = int(st4)
count = st1 + st2 + st3 + st4

if count == 1:
    print("도")
elif count == 2:
    print("개")
elif count == 3:
    print("걸")
elif count == 4:
    print("윷")
else:
    print("모")