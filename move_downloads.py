import os
import shutil
import glob

download_dir = r'C:\Users\student\Downloads'
target_dirs = {
    'images': ['*.jpg', '*.jpeg'],
    'data': ['*.csv', '*.xlsx'],
    'docs': ['*.txt', '*.doc', '*.pdf'],
    'archive': ['*.zip']
}

# 다운로드 폴더 하단에 분류 폴더 생성
for folder in target_dirs.keys():
    target_path = os.path.join(download_dir, folder)
    if not os.path.exists(target_path):
        os.makedirs(target_path)

# 파일 이동
for folder, patterns in target_dirs.items():
    target_path = os.path.join(download_dir, folder)
    for pattern in patterns:
        for file_path in glob.glob(os.path.join(download_dir, pattern)):
            dest_path = os.path.join(target_path, os.path.basename(file_path))
            shutil.move(file_path, dest_path)
            print(f"{file_path} -> {dest_path}")