import requests
import bs4

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8'
headers = {'User-Agent':"mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/102.0.0.0 safari/537.36"} 

myurl = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(myurl.text, 'html.parser')  #파서 사용

# temper = soup.find('span', attrs={"class":"rainfall"}).get_text().replace("%", "퍼센트 확률")
# temper = soup.find_all('span', attrs={"class":"date"}).get_text().replace("%", "퍼센트 확률")
# for i in temper :
#     print(i)
    
    
list_p = soup.find_all('li',attrs={"class":"week_item"})
for i in list_p :
    print(i.get_text().replace("기온", "온도"))
    
    
