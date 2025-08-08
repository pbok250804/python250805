import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                            QWidget, QPushButton, QLineEdit, QLabel, QTableWidget, 
                            QTableWidgetItem, QMessageBox, QHeaderView, QGroupBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class ElectronicsManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_database()
        self.init_ui()
        self.load_data()
        
    def init_database(self):
        """SQLite 데이터베이스 초기화"""
        self.conn = sqlite3.connect('electronics.db')
        self.cursor = self.conn.cursor()
        
        # MyProducts 테이블 생성
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS MyProducts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()
    
    def init_ui(self):
        """UI 초기화"""
        self.setWindowTitle('전자제품 데이터 관리')
        self.setGeometry(100, 100, 800, 600)
        
        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 메인 레이아웃
        main_layout = QVBoxLayout(central_widget)
        
        # 입력 그룹박스
        input_group = QGroupBox("제품 정보 입력/수정")
        input_layout = QVBoxLayout(input_group)
        
        # 제품명 입력
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("제품명:"))
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("제품명을 입력하세요")
        name_layout.addWidget(self.name_input)
        input_layout.addLayout(name_layout)
        
        # 가격 입력
        price_layout = QHBoxLayout()
        price_layout.addWidget(QLabel("가격:"))
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("가격을 입력하세요")
        price_layout.addWidget(self.price_input)
        input_layout.addLayout(price_layout)
        
        # 버튼들
        button_layout = QHBoxLayout()
        
        self.add_btn = QPushButton("추가")
        self.add_btn.clicked.connect(self.add_product)
        button_layout.addWidget(self.add_btn)
        
        self.update_btn = QPushButton("수정")
        self.update_btn.clicked.connect(self.update_product)
        self.update_btn.setEnabled(False)
        button_layout.addWidget(self.update_btn)
        
        self.delete_btn = QPushButton("삭제")
        self.delete_btn.clicked.connect(self.delete_product)
        self.delete_btn.setEnabled(False)
        button_layout.addWidget(self.delete_btn)
        
        self.clear_btn = QPushButton("초기화")
        self.clear_btn.clicked.connect(self.clear_inputs)
        button_layout.addWidget(self.clear_btn)
        
        input_layout.addLayout(button_layout)
        main_layout.addWidget(input_group)
        
        # 검색 그룹박스
        search_group = QGroupBox("검색")
        search_layout = QHBoxLayout(search_group)
        
        search_layout.addWidget(QLabel("제품명 검색:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("검색할 제품명을 입력하세요")
        self.search_input.textChanged.connect(self.search_products)
        search_layout.addWidget(self.search_input)
        
        self.search_clear_btn = QPushButton("검색 초기화")
        self.search_clear_btn.clicked.connect(self.clear_search)
        search_layout.addWidget(self.search_clear_btn)
        
        main_layout.addWidget(search_group)
        
        # 테이블 위젯
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "제품명", "가격"])
        
        # 테이블 헤더 설정
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        
        # 테이블 선택 이벤트
        self.table.itemSelectionChanged.connect(self.on_table_selection_changed)
        
        main_layout.addWidget(self.table)
        
        # 현재 선택된 제품 ID 저장
        self.selected_product_id = None
    
    def add_product(self):
        """제품 추가"""
        name = self.name_input.text().strip()
        price_text = self.price_input.text().strip()
        
        if not name:
            QMessageBox.warning(self, "경고", "제품명을 입력하세요.")
            return
        
        if not price_text:
            QMessageBox.warning(self, "경고", "가격을 입력하세요.")
            return
        
        try:
            price = float(price_text)
            if price < 0:
                QMessageBox.warning(self, "경고", "가격은 0 이상이어야 합니다.")
                return
        except ValueError:
            QMessageBox.warning(self, "경고", "올바른 가격을 입력하세요.")
            return
        
        try:
            self.cursor.execute("INSERT INTO MyProducts (name, price) VALUES (?, ?)", (name, price))
            self.conn.commit()
            QMessageBox.information(self, "성공", "제품이 추가되었습니다.")
            self.clear_inputs()
            self.load_data()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "오류", f"데이터베이스 오류: {e}")
    
    def update_product(self):
        """제품 수정"""
        if self.selected_product_id is None:
            QMessageBox.warning(self, "경고", "수정할 제품을 선택하세요.")
            return
        
        name = self.name_input.text().strip()
        price_text = self.price_input.text().strip()
        
        if not name:
            QMessageBox.warning(self, "경고", "제품명을 입력하세요.")
            return
        
        if not price_text:
            QMessageBox.warning(self, "경고", "가격을 입력하세요.")
            return
        
        try:
            price = float(price_text)
            if price < 0:
                QMessageBox.warning(self, "경고", "가격은 0 이상이어야 합니다.")
                return
        except ValueError:
            QMessageBox.warning(self, "경고", "올바른 가격을 입력하세요.")
            return
        
        try:
            self.cursor.execute("UPDATE MyProducts SET name=?, price=? WHERE id=?", 
                              (name, price, self.selected_product_id))
            self.conn.commit()
            QMessageBox.information(self, "성공", "제품이 수정되었습니다.")
            self.clear_inputs()
            self.load_data()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "오류", f"데이터베이스 오류: {e}")
    
    def delete_product(self):
        """제품 삭제"""
        if self.selected_product_id is None:
            QMessageBox.warning(self, "경고", "삭제할 제품을 선택하세요.")
            return
        
        reply = QMessageBox.question(self, "확인", "선택한 제품을 삭제하시겠습니까?",
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                self.cursor.execute("DELETE FROM MyProducts WHERE id=?", (self.selected_product_id,))
                self.conn.commit()
                QMessageBox.information(self, "성공", "제품이 삭제되었습니다.")
                self.clear_inputs()
                self.load_data()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "오류", f"데이터베이스 오류: {e}")
    
    def clear_inputs(self):
        """입력 필드 초기화"""
        self.name_input.clear()
        self.price_input.clear()
        self.selected_product_id = None
        self.update_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        self.table.clearSelection()
    
    def clear_search(self):
        """검색 초기화"""
        self.search_input.clear()
        self.load_data()
    
    def search_products(self):
        """제품 검색"""
        search_text = self.search_input.text().strip()
        
        if search_text:
            try:
                self.cursor.execute("SELECT * FROM MyProducts WHERE name LIKE ? ORDER BY id",
                                  (f"%{search_text}%",))
                products = self.cursor.fetchall()
                self.populate_table(products)
            except sqlite3.Error as e:
                QMessageBox.critical(self, "오류", f"검색 중 오류: {e}")
        else:
            self.load_data()
    
    def load_data(self):
        """전체 데이터 로드"""
        try:
            self.cursor.execute("SELECT * FROM MyProducts ORDER BY id")
            products = self.cursor.fetchall()
            self.populate_table(products)
        except sqlite3.Error as e:
            QMessageBox.critical(self, "오류", f"데이터 로드 오류: {e}")
    
    def populate_table(self, products):
        """테이블에 데이터 채우기"""
        self.table.setRowCount(len(products))
        
        for row, product in enumerate(products):
            id_item = QTableWidgetItem(str(product[0]))
            id_item.setFlags(id_item.flags() & ~Qt.ItemIsEditable)
            self.table.setItem(row, 0, id_item)
            
            name_item = QTableWidgetItem(product[1])
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
            self.table.setItem(row, 1, name_item)
            
            price_item = QTableWidgetItem(f"{product[2]:,.0f}원")
            price_item.setFlags(price_item.flags() & ~Qt.ItemIsEditable)
            self.table.setItem(row, 2, price_item)
    
    def on_table_selection_changed(self):
        """테이블 선택 변경 이벤트"""
        selected_rows = self.table.selectionModel().selectedRows()
        
        if selected_rows:
            row = selected_rows[0].row()
            
            # 선택된 행의 데이터 가져오기
            id_item = self.table.item(row, 0)
            name_item = self.table.item(row, 1)
            price_item = self.table.item(row, 2)
            
            if id_item and name_item and price_item:
                self.selected_product_id = int(id_item.text())
                self.name_input.setText(name_item.text())
                
                # 가격에서 쉼표와 "원" 제거
                price_text = price_item.text().replace(',', '').replace('원', '')
                self.price_input.setText(price_text)
                
                self.update_btn.setEnabled(True)
                self.delete_btn.setEnabled(True)
        else:
            self.selected_product_id = None
            self.update_btn.setEnabled(False)
            self.delete_btn.setEnabled(False)
    
    def closeEvent(self, event):
        """프로그램 종료 시 데이터베이스 연결 종료"""
        self.conn.close()
        event.accept()

def main():
    app = QApplication(sys.argv)
    
    # 애플리케이션 스타일 설정
    app.setStyleSheet("""
        QMainWindow {
            background-color: #f0f0f0;
        }
        QGroupBox {
            font-weight: bold;
            border: 2px solid #cccccc;
            border-radius: 5px;
            margin-top: 1ex;
            padding-top: 10px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
        }
        QPushButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 8px 16px;
            text-align: center;
            font-size: 14px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:disabled {
            background-color: #cccccc;
            color: #666666;
        }
        QLineEdit {
            border: 2px solid #ddd;
            border-radius: 4px;
            padding: 5px;
            font-size: 14px;
        }
        QLineEdit:focus {
            border-color: #4CAF50;
        }
        QTableWidget {
            border: 1px solid #ddd;
            selection-background-color: #4CAF50;
        }
        QHeaderView::section {
            background-color: #f1f1f1;
            padding: 8px;
            border: 1px solid #ddd;
            font-weight: bold;
        }
    """)
    
    window = ElectronicsManager()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()