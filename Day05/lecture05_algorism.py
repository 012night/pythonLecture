# ========================================================================
# # 알고리즘
# # 최대값 최소값 을 for문을 이용하여 구하라    
# import random
# num_list = []
# initNum = 0
# while initNum < 10:
#     num_list.append(random.randint(1, 100))
#     initNum += 1
# print(num_list)
# # lst = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# max = num_list[0]
# min = num_list[0]

# for i in num_list:
#     if max < i:
#         max = i
#     if min > i:
#         min = i
# print("최대값 : ", max)
# print("최소값 : ", min)
# ========================================================================


# ========================================================================
# # 선택정렬 몸풀기 문제 lst = [1,4]가 있다. 1과 4의 위치를 바꾸어, lst=[4,1]로 바꾸는 방법은?
# lst = [1,4]
# tmp = lst[0]
# lst[0] = lst[1]
# lst[1] = tmp
# print(lst)

# lst = [1,4]
# (lst[0], lst[1]) = (lst[1], lst[0])
# print(lst)
# ========================================================================


# ========================================================================
# # 선택정렬 알고리즘을 2중 for문을 이용하여 구현하라.
# # 오름차순
# import random
# lst = []
# initNum = 0
# while initNum < 10:
#     lst.append(random.randint(1, 100))
#     initNum += 1
# count = 0
# for x in range(0, len(lst)-1):
#     for y in range(x+1,len(lst)):
#         count += 1
#         if lst[x] > lst[y]:
#             (lst[x], lst[y]) = (lst[y], lst[x])
#             # tmp = lst[x]
#             # lst[x] = lst[y]
#             # lst[y] = tmp
# print(lst)
# print("반복횟수", count)
# ========================================================================


# ========================================================================
# # 버블정렬
# import random
# list_arr = []
# initNum = 0
# while initNum < 10:
#     list_arr.append(random.randint(1, 100))
#     initNum += 1
# # list_arr = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# count = 0
# for i in range(len(list_arr)-1, 0, -1):
#     swapped = False
#     for j in range(i):
#         count += 1
#         if list_arr[j] > list_arr[j + 1]:
#             list_arr[j], list_arr[j + 1] = list_arr[j + 1], list_arr[j]
#             swapped = True
#     if not swapped:
#         break
# print(list_arr)
# print("반복횟수", count)
# ========================================================================