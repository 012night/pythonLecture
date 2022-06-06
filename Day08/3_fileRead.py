#파일의 내용을 읽어오는 명령어들(파일의 형식에 따라 방법 달라)
#txt라면... readline

# #하드디스크에 있는 내용을 메모리로 가져와...
# f = open("C:\chicoding\\test1.txt","r")
# # #여러줄의 데이터가 있을때 한번에 한줄씩 읽어 불러와라
# print(f.readline())
# print(f.readline())
# print(f.readline())
# # #한번에 불러와라(줄바꿈이 안되는 단점이 있어 for문과 같이 쓰는것을 권장)
# result = f.readlines()
# print(result)
# print("\n")

# #index 방법으로 특정 행을 조회하기
# print(result[0])
# print(result[1])
# print("\n")

# #for 반복문으로 한꺼번에 출력하기
# for i in result :
#     print(i)   



# #################################################################3
# #csv, 엑셀 파일 불러오기(기본적으로 내장 되어 있지 않아 추가 설치 필요해)
# #pip install openpyxl
# #openpyxl패키지안에 많은 함수가 있지만 엑셀 시트를 불러오는 함수가 load_workbook
# import openpyxl
# wb = openpyxl.load_workbook("C:\chicoding\\subject_xlsx.xlsx")

# #엑셀 안에는 시트가 여러개 있을수 있으니 어떤 시트를 볼것인지 정해줘야해
# sheet = wb["Sheet1"]
# member = {}
# for i in range(1, sheet.max_row + 1) :
#     cnt = sheet.cell(row=i,column=1).value
#     name = sheet.cell(row=i,column=2).value
#     member[cnt] = name

# print(member)




# csv 형식의 파일 내용 불러오기
# import csv

# # f = open('c:\chicoding\subject_csv.csv', 'r')
# f = open('c:\chicoding\subject_csv.csv', 'r', encoding="UTF-8-sig")
# f_csv = csv.reader(f)
# for i in f_csv :
#     print(i)