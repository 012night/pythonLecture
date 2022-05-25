#모듈 : 함수, 클래스등 .py 안에 선언된 내용은 다른 py프로그램에서 import를 통해 활용할 수 있다.
#lecture06_2_1.py 참고.

#if __name__ == '__main__': 의 문법의 의미
#__name__ : 프로그램의 이름 을 의미
#__main__ : 실행의 주체가 되는 프로그램의 이름 을 의미
#그러므로, 위의 if문의 의미는 해당 프로그램이 실행의 주체가 될 때만 실행하라는 의미이다.

#패키지 = 모듈 여러개를 모아놓은 것. 라이브러리랑 같은 개념



# #같은 경로상의 모듈에서 함수를 사용하기
# import lecture06_2_class

# result = lecture06_2_class.add(4,3)
# print(result)



# # 같은 경로상의 모듈에서 클래스를 사용하기
# import lecture06_2_class

# class_import = lecture06_2_class.Calculator(20, 30)
# class_import.add()
# print(class_import.result)




# import sys

# print(sys.path)
# sys.path.append('C:\chicoding')
# print(sys.path)


# #다른 경로상의 모듈에서 함수를 사용하기
# import sys
# sys.path.append('C:\chicoding')

# import module_test

# result = module_test.add(4,3)
# print(result)


# #다른 경로상의 모듈에서 클래스를 사용하기
# import module_test

# class_import = module_test.Calculator(20, 30)
# class_import.sum()
# print(class_import.result)


# Lib\site-packages에 경로를 추가하여 영구적으로 path 등록하기
# import sys
# print(sys.path)



# #패키지 사용하기 1
# # import bank.deposit.deposit
# bank.deposit.deposit.deposit()


# #패키지 사용하기 2(사용하고자 하는 함수의 모듈까지 import하는 방법)
# from bank.deposit import deposit
# deposit.deposit()


# #패키지 사용하기 3(모듈내 함수 하나를 직접 실행하는방법)
# from bank.deposit.deposit import deposit
# deposit()


# #패키지 사용하기 4(__init__ 내 all사용의 의미)
# #아래와 같이 선언시 deposit 폴더 내 모든 함수를 사용하겠다는 의미이나 찾지 못한다. 이때 all 변수 선언에 의미가있다
# from bank.deposit import *
# deposit.deposit()
