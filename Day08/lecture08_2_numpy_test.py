# ========================================================================
# # txt형식으로 저장하는 기능은 추가 설치 없이 파이썬 안에 내장되어 있다.
# # 하지만 엑셀이나 CSV(표형태)로 저장하기 위해서는 numpy 또는 pandas 패키지를 설치해야 한다 
# # pip install numpy
# # pip install pandas
# # pip는 파이썬에서 추가 모듈을 설치할 때 쓰는 명령어 -> 이는 idle이나 IDE, 인터프리터 환경에서 작성하는게 아니고 window cmd창에서 작성
# ========================================================================

# ========================================================================
# # import numpy
# import pandas as pd
# ========================================================================

# ========================================================================
# # 크롤링한 결과를 우선 표로 만들어 놓고 파이썬에게 저 표를 엑셀 또는 CSV 형태로 저장해라고 한다.
# # 표 구성 할 컬럼 만들기
# no = []             # 번호컬럼 생성
# subject_name = []   # 이름컬럼 생성
# ========================================================================

# ========================================================================
# # 내용 추가
# no.append(1)
# no.append(2)
# no.append(3)

# subject_name.append('수학')
# subject_name.append('과학')
# subject_name.append('빅데이터')
# ========================================================================

# ========================================================================
# # 소스에서 DataFrame이 보이면 아 표와 관련된거구나 하고 생각하면 된다
# # 표 (데이터 프레임) 만들기
# subject = pd.DataFrame()   # 표 만들기, 판다스에 있는 함수를 이용해 표를 만들어라~
# subject['과목번호'] = no
# subject['과목명'] = subject_name
# print(subject)
# ========================================================================

# ========================================================================
# # 표 저장
# # subject.to_csv("c:\chi_py_project\subject_csv.csv", encoding="utf-8-sig",index=True)  # csv 형태로 저장, index=True 맨 왼쪽에 순번을 넣을래
# subject.to_csv("C:\chi_py_project\subject_csv.csv", encoding="utf-8-sig", index=False)  # csv 형태로 저장, index=False 맨 왼쪽에 순번을 안넣을래
# subject.to_excel("C:\chi_py_project\subject_xlsx.xlsx" , index=False)                   # 엑셀 형태로 저장
# ========================================================================

# ========================================================================
# # excel 표 불러오기(openpyxl 모듈 설치 필요)
# import openpyxl
# wb = openpyxl.load_workbook("C:\chi_py_project\subject_xlsx.xlsx")
# sheet = wb["Sheet1"]
# print(sheet)

# dict_member = {}
# for i in range(2, sheet.max_row+1) :
#     no = sheet.cell(row=i, column=1).value
#     title = sheet.cell(row=i, column=2).value
#     dict_member[no] = title

# print(dict_member)
# ========================================================================

# ========================================================================
# # csv 불러오기(내장 모듈 사용하으로 다른 설치 필요 없다)
# # UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 12: illegal multibyte sequence
# import csv
# # encoding 미 설정시 인코딩 에러 발생하므로 생성 당시 인코딩과 같은 형태로 불러와야함
# file_csv = open("C:\chi_py_project\subject_csv.csv", encoding="utf-8") 

# read_csv = csv.reader(file_csv)
# for i in read_csv :
#     print(i)
# ========================================================================