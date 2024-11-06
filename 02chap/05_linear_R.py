import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats

obs_w_speed = np.array([2, 4, 7, 8, 9, 12, 18, 13, 12, 19, 8, 9])
mod_w_speed = np.array([3, 4, 6, 10, 15, 11, 12, 24, 20, 24, 9, 8])

# Correlation coefficient with linregress()
slope, intercept, r, p, stderr = scipy.stats.linregress(obs_w_speed, mod_w_speed)
line = f'Regression line: y = {slope:.2f}x + {intercept:.2f}, R ={r: .2f}'

fig, ax = plt.subplots()
ax.plot(obs_w_speed, mod_w_speed, linewidth=0, marker='s', label='Data Points')
ax.plot(obs_w_speed, intercept + slope*obs_w_speed, label=line)

plt.xlim([0,25])
plt.ylim([0,25])

ax.set_xlabel("Obs. data")
ax.set_ylabel("Model data")
ax.legend(facecolor = 'white')
plt.show()
