# demoOS.py
from os.path import *
from os import *
import glob

fName = 'sample.txt'
print(abspath(fName))
print(basename(r'C:\work\test.txt'))

if(exists(r'c:\python310\python.exe')):
    print(getsize(r'c:\python310\python.exe'))
else:
    print('파일이 없음')


print('운영체계명 :', name)
print('환경변수 :', environ)
system('notepad.exe')

print(glob.glob('*.py'))

for item in glob.glob('*.py'):
    print(item)


