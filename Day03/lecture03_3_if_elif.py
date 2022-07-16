# # if - elif - else 기본 파악 예제
# a = 100
# if 10 < a :
#     print("10보다 크다")
# elif 20 < a :
#     print("20보다 크다")
# elif 30 < a :
#     print("20보다 크다")
# else :
#     print("종료")


# # if - elif - else 구문을 쓰지 않는다면
# a = 100
# if 10 < a :
#     print("10보다 크다")
# if 20 < a :
#     print("20보다 크다")
# if 30 < a :
#     print("30보다 크다")


# # if - elif - else 실습
# weight = int(input("몸무게를 입력하세요:"))

# if weight <= 70:     # ~70
#     print("치킨")
# elif weight <= 75:   # 71 ~ 75
#     print("닭가슴살")
# elif weight <= 80:   # 76 ~ 80
#     print("샐러드")
# else:
#     print("굶자")


# # if - elif - else 
# money = int(input("가지고 있는 금액을 입력하시오."))
# if money >= 10000:
#     print("택시를 타시오")
# elif 10000 > money >=2000:
#     print("버스를 타시오")
# elif 2000 > money >=1000:
#     print("킥보드를 타시오")
# else:
#     print("걸어가라")


# # 연습문제11 : 다중조건문(학점 - 등급)
# score = float(input("점수를 입력하세요. "))
# grade = ""
# if score == 4.5 :
#     grade = 'A+'
# elif 4.25 <= score :
#     grade = 'A'
# elif 4.0 <= score :
#     grade = 'A-'
# elif 3.75 <= score :
#     grade = 'B+'
# elif 3.5 <= score  :
#     grade = 'B'
# elif 3.25 <= score :
#     grade = 'B-'
# elif 3.0 <= score :
#     grade = 'C+'
# elif 2.75 <= score :
#     grade = 'C'
# elif 2.5 <= score :
#     grade = 'C-'
# else :
#     grade = 'F'
# print(f"당신의 학점은 {grade} 입니다.")
  

# # 조건부 표현식, 다른언어에서는 3항 연산자라 표현
# # 일반적인 if-else 구문
# score = 95
# if score >= 80 :
#     print("success")
#     msg = "success"
# else :
#     print("failure")
#     msg = "failure"
# print(msg)    
    

# # 조건부 표현식 구문
# score = 95
# print("success") if score > 10 else print("failure")
# message = "success" if score > 10 else "failure"
# print(message)


# # [참고]입력값을 올바르게 받기위한 작업
# answer = input("돈이있습니까? ").lower().strip()
# if answer == "true":
#     pass #여기에 코드 작성
# elif answer == "false":
#     pass #여기에 코드 작성
# else:
#     print("True나 False로 답해주세요.")