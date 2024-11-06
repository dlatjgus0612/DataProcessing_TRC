import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt  
from mpl_toolkits.basemap import Basemap

# Set absolute path
work_path = '/Users/imseohyeon/Documents/TRC/DataProcessing_TRC/'
input_file = 'data/KHOA_SCU_L4_Z004_Y01_U2023_EastSea.nc'


''' File Processing '''
f_name = work_path + input_file
ds = xr.open_dataset(f_name)                    # Open the NetCDF dataset

# f_data = xr.open_dataset(f_name)
# print(f_data)
# u_comp = f_data.data_vars['u']
# print(u_comp)

lat = ds["lat"].values                          # 위도.values 로 numpy 변환
lon = ds["lon"].values                          # 경도.values 로 numpy 변환

# Transpose the u and v velocity components
u_velocity = np.transpose(ds["u"].values)       # East-west velocity
v_velocity = np.transpose(ds["v"].values)       # North-south velocity


''' Convert to DataFrame for calculations '''
# Generate a grid for longitude and latitude
lon_grid, lat_grid = np.meshgrid(lon, lat)
# Create a DataFrame with longitude, latitude, and velocity components
data_frame = pd.DataFrame({
    "lon": lon_grid.ravel(),
    "lat": lat_grid.ravel(),
    "u_velocity": u_velocity.ravel(),           # Flatten to 1D
    "v_velocity": v_velocity.ravel()            # Flatten to 1D
})

''' Map plotting '''
fig, ax = plt.subplots(figsize=(10, 8))
m = Basemap(llcrnrlon=126,                      # Lower-left corner longitude
            llcrnrlat=33,                       # Lower-left corner latitude
            urcrnrlon=142,                      # Upper-right corner longitude
            urcrnrlat=48,                       # Upper-right corner latitude
            lon_0=134,                          # Central longitude
            lat_0=40,                           # Central latitude
            projection="merc",                  # Mercator projection
            resolution="h",                     # High resolution
            ax=ax)                              # Specify the axes object

# Fill continents and draw coastlines
m.fillcontinents(color="#D3D3D3", lake_color="lightblue")
m.drawcoastlines()


''' Calculate velocity of sea '''
# np.hypot (a, b) Calculate between a and b. 
# Calculate the horizontal speed using u and v components.
speeds = np.hypot(data_frame.u_velocity, data_frame.v_velocity)
 
# Plot arrows to represent velocity
X, Y = m(data_frame.lon, data_frame.lat)
quiver = m.quiver(X, Y, data_frame.u_velocity, data_frame.v_velocity, speeds, cmap="jet")


''' Add remaining elements '''
# Add color bar
cbar = plt.colorbar(quiver, 
                    ax=ax,
                    orientation='horizontal',
                    shrink=0.4, 
                    aspect=12, 
                    pad=0.04)

# Draw meridians and parallels
m.drawmeridians(np.arange(126, 142, 3), labels=[0, 0, 0, 1])  # Meridians with label on top
m.drawparallels(np.arange(33, 49, 3), labels=[1, 0, 0, 0])    # Parallels with label on left

# Set title and show the plot
plt.title("Ocean Current Vector Map using Quiver", fontsize=14)
plt.show()


