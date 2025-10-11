"""
Normalize 위해서 MAX 항목 중 최대값을 찾아야함


"""
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# dict_savename = {"d5_normal_training":"d5normal_", "d1_out_training" : "d1out_", "d2_in_training" : "d2in_", "d3_noise_training" : "d3noise_", "d4_other_training" : "d4other_"}
dict_savename = {"d2_in_training" : "d2in_", "d3_noise_training" : "d3noise_", "d4_other_training" : "d4other_"}

samplename =  f"../data/bms2/Training/training/d5_normal_training.csv"
df_sample = pd.read_csv(samplename)
df_keys = df_sample.keys()

# for k in df_keys:
#     print(k)

x_hz = []
y_hz = []
x_max = []
y_max = []

# x축 Label 추출 HZ, MAX (NOTE : 이렇게 매번 샘플 파일 하나 열어서 하는게 효율적인 걸까?)
for k in df_keys: # 숫자 순서대로 HZ, MAX 저장되는지 확인 필요
    if "HZ" in k:
        x_hz.append(k)

    elif "MAX" in k:
        x_max.append(k)

# 모든 파일별로 Figure 그리는 코드
for d_name in dict_savename.keys():
    print(d_name)
    print(dict_savename[d_name])
    
    filename =  f"../data/bms2/Training/training/{d_name}.csv"

    df = pd.read_csv(filename)

    n = len(df['10HZ'])
    # n = 1000

    # HZ 데이터를 Numpy array에 담아서 확인(NOTE : Numpy가 맞는지 List 가 맞는지)
    rows, cols = n, len(x_hz)
    arr_hz = np.zeros((rows, cols), dtype=np.float64)

    # MAX 데이터 추출
    rows, cols = n, len(x_max)
    arr_max = np.zeros((rows, cols), dtype=np.float64)
    
    # NOTE Normalize 위한 변수 1(2번은 일반 HZ 에서 MAX 값 찾는 방법)
    key_norm_max = ['MAX1', 'MAX3', 'MAX5', 'MAX7', 'MAX9','MAX11', 'MAX13', 'MAX15', 'MAX17', 'MAX19']

    for i in range(n):

        # Normalize 위해서 최댓값 정해줌
        norm_max = -10000.0

        for key_ in x_hz:
            if norm_max < float(df[key_][i]):
                norm_max =  df[key_][i]

        for j, k in enumerate(x_hz):
            arr_hz[i, j] = df[k][i]/norm_max

        for j_max, k in enumerate(x_max):
            arr_max[i, j_max] = df[k][i]/norm_max

    # Figure 그리는 부분
    for i in range(n):
        path = dict_savename[d_name]
        if not os.path.exists(path):
            print(f"{path} 가 없어서 새로 만듭니다.")
            os.makedirs(path)    
        filename = f"{path}/{dict_savename[d_name]}_{i}.png"
        filename_max = f"{path}/{dict_savename[d_name]}_max_{i}.png"
        
        if os.path.exists(filename):
            continue
        
        if (i+1)%10 ==0:
            print(f"{(i+1)} saving")

        str_max = f"{df['MAX0'][i]} {df['MAX1'][i]}/{df['MAX2'][i]} {df['MAX3'][i]}/{df['MAX4'][i]} {df['MAX5'][i]}/{df['MAX6'][i]} {df['MAX7'][i]}/{df['MAX8'][i]} {df['MAX9'][i]}/{df['MAX10'][i]} {df['MAX11'][i]} / {df['MAX12'][i]} {df['MAX13'][i]} / {df['MAX14'][i]} {df['MAX15'][i]} / {df['MAX14'][i]} {df['MAX17'][i]} / {df['MAX18'][i]} {df['MAX19'][i]}"

        # MAX 값 포함하지 않음
        plt.figure(figsize=(12, 4))
        plt.bar(x_hz, arr_hz[i], width=1, color="steelblue", alpha = 1)

        plt.title(f"Spectrum of {d_name} lrate = {df["lrate"][i]}%   leak level = {df["llevel"][i]}")
        # plt.xlabel("HZ")
        plt.xticks(x_hz[::100])
        plt.xlabel(str_max)
        plt.ylabel("Value")

        plt.savefig(filename, dpi=150, bbox_inches="tight")
        plt.close()

        # MAX 값 포함
        plt.figure(figsize=(12, 4))
        plt.bar(x_hz, arr_hz[i], width=1, color="steelblue", alpha = 1)

        # MAX 데이터들은 변환 필요 : 
        x_max_new = []
        y_max_new = []
        for i_max in range(len(arr_max[i])//2):
            x_max_new.append(f"{int(arr_max[i][2*i_max])}HZ")
            y_max_new.append(arr_max[i][2*i_max+1])
        plt.bar(x_max_new, y_max_new, width=2.0, color="steelblue", alpha = 0.4)
           
        plt.title(f"Spectrum of {d_name} lrate = {df["lrate"][i]}%   leak level = {df["llevel"][i]}")
        # plt.xlabel("HZ")
        plt.xticks(x_hz[::100])
        plt.xlabel(str_max)
        plt.ylabel("Value")

        plt.savefig(filename_max, dpi=150, bbox_inches="tight")
        plt.close()