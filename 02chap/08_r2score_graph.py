import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
import scipy.stats

obs_w_speed = np.array([2, 4, 7, 8, 9, 12, 18, 13, 12, 19, 8, 9])
mod_w_speed = np.array([3, 4, 6, 10, 15, 11, 12, 24, 20, 24, 9, 8])
  

# 1) R - Correlation coefficient with linregress()
slope, intercept, r, p, stderr = scipy.stats.linregress(obs_w_speed, mod_w_speed)
line = f'Regression line: y = {slope:.2f}x + {intercept:.2f}'

# 2) R2 (correlation)
corr_matrix = np.corrcoef(obs_w_speed, mod_w_speed)             # 피어슨 상관계수 행렬 구하기
corr = corr_matrix[0,1]                                         # 계수 r값 넣기. r=1, r=-1, r=0 관계없음
r2_corr = corr**2                                               # 0~1의 값을 가지며 1에 가까울 수록 강하다 

# 3) R2 (sklearn model score)
r2_sklearn = r2_score(obs_w_speed, mod_w_speed)                 # 모델 돌린 후 값 넣어야 해서 오차 발생

# 4) RMSE = MSE의 제곱근
RMSE = np.sqrt(mean_squared_error(obs_w_speed, mod_w_speed))  

# Create a plot
fig, ax = plt.subplots(figsize=(10,8))
ax.plot(obs_w_speed, mod_w_speed, linewidth = 0, marker='s', label = 'Data Points')
ax.plot(obs_w_speed, slope*obs_w_speed + intercept, label=line)
plt.xlim([0,25])
plt.ylim([0,25])
ax.set_xlabel("Obs. data")
ax.set_ylabel("Model data")

# Customize the legend
legend_text = f"R = {r:.2f}\nR2 (corr) = {r2_corr:.2f} \nR2 (sklearn) = {r2_sklearn:.2f}\nRMSE = {RMSE:.2f}"
ax.text(0.05, 0.95, legend_text,
        transform = ax.transAxes, 
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.legend()
plt.tight_layout()
plt.show()

print(f"R = {r:.2f} \nR2 (corr) = {r2_corr:.2f} \nR2 (sklearn) = {r2_sklearn:.2f} \nRMSE = {RMSE:.2f}")