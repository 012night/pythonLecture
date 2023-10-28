# import random
# # num_random = random.randint(1,10) 
# num_random = random.randint(1,10) 

# while True :
#     print("결과값 :", num_random)
#     item = int(input("예상되는 값 입력 : "))
#     if item > num_random :
#         print("더 작은값을 입력 하세요")
#     elif item < num_random :
#         print("더 큰값을 입력 하세요")

#     else :
#         print("정답입니다.")
#         break



# num_list = [57, 9, 27, 34, 58, 79, 61, 64, 15, 98]
# # print(max(num_list))
# # print(min(num_list))

# max_value = num_list[0]
# min_value = num_list[0]

# for x in num_list :
#     if max_value < x :
#         max_value = x
#     if min_value > x :
#         min_value = x

# print(max_value, min_value)



# a = 1
# b = 2
# a,b = b,a
# print(a,b)

# list_num = [1,10]
# list_num[0],list_num[1] =  list_num[1], list_num[0]



list_num = [5, 1, 3, 7, 2, 111, 9]
count = 0
for x in range(0, len(list_num)-1) :
    for y in range(x+1, len(list_num)) :
        if list_num[x] > list_num[y] :
            list_num[x],list_num[y] = list_num[y],list_num[x]
        count += 1

print(list_num, count)