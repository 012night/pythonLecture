#폴더 생성 및 이동, 삭제 시 사용 OS 모듈
import os

# 현재 작업중인 디렉토리의 경로를 보여주는 Current working dir
# print(os.getcwd())

# #디렉토리를 이동하는 함수 chdir
# #\n, \t 등 문자열 조작하는 이스케이프 함수 쓸때 조심하라. \\로 작성해서 오류 없게...
# os.chdir('C:\chicoding\Day08')
# print(os.getcwd())

# #특정 디렉토리안에 있는 파일등의 목록을 보여주는 listdir
# print(os.listdir('C:\chicoding'))

# #디렉토리 구조 보기 예쁘게
# for dir_list in os.listdir('C:\chicoding') :
#     print(dir_list)

# #폴더를 만드는 함수(한번에 하나만) mkdir
# os.mkdir('C:\chicoding\\test_dir\\test')

# #하위에 폴더를 연속적으로 만들어주는 함수 makedirs
# os.makedirs('C:\chicoding\\test_dir\\test\\temp1\\temp2\\temp3') 
# os.mkdir('C:\chicoding\\test_dir\\test\\temp1\\temp2\\temp3\python') 

# # #비어있는 폴더 하나 삭제하는 함수 rmdir
# os.rmdir("C:\chicoding\\test_dir\\test\\temp1\\temp2\\temp3\python")


# # 안에 파일이 존재할때 디렉토리 지우는 파일관리 shutil 모듈
# import shutil
# os.makedirs('C:\chicoding\\rew\\temp1\\temp2\hyhrh')
# shutil.rmtree('C:\chicoding\\rew\\temp1')




####################################################
#위에가 폴더를 다루는 함수였다면 이번에는 파일을 다루는 함수
#txt형식으로 저장하는 기능은 파이썬 안에 내장되어있다.
#함수는 어렵지 않으나 만드는 순서가 중요하다.

# #1.비어있는 파일을 우선 준비한다. A4준비하듯 r읽기전용 w쓰기 a붙여쓰기
# print(os.getcwd())
# os.makedirs("py_temp2")
# os.chdir("py_temp2")
# print(os.getcwd())

file = open("C:\chicoding\\test1.txt","w")
file.write(" 텍스트 파일에 처음 쓴 글입니다")
file.close()

file = open("C:\chicoding\\test1.txt","w")
file.write("텍스트 파일에 두번째 쓴 글입니다")
file.close()

#2. 준비된 종이에 내용을 적어라(현재까지는 메모리에 쓴것이다)
file = open("C:\chicoding\\test1.txt","a")
file.write("\n텍스트 파일에 추가모드로 쓴 첫번째 글입니다")
file.close()

file3 = open("C:\chicoding\\test1.txt","a")
file3.write("\n텍스트 파일에 추가모드로 두번째 글입니다")
file3.close( )

#개행 전까지 읽어오기 -> 문자열을 반환
file = open("C:\chicoding\\test1.txt","r")
print(file.readline())
file.close( )

#개행 기준으로 리스트로 불러오기 -> List[문자열]을 반환
file = open("C:\chicoding\\test1.txt","r")
print(file.readlines())
file.close( )

#n바이트씩 읽어오기 -> 문자N개를 반환
file = open("C:\chicoding\\test1.txt","r")
print(file.read())
file.close( )

#file.close( )를 하지 않고 실행시 삭제 안되는걸 확인 하라
os.remove('C:\chicoding\\test1.txt')

# print(ord('가'))
# print(hex(44032))