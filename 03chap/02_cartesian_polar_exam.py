#import matplotlib
#matplotlib.use("TkAgg")  # 또는 "Qt5Agg"
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1000)

N = 150 
r = 2* np.random.rand(N)
theta = 2*np.pi *np.random.rand(N)
area = 200*r*2
colors = theta

fig, (ax1, ax2) = plt.subplots(1, 2, figsize= (12, 6),
                               subplot_kw={'projection': 'polar'})

ax1.scatter(theta, r, c=colors, s = area, cmap = 'hsv', alpha = 0.75)
ax1.set_title('Polar Axis')

ax2.scatter(theta, r, c=colors, s=area, cmap = 'hsv', alpha = 0.75)
ax2.set_theta_zero_location('N')        # set North 0 degree
ax2.set_theta_direction(-1)             # increase opposite clock 
plt.show()
