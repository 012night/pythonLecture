# 2개의 수를 받아 그 합을 돌려주는 함수
# def plus(x,y) :
#     return x+y

# plus = lambda x,y : x+y
# print(plus(1,2))

# list_calFunc = [lambda x,y : x+y, lambda x,y : x-y, lambda x,y : x*y]
# print(list_calFunc[0](1,2))
# print(list_calFunc[1](1,2))

def starCount(layer) :
    # layer라는 매개변수의 값을 가공하여 별을 찍어내고 그개수의 합을
    # 출력해주는 기능
    pass


def starCount(layer) :
    # layer = 5
    sum_result = 0
    for count in range(layer+1) :
        print("*"*count)
        sum_result += count
    print("총별의 개수 : ", sum_result)

starCount(3)
