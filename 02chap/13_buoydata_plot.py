import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data
file_path = 'data/ulsan_kma_buoy_2016.csv'
df = pd.read_csv(file_path, names = ['station', 'date', 'wind_spd', 
                                         'wind_dir', 'air_pr', 'air_temp', 
                                         'sea_temp', 'max_W_H', 'sig_W_H', 
                                         'wave_peri', 'wave_dir'],
                                         skiprows=1, encoding="euc-kr")
df['date'] = pd.to_datetime(df['date'])                  # date to datetime frame

# Calculate wind speed and direction components
theta_rad = np.deg2rad(270 - df.wind_dir)                # degree to radian(270 - winddirection)
u_wind = df.wind_spd * np.cos(theta_rad)                 # Get U East component
v_wind = df.wind_spd * np.sin(theta_rad)                 # Get V West component

# Create canvas
fig = plt.figure(figsize=(10, 6))
plt.suptitle("Ocean wind, Temperature and Wave of Ulsan Buoy", fontsize=16)

ax0 = fig.add_subplot(4, 1, 1)                           # Wind Speed and Direction
ax1 = fig.add_subplot(4, 1, 2)                           # Ocean_Temperature
ax2 = fig.add_subplot(4, 1, 3)                           # Wave_max
ax3 = fig.add_subplot(4, 1, 4)                           # Wave_sig

# Wind Speed and Direction
ax0.quiver(df.date, 0, u_wind, v_wind,
           color='k', units='y', scale_units='y',       # arrowcolor = black / 단위는 y축 기준 / scale 기준 y 단위
           scale=1, headlength=1, headaxislength=1,     # arrow 크기 비율.(작을 수록 길다) / 화살표머리길이 / 화살표머리축길이
           width=0.02, alpha=1.0)                       # arrow width / 투명도
ax0.set_ylabel('Wind Speed(m/s)', fontsize=10)
ax0.grid(True)
ax0.tick_params(axis='both', which='major', direction='out', length=2, width=1)
ax0.set_xlim(df.date[0], df.date[len(df.date)-1])
ax0.set_ylim([-15, 15])

ax0.xaxis.set_major_locator(mdates.MonthLocator(interval=1))    # tick by month
ax0.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Ocean_Temperature
ax1.plot(df.date, df.sea_temp, color='blue')
ax1.set_ylabel('Sea Temp. (°C)', fontsize=10)           #원시 문자열말고 그냥 표시함.
ax1.grid(True)
ax1.tick_params(axis='both', which='major', direction='out', length=2, width=1)
ax1.set_xlim(df.date[0], df.date[len(df.date)-1])
ax1.set_ylim([5, 35])

# Wave_max
ax2.plot(df.date, df.max_W_H, color='red')
ax2.set_ylabel('Max Wave Height (m)', fontsize=10)
ax2.grid(True)
ax2.tick_params(axis='both', which='major', direction='out', length=2, width=1)
ax2.set_xlim(df.date[0], df.date[len(df.date)-1])
ax2.set_ylim([0, 15])

# Wave_sig
ax3.plot(df.date, df.sig_W_H, color='pink')
ax3.set_ylabel('Sig. Wave Height (m)', fontsize=10)
ax3.set_xlabel('Date', fontsize=10)
ax3.grid(True)
ax3.tick_params(axis='both', which='major', direction='out', length=2, width=1)
ax3.set_xlim(df.date[0], df.date[len(df.date)-1])
ax3.set_ylim([0, 15])

# Overall layout adjustments
plt.tight_layout() 
plt.show()
