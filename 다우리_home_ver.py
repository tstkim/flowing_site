from selenium import webdriver  # 웹 브라우저를 제어하기 위한 라이브러리
from selenium.webdriver.common.by import By  # HTML 요소를 찾기 위한 방법들을 제공하는 라이브러리
from selenium.webdriver.chrome.service import Service  # Chrome 웹드라이버의 서비스를 관리하는 라이브러리
from selenium.webdriver.chrome.options import Options  # Chrome 웹드라이버의 옵션을 설정하는 라이브러리
from webdriver_manager.chrome import ChromeDriverManager  # Chrome 웹드라이버를 자동으로 다운로드하고 업데이트하는 라이브러리
from selenium.webdriver.common.keys import Keys  # 키보드 키를 사용하기 위한 라이브러리
from selenium.webdriver.support.ui import WebDriverWait  # 웹 페이지가 로드될 때까지 기다리는 라이브러리
from selenium.webdriver.support import expected_conditions as EC  # 특정 조건이 만족될 때까지 기다리는 라이브러리
from bs4 import BeautifulSoup  # HTML 파일을 파싱(분석)하기 위한 라이브러리
import time  # 시간 관련 기능을 제공하는 라이브러리

# ChromeDriver 자동 설치 및 업데이트 설정
chrome_service = Service(ChromeDriverManager().install())  # Chrome 웹드라이버를 자동으로 다운로드하고 설정
chrome_options = Options()
chrome_options.add_argument('--headless')  # 브라우저 창을 띄우지 않도록 설정 (백그라운드에서 실행)
chrome_options.add_argument('--disable-gpu')  # GPU(그래픽 처리 장치)를 사용하지 않도록 설정

# 웹드라이버 시작
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)  # Chrome 웹드라이버를 시작
wait = WebDriverWait(driver, 10)  # 웹 페이지 로드를 최대 10초까지 기다림

try:
    # 로그인 페이지로 이동
    driver.get('https://dawoori-sports.kr/member/login')  # 웹사이트의 로그인 페이지로 이동

    # 로그인 정보 입력
    userid_input = driver.find_element(By.NAME, 'userid')  # 사용자 아이디 입력란을 찾음
    password_input = driver.find_element(By.NAME, 'password')  # 사용자 비밀번호 입력란을 찾음
    userid_input.send_keys('flowing')  # 아이디 입력란에 아이디 입력
    password_input.send_keys('q6160q6160q')  # 비밀번호 입력란에 비밀번호 입력

    # 엔터 키로 로그인
    password_input.send_keys(Keys.ENTER)  # 비밀번호 입력란에서 엔터 키를 누름

    # 로그인 완료 대기
    time.sleep(5)  # 충분한 대기 시간을 줌

    # 보호된 페이지로 이동
    driver.get('https://dawoori-sports.kr/goods/catalog?page=1&searchMode=catalog&category=c0019&per=20&filter_display=lattice&code=0019')  # 보호된 페이지로 이동

    # 페이지 로드 대기
    time.sleep(5)  # 페이지가 완전히 로드될 때까지 5초 대기

    # 페이지 내용 파싱 (HTML 분석)
    page_source = driver.page_source  # 페이지의 HTML 소스를 가져옴
    soup = BeautifulSoup(page_source, 'html.parser')  # BeautifulSoup을 사용하여 HTML 소스를 파싱

    # 상품명 추출
    product_names = soup.find_all('span', class_='name')  # HTML 소스에서 'span' 태그 중 클래스가 'name'인 모든 요소를 찾음
    for product in product_names:  # 찾은 모든 상품명 요소에 대해 반복
        print(product.get_text(strip=True))  # 각 상품명의 텍스트를 출력

except Exception as e:
    print(f"오류 발생: {e}")

finally:
    # 웹드라이버 종료
    driver.quit()  # 웹드라이버 종료
