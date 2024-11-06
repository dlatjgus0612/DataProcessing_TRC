import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, root_mean_squared_error

obs_w_speed = np.array([2, 4, 7, 8, 9, 12, 18, 13, 12, 19, 8, 9])
mod_w_speed = np.array([3, 4, 6, 10, 15, 11, 12, 24, 20, 24, 9, 8])

# define rmse function 
def rmse(y, y_pred):
    return np.sqrt(np.mean(np.square(y - y_pred)))

RMSE_1 = rmse(obs_w_speed, mod_w_speed)
RMSE_2 = root_mean_squared_error(obs_w_speed, mod_w_speed)
RMSE_3 = mean_squared_error(obs_w_speed, mod_w_speed, squared=False)        #제곱근이 반환되는 옵션.
print(RMSE_1, RMSE_2, RMSE_3)

# 계수 계산 for linear regression 
coefficients = np.polyfit(obs_w_speed, mod_w_speed, 1)                      #다항식 계산. 1은 1차다항식.
linear_fit = np.poly1d(coefficients)                                        #기울기, 절편 넣어주면 방정식만듦.

fig, ax = plt.subplots()
plt.plot(obs_w_speed, mod_w_speed, 'bo', label='wind speed')
plt.plot(obs_w_speed, linear_fit(obs_w_speed), 'r-', label= 'Linear fit')
plt.xlim([0,25])
plt.ylim([0,25])
plt.xlabel("Observed wind speed")
plt.ylabel("Modeled wind speed")
plt.legend()
plt.show()
