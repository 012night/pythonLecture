#pip install bs4
#pipy.org에 접속하여 다운받아오는 명령어

import bs4

ex1 = '''
<html>
    <!-- <head>태그 문서에 대한 기본 정보를 담는다 -->
        <head>
            <meta charset="utf-8">
            <!-- <title>브라우저 위에 나타나는 제목 -->
            <title>메가스터디 HTML 페이지</title>
            <!-- <link href=".//test_css.css" rel="stylesheet" type="text/css"> -->
            <!-- <style>
                nav {background-color:black; font-size: 150%; text-align: center}
                nav a {color: gold}
                h1 {color:red}
            </style> -->
        </head>
        <!-- <body>주로 화면에 나타나는 내용이 담겨있다 -->
        <body>
            <!-- <nav>웹 사이트의 주요 페이지를 안내하는 네비게이션 역할 -->
            <nav>
                <a href="./index.html">Home</a>
                <a href="./about_me.html">About Me</a>
                <a href="https://www.naver.com/">네이버 바로가기</a>
            <!-- <nav style="background-color: black; font-size: 150%; text-align: center">
                <a href="./index.html" style="color: white">Home</a>
                <a href="./about_me.html" style="color: white">About Me</a>
                <a href="https://www.naver.com/" style="color: white">네이버 바로가기</a> -->
            </nav>
            <!-- <h#>헤드라인을 작성 -->
            <h1>h1 태그의 사이즈</h1>
            <h2>h2 태그의 사이즈</h2>
            <h3>h3 태그의 사이즈</h3>
            <h4>h4 태그의 사이즈</h4>
            <h5>h5 태그의 사이즈</h5>

            <p>p태그는 일반적인 문장을 작성할 때 사용합니다.</p>
            <hr>
            <img src="C:\chi_py_project\pic_test.jpg" width="400px" heigth="100px">
            <hr>
            
            <h1>표 만들기</h1>
            <table>
                <tr>
                    <td> 내용 1 </td>
                    <td> 내용 2 </td>
                    <td> 내용 3 </td>
                </tr>
                <tr>
                    <td> 내용 4 </td>
                    <td> 내용 5 </td>
                    <td> 내용 6 </td>
                </tr>
            </table>


            <h1>strong/b태그 그리고 em태크를 이용하여 문자를 강조</h1>
            <strong><em>em 태그로 이탤릭체 표현하기</em></strong> <br>
            <b><i> i 태그로 이탤릭체 표현하기 <i></b> <br>

            <h1>순서가 있는 목차</h1>
            <ol type="i">
                <li> 예습 </li>
                <li> 복습 </li>
            </ol>

            <h1>순서가 없는 목차</h1>
            <ul>
                <li>목차1</li>
                <li>목차2</li>
                <li>목차3</li>
                <li>목차4</li>
            </ul>

            <h1>ol과 ul을 조합한 목차</h1>
            <ul>
                <li> 음료
                    <ol type="1">
                        <li> 환타
                        <li> 소주
                    </ol>
                </li> <br>
                <li> 과자
                    <ol type="i" start="3">
                        <li> 홈런볼
                        <li> 몽쉘
                    </ol>
                </li>
            </ul>
        </body>
</html> '''

soup = bs4.BeautifulSoup(ex1, 'html.parser')
print(soup.find('title'))
print("="*30)
print(soup.find_all('p'))
print("="*30)

# list_p = soup.find_all('li',attrs={"class":"li_list"})
# print("="*30)

txt3 = soup.find_all('li')
for i in txt3 :
    print(i.get_text())
print("="*30)

list_p = soup.find_all('li',attrs={"id":"1"})
for i in list_p :
    print(i.get_text(), '11111111')
print("="*30)
