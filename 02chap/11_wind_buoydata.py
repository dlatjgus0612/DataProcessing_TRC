import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# File path
csv_file_path = 'data/ulsan_kma_buoy_2016.csv'
df = pd.read_csv(csv_file_path, names = ['station', 'date', 'wind_spd', 
                                         'wind_dir', 'air_pr', 'air_temp', 
                                         'sea_temp', 'max_W_H', 'sig_W_H', 
                                         'wave_peri', 'wave_dir'],
                                         skiprows=1, encoding="euc-kr")

# Define Wind direction & Wind Speed data
wind_direction = df['wind_dir']
wind_speed = df['wind_spd']

# Generate New Figure
fig = plt.figure(figsize=(15, 5))

# 1st subplot (polar coordinate _ scatter)
ax0 = fig.add_subplot(1, 3, 1, projection= 'polar')
ax0.set_theta_zero_location('N')                                        # degree 0 = North
ax0.set_theta_direction(-1)                                             # direction 반시계 
ax0.scatter(np.radians(wind_direction), wind_speed, s=10, alpha=0.3)

xticks = list(np.radians(np.arange(0, 360, 45)))
ax0.set_xticks(xticks)
ax0.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])       # label은 오른쪽으로 도는 군
ax0.set_title('Scatter plot of wind')

# 2nd subplot (wind direction _ scatter)
ax1 = fig.add_subplot(1, 3, 2)
df.plot(kind='scatter', x = 'wind_dir', y = 'wind_spd', alpha=0.5, ax = ax1)
ax1.set_xticks(np.arange(0, 360, 30))
ax1.set_xlabel('Wind direction (deg.)')
ax1.set_ylabel('Wind Speed (m/s)')

# 3rd subplot (wind speed _ histogram)
ax2 = fig.add_subplot(1, 3, 3)
df['wind_spd'].plot(kind='hist', color = 'skyblue', edgecolor = 'black', ax = ax2, bins = 25, density = True)
ax2.set_xlabel('Wind Speed (m/s)')
ax2.set_ylabel('Probability Density')
ax2.set_title('Histogram of Wind Speed')

plt.tight_layout()
plt.show()