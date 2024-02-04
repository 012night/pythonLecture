import os

# 현재 작업중인 디렉토리 경로 보여주는...
print(os.getcwd())

# 현재 경로를 원하는 경로로 바꾸는...
os.chdir("C:\py_jan\Day08")
print(os.getcwd())

# # 현재 디렉토리 내부의 구조를 보기위한 명령어
# for x in os.listdir() :
#     print(x)

# # 현재 경로에 하나의 디렉토리 생성
# os.mkdir("sample")
# os.mkdir("sample/smaple1")

# # 현재 경로에 하나의 디렉토리 삭제
# os.rmdir("sample/smaple1")
# os.rmdir("sample")

# # 현재 경로에 여러의 디렉토리 생성
# os.makedirs("sample/sample1/sample2")

# # 현재 경로에 여러의 디렉토리 삭제(내부에 타 파일이 존재하지 않는다면....)
# os.removedirs("sample/sample1/sample2")

# # # # 현재 경로에 여러의 디렉토리 삭제(내부에 타 파일이 존재하지 않는다면....)
# import shutil
# shutil.rmtree("sample")


# os.mkdir("sample")
os.chdir("C:\py_jan\Day08\sample")

# 파일 만들기(open-내장함수)
# open("파일명","mode") # mode w, r ,a
# 순서 1) open
# 순서 2) write
# 순서 3) close

file = open("apple.txt", "w")
file.write("처음으로 입력하는 내용입니다.")
file.close()

file = open("apple.txt", "a")
file.write("두번째로 입력하는 내용입니다.")
file.close()

file = open("apple.txt", "r")
# print(file.read(5))
print(file.readline())
file.close()

# # 삭제.
# os.remove("C:\py_jan\Day08\sample\\apple.txt")






