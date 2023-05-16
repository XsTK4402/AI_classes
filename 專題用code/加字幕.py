import os
import random
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

for i in range(2457, 2507):
# 设置原始图像文件夹路径和新文件夹路径
    org_path = f"C:\\Users\\Matthew\\Desktop\\[test]50classes_origin800x800_25\\Endgame_{i}"
    new_path = f"C:\\Users\\Matthew\\Desktop\\[test]50classes_800x800arguments\\Endgame_{i}"

    # 获取原始文件夹内的所有图像文件名
    org_img_list = os.listdir(org_path)

    for i in org_img_list:
        cur_img = cv2.imread(os.path.join(org_path, i))

        # 添加文本到图像
        text = ['This is mememaster', '破梗之局製作', "我就feel,應該random加入some字"]
        random_int = random.randint(0, 2)
        font = ImageFont.truetype("msjh.ttc", 50, encoding='utf-8')
        img_pil = Image.fromarray(cv2.cvtColor(cur_img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        thickness = 20
        color = (255, 255, 255)
        text_width, text_height = font.getsize(text[random_int])
        x, y = (cur_img.shape[1] - text_width)//2, 50
        draw.text((x, y),  text[random_int], font=font, fill=color)
        cur_img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

        # 将修改后的图像保存到新文件夹下
        new_img_path = os.path.join(new_path, f"font_{i}")
        cv2.imwrite(new_img_path, cur_img)