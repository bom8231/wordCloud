from bs4 import BeautifulSoup 
from selenium import webdriver
import chromedriver_autoinstaller
import requests
import time

# 크롬 드라이버 구동 위함 
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0] #크롬드라이버 버전 확인
try: #크롬 드라이버가 설치된 경우
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')   
except: #크롬 드라이버가 설치되지 않은 경우
    chromedriver_autoinstaller.install(True) #크롬브라우저 설치
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.implicitly_wait(10) # 10초동안 기다림
driver.maximize_window() #창을 최대화 시킴

# 크롤링 부분
headers = {'User-Agent': 'Mozilla/5.0'} #크롤링 차단 예방, 유저 에이전트 지정
url = "https://www.campuspick.com/contest?category=108"
response = requests.get(url, headers=headers) #html 조회 요청
driver.get(url) #크롬창을 열어줌.

#맨 밑까지 스크롤
prev_height = driver.execute_script("return document.body.scrollHeight") 

# 웹페이지 맨 아래까지 무한 스크롤
while True:
    # 스크롤을 화면 가장 아래로 내린다
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(2)

    # 현재 문서 높이를 가져와서 저장
    curr_height = driver.execute_script("return document.body.scrollHeight")

    if (curr_height == prev_height):
        break
    else:
        prev_height = driver.execute_script("return document.body.scrollHeight")

html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')


title_list = soup.select("#container > div.list > div > a > h2") #뷰티플 소프를 이용하여 선택
title_list_final = []
for title in title_list:
  title_list_final.append(title.text)

with open('competition_title.txt','w',encoding='UTF-8') as f:
    for content in title_list_final:
        f.write(content+'\n')




