import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone

# 네이버 금융에서 원하는 종목의 코드를 사용
stock_code = '005930'  # 삼성전자

# 네이버 금융 주식 URL
url = f'https://finance.naver.com/item/sise.nhn?code={stock_code}'

# 페이지 요청
response = requests.get(url)
html = response.text

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 주가 정보 추출 (현재가)
price = soup.select_one('.no_today .blind').text

# 한국 시간 기준으로 현재 날짜와 시간 가져오기
kst = timezone('Asia/Seoul')
now = datetime.now(kst)
current_time = now.strftime("%Y-%m-%d %H:%M")

# 결과 출력
print(f"{current_time} 기준 삼성전자 주가 : {price}원")
