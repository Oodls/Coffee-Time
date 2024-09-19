# Coffee-Time

## 👥 팀원 소개

| 이승준 | 이주원 |
|:-----------:|:-----------:|
| <img width="120px" src="https://avatars.githubusercontent.com/leesj000603"/> | <img width="120px" src="https://avatars.githubusercontent.com/2oo1s"/> |
| [@leesj000603](https://github.com/leesj000603) | [@2oo1s](https://github.com/2oo1s) |

## 📌 프로젝트 개요

리눅스에서 Crontab을 사용해서 매일 오전 9시에 script를 실행하여 https://finance.naver.com 에서 금융 정보 (원하는 종목의 시가, 핫 뉴스 등을) 저장하는 간단한 실습을 진행

## 🗂 코드 정보

### 크롤링 코드 (특정 종목의 현재 가격)

```python
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
```

### 크롤링 코드 (hot 뉴스)
```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

# 네이버 금융 주요뉴스 URL
news_url = 'https://finance.naver.com/'

def get_news_items(url):
    try:
        # 페이지 요청
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # 주요 뉴스 섹션 선택
        news_section = soup.select_one('div.section_strategy ul')
        if news_section is None:
            raise ValueError("뉴스 섹션을 찾을 수 없습니다. HTML 구조를 확인하세요.")
        
        # 뉴스 항목 추출
        news_items = news_section.select('li')
        top_news = []
        for item in news_items:
            title_tag = item.select_one('span a')
            if title_tag:
                title = title_tag.text.strip()
                link = title_tag['href']
                full_link = 'https://finance.naver.com' + link
                top_news.append({
                    '제목': title,
                    '링크': full_link
                })
        return top_news
    except Exception as e:
        print(f'오류 발생: {e}')
        return []

# 뉴스 제목과 링크 추출
top_news = get_news_items(news_url)

# 현재 날짜와 시간 가져오기 (한국 시간으로 설정)
kst = pytz.timezone('Asia/Seoul')
now = datetime.now(kst)
current_time = now.strftime('%Y-%m-%d %H:%M:%S')

# 결과를 출력
print(f"\n뉴스 목록 (수집일: {current_time})\n")
for idx, news in enumerate(top_news, 1):
    print(f"{idx}. 제목: {news['제목']}")
    print(f"   링크: {news['링크']}")
    print()
```

### Crontab 설정 코드

```shell
username@servername:~$ crontab -e
no crontab for username - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/vim.tiny
  4. /bin/ed

Choose 1-4 [1]: 1

# 매일 오전 9시에 정보 받아오는 거
# 0 9 * * * /usr/bin/python3 /home/username/crontab_test/stock_price.py >> /home/username/crontab_test/stock_price.log 2>&1
# 0 9 * * * /usr/bin/python3 /home/username/crontab_test/finance_news.py >> /home/username/crontab_test/finance_news.log 2>&1

# 테스트 동안엔 정상 동작하는지 확인하기 위해 5분마다 정보 받아오기
*/5 * * * * /usr/bin/python3 /home/username/crontab_test/stock_price.py >> /home/username/crontab_test/stock_price.log 2>&1
*/5 * * * * /usr/bin/python3 /home/username/crontab_test/finance_news.py >> /home/username/crontab_test/finance_news.log 2>&1
```

### 실행 결과
