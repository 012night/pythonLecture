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
# lst = [5, 1, 3, 7, 2, 9]
# for x in range(0, len(lst)-1):
#     for y in range(x+1,len(lst)):
#         if lst[x] > lst[y]:
#             (lst[x], lst[y]) = (lst[y], lst[x])
#             # tmp = lst[x]
#             # lst[x] = lst[y]
#             # lst[y] = tmp
# print(lst)

# # 내림차순
# lst = [5, 1, 3, 7, 2, 9]
# for a in range(0,len(lst)-1):
#     for b in range(a+1,len(lst)):
#         if lst[a] < lst[b]:
#             (lst[a], lst[b]) = (lst[b], lst[a])
#             # tmp = lst[a]
#             # lst[a] = lst[b]
#             # lst[b] = tmp
# print(lst)