from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scroll_to_bottom(driver):
    # 페이지 맨 아래로 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 페이지가 로딩될 때까지 대기

def get_product_titles(driver):
    # 현재 페이지 HTML 가져오기
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # 상품 제목 가져오기
    product_titles = soup.find_all('div', class_='product_title__Mmw2K')
    
    return [title.text.strip() for title in product_titles]

def search_naver_shopping(query):
    # ChromeDriverManager로 Chrome WebDriver 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # 네이버 쇼핑 검색 URL
    url = f"https://search.shopping.naver.com/search/all?query={query}"
    
    # 검색 페이지 열기
    driver.get(url)
    time.sleep(2)  # 페이지가 로딩될 때까지 대기
    
    try:
        # 스크롤을 맨 아래로 내림
        scroll_to_bottom(driver)
        
        # 추가로 스크롤을 내릴 때마다 새로운 상품이 로딩될 수 있으므로 여러 번 스크롤을 진행
        for _ in range(5):  # 5번 스크롤
            scroll_to_bottom(driver)
        
        # 스크롤이 완료되면 모든 상품 제목 가져오기
        product_titles = get_product_titles(driver)
        
        # 검색 결과 출력
        for title in product_titles:
            print(title)
    finally:
        # WebDriver 종료
        driver.quit()

# 검색어 입력 받기     
query = input("검색어를 입력하세요: ")

# 검색 함수 호출
search_naver_shopping(query)