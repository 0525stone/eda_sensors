import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dict_savename = {"d5_normal_training":"d5normal_", "d1_out_training" : "d1out_", "d2_in_training" : "d2in_", "d3_noise_training" : "d3noise_", "d4_other_training" : "d4other_"}

samplename =  f"../data/bms2/Training/training/d5_normal_training.csv"
df_sample = pd.read_csv(samplename)
df_keys = df_sample.keys()

for k in df_keys:
    print(k)

x_hz = []
y_hz = []
x_max = []
y_max = []

for k in df_keys: # 숫자 순서대로 HZ, MAX 저장되는지 확인 필요
    if "HZ" in k:
        # print(k)
        x_hz.append(k)
        y_hz.append(df_sample[k][n_column])

    elif "MAX" in k:
        # print(k)
        x_max.append(k)
        y_max.append(df_sample[k][n_column])

keys_hz = []
for k in df_keys:
    if "HZ" in k:
        keys_hz.append(k)



for d_name in dict_savename.keys():
    print(d_name)
    print(dict_savename[d_name])
    
    filename =  f"../data/bms2/Training/training/{d_name}.csv"

    df = pd.read_csv(filename)

    n = len(df['10HZ'])

    # HZ 데이터를 Numpy array에 담아서 확인
    rows, cols = len(df['10HZ']), len(keys_hz)
    arr_d = np.zeros((rows, cols), dtype=np.float64)
    
    for i in range(len(df['10HZ'])):
        for j, k in enumerate(keys_hz):
            arr_d[i, j] = df[k][i]

    # MAX 데이터 추출
    
