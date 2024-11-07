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




# 2nd subplot (wind direction _ scatter)

# 3rd subplot (wind speed _ histogram)