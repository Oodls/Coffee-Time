import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

# 네이버 금융 주요뉴스 URL
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

# 네이버 금융 주요뉴스 URL
news_url = 'https://finance.naver.com/'

def get_news_items(url):
    # 페이지 요청
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # 주요 뉴스 섹션 선택
    news_section = soup.select_one('div.section_strategy ul')
    
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


# 결과를 출력
print(f"\n뉴스 목록 (수집일: {current_time})\n")
for idx, news in enumerate(top_news, 1):
    print(f"{idx}. 제목: {news['제목']}")
    print(f"   링크: {news['링크']}")
    print()
