import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




dict_savename = {"d5_normal_training":"d5normal_", "d1_out_training" : "d1out_", "d2_in_training" : "d2in_", "d3_noise_training" : "d3noise_", "d4_other_training" : "d4other_"}
samplename =  f"../data/bms2/Training/training/d5_normal_training.csv"
df_sample = pd.read_csv(samplename)
df_keys = df_sample.keys()


keys_hz = []
for k in df_keys:
    if "HZ" in k:
        keys_hz.append(k)


for d_name in dict_savename.keys():
    print(d_name)
    print(dict_savename[d_name])
    
    filename =  f"../data/bms2/Training/training/{d_name}.csv"

    df = pd.read_csv(filename)

    # 데이터 확인
    # print(df.head())        # 상위 5개 행
    # print(df.columns)       # 컬럼명 출력
    print(df.shape)         # (행 수, 열 수)

    # bar 형 그래프 확인 후 저장
    n = len(df['10HZ'])

    # 2. 데이터를 Numpy array에 담아서 확인
    rows, cols = len(df['10HZ']), len(keys_hz)
    arr_d = np.zeros((rows, cols), dtype=np.float64)
    
    for i in range(len(df['10HZ'])):
        for j, k in enumerate(keys_hz):
            arr_d[i, j] = df[k][i]

   
    print(f"{dict_savename[d_name]} : {n}")
    for i in range(n):
        path = dict_savename[d_name]
        if not os.path.exists(path):
            print(f"{path} 가 없어서 새로 만듭니다.")
            os.makedirs(path)    
        filename = f"{path}/{dict_savename[d_name]}_{i}.png"
        
        if os.path.exists(filename):
            continue
        
        if (i+1)%10 ==0:
            print(f"{(i+1)} saving")
        
        plt.figure(figsize=(12, 4))
        plt.bar(keys_hz,arr_d[i], width=1.0, color="steelblue")
        plt.title(f"Spectrum of {d_name} lrate = {df["lrate"][i]}%   leak level = {df["llevel"][i]}")
        plt.xlabel("HZ")
        plt.ylabel("Value")
            
        plt.savefig(filename, dpi=150, bbox_inches="tight")
        plt.close()
    
    
