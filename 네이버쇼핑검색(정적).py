


import requests
from bs4 import BeautifulSoup

def search_naver_shopping(query):
    # 네이버 쇼핑 검색 URL
    url = f"https://search.shopping.naver.com/search/all?query={query}"
    
    # HTTP GET 요청 보내기
    response = requests.get(url)
    
    # 응답 코드 확인
    if response.status_code == 200:
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 상품 제목 가져오기
        product_titles = soup.find_all('div', class_='product_title__Mmw2K')
        
        # 검색 결과 출력
        for title in product_titles:
            print(title.text.strip())  # 공백 제거 후 출력
  
    else:
        print("네이버에 접속할 수 없습니다.")

# 검색어 입력 받기     
query = input("검색어를 입력하세요: ")

# 검색 함수 호출
search_naver_shopping(query)





