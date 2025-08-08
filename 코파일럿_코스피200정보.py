import requests
from bs4 import BeautifulSoup
import re

url = "https://finance.naver.com/sise/sise_index.naver?code=KPI200"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 편입종목 상위 테이블(class="type_1") 찾기
table = soup.find("table", class_="type_1")
stocks = []

if table:
    rows = table.find_all("tr")
    for row in rows[2:]:  # 0:헤더, 1:blank, 2부터 데이터
        cols = row.find_all("td")
        if len(cols) == 7:
            name = cols[0].get_text(strip=True)
            price = cols[1].get_text(strip=True)
            change = cols[2].get_text(strip=True)
            rate = cols[3].get_text(strip=True)
            volume = cols[4].get_text(strip=True)
            amount = cols[5].get_text(strip=True)
            marketcap = cols[6].get_text(strip=True)
            if name:  # 빈 행 제외
                stocks.append({
                    "종목명": name,
                    "현재가": price,
                    "전일비": change,
                    "등락률": rate,
                    "거래량": volume,
                    "거래대금(백만)": amount,
                    "시가총액(억)": marketcap
                })

for stock in stocks:
    print(stock)