#외부라이브러리 설치 
#cmd 
#pip install openpyxl
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4&ackey=o758hdw0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 신문기사 제목 추출 (네이버 뉴스 영역)
titles = []
# 기사 제목은 headline1, body2 등 다양한 class에 존재할 수 있으므로 headline1 우선 사용
for span in soup.select("span.sds-comps-text-type-headline1"):
    title = span.get_text(strip=True)
    if title:
        titles.append(title)

# headline1이 없을 경우 body2로 대체
if not titles:
    for span in soup.select("span.sds-comps-text-type-body2"):
        title = span.get_text(strip=True)
        if title:
            titles.append(title)

# 엑셀 파일로 저장
wb = Workbook()
ws = wb.active
ws.title = "네이버 뉴스 수집"
ws.append(["번호", "제목"])

for idx, title in enumerate(titles, 1):
    ws.append([idx, title])

wb.save("naverResult.xlsx")
print("naverResult.xlsx 파일로 저장 완료")