#import matplotlib
#matplotlib.use("TkAgg")  # 또는 "Qt5Agg"
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

'''
Cartesian Coordination
'''
x = np.arange(1, 12, 2)
y = np.arange(3, -3, -1)

# Cartesian 좌표계에서 산점도 그리기
ax1.scatter(x, y)
ax1.set_title('Cartesian Coordinates')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

'''
Polar Coordinate
Cartesian 좌표를 Polar 좌표로 변환
'''
r = np.sqrt(x**2 + y**2)                    # r = sqrt(x^2 + y^2)
theta = np.arctan2(y, x)                    # theta = arctan(y/x)

# Polar 좌표계에서 산점도 그리기
ax2 = plt.subplot(122, projection='polar')  # 'polar' projection을 사용
ax2.scatter(theta, r)                       # theta(각도)와 r(반지름) 그리기
ax2.set_title('Polar Coordinates')

plt.tight_layout()
plt.show()

# 그래프를 이미지로 저장 (GUI test)
#plt.savefig('data/mappingplot.png')  # 원하는 경로에 저장
