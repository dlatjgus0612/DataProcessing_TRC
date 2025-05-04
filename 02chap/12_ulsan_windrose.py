import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes

# Load data
file_path = 'data/ulsan_kma_buoy_2016.csv'
df = pd.read_csv(file_path, names = ['station', 'date', 'wind_spd', 
                                    'wind_dir', 'air_pr', 'air_temp', 
                                    'sea_temp', 'max_W_H', 'sig_W_H', 
                                    'wave_peri', 'wave_dir'],
                                     skiprows=1, encoding="euc-kr")
wind_direction = df['wind_dir']
wind_speed = df['wind_spd']

df.rename(columns={'wind_dir' : 'wind_direction'}, inplace=True)    # inplace : 원본 데이터프레임 자체를 수정
df.rename(columns={'wind_spd' : 'wind_speed'}, inplace=True)

# Create canvas
fig = plt.figure(figsize=(10,10), dpi=100)

# First row: bar Windrose
ax0 = fig.add_subplot(221, projection = 'windrose')
ax0.bar(wind_direction, wind_speed, normed = True, # normed는 windrose's bar에 만 사용. y축 정규화 되어 총 면적 합 = 1
        label = 'Wind Speed', edgecolor='white')
ax0.set_title('Wind rose of Ulasn Buoy (2016)', fontsize = 16)
ax0.set_legend()
ax0.set_label('Wind speed (m/s)')

# Second row: Scatter plot wind direction & speed
ax1 = fig.add_subplot(222)
ax1.scatter(wind_direction, wind_speed, alpha = 0.5, s = 4)         # s = symbol size
ax1.set_title('Scatter plot of Wind Direction vs Speed')
ax1.set_xlabel('Wind Direction (degrees)')
ax1.set_ylabel('Wind Speed (m/s)')

# Third row: Histogram of Wind Speed
ax2 = fig.add_subplot(223)
ax2.hist(df['wind_speed'], bins=20, edgecolor='black', alpha=0.7)
ax2.set_title('Histogram of Wind Speed')
ax2.set_xlabel('Wind Speed (m/s)')
ax2.set_ylabel('Number')

# Fourth row: Histogram of Wind Direction
ax3 = fig.add_subplot(224)
ax3.hist(df['wind_direction'], bins=20, edgecolor='black', alpha=0.7)
ax3.set_title('Histogram of Wind Direction')
ax3.set_xlabel('Wind Direction (degrees))')
ax3.set_ylabel('Number')

# Overall title
plt.tight_layout()
plt.show()
