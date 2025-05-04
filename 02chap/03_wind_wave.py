import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'data/KMA_Ulsan_buoy_2021_2023.csv'

df = pd.read_csv(file_path, sep=',', 
                 names = ['ID', 'obs_date', 'wind_speed', 'wind_direction', 
                 'air_pr', 'air_temp', 'water_temp',
                 'max_wave_hi', 'sig_wave_ht', 'wave_period', 'wave_direction'],
                 encoding="EUC-KR", skiprows= 1)
df['date'] = pd.to_datetime(df['obs_date'])     # translate data to datetime frame **
wind_speed = df['wind_speed']
wave_max = df['max_wave_hi']

fig, ax1 = plt.subplots(figsize = (10, 6))

# line1 for wind speed
line1 = ax1.plot(df.date, wind_speed, 'b.', markersize = 2, 
                 alpha = 0.40, label = "wind speed (m/sec)")
ax1.set_ylabel('Wind speed (m/s)', color = 'blue', fontsize = 12)

#line2 for wave max
ax2 = ax1.twinx()                               # Means share X ax for Y2 graph **
line2 = ax2.plot(df.date, wave_max, 'r.', markersize = 2, 
                 label = "Max. Wave Hight")
ax2.set_ylabel('Max. Wave Hight (m)', color = 'red', fontsize = 12)
ax2.grid(True)
ax2.tick_params(axis = "both", which = 'major', direction = 'out', length = 2, width = 1)

plt.show()
