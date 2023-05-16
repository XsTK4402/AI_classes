import h5py
import numpy as np
from sklearn.metrics import confusion_matrix

# 讀取HDF5檔案
with h5py.File('C:\\Users\\Matthew\\Desktop\\測試用h5檔案\\keras_model.h5', 'r') as f:
    
    # f.visit(print)
    # print(list(f.keys()))
    
    # 從檔案中讀取真實標籤和預測標籤
    y_true = np.array(f['model_weights'])
    y_pred = np.array(f['model_weights'])
    
# 製作混淆矩陣
cm = confusion_matrix(y_true, y_pred)
print(cm)