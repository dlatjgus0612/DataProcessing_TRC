import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes
from matplotlib import cm       # colormap module 

# Load data
file_path = 'data/wind_sample_data.csv'
df = pd.read_csv(file_path, names=['date', 'wind_speed', 'wind_direction', 'wind_dir_16'], skiprows=1)
df['wind_direction'] = pd.to_numeric(df['wind_direction'])          # df data translate to int or float type

# Calculate wind speed and direction components
theta_rad = np.deg2rad(270 - df.wind_direction)                     # degree to radian(270 - winddirection)
df['U_comp'] = df['wind_speed'] * np.cos(theta_rad)                 # Get U East component
df['V_comp'] = df['wind_speed'] * np.sin(theta_rad)                 # Get V West component

# Create canvas
fig, axs = plt.subplots(2, 2, figsize=(10, 10), dpi = 100, subplot_kw=dict(projection='windrose'))

# First row: Bar Windrose
ax0 = axs[0, 0]
ax0.bar(df.wind_direction, df.wind_speed, bins = np.arange(0, 10, 1),
        opening=0.8, edgecolor='white')
ax0.set_title('Bar Windrose')
ax0.set_legend()

# Second row: Box Windrose
ax0 = axs[0, 1]
ax0.box(df.wind_direction, df.wind_speed, bins = np.arange(0, 10, 1))
ax0.set_title('Box Windrose')
ax0.set_legend()

# Third row: Filled Windrose
ax0 = axs[1, 0]
ax0.contourf(df.wind_direction, df.wind_speed, bins = np.arange(0, 10, 1), cmap=cm.hot)
ax0.set_title('Filled Contour Windrose')
ax0.set_legend() 

# Fourth row: contour Windrose
ax0 = axs[1, 1]
ax0.contour(df.wind_direction, df.wind_speed, bins = np.arange(0, 10, 1), cmap=cm.hot)
ax0.set_title('Contour Windrose')
ax0.set_legend()

# Overall title
plt.tight_layout()
plt.show()
