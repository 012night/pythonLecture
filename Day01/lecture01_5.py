# date = '1225'
# day = '크리스마스'

# a = '1225은 크리스마스 입니다.'
# print(a)
# print(date + "은 "+ day + " 입니다.")
# print("%s은 %s 입니다."%(date, day))
# print("%d은 %s 입니다."%(int(date), day))
# print('my age is %d, and weight is %f kg %s very handsome'%(19, 70.4, '나는'))


#1.문자열 포매팅 %s는 문자열, %d는 정수 >> 사실 %s는 전부 다 호환이 된다는 점.
# a = "I studied %s" % "python"
# print(a)

# a = "I studied python %d times" % 2
# print(a)

#2.포매팅을 왜 쓰는가? 따옴표를 여러번 안닫아도 된다.
# a = "I studied python " +str(2) + " times"
# print(a)

#3.여러개 활용시에 더 효과적
# language = 'python'
# times = 2
# a = "I studied %s %d times. So, I'm good at %s well" %(language, times, language)
# print(a)


#4.포매팅시, 소수점 자리(0.x) x번째 자리까지
# print("현재 이자율은 %0.4f 이다." %3.123521)

#반복문에서도 직관적으로 활용가능(아래 로직은 아직 알 필요X)
# languages = ['java', 'python', 'C', 'PHP']
#
# for lang in languages:
#     a = "I like %s much" % lang
#     print(a)

a = 2022
b = '호랑이'
print('올해는 %d년 %s의 해 입니다'%(a,b))