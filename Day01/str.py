# msg = "Hello world"
# print(type(msg), msg)

# msg01 = "I \"like\" python"
# msg01 = 'I \'like\' python'
# msg01 = "나는 \n쉬고싶다"
# print(msg01)

# msg_new = """I "like" 
# Python"""
# print(msg_new)

# word01 = "mega"
# word02 = "study"
# # 문자열 더하기
# print(word01+word02)

# print(word01, word02)

# 문자열 곱하기(문자열 반복)
# grade = "A+"
# print(grade*3)

# mark = "*"
# print(mark*30)
# print("결과 : ")
# print(mark*30)

# # 문자열 인덱싱
# word = "python is fun"
# # print(word[0])
# # print(word[5])
# print(word[10]+ word[11]+word[12])

# 문자열 슬라이싱
# # 대상데이터 또는 변수[시작지점:끝지점]
# word = "python is fun"
# # print(word[10:])
# print(word[:6])

# number = "0123456789"
# print(number[2::2])


# a라는 변수에 문자열 20231225Christmas를 담고
# 슬라이싱을 이용하여 date라는 변수에 날짜(20231225)
# day라는 변수에 Christmas을 담아 
# 출력(print) 하시오

# a = "20241225Christmas"
# date = a[:8]
# day = a[8:]
# print(date+"은",day+"입니다")
# # 포메팅 1(legacy)
# print("%s은 %s입니다"%(date, day))
# # 포메팅 2(.format 함수를 사용)
# print("{}은 {}입니다".format(date, day))
# # 포메팅 3
# print(f"{date}은 {day}입니다")


word = "megastudymm"
print(word.count("m"))


print("python".index("y"))