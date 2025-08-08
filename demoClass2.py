#개발자 클래스를 정의
class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def get_info(self):
        return f"Developer Name: {self.name}, Programming Language: {self.language}"

#인스턴스를 2개 생성
dev1 = Developer("Alice", "Python")
dev2 = Developer("Bob", "Java")

#정보 출력
print(dev1.get_info())
print(dev2.get_info())