import sqlite3
import random

class ElectronicsDB:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_product(self, product_id, name, price):
        query = "INSERT INTO products (product_id, name, price) VALUES (?, ?, ?)"
        self.conn.execute(query, (product_id, name, price))
        self.conn.commit()

    def update_product(self, product_id, name=None, price=None):
        fields = []
        params = []
        if name is not None:
            fields.append("name = ?")
            params.append(name)
        if price is not None:
            fields.append("price = ?")
            params.append(price)
        params.append(product_id)
        query = f"UPDATE products SET {', '.join(fields)} WHERE product_id = ?"
        self.conn.execute(query, params)
        self.conn.commit()

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE product_id = ?"
        self.conn.execute(query, (product_id,))
        self.conn.commit()

    def select_products(self):
        query = "SELECT product_id, name, price FROM products"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()

# 샘플 데이터 100개 생성 및 삽입
if __name__ == "__main__":
    db = ElectronicsDB()
    product_types = ["TV", "냉장고", "세탁기", "에어컨", "전자레인지", "청소기", "오븐", "노트북", "스피커", "모니터"]
    for i in range(1, 101):
        type_name = random.choice(product_types)
        model_num = f"{random.randint(100,999)}-{random.choice('ABCDE')}"
        name = f"{type_name} 모델 {model_num}"
        price = round(random.uniform(10000, 1000000), 2)
        db.insert_product(i, name, price)
    print("샘플 데이터 100개가 삽입되었습니다.")
    print(db.select_products()[:5])  # 일부 데이터 출력
    db.close()