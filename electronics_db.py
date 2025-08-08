import sqlite3
import random

class ElectronicsDB:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS electronics (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price INTEGER NOT NULL
                )
            """)

    def insert_product(self, product_id, name, price):
        with self.conn:
            self.conn.execute(
                "INSERT INTO electronics (id, name, price) VALUES (?, ?, ?)",
                (product_id, name, price)
            )

    def update_product(self, product_id, name=None, price=None):
        with self.conn:
            if name and price is not None:
                self.conn.execute(
                    "UPDATE electronics SET name=?, price=? WHERE id=?",
                    (name, price, product_id)
                )
            elif name:
                self.conn.execute(
                    "UPDATE electronics SET name=? WHERE id=?",
                    (name, product_id)
                )
            elif price is not None:
                self.conn.execute(
                    "UPDATE electronics SET price=? WHERE id=?",
                    (price, product_id)
                )

    def delete_product(self, product_id):
        with self.conn:
            self.conn.execute(
                "DELETE FROM electronics WHERE id=?",
                (product_id,)
            )

    def select_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM electronics")
        return cursor.fetchall()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = ElectronicsDB()

    # 샘플 데이터 100개 생성 및 삽입
    sample_names = ["TV", "냉장고", "세탁기", "에어컨", "노트북", "스마트폰", "태블릿", "청소기", "전자레인지", "오븐"]
    for i in range(1, 101):
        name = f"{random.choice(sample_names)}_{i}"
        price = random.randint(100000, 2000000)
        db.insert_product(i, name, price)

    # 전체 데이터 조회
    products = db.select_products()
    for product in products[:5]:  # 처음 5개만 출력
        print(product)