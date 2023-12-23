#3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72 75 78 81 84 87 90 93 96 99
# l_result = []
# for x in range(1,101) :
#     if x % 3 == 0 :
#         l_result.append(x)
# print(l_result)

# l_result = [x for x in range(1,101) if x % 3 == 0]
# print(l_result)


# # intersectoin
# list01 = [1,2,3,4,5]
# list02 = [3,4,5,6,7,3]
# result = []
# count = 0
# for x in list01 :
#     for y in list02 :
#         if x == y :
#             result.append(x)
#             count += 1
#             break
# print(result, count)

# for dan in [2,3,4,5,6,7,8,9] :
#     print()
#     print(f"{dan}단 시작 : ", end=" ")
#     for num in [1,2,3,4,5,6,7,8,9] :
#         print(f"{dan} * {num} = {dan*num}", end=" ")


# list_position = ['c.과장', 'b.부장', 'd.대리', 'a.사장', 'd.대리', 'c.과장']
# 위 리스트를 대상으로 1)중복되지 않은 직급 2)직급별 인원 수를 dict형으로 출력하라

list_position = ['c.과장', 'b.부장', 'd.대리', 'a.사장', 'd.대리', 'c.과장']
# 1)중복되지 않은 직급
lToS = set(list_position)
sToL = list(lToS) # ['a.사장', 'b.부장', 'd.대리', 'c.과장']
sToL.sort() 
print(sToL)
# 2)직급별 인원 수를 dict형으로 출력

dic_result = {}
for x in sToL : # ['a.사장', 'b.부장', 'd.대리', 'c.과장']
    count = 0
    for y in list_position : # ['c.과장', 'b.부장', 'd.대리', 'a.사장', 'd.대리', 'c.과장']
        if x == y :
            count += 1
    dic_result[x] = count
print(dic_result)
