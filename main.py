import os

folder_path = "./files"
prefix = "new_"

for i, filename in enumerate(os.listdir(folder_path)):
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, f"{prefix}{i}.txt")
    os.rename(old_path, new_path)

print("✅ 모든 파일 이름이 변경되었습니다!")
