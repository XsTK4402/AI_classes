import os
import shutil

def copy_files(src_folder):
    # 遍歷資料夾內的所有檔案
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # 構造新的檔案路徑和名稱
            src_path = os.path.join(root, file)
            dst_path = os.path.join(root, f"new_{file}")
            # 複製檔案
            shutil.copy2(src_path, dst_path)

# 呼叫函數，將檔案複製並貼在原資料夾內
for i in range(2457, 2507):
    copy_files(f'C:\\Users\\Matthew\\Desktop\\800x800_10分鏡100張\\Endgame_{i}')
