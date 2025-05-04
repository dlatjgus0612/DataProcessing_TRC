"""
This script downloads Sea Surface Temperature (SST) and ice concentration (ICE) data, 
processes the data for a specified date, and generates a visualization using a map projection.

Args:
    date (datetime): The date for which the SST and ice data should be visualized.
    sst_url (str): URL to download SST data in NetCDF format.
    ice_url (str): URL to download ice concentration data in NetCDF format.
    sst_file (str): Local path to save the downloaded SST data.
    ice_file (str): Local path to save the downloaded ice concentration data.

Returns:
    None: The function downloads the data, processes it, and plots the results.
    
Raises:
    requests.exceptions.RequestException: If there is an error in downloading the data.
    KeyError: If the expected data variable is not found in the NetCDF file.
"""

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset, date2index
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import requests
from tqdm import tqdm
import os

def download_file_with_progress(url, local_filename):
    # Check already Exist files
    if os.path.exists(local_filename):
        print(f"{local_filename} already exists, skipping download.")
        return local_filename                                       # if exist, return file direct
    
    response = requests.get(url, stream=True)                       # Enable streaming
    total_size = int(response.headers.get('content-length', 0))     # Total file size
    chunk_size = 8192  # Size of chunks to download
    
    with open(local_filename, 'wb') as f:
        # Use tqdm to show a progress bar 
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=local_filename) as pbar:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:                                           # Filter out keep-alive chunks
                    f.write(chunk)
                    pbar.update(len(chunk))                         # Update progress bar
    return local_filename

# Date to plot
date = datetime(2007, 12, 15, 0)

# URLs for SST and ice datasets
sst_url = f"https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.{date.year}.nc"
ice_url = f"https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/icec.day.mean.{date.year}.nc"

# Local file paths
sst_file = "data/sst.day.mean.nc"
ice_file = "data/icec.day.mean.nc"

# Download SST and ice data
download_file_with_progress(sst_url, sst_file)
dataset = Dataset(sst_file)                             # Open NetCDF file for SST data
timevar = dataset.variables['time']                     # Access time variable
timeindex = date2index(date, timevar)                   # Get index for the specified date
sst = dataset.variables['sst'][timeindex, :].squeeze()  # Extract SST data and remove singleton dimensions
dataset.close()

download_file_with_progress(ice_url, ice_file)
dataset = Dataset(ice_file)                             # Open NetCDF file for ice data
ice = dataset.variables['icec'][timeindex, :].squeeze() # Extract ice concentration data
lats = dataset.variables['lat'][:]                      # Get latitude data (1D array)
lons = dataset.variables['lon'][:]                      # Get longitude data (1D array)
dataset.close()

# Adjust latitude and longitude for grid box centers
latstep, lonstep = np.diff(lats[:2]), np.diff(lons[:2]) # Calculate grid spacing
lats = np.append(lats - 0.5 * latstep, lats[-1] + 0.5 * latstep)  # Adjust latitude
lons = np.append(lons - 0.5 * lonstep, lons[-1] + 0.5 * lonstep)  # Adjust longitude
lons, lats = np.meshgrid(lons, lats)                    # Create 2D grid for lons and lats

# Create figure and map
fig = plt.figure()
ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])

# Initialize Basemap projection
m = Basemap(projection='kav7', lon_0=0, resolution=None) # Kacrayskiy VII projection
m.drawmapboundary(fill_color='0.3')                      # Draw map boundary with dark gray fill
im1 = m.pcolormesh(lons, lats, sst, shading='flat', cmap=plt.cm.jet, latlon=True)  # Plot SST
im2 = m.pcolormesh(lons, lats, ice, shading='flat', cmap=plt.cm.gist_gray, latlon=True)  # Plot ice concentration
m.drawparallels(np.arange(-90., 99., 30.))               # Draw parallels (latitudes)
m.drawmeridians(np.arange(-180., 180., 60.))             # Draw meridians (longitudes)

# Add colorbar and title
cb = m.colorbar(im1, "bottom", size="5%", pad="2%")  # Add colorbar for SST
ax.set_title(f'SST and ICE analysis for {date}')  # Add title with date

# Display the plot
plt.show()
