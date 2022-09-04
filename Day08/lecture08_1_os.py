# =======================================================================================
# os(Operating System) 모듈은 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해준다.
# 폴더, 파일 생성 및 이동, 삭제 시 OR 디렉터리 내의 파일 목록 확인시 사용
import os
# =======================================================================================

# =======================================================================================
# # 현재 작업중인 디렉토리의 경로를 보여주는 Current working dir
# print(os.getcwd())
# =======================================================================================

# =======================================================================================
# # 디렉토리를 이동하는 함수 chdir
# # \n, \t 등 문자열 조작하는 이스케이프 함수 쓸때 조심하라. \\로 작성해서 오류 없게...
# os.chdir('C:\chi_py_project\Day08')
# print(os.getcwd())
# =======================================================================================

# =======================================================================================
# # 특정 디렉토리안에 있는 파일등의 목록을 보여주는 listdir
# print(os.listdir('C:\chi_py_project\Day08'))
# =======================================================================================

# =======================================================================================
# # 디렉토리 구조 보기 예쁘게
# for names in os.listdir('C:\chi_py_project') :
#     # if names.endswith('jpg') :
#         print(names)
# =======================================================================================

# =======================================================================================
# # 폴더를 만드는 함수(한번에 하나만) mkdir
# os.mkdir('C:\chi_py_project\\test_dir')
# # 비어있는 폴더 하나 삭제하는 함수 rmdir
# os.rmdir("C:\chi_py_project\\test_dir")
# =======================================================================================

# =======================================================================================
# # 하위에 폴더를 연속적으로 만들어주는 함수 makedirs
# os.makedirs('C:\chi_py_project\\test_dir\chi') 
# # 비어있는 폴더를 하위까지 삭제하는 함수 rmdir
# os.removedirs("C:\chi_py_project\\test_dir\chi")
# # os.rmdir("C:\chi_py_project\\test_dir")
# =======================================================================================

# =======================================================================================
# # 안에 파일이 존재할때 디렉토리 지우는 파일관리 shutil 모듈
# import shutil
# os.makedirs('C:\chi_py_project\\test_dir\chi\\temp1\\temp2\hyhrh')
# # shutil.rmtree('C:\chi_py_project\\test_dir')
# =======================================================================================

# =======================================================================================
# # 지금까지 폴더를 다루는 함수였다면 이번에는 파일을 다루는 함수, 어렵지 않으나 만드는 순서가 중요하다.
# # txt형식으로 저장하는 기능은 파이썬 안에 내장되어있다.
# =======================================================================================

# =======================================================================================
# # 1.비어있는 A4페이지를 준비하듯 파일을 준비한다. r:읽기 w:쓰기 a:붙여쓰기
# # 2.준비된 종이에 내용을 적어라(현재까지는 메모리에 쓴것이다)
# file = open("C:\chi_py_project\\text_01.txt","w")
# file.write(" 텍스트 파일에 처음 쓴 글입니다")
# file.close()

# # 같은 파일을 w모드로 오픈할 경우 덮어씌운다. 
# file = open("C:\chi_py_project\\text_01.txt","w")
# file.write("텍스트 파일에 두번째 쓴 글입니다")
# file.close()
# =======================================================================================

# =======================================================================================
# file = open("C:\chi_py_project\\text_01.txt","a")
# file.write("\n텍스트 파일에 추가모드로 쓴 첫번째 글입니다")
# file.close()
# =======================================================================================

# =======================================================================================
# file3 = open("C:\chi_py_project\\text_01.txt","a")
# file3.write("\n텍스트 파일에 추가모드로 쓴 두번째 글입니다")
# file3.close( )
# =======================================================================================

# =======================================================================================
# # 개행 전까지 읽어오기 -> 문자열을 반환
# file = open("C:\chi_py_project\\text_01.txt","r")
# print(file.readline())
# file.close( )
# =======================================================================================

# =======================================================================================
# # 개행 기준으로 리스트로 불러오기 -> List[문자열]을 반환
# file = open("C:\chi_py_project\\text_01.txt","r")
# print(file.readlines())
# file.close( )
# =======================================================================================

# =======================================================================================
# # n바이트씩 읽어오기 -> 문자N개를 반환
# file = open("C:\chi_py_project\\text_01.txt","r")
# print(file.read(5))
# file.close( )
# os.remove('C:\chi_py_project\\text_01.txt')
# =======================================================================================

# =======================================================================================
# # file.close()를 하지 않고 실행시 삭제 안되는걸 확인 하라
# file = open("C:\chi_py_project\\text_01.txt","w")
# file.close()
# os.remove('C:\chi_py_project\\text_01.txt')
# =======================================================================================

# print(ord('가'))
# print(hex(44032))

# print(ord('메'))
# print(ord('가'))

# print(hex(47700))
# print(hex(44032))

# print(chr(47700))
# print(chr(44032))