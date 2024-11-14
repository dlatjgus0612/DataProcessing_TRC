import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

'''
1. contour, contourf
f(x, y) = x^2 + y^2 로 mesh grid 생성하고 시각화. 
'''

def f(x, y):
    return x**2 + y**2

xrange = np.linspace(-10, 10, 50)
yrange = np.linspace(-10, 10, 50)
xmesh, ymesh = np.meshgrid(xrange, yrange)
zmesh = f(xmesh, ymesh)

plt.contour(xmesh, ymesh, zmesh, levels=15)
plt.contourf(xmesh, ymesh, zmesh, levels = 15, cmap='jet')
plt.show()

'''
2. scipy 제공하는 grid data 이용

무작위 위치의 x,y -> z = x* exp(-x^2 -y^2)
x, y 이용하여 배열 -> 격자데이터 행렬 -> 각 격자에 대응하는 z 데이터를 보간. Interpolation 하는 방법.
'''
np.random.seed(1000)
sample_size = 50
x = np.random.uniform(-2, 2, sample_size)
y = np.random.uniform(-1.3, 1.3, sample_size)
z = x * np.exp(-x**2 - y**2)

# set grid for interpolation
grid_size = 100
x_range = np.linspace(np.min(x), np.max(x), grid_size)
y_range = np.linspace(np.min(y), np.max(y), grid_size)
X, Y = np.meshgrid(x_range, y_range)

# Interpolation with griddata
# np.c_[x, y] = 열 방향으로 병합해 (x, y) 좌표 쌍을 얻을 수 있게 함. 
# z는 함수 값. -> 이를 grid X, Y 에 대응. 
Z = griddata(np.c_[x, y], z, (X, Y), method='cubic')
# linear : 선형보간, nearest : 이웃할당, cubic : 삼차보간 

# plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(x, y, color='r', marker='+', alpha=0.5, s=36)
ax1.set_title("Sample Points")

# plot
contour1 = ax2.contour(X, Y, Z, levels=10, colors='k', linewidths=1, linestyles='--')
contour2 = ax2.contourf(X, Y, Z, levels=256, cmap='jet')
ax2.clabel(contour1, contour1.levels, inline=True, fontsize=8)
fig.colorbar(contour2, ax=ax2, shrink=0.7)
ax2.scatter(x, y, color='k', marker='+', alpha=0.5, s=36)
ax2.set_title("Contour Plot with Interpolated Data")
plt.show()