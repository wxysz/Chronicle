from bs4 import BeautifulSoup

html1 = """<p>test1</p>"""
soup1 = BeautifulSoup(html1, 'lxml')
print(soup1)


html2 = """<html><p>test2</p></html>"""
soup2 = BeautifulSoup(html2, 'lxml')
print(soup2)

html3 = """<body><p>test3</p></body>"""
soup3 = BeautifulSoup(html3, 'lxml')
print(soup3)

''' 실해한 코드
from bs4 import BeautifulSoup
import requests
import json

file = open("./naver.json", "w")

url = "https://search.shopping.naver.com/search/all?query=%EA%B1%B4%EC%A1%B0%EA%B8%B0&cat_id=&frm=NVSHATC"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
cnt = len(soup.find_all('div', class_='basicList_title__3P9Q7'))

for i in range(0,cnt) :
    naver = {}
    metadata = soup.find_all('div', class_='basicList_title__3P9Q7')[i]
    title = metadata.a.get('title')
    print("<제품명> : ", title)               # title
    
    price = soup.find_all('span', class_='price_num__2WUXn')[i].text
    print("<가격> : ", price)                # 가격
    
    url = metadata.a.get('href')
    print("<url> : ", url)                  # url
         
    print("===================================================")
    
    naver = {'제품명' : title , '가격' : price, 'url' : url }
    file.write(json.dumps(naver))

file.close()
'''
''' 성공한 코드
import json,re
from urllib.request import urlopen
from html import unescape

# 웹 페이지 읽어오기
req = urlopen("http://www.hanbit.co.kr/store/books/full_book_list.html")
encoding = req.info().get_content_charset(failobj="utf-8")
html = req.read().decode(encoding)

# 파일 생성
with open("booklist.json", "w", encoding="utf-8") as f:
    data = []
    # 데이터 추출
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        data.append({"BookName": title, "Link": url})
        # 데이터 json 형태로 출력
        print(json.dumps(data, ensure_ascii=False, indent=2))

    # 데이터 변형 및 추가
    json.dump(data, f, ensure_ascii=False, indent=2)
'''
