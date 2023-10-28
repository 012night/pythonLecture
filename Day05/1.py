# result = 0
# for a in range(1,101) :
#     if a % 2 == 0 :
#         result += a

# print(result)


# 1)중복되지 않은 직급 
list_position = ['c.과장', 'b.부장', 'd.대리', 'a.사장', 'd.대리', 'c.과장']
# # 1)
# lToS = set(list_position)
# sToL = list(lToS)
# sToL.sort()
# print(sToL)

result_list = []
for position in list_position :
    if position not in result_list :
        result_list.append(position)
result_list.sort()
print(result_list)  # ['a.사장', 'b.부장', 'c.과장', 'd.대리']

# 2)직급별 인원 수를 dict형으로 출력하라

dict_sample = {}

for x in result_list :
    count = 0
    for y in list_position :
        if x == y :
            count += 1

    dict_sample[x] = count
        
print(dict_sample)















# p = []
# list_position = ['c.과장', 'b.부장', 'd.대리', 'a.사장', 'd.대리', 'c.과장']
# for x in list_position :
#     if x not in p :
#         p.append(x)

# p.sort()
# print(p)