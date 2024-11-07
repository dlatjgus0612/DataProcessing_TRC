import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

# Load data
file_path = 'data/wind_sample_data.xlsx'
df = pd.read_excel(file_path, names=['date', 'wind_speed', 'wind_direction', 'wind_dir_16'], skiprows=1)

# Convert date format : pd to df
df['date'] = pd.to_datetime(df['date'])

# Calculate wind speed and direction components
df['wind_direction'] = pd.to_numeric(df['wind_direction'])          # df data translate to int or float type
theta_rad = np.deg2rad(270 - df.wind_direction)                     # degree to radian(270 - winddirection)
df['U_comp'] = df['wind_speed'] * np.cos(theta_rad)                 # Get U East component
df['V_comp'] = df['wind_speed'] * np.sin(theta_rad)                 # Get V West component

# Create canvas
fig = plt.figure(figsize=(14, 9))

# First row: Combined graph
ax0 = fig.add_subplot(2, 1, 1)
ax0.quiver(df.date, 0, df.U_comp, df.V_comp, color='k', units='y',  # Draw the arrow for vectors direction, size
        scale_units='y', scale=1, headlength=1, headaxislength=1, width=0.02, alpha=1.0)
ax0.set_ylabel('Wind Speed (m/s)', fontsize=10)
ax0.grid(True)
ax0.tick_params(axis='both',                                        # Define axis's tick style. both means x, y axis
                which='major',                                      # Major like date, interger..
                direction='out',                                    # Look for Out direction
                length=2, width=1)
ax0.set_xlim(df.date.iloc[0], df.date.iloc[-1])                     # 'data' row's first data to last data
ax0.set_ylim([-3, 3])
ax0.xaxis.set_major_locator(mdates.MonthLocator(interval=1))        # Set major's tick location - Month
ax0.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))     # Set major's tick format - date 'YYYY-MM-DD'

# Second row: Three graphs
# Scatter plot 2x3 격자의 4번째 
ax1 = fig.add_subplot(2, 3, 4)      
df.plot(kind='scatter', x='U_comp', y='V_comp', alpha=0.35, ax=ax1) # alpha 투명도 -> 겹칠 때 덜 두껍게 보임
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.axhline(y=0, color='b', linewidth=1)                            # add y axis. horizontal line
ax1.axvline(x=0, color='b', linewidth=1)                            # add x axis. vertical line
ax1.set_title('Scatter plot of wind data')

# Wind speed histogram 2x3 격자의 5번째
ax2 = fig.add_subplot(2, 3, 5)     
df['wind_speed'].plot(kind='hist', color='skyblue', edgecolor='black', ax=ax2, bins=10)
ax2.set_ylabel('number')
ax2.set_xlabel('Wind speed (m/s)')
ax2.set_title('Histogram of Wind speed')

# Wind direction histogram 2x3 격자의 6번째
ax3 = fig.add_subplot(2, 3, 6)  
df['wind_direction'].plot(kind='hist', color='skyblue', edgecolor='black', ax=ax3, bins=16)
ax3.set_ylabel('number')
ax3.set_xlabel('Wind direction (deg.)')
ax3.set_title('Histogram of Wind direction')

# Overall title
plt.suptitle("This graph helps to understand the wind data", fontsize=16)
plt.show()
