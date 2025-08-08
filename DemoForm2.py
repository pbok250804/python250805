# DemoForm2.py 
# DemoForm2.ui(화면) + DemoForm2.py(로직)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup
import urllib.request
import re 

#디자인한 파일을 로딩(DemoForm2.ui)
form_class = uic.loadUiType("DemoForm2.ui")[0]
#DemoForm클래스를 정의(QMainWindow를 상속받음) 
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 설정
    def firstClick(self):
        #User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
        hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

        f = open('todayhumor.txt', 'wt', encoding='utf-8')
        for n in range(1,11):
                #오늘의 유머 베스트게시판
                data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
                print(data)
                #웹브라우져 헤더 추가 
                req = urllib.request.Request(data, headers = hdr)
                data = urllib.request.urlopen(req).read()
                #한글이 깨지는 경우 
                page = data.decode('utf-8', 'ignore')
                soup = BeautifulSoup(page, 'html.parser')
                list = soup.find_all('td', attrs={'class':'subject'})
                for item in list:
                        try:
                                #내부에 <a>태그가 있는 경우
                                title = item.find('a').text.strip()
                                if (re.search('미국', title)):
                                        print(title)
                                        f.write(title + '\n')
                        except:
                                pass
            
        f.close()
        self.label.setText("클리앙 중고 장터 크롤링 완료!")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭했습니다~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭입니다")        

#진입점을 체크 
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    demoWindow = DemoForm()  # DemoForm 객체 생성
    demoWindow.show()  # 윈도우 표시
    app.exec_()  # 이벤트 루프 실행