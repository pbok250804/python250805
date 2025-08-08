# demoFile.py
#블럭을 선택하고 주석처리:ctrl + /
# #파일쓰기
# f= open("c:\\work\\test.txt", "wt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close()

# #파일읽기(raw string notation)
# f = open(r"c:\work\test.txt", "rt", encoding="utf-8")
# print(f.read())
# f.close()

#문자열 처리
strA = "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA))  # 문자열 길이
print(len(strB)) 
print(strB.capitalize())  # 첫 글자 대문자
print(strB.upper())  # 모두 대문자  
print("MBC2580".isalnum())  # 알파벳과 숫자만으로 구성
print("2580".isdecimal())  # 숫자로만 구성
data = "<<<  spam and ham  >>>"
result = data.strip("<> ")  # 양쪽 공백 제거
print(data)
print(result)
result2 = result.replace("spam", "spam egg")  # 문자열 치환
print(result2)
#리스트로 리턴
lst = result2.split()  # 공백으로 분리
print(lst)
#하나의 문자열로 합치기
print(":)".join(lst))  

#정규표현식
import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())  # 검색된 문자열 출력

#블럭: ctrl + / 
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())  # 검색된 문자열 출력

result = re.search("apple", "this is apple")
print(result.group())

result = re.search(r"\d{4}", "올해는 2025년입니다.")
print(result.group())

result = re.search(r"\d{5}", "우리 동네는 51200입니다.")
print(result.group())

