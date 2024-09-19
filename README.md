# Coffee-Time

## 👥 팀원 소개

| 이승준 | 이주원 |
|:-----------:|:-----------:|
| <img width="120px" src="https://avatars.githubusercontent.com/leesj000603"/> | <img width="120px" src="https://avatars.githubusercontent.com/2oo1s"/> |
| [@leesj000603](https://github.com/leesj000603) | [@2oo1s](https://github.com/2oo1s) |

## 📌 프로젝트 개요

리눅스에서 Crontab을 사용해서 매일 오전 9시에 파이썬 파일을 실행하여 ~~~ 정보 받아오는 실습 진행

## 🗂 코드 정보

### 크롤링 코드

```python

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
# 0 9 * * * /usr/bin/python3 /home/username/mission/stock_price.py >> /home/username/mission/stock_price_log.log 2>&1

# 테스트 동안엔 정상 동작하는지 확인하기 위해 5분마다 정보 받아오기
*/5 * * * * /usr/bin/python3 /home/username/mission/stock_price.py >> /home/username/mission/stock_price_log.log 2>&1
```

### 실행 결과
