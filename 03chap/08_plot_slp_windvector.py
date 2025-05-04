"""
This script visualizes Sea Level Pressure (SLP) and wind vectors for a specified date
using data from the NOAA OpenDAP server.

Classes:
    SLPWindVisualizer: Handles downloading, processing, and visualizing SLP and wind vector data.
"""

import numpy as np 
import matplotlib.pyplot as plt
import datetime
from mpl_toolkits.basemap import Basemap, shiftgrid
from netCDF4 import Dataset

# Specify date to plot
yyyy=1993; mm=3; dd=14; hh=0
date = datetime.datetime(yyyy,mm,dd,hh)

# set OpenDAP server URL.
URLbase="https://www.ncei.noaa.gov/thredds/dodsC/model-cfs_reanl_6h_pgb/"
URL=URLbase+"%04i/%04i%02i/%04i%02i%02i/pgbh00.gdas.%04i%02i%02i%02i.grb2" %\
            (yyyy,yyyy,mm,yyyy,mm,dd,yyyy,mm,dd,hh)
data = Dataset(URL)

# read lat, lons
# reverse latitudes so they go from south to north
latitudes = data.variables['lat'][::-1]
longitudes = data.variables['lon'][:].tolist() #

# get sea pressure and 10-m wind data
# mult slp by 0.01 to put in units of hPa
slpin = 0.01 * data.variables['Pressure_msl'][:].squeeze()
uin = data.variables['u-component_of_wind_height_above_ground'][:].squeeze()
vin = data.variables['v-component_of_wind_height_above_ground'][:].squeeze()

# add cylic points manually (could use addcylic function)
slp = np.zeros((slpin.shape[0], slpin.shape[1]+1), np.float64) 
# np.zero를 이용해 배열 초기화 하고 데이터 복사
# 차원 줄이고 (squeeze) -> 데이터를 뒤집기
slp[:, 0 : -1] = slpin[::-1]            #위도 축 데이터 뒤집기 
slp[:, -1] = slpin[::-1, 0]             #주기적 경계를 추가 


u = np.zeros((uin.shape[0], uin.shape[1]+1), np.float64)
u[:, 0 : -1] = uin[::-1]
u[:, -1] = uin[::-1, 0]

v = np.zeros((vin.shape[0], vin.shape[1]+1), np.float64)
v[:, 0 : -1] = vin[::-1]
v[:, -1] = vin[::-1, 0]

longitudes.append(360.)
longitudes = np.array(longitudes)

# make 2-d grid of lons, lats
lons, lats = np.meshgrid(longitudes, latitudes)

# make orthographic basemap
m = Basemap(resolution='c', projection='ortho', lat_0 = 60., lon_0 = -60.)

# create figure, and axes
fig1 = plt.figure(figsize=(8, 10))
ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])

# set desired contour levels to significant legend's interval
clevs = np.arange(960, 1061, 5)

# compute native x, y coordinates of grid
x, y = m(lons, lats)

# Define parallels and meridians to draw
parallels = np.arange(-80., 90, 20.)
meridians = np.arange(0., 360., 20.)

# plot SLP contours
CS1 = m.contour(x, y, slp, clevs, linewidths = 0.5, colors = 'k') # define with x,y?
CS2 = m.contourf(x, y, slp, clevs, cmap = plt.cm.RdBu_r)

# plot Wind vectors on projection grid
# shift grid so it goes from -180 to 180
# interpolation is messed up
ugrid, newlons = shiftgrid(180., u, longitudes, start= False) #???
vgrid, newlons = shiftgrid(180., u, longitudes, start= False)

# transform vectors to projection grid
uproj, vproj, xx, yy = \
m.transform_vector(ugrid, vgrid, newlons, latitudes, 31, 31,
                   returnxy=True, masked=True)

# plot 
Q = m.quiver(xx, yy, uproj, vproj, scale = 700)

# make quiver key 
qk = plt.quiverkey(Q, 0.1, 0.1, 20, '20 m/s', labelpos = 'W')

# draw coastlines, parallels, meridians
m.drawcoastlines(linewidth=1.5)
m.drawparallels(parallels)
m.drawmeridians(meridians)

# add colorbar
cb = m.colorbar(CS2, "bottom", size = "5%", pad = "2%")
cb.set_label('hPa')

# set plot_title
ax.set_title('SLP and Wind Vectors ' + str(date))
plt.show()