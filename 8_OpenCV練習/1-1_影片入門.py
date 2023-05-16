import cv2
import numpy as np

vc = cv2.VideoCapture("IronMan3.mp4")  # 開啟檔案
# print(vc.get(cv2.CAP_PROP_FPS)) #獲得偵率

total_frame = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))  # 獲得總偵數
# print(total_frame)

# 用while方式開啟影片檔案
# if vc.isOpened():
#     open, frame = vc.read()
# else:
#     open = False

# while open:
#     ret, frame = vc.read()
#     if frame is None:
#         break
#     if ret == True:
#         # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow("result", frame)
#         if cv2.waitKey(1) & 0xFF == 27:
#             break

# 用for方式開啟影片檔
for idx in range(total_frame)[::22]:
    vc.set(cv2.CAP_PROP_POS_FRAMES, idx)  # 設置偵數為當前偵數
    ret, frame = vc.read()
    height, width, layers = frame.shape  # 當前frame的長、寬、像素的顏色通道數
    size = (width, height)

    if frame is not None:
        file_name = 'IronMan3_1FPS\{:03d}.jpg'.format(idx//23+1)
        cv2.imwrite(file_name, frame)

    print("\rprocess: {}/{}".format(idx//23+1 , (total_frame/23)), end = '')

vc.release()
cv2.destroyAllWindows
