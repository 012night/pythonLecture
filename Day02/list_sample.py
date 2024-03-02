# age01 = 30
# age02 = 19
# age03 = 25

# age = [30, 19, 25]
# print(type(age), age)

# print((age[0]+age[1]+age[2])/3)

# list_name = ["새우깡", "홈런볼", "포키"]
# print(list_name[0])

# list_num = [[1,2],[3,4],[5,6]]
# print(list_num[0][1])
# print(list_num[2][0])

# list_ex1 = ['a', 'b', 'c', [1, 2, 3]] 
# print(list_ex1[3][0]+list_ex1[3][2])

# number = list_ex1[3] # [1, 2, 3]
# print(number[0]+number[2])

# # 리스트 슬라이싱
# name = ["김", "이", "박", "최"]
# print(name[:2])
# print(name[::2])

# # 리스트 더하기
# numList01 = [1,2]
# numList02 = [3,4]
# print(numList01+numList02)

# # 리스트 곱하기(반복)
# print(numList01*3)

# # 리스트 수정
# a = 1
# print(a)
# a =2
# print(a)

# msg = "i like python"
# print(msg.replace("python", "java"))
# print(msg)



# a = 1 
# print(id(a))
# a = 3 
# print(id(a))

# list_num = [1,2,3]
# print("수정 전 :",id(list_num), list_num)
# list_num[0] = 10
# print("수정 후 :",id(list_num), list_num)

# list_num = [1,2,3]
# list_num[1:] = [20,30]
# print(list_num)

# 비어있는 리스트로 교체 및 삭제
# list_num = [1,2,3]
# list_num[:2] = []
# list_num[2] = []
# print(list_num)

# # 리스트 값 삭제하기(인덱스 번호)
# list_num = [1,2,3,4,5,6]
# del list_num[:2]
# del list_num[4]
# print(list_num)

# # 원하는 값 삭제(remove)
# list_num = [1,2,3,4,5,6]
# list_num.remove(6)
# print(list_num)
# 없는 값 삭제 했을 시 에러 발생(추후 예외처리로 처리)
# list_num.remove(10)


# list_num = [1,2,3,4,5]
# # 리스트 값 마지막에 추가(append - 하나의 값)
# list_num.append(11)
# list_num.append([10,11,12])
# print(list_num)

# 리스트 값 원하는 위치에 추가(insert - 하나의 값)
# list_num = [1,2,3,4,5]
# list_num.insert(1,1.5)
# list_num.insert(1,[1.6, 1.7, 1.8])
# print(list_num)

# # 리스트 값 추가-확장(extend - 여러개의 값)
# list_num = [1,2,3,4,5]
# list_num.extend([1,2,3,4])
# print(list_num)

# 정렬(오름차순)
# list_name = ["박효신", "이수", "김범수", "나얼"]
# list_name.sort()
# print(list_name)

# # 역정렬
# list_name = ["박효신", "이수", "김범수", "나얼"]
# list_name.reverse()
# print(list_name)

# list_lang = ['banana', 'cat', 'egg', 'apple', 'door']
# # list_lang.sort()
# # list_lang.reverse()
# list_lang.sort(reverse=True)
# print(list_lang)

# list_num = [1,2,3,4,5,1,2,3]
# 찾고자 하는 값의 개수 파악
# # print(list_num.count(4))

# 찾고자 하는 값의 인덱스 위치
# print(list_num.index(2))

# list_num = [1,2,3,4,5]
# print(list_num.pop(1))
# print(list_num)

# # split(하나의 문자열을 어떤 기준을 가지고 분리시키는 역할)
# msg = "i Like Python"
# print(msg.split(" "))

# msg = "i#Like#Python"
# print(msg.split("#"))

#join(여러개의 문자열로 구성되어있는 리스트를 하나의 문자열로 변환 시키는 기능)
list_msg = ['i', 'Like', 'Python']
print("#".join(list_msg))




