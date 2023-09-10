# # 1. 문자열 더하기
# a = "I like "
# b = "python"
# c = a + b
# print(c)

# # 2. 문자열 곱하기
# print("=" * 50)
# print(b * 3)

# # 3. 문자열 길이 구하기
# print(len(c))

# # 4. 문자열 index
# print(c[0])
# print(c[12])
# print(c[len(c) - 1])
# print(c[-1])

# # 5. 문자열 index로 값 변경 시도
# str = "abc"
# # str[1] = 'z'     안된다. 변경하고 싶은 경우 문자열을 새로 구성해서 넣는다.
# # print(str)
# str = "azc"

# # 6. 문자열 슬라이싱
# # like만 뽑아내기
# print(c[2:6])

# # python만 뽑아내기
# print(c[7:])
# print(c[:6])

# # 7. 특정 문자의 개수 세기
# print("i의 개수:", c.count('i'))

# # 8. 찾는 문자의 첫번째 index (1)
# print("y의 index는", c.index('y'))
# #print("a의 index는", c.index('a'))  # 없는 문자를 찾는 경우 오류 발생

# # 9. 찾는 문자의 첫번째 index (2)
# print("y의 index는", c.find('y'))
# print("a의 index는", c.find('a'))    # 없는 문자를 찾는 경우 -1

# # 10. 문자열 치환
# # I like python => I like java
# c = c.replace("python", "java") # 변수에 꼭 다시 저장해주어야 한다.
# print(c)

# # 11. 문자열 나누기
# words = c.split()  # 인자값을 넣지 않으면 공백을 기준으로 문자열 자른다.
# print(words)

# fruits = "grape,apple,orange,peach"
# fruits_list = fruits.split(",")
# print(fruits_list)


# ======================================================================
# # quiz
# # 1. Oh My God
# a = "Oh "
# b = "My "
# c = "God"
# print(a + b + c)

# # 2.
# grade = "My grade is F"
# grade = grade.replace("F", "B")
# print(grade)

# # 3.
# yearStr = "1994년생"
# yyyy = yearStr[:4]
# age = 2021 - int(yyyy) + 1
# print("나이는 %d살 입니다." % age)
# ======================================================================