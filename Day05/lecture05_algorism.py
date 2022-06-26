#알고리즘
#최대값 최소값 을 for문을 이용하여 구하라



# #알고리즘 1(최대값/최소값)
# from random import randint

# list_random = []
## list_random = [93, 45, 21, 30, 20, 94, 66, 71, 45] #이런식으로 할당 해 놓고 해도되지만...
# 아래 for문을 완벽하게 대신 할수 있는 리스트 내포
# list_random = [randint(1,100) for i in range(10)]
# for i in range(10) :
#     num_random = randint(1,100)
#     list_random.append(num_random)
# print(list_random)

# maxNum = minNum = list_random[0]
# # maxNum = list_random[0]
# # minNum = list_random[0]

# for i in list_random :
#     if maxNum < i :
#         maxNum = i
#     if minNum > i :
#         minNum = i
# print(f"최대값 = {maxNum}, 최소값 = {minNum}")





#알고리즘
#선택정렬 몸풀기 문제 lst = [1,4]가 있다. 1과 4의 위치를 바꾸어, lst=[4,1]로 바꾸는 방법은?
# lst = [1,4]
# tmp = lst[0]
# lst[0] = lst[1]
# lst[1] = tmp
# print(lst)

# lst = [1,4]
# (lst[0], lst[1]) = (lst[1], lst[0])
# print(lst)




# 선택정렬을 이용한 오름차순 정렬
# list_num = [3,5,1,2,4]
# print(f"초기 리스트 : {list_num}")
# rotate = len(list_num)

# for i in range(0, rotate-1) :
#     for j in range(i+1, rotate) :
#         if list_num[i] > list_num[j] :
#             temp = list_num[i]
#             list_num[i] = list_num[j]
#             list_num[j] = temp
#     print(f"{i+1}번째 정렬 : {list_num}")




#파이썬에서 가능한 오름차순 정렬 코드
list_num = [5, 1, 3, 7, 2, 9]
print(f"초기 리스트 : {list_num}")
rotate = len(list_num)

for i in range(0, rotate-1) :
    for j in range(i+1, rotate) :
        if list_num[i] > list_num[j] :
            list_num[i], list_num[j] = list_num[j], list_num[i]
            

    print(f"{i+1}번째 정렬 : {list_num}")