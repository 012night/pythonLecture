# #if 기초 예제
# a = 1
# if a > 10 :
#     print("1은 10보다 큽니다.")
# print("결과가 출력되지 않았습니다")


# #if 기초 예제(포메팅 추가)
# a = 1
# compare = 10
# if a > compare :
#     print("{}은 {}보다 큽니다.".format(a, compare))
# print(str(a) + "가 " + str(compare) + "보다 작아서 결과가 출력되지 않았습니다. 포멧팅 안한것")
# print("%d가 %d보다 작아서 결과가 출력되지 않았습니다. 첫번째 포멧팅"%(a, compare))
# print("{}가 {}보다 작아서 결과가 출력되지 않았습니다. 두번째 포멧팅".format(a, compare))
# print(f"{a}가 {compare}보다 작아서 결과가 출력되지 않았습니다. 세번째 포멧팅")



#if문 기본
# trueornot = False
# if trueornot:
#     print("참입니다.")
# else:
#     print("거짓입니다.")



# num_list = [1,2,3,4,5,6,7,8,9,10]
# print(num_list)
# a = int(input("숫자 하나를 입력하세요 "))
# if a in num_list :
#     print(f"입력하신 숫자는 num_list[{num_list.index(a)}]에 존재합니다.")
# else :
#     print(f"해당값{a}은 리스트에 포함되지 않았습니다")



# #if_else 연습문제01
#돈이 3만원 이상 있으면 '택시를 타라', 
#그렇지 않으면 '걸어가라'가 출력되도록 프로그래밍 하시오 
#현재 돈은 13000원 보유
# money = 13000
# if money >= 30000:
#     print("택시를 타라")
# else:
#     print("걸어가라")
    
    

# #if_else 연습문제02
# a = int(input("1.정수(a)를 입력하세요."))
# b = int(input("2.정수(b)를 입력하세요."))
# if a > b :
#     print(a)
# else : 
#     print(b)



#수하물 - 수수료 문제
# weight = int(input('짐의 무게는 얼마입니까? '))

# if weight >= 10 :
#     price = (weight//10) * 10000
#     print('짐의 무게는 {}kg이며 수수료는 {}원 입니다'.format(weight,price))
# else :
#     print('수수료는 없습니다.')



# #if_else 연습문제03
# 현재 얼마가 있나요?라는 문구 & input 함수를 사용해 돈(값)을 받고
# 돈이 만원 이상 있으면 “택시를 타시오”, 
# 그렇지 않으면 “걸어가시오” 를 출력되도록 프로그래밍 하시오
# money = input("얼마가 있나요?")
# if int(money) >= 30000:
#     print("택시를 타시오")
# else:
#     print("걸어가시오")




# #if_else 연습문제04
#파이썬에서는 들여쓰기가 매우 중요하다. 
#들여쓰기를 통해 논리의 흐름을 따진다.
#원하는 프로그래밍이 아니다...
# money = 9000
# talk = True
# if money >= 10000:
#     print("택시를 타라")
# else:
#     print("걸어가라")
# if talk:
#     print("정치이야기 좋아하시죠?")
# else:
#     print("어 이상한 길로 가는데... 저기요 아저씨...")


# #우리가 원하는 프로그래밍
# money = 13000
# talk = True
# if money >= 10000 :
#     print("택시를 타라")
#     if talk :
#         print("정치이야기 좋아하시죠?")
#     else :
#         print("어 이상한 길로 가는데... 저기요 아저씨...")
# else :
#     print("걸어가라")


# money = int(input("얼마가 있으신가요? ex)30000 \n"))
# if money >= 10000 :
#     print("택시를 타라")
#     while 1 :
#         talk = input("대화를 하시겠습니까? True 또는 False로 대답해주세요. ")
#         if talk == "True" :
#             talk = True
#             break
#         elif talk == "False" :
#             talk = False
#             break
#         else : 
#             print("다시 대답해주세요")
#             continue
#     print(type(talk))
#     if talk :
#         print("정치이야기 좋아하시죠?")
#     else :
#         print("어 이상한 길로 가는데... 저기요 아저씨...")
# else :
#     print("걸어가라")


# #A and B >> A, B모두 True 일때 True
# a = True
# b = False
# if a and b :
#     print("참입니다.")
# else :
#     print("거짓입니다.")


# #A or B >> A, B 둘중하나라도 True 일때 True
# a = True
# b = False
# if a or b :
#     print("참입니다.")
# else :
#     print("거짓입니다.")


#not A : A가 참인경우, not A는 false
# a = True
# if not a:
#     print("참입니다.")
# else:
#     print("거짓입니다.")


#A & B : A and B와 동일
#A | B : A or B와 동일


#in, not in : a가 변수 이고, b가 리스트 일 경우, 
# a가 b에 속하면 True
# a = 1
# b = [1,2,3]
# if a in b:
#     print("a는 b에 속한다")
# else:
#     print("a는 b에 속하지 않는다")


# #if_else 연습문제05~06
# money = int(input("얼마 있으신가요? "))
# hungry = True
# if money >= 10000 and hungry : 
#     print("저녁을 사먹으시오")
# else :
#     print("집에 가시오")




#홀수 짝수 구분 예제(약간의 알고리즘)
# num = int(input("정수를 입력하세요. "))
# if num % 2 == 0 :
#     print(f"정수 {num}는 짝수입니다")
# else :
#     print(f"정수 {num}는 홀수입니다")




#조건 pass문, 최소한의 자격을 갖췄는지를 파악하고 싶을때 사용.
# option = ['money', 'smartphone', 'card']
# my_item = 'trash'
# if my_item in option:
#     pass
# else:
#     print("돈 되는걸 꺼내시오")



# #다중 조건문
# money = int(input("가지고 있는 금액을 입력하시오."))
# if money >= 10000:
#     print("택시를 타시오")
# elif 10000 > money >=2000:
#     print("버스를 타시오")
# elif 2000 > money >=1000:
#     print("킥보드를 타시오")
# else:
#     print("걸어가라")


#학점 - 등급 연습문제
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
  

#조건부표현식, 다른언어에서는 3항연산자라 표현
# a=3
# print("성공했을때 실행문") if a > 10 else print("실패했을때 실행문")
# a=30
# message = "성공했을때 실행문" if a > 10 else "실패했을때 실행문"
# print(message)





# answer = input("돈이있습니까? ").lower().strip()
# if answer == "true":
#     pass #여기에 코드 작성
# elif answer == "false":
#     pass #여기에 코드 작성
# else:
#     print("True나 False로 답해주세요.")