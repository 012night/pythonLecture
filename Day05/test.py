# result = 0
# sample_list = []
# for num in range(1,101) :
#     if num % 2 == 0 :
#         result = result + num
#         sample_list.append(num)
    
# print(result)
# print(sample_list)

# sample_list = [num for num in range(1,101) if num % 2 == 0 ]
# print("리스트 내포를 통해 만들어진 ... :\n", sample_list)


list_position = ['c.과장', 'b.부장', 'd.대리', 'a.사장', 'd.대리', 'c.과장']
# 1)중복되지 않은 직급

# # 조건문과 반복문을 사용한 해결방법
# unique_list = []
# for x in list_position :
#     if x not in unique_list :
#         unique_list.append(x)

# unique_list.sort()
# print(unique_list)

# convert_list = list(set(list_position))
# convert_list.sort()
# print(convert_list)

# # 2)직급별 인원 수를 dict형으로 출력하라
# dic_sample = {}
# for x in convert_list :
#     count = 0
#     for y in list_position :
#       if x == y :
#         count += 1
#     dic_sample[x] = count
#     print(x, count)
# print(dic_sample)

