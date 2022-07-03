#pip install bs4
#pipy.org에 접속하여 다운받아오는 명령어

import bs4

ex1 = '''
<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <title>메가스터디 HTML 테스트</title>
</head>

<body>
    <h1>p태그와 hr 태그를 확인해봅시다.</h1>
    <p>우리는 여기서 테스트를 한답니다. 여러분 수업 재미있나요?</p>
    <hr>

    <h1>하이퍼 링크 테스트에요</h1>
    <a href="https://www.naver.com/">네이버 바로가기</a>

    <h1>이미지 테스트에요</h1>
    <img src="C:\chicoding\\test_img.jpg" width="500" heigth="200">


    <h1> 표 만들기 연습 </h1>
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


    <h1> strong과 b태그, 그리고 em 태크를 이용하여 문자를 강조해봅시다. </h1>
    <strong><em>em 태그로 이탤릭체 표현하기</em></strong> <br>
    <b><i> i 태그로 이탤릭체 표현하기 <i></b> <br>

    <h1> span태그를 이용한 색상 강조 </h1>
    <p><strong><span style="color:red">1만원</span></strong> 에 팔아요~! </p>

    <h1>순서가 있는 목차</h1>
    <ol type="a">
        <li class='li_list'> 양치질 하기 </li>
        <li class='li_list'> 샴푸로 머리감기 </li>
    </ol>

    <ul>
        <li>목차1
            <ol>
                <li id = '1'>가</li>
                <li id = '2'>나</li>
                <li id = '3'>다</li>
                <li>라</li>
            </ol>
        </li>
        <li>목차2</li>
        <li>목차3</li>
        <li>목차4</li>
    </ul>

    <ul>
        <li> 외모 가꾸기
            <ol type="a">
                <li> 양치질 하기
                <li> 샴푸로 머리감기
            </ol>
        </li> <br>
        <li> 옷 잘입기
            <ol type="a" start="3">
                <li> 양말은 반양말 신기
                <li> 상의와 신발 깔맞춤 신경쓰기
            </ol>
        </li>
    </ul>
</body>

</html> '''

soup = bs4.BeautifulSoup(ex1 , 'html.parser')
print(soup.find('title'))
print(soup.find_all('p'))

# list_p = soup.find_all('li',attrs={"class":"li_list"})
list_p = soup.find_all('li',attrs={"id":"1"})

txt3 = soup.find_all('li')
for i in txt3 :
    print(i.get_text())

for i in list_p :
    print(i.get_text(), '11111111')
