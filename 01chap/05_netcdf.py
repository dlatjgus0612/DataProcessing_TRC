import numpy as np
import xarray as xr
import os
import matplotlib.pyplot as plt  

# Set absolute path
work_path = '/mnt/c/Users/MML/sh/DataProcessing_TRC/'
input_file = 'data/CTD_station_P1_NLEG01-1_-_Nansen_Legacy_Cruise_-_2021_Joint_Cruise_2-1.nc'
out_file = 'data/ctd_data_set.csv'

# Use path join to create full file paths
f_name = os.path.join(work_path, input_file)
f_out_name = os.path.join(work_path, out_file)

# Load the dataset
ds = xr.open_dataset(f_name)

# Extract temperature values
temperature = ds['TEMP'].values

# Convert selected variables to a DataFrame
df = ds[['PRES', 'TEMP', 'PSAL']].to_dataframe()

# Save the DataFrame to a CSV file
df.to_csv(f_out_name)

# Plotting
fig1 = plt.figure()

# Temperature plot
ax1 = fig1.add_subplot(121)
ax1.plot(ds['TEMP'], ds['PRES'], 'bo-', markersize=2, linewidth=0.5)
ax1.set_ylim(ax1.get_ylim()[::-1])  # Reverse the y-axis
ax1.set_xlabel('Temperature (C)')
ax1.set_ylabel('Depth (m)')
plt.grid(True)
ax1.xaxis.set_label_position('top')  # Move the label to the top
ax1.xaxis.set_ticks_position('top')   # Move the ticks to the top

# Salinity plot
ax2 = fig1.add_subplot(122)
ax2.plot(ds['PSAL'], ds['PRES'], 'ro-', markersize=2, linewidth=0.5)
ax2.xaxis.set_label_position('top')
ax2.xaxis.set_ticks_position('top')
ax2.set_ylim(ax2.get_ylim()[::-1])  # Reverse the y-axis
plt.grid(True)
ax2.set_xlabel('Salinity (PSU)')

# Show the plots
plt.show()
