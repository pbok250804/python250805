import os
import shutil
import glob

# 다운로드 폴더 경로
download_dir = r"C:\Users\student\Downloads"

# 이동할 폴더 경로
dest_dirs = {
    "images": ["*.jpg", "*.jpeg"],
    "data": ["*.csv", "*.xlsx"],
    "docs": ["*.txt", "*.doc", "*.pdf"],
    "archive": ["*.zip"]
}

for folder, patterns in dest_dirs.items():
    target_dir = os.path.join(download_dir, folder)  # 다운로드 폴더 하단에 생성
    # 폴더가 없으면 생성
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    # 각 패턴별로 파일 이동
    for pattern in patterns:
        files = glob.glob(os.path.join(download_dir, pattern))
        for file_path in files:
            try:
                shutil.move(file_path, target_dir)
                print(f"{os.path.basename(file_path)} → {target_dir} 이동 완료")
            except Exception as e:
                print(f"{os.path.basename(file_path)} 이동 실패: {e}")