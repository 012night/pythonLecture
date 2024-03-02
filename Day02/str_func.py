# msg = "pythonyyyttt"
# # print(msg.count("y"))
# # print(msg.index("t"))
# # print(msg.index("x"))
# # print(msg.find("t"))
# # print(msg.find("x"))

# result = "  Yes"
# print(result.lower())
# print(result.upper())

# # 문자열 앞 뒤 공백 삭제 기능
# print(result.strip())
# # 문자열 왼쪽 공백 삭제 기능
# print(result.lstrip())
# # 문자열 오른쪽 공백 삭제 기능
# print(result.rstrip())

# # 내가 원하는 문자열로 해당 문자를 교체하는 기능
# msg = "I like Soccer"
# print(msg.replace("Soccer", "python"))
# print(msg)

# # 사용자의 입력을 기다림...
# count = int(input("사려고 하는 상품의 개수를 입력하세요"))
# print(f"육개장 {count}개의 가격 : {900*count}")


# Y = 2.5 ×𝑥^2+3.3 ×𝑥+6(단 x = 2일때)
# [출력화면]
# 2차 방정식 결과 = 22.6

# x = 2
# Y = 2.5 * x**2 + 3.3 * x + 6
# print("2차 방정식 결과 =", Y)
# print(f"2차 방정식 결과 = {Y}")


# [출력화면 예시]
# <조건1> 각 단어 변수(word1, word2, word3)
# <조건2> 입력과 출력 구분선 : 문자열 연산
# <조건3> 각 변수의 첫 단어만 추출하여 변수(abbr) 저장

# [출력화면 예시]
# 첫번째 단어 : Korea
# 두번째 단어 : Baseball
# 세번째 단어 : Orag

# word1 = "Korea"
# word2 = "Base"

# word1 = input("첫번째 단어 : ").upper()
# word2 = input("두번째 단어 : ").upper()
# word3 = input("세번째 단어 : ").upper()
word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")

abbr = word1[0]+word2[0]+word3[0]
print(abbr.upper())

print("사용자가 입력한 값",word1,word2,word3)





