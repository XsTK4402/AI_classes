import numpy as np
import cv2
import os

for i in range(2457, 2507):
    file_path = f"C:\\Users\\Matthew\\Desktop\\[test]50classes_origin800x800_25\\Endgame_{i}"
    # file_path = "C:\\Users\\Matthew\\Desktop\\Endgame_2457"
    file = os.listdir(file_path)
    preview = f"C:\\Users\\Matthew\\Desktop\\[test]50classes_800x800arguments\\Endgame_{i}"
    # preview = "C:\\Users\\Matthew\\Desktop\\Endgame_245777"

    for i in file:
        img = cv2.imread(os.path.join(file_path, i))
        square_size = np.random.choice([400, 500, 600])

        # 計算圖片中隨機選擇的正方形的左上角坐標
        h, w, c = img.shape
        x = np.random.randint(0, w - square_size)
        y = np.random.randint(0, h - square_size)

        # 裁剪正方形
        square = img[y:y+square_size, x:x+square_size]
        save_path = os.path.join(preview, f"crop_{i}")
        cv2.imwrite(save_path, square)