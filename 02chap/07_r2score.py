import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from scipy import stats

obs_w_speed = np.array([2, 4, 7, 8, 9, 12, 18, 13, 12, 19, 8, 9])
mod_w_speed = np.array([3, 4, 6, 10, 15, 11, 12, 24, 20, 24, 9, 8])

# 1) define basic function 
def calculate_r2 (y_true, y_pred):                      # 단순 잔차 계산이라 오차 발생
    y_mean = np.mean(y_true)
    ss_tot = np.sum((y_true - y_mean)**2)
    ss_res = np.sum((y_true - y_pred)**2)
    r2 = 1 - (ss_res / ss_tot)
    return r2, ss_tot, ss_res
r2_1, ss_tot, ss_res = calculate_r2(obs_w_speed, mod_w_speed)

# 2) Using numpy library
corr_matrix = np.corrcoef(obs_w_speed, mod_w_speed)     # 피어슨 상관계수 행렬 구하기
corr = corr_matrix[0,1]                                 # 계수 r값 넣기. r=1, r=-1, r=0 관계없음
r2_2 = corr**2                                          # 0~1의 값을 가지며 1에 가까울 수록 강하다 

# 3) Using sklearn library 1
r2_3 = r2_score(obs_w_speed, mod_w_speed)               # 모델 돌린 후 값 넣어야 해서 오차 발생

# 4) Using sklearn library 2
model = LinearRegression()                              # 모델 호출
x = obs_w_speed.reshape(-1,1)                           # 1d -> 2d 배열로 변환 (n_samples, 1). 
y = mod_w_speed.reshape(-1,1)                           # -1 = 행수 자동으로 결정
model.fit(x, y)                                         # 학습
r2_4 = model.score(x, y)                

# 5) Using scipy Pearson's correlation coefficient 
r, p = stats.pearsonr(obs_w_speed, mod_w_speed)         # 결정계수 r, 상관관계 통계적 유의성 p
r2_5 = r**2

print(f"R-Squared (1:basic)         : {r2_1}")
print(f"R-Squared (2:numpy)         : {r2_2}")
print(f"R-Squared (3:sklearn)       : {r2_3}")
print(f"R-Squared (4:sklearnmodel)  : {r2_4}")
print(f"R-Squared (5:scipy Pearson) : {r2_5}")
print("-----Fixed R-Squared 3:sklearn-----")

x = obs_w_speed.reshape(-1, 1)
y = mod_w_speed

model = LinearRegression()
model.fit(x,y)
y_pred = model.predict(x)                               # 모델 직접 예측
r2_sklearn = r2_score(y, y_pred)
print("Re- R2score by sklearn : ", r2_sklearn)