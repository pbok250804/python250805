# db1.py
import sqlite3

# 연결객체를 리턴(메모리 임시)
# con = sqlite3.connect(':memory:')

# 파일에 저장
con = sqlite3.connect(r"c:\work\sample.db")

# 커서객체를 리턴
cur = con.cursor()

# 테이블 생성
cur.execute("create table PhoneBook (name text, phone text);")

# 데이터 삽입
cur.execute("insert into PhoneBook values ('홍길동', '123-4567');")

# 입력 파라미터 처리
name = '이순신'
phone = '987-6543'
cur.execute("insert into PhoneBook values (?, ?);", (name, phone))

# 여러건 입력
datalist = (("김길동","010-1111"), ("전우치","001-3333"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

# 데이터 조회
cur.execute("select * from PhoneBook;")  
for row in cur:
    print(row)

# 작업을 정상적으로 종료
con.commit()