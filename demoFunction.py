#  demoFunction.py

print('--- 함수 이름 해석 ---')
x = 5
def func(a):
    return a+x

# 호출
print(func(1))


def func2(a):
    x = 10
    return a+x

# 호출
print(func2(1))

# 키워드 인자
def connectURI(server, port):
    strURL = 'https://' + server + ':' + port
    return strURL

#  호출
print(connectURI('multi.com','80'))
print(connectURI(port='80', server='test.com'))