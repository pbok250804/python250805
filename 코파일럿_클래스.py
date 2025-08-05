class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
def test_person():
    p = Person(1, "홍길동")
    assert p.id == 1
    assert p.name == "홍길동"

def test_person_printInfo(capsys=None):
    p = Person(2, "김철수")
    p.printInfo()
    if capsys:
        captured = capsys.readouterr()
        assert "ID: 2, Name: 김철수" in captured.out

def test_manager():
    m = Manager(3, "이영희", "팀장")
    assert m.id == 3
    assert m.name == "이영희"
    assert m.title == "팀장"

def test_manager_printInfo(capsys=None):
    m = Manager(4, "박민수", "부장")
    m.printInfo()
    if capsys:
        captured = capsys.readouterr()
        assert "ID: 4, Name: 박민수, Title: 부장" in captured.out

def test_employee():
    e = Employee(5, "최지우", "Python")
    assert e.id == 5
    assert e.name == "최지우"
    assert e.skill == "Python"

def test_employee_printInfo(capsys=None):
    e = Employee(6, "정우성", "Java")
    e.printInfo()
    if capsys:
        captured = capsys.readouterr()
        assert "ID: 6, Name: 정우성, Skill: Java" in captured.out

def test_inheritance_manager():
    m = Manager(7, "김유신", "이사")
    assert isinstance(m, Person)

def test_inheritance_employee():
    e = Employee(8, "유관순", "C++")
    assert isinstance(e, Person)

def test_manager_overriding(capsys=None):
    m = Manager(9, "장보고", "대표")
    m.printInfo()
    if capsys:
        captured = capsys.readouterr()
        assert "Title: 대표" in captured.out

def test_employee_overriding(capsys=None):
    e = Employee(10, "이순신", "Go")
    e.printInfo()
    if capsys:
        captured = capsys.readouterr()
        assert "Skill: Go" in captured.out

# pytest로 실행 시 capsys를 자동으로 주입받아 테스트할
if __name__ == "__main__":
    p = Person(1, "홍길동")
    p.printInfo()

    m = Manager(2, "김철수", "팀장")
    m.printInfo()

    e = Employee(3, "이영희", "Python")