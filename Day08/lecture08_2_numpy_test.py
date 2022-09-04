####################################################
#txt형식으로 저장하는 기능은 특별한 설정이나 추가 설치 없이 파이썬 안에 내장되어있다.
#하지만 기업에서 많이 사용하는 엑셀이나 CSV(표형태)로 저장하기위해서는 다르다
#크롤링한 결과를 우선 표로 만들어 놓고 파이썬에게 저 표를 엑셀 또는 CSV 형태로 저장해라고 한다...
#이때 설치해야 하는 패키지가 numpy 또는 pandas
#pip install numpy
#pip install pandas
#pip는 파이썬에서 추가 모듈을 설치할 때 쓰는 명령어 -> 이는 idle이나 IDE에서 치는게 아니고 window cmd창에서 쓰는거야

import numpy
import pandas as pd

# # 표 ( 데이터 프레임 ) 만들기
# no = [ ]             #번호컬럼 생성
# subject_name = [ ]   #이름컬럼 생성

# no.append(1)
# no.append(2)
# no.append(3)

# subject_name.append('수학')
# subject_name.append('과학')
# subject_name.append('빅데이터')

# # 소스에서 DataFrame이 보이면 아 표와 관련된거구나 하고 생각하면 된다
# # subject = pd.DataFrame()  # 표만들기, 판다스에 있는 함수를 이용해 표를 만들어라~
# subject = pd.DataFrame( )
# subject['과목번호'] = no
# subject['과목명'] = subject_name
# print(subject)

# # subject.to_csv("c:\\chicoding\\subject.csv", encoding="utf-8-sig",index=False)  #csv 형태로 저장, index는 맨 왼쪽에 순번을 넣을래 안넣을래
# subject.to_csv("c:\chicoding\subject_csv.csv", encoding="utf-8-sig", index=False)  #csv 형태로 저장, index는 맨 왼쪽에 순번을 넣을래 안넣을래
# subject.to_excel("c:\chicoding\subject_xlsx.xlsx" , index=False)                     #엑셀 형태로 저장