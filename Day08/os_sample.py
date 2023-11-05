import os

#현재 작업경로 보여주는 함수
print(os.getcwd())
# 디렉토리 경로 변경
os.chdir("C:\python_oct\Day08")
print(os.getcwd())

# # 특정 디렉토리 내부의 구조를 보여주는 함수
# # print(os.listdir("C:\python_oct"))
# print(os.listdir())
# for x in os.listdir() :
#     print(x)

# # 폴더 생성(한번에 하나의 디렉토리만 가능)
# os.mkdir("appple")

# 폴더 삭제(한번에 하나의 디렉토리만 가능)
# os.rmdir("appple")

# # 재귀적으로 생성 / 삭제
# os.makedirs("appple\\banana")
# os.removedirs("appple\\banana")


# os.mkdir("appple")

# # 디렉터리 내부에 파일이 존재 하더라도 무시하고 삭제
# 권장X
# import shutil
# shutil.rmtree("C:\python_oct\Day08\\appple")


# 파일 만들기
# os.mkdir("sample_text")
print(os.getcwd())
os.chdir("C:\python_oct\Day08\sample_text")
print(os.getcwd())

# open 3가지 타입이 존재(읽기(r), 쓰기(w), 추가(a))
# 1) 비어있는 파일 생성
file1 = open("word.txt", "w")
# 2) 내용작성(메모리에)
file1.write("내용작성")
# 3) 하드에 기록
file1.close()

file2 = open("word.txt", "w")
file2.write("내용작성 22222")
file2.close()


file3 = open("word.txt", "a")
file3.write("\n내용 추가")
file3.close()

file4 = open("word.txt", "r")
# 문서전체(바이트단위) 읽어 오기
print(file4.read())
# # 줄단위로 읽어 오기
# print(file4.readline())
# print(file4.readline())
file4.close()


# 파일 삭제
os.remove("C:\python_oct\Day08\sample_text\word.txt")


