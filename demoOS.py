# demoOS.py 
from os.path import * 
from os import *
import glob 

fName = "sample.txt"
print(abspath(fName))    # Prints the absolute path of sample.txt
print(basename(r"c:\work\text.txt")) 

if (exists(r"c:\python310\python.exe")):
    print(getsize(r"c:\python310\python.exe"))  # Prints the size of python.exe
else:
    print("파일이 없음")
    
print("운영체제명:", name)  # Prints the name of the operating system
print("환경변수:", environ)  # Prints the environment variables
system("notepad.exe")  # Opens Notepad application

print(glob.glob("*.py"))  # Lists all Python files in the current directory
for item in glob.glob("*.py"):
    print(item)  # Prints each Python file found

    
