import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# DB파일이 없으면 만들고 있다면 접속한다. 
con = sqlite3.connect("ProductList.db")
cur = con.cursor()

# 테이블이 존재하지 않는 경우에만 생성
cur.execute('''CREATE TABLE IF NOT EXISTS Products 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              Name TEXT NOT NULL, 
              Price INTEGER NOT NULL)''')
con.commit()

# 디자인 파일을 로딩
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 초기값 셋팅 
        self.id = 0 
        self.name = ""
        self.price = 0 

        # QTableWidget의 컬럼폭 셋팅하기 
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        # QTableWidget의 헤더 셋팅하기
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품명", "가격"])
        # 탭키로 네비게이션 금지 
        self.tableWidget.setTabKeyNavigation(False)
        # 엔터키를 클릭하면 다음 컨트롤로 이동하는 경우 
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        # 더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)
        
        # 초기 데이터 로드
        self.getProduct()

    def addProduct(self):
        try:
            # 입력값 검증
            name = self.prodName.text().strip()
            price_text = self.prodPrice.text().strip()
            
            if not name:
                QMessageBox.warning(self, "경고", "제품명을 입력해주세요.")
                return
            
            if not price_text:
                QMessageBox.warning(self, "경고", "가격을 입력해주세요.")
                return
                
            try:
                price = int(price_text)
                if price < 0:
                    QMessageBox.warning(self, "경고", "가격은 0 이상이어야 합니다.")
                    return
            except ValueError:
                QMessageBox.warning(self, "경고", "가격은 숫자여야 합니다.")
                return
            
            # 데이터베이스에 삽입
            cur.execute("INSERT INTO Products (Name, Price) VALUES(?,?)", (name, price))
            con.commit()
            
            # 입력 필드 초기화
            self.prodName.clear()
            self.prodPrice.clear()
            
            # 리프레시
            self.getProduct()
            
        except sqlite3.Error as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"제품 추가 중 오류가 발생했습니다: {e}")

    def updateProduct(self):
        try:
            # 입력값 검증
            id_text = self.prodID.text().strip()
            name = self.prodName.text().strip()
            price_text = self.prodPrice.text().strip()
            
            if not id_text:
                QMessageBox.warning(self, "경고", "제품ID를 입력해주세요.")
                return
                
            if not name:
                QMessageBox.warning(self, "경고", "제품명을 입력해주세요.")
                return
            
            if not price_text:
                QMessageBox.warning(self, "경고", "가격을 입력해주세요.")
                return
            
            try:
                product_id = int(id_text)
                price = int(price_text)
                if price < 0:
                    QMessageBox.warning(self, "경고", "가격은 0 이상이어야 합니다.")
                    return
            except ValueError:
                QMessageBox.warning(self, "경고", "ID와 가격은 숫자여야 합니다.")
                return
            
            # 데이터베이스 업데이트
            cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?", (name, price, product_id))
            
            if cur.rowcount == 0:
                QMessageBox.warning(self, "경고", "해당 ID의 제품을 찾을 수 없습니다.")
                return
                
            con.commit()
            
            # 입력 필드 초기화
            self.prodID.clear()
            self.prodName.clear()
            self.prodPrice.clear()
            
            # 리프레시
            self.getProduct()
            
        except sqlite3.Error as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"제품 수정 중 오류가 발생했습니다: {e}")

    def removeProduct(self):
        try:
            # 입력값 검증
            id_text = self.prodID.text().strip()
            
            if not id_text:
                QMessageBox.warning(self, "경고", "삭제할 제품의 ID를 입력해주세요.")
                return
            
            try:
                product_id = int(id_text)
            except ValueError:
                QMessageBox.warning(self, "경고", "ID는 숫자여야 합니다.")
                return
            
            # 삭제 확인
            reply = QMessageBox.question(self, "확인", "정말로 삭제하시겠습니까?", 
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                cur.execute("DELETE FROM Products WHERE id=?", (product_id,))
                
                if cur.rowcount == 0:
                    QMessageBox.warning(self, "경고", "해당 ID의 제품을 찾을 수 없습니다.")
                    return
                    
                con.commit()
                
                # 입력 필드 초기화
                self.prodID.clear()
                self.prodName.clear()
                self.prodPrice.clear()
                
                # 리프레시
                self.getProduct()
                
        except sqlite3.Error as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"제품 삭제 중 오류가 발생했습니다: {e}")

    def getProduct(self):
        try:
            # 검색 결과를 보여주기전에 기존 컨텐트를 삭제(헤더는 제외)
            self.tableWidget.clearContents()

            cur.execute("SELECT * FROM Products ORDER BY id")
            products = cur.fetchall()
            
            # 행 개수 설정
            self.tableWidget.setRowCount(len(products))
            
            # 데이터 표시
            for row, item in enumerate(products):
                # ID 표시 (오른쪽 정렬)
                itemID = QTableWidgetItem(str(item[0]))
                itemID.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.tableWidget.setItem(row, 0, itemID)
                
                # 제품명 표시
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(item[1])))
                
                # 가격 표시 (오른쪽 정렬) - 수정된 부분
                try:
                    price_value = int(item[2])
                    price_formatted = "{:,}".format(price_value)
                except (ValueError, TypeError):
                    price_formatted = str(item[2])
                
                itemPrice = QTableWidgetItem(price_formatted)
                itemPrice.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.tableWidget.setItem(row, 2, itemPrice)
                
        except sqlite3.Error as e:
            QMessageBox.critical(self, "데이터베이스 오류", f"제품 조회 중 오류가 발생했습니다: {e}")

    def doubleClick(self):
        try:
            current_row = self.tableWidget.currentRow()
            if current_row >= 0:
                # 각 항목이 존재하는지 확인
                id_item = self.tableWidget.item(current_row, 0)
                name_item = self.tableWidget.item(current_row, 1)
                price_item = self.tableWidget.item(current_row, 2)
                
                if id_item and name_item and price_item:
                    self.prodID.setText(id_item.text().strip())
                    self.prodName.setText(name_item.text().strip())
                    # 가격에서 천 단위 구분자 제거
                    price_text = price_item.text().replace(',', '')
                    self.prodPrice.setText(price_text)
                    
        except Exception as e:
            QMessageBox.warning(self, "오류", f"데이터 로드 중 오류가 발생했습니다: {e}")

    def closeEvent(self, event):
        # 애플리케이션 종료 시 데이터베이스 연결 닫기
        if con:
            con.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()




