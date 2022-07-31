# # 알고리즘
# # 최대값 최소값 을 for문을 이용하여 구하라
# lst = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# max = lst[0]
# min = lst[0]
#
# for i in lst:
#     if max < i:
#         max = i
#     if min > i:
#         min = i
# print("최대값 : ", max)
# print("최소값 : ", min)



# # 선택정렬 몸풀기 문제 lst = [1,4]가 있다. 1과 4의 위치를 바꾸어, lst=[4,1]로 바꾸는 방법은?
# lst = [1,4]
# tmp = lst[0]
# lst[0] = lst[1]
# lst[1] = tmp
# print(lst)

# lst = [1,4]
# (lst[0], lst[1]) = (lst[1], lst[0])
# print(lst)


# # 선택정렬 알고리즘을 2중 for문을 이용하여 구현하라.
# lst = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# #오름차순
# for a in range(0,len(lst)-1):
#     for b in range(a+1,len(lst)):
#         if lst[a] > lst[b]:
#             (lst[a], lst[b]) = (lst[b], lst[a])
#             tmp = lst[a]
#             lst[a] = lst[b]
#             lst[b] = tmp
# 
# print(lst)
# lst = [93, 45, 21, 30, 20, 94, 66, 71, 45]
# #내림차순
# for a in range(0,len(lst)-1):
#     for b in range(a+1,len(lst)):
#         if lst[a] < lst[b]:
#             (lst[a], lst[b]) = (lst[b], lst[a])
#             # tmp = lst[a]
#             # lst[a] = lst[b]
#             # lst[b] = tmp
# print(lst)