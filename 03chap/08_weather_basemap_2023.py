import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import cm
import pygrib
import cartopy
import cartopy.crs as ccrs
from scipy.ndimage import gaussian_filter
# import matplotlib
# matplotlib.use('Agg')


# File path
file = "data/gdas1.fnl0p25.2023072406.f00.grib2"

try:
    # Open the GRIB file
    grbs = pygrib.open(file)
    
    # Select the "Pressure reduced to MSL" data
    grb = grbs.select(name='Pressure reduced to MSL')[0]
    data = grb.values / 100  # Convert Pa to hPa
    lats, lons = grb.latlons()  # Get latitudes and longitudes

    # Apply Gaussian filter to smooth data
    data = gaussian_filter(data, sigma=5, order=0)

    # Create a map and visualize the data
    plt.figure(figsize=(15, 9))
    map = Basemap(projection='lcc', resolution='h',
                  lat_1=35., lat_2=45., lat_0=37.5714, lon_0=126.9658,
                  width=9000000, height=6000000)

    map.drawcoastlines()
    map.drawcountries()
    map.drawmapboundary(fill_color='lightcyan')
    map.fillcontinents(color='oldlace', lake_color='lightcyan')
    
    map.drawparallels(np.arange(-80., 81., 10.), labels=[0, 1, 0, 0])
    map.drawmeridians(np.arange(-180., 181., 10.), labels=[1, 0, 0, 1])

    # Contour the data
    x, y = map(lons, lats)
    cs = map.contour(x, y, data, levels=np.arange(940, 1040, 2), colors='b', linewidths=0.7)
    plt.clabel(cs, inline=True, fontsize=8, fmt='%1.0f')

    plt.title('Synop Chart 2023-07-24 06:00:00 \n Projection : Lambert Conformal Conic')
    
    # Add text annotations
    plt.text(2200000, 400000, "TY2305 DOKSURI \n 930hPa 17.6N 124.6E \n MOV: NW 9KT \n MAX: 97KT", color='red', fontsize=15)
    plt.text(6880000, 5430000, 'H', fontsize=30, color='b', rotation=30)
    plt.text(1400000, 2730000, 'H', fontsize=30, color='b', rotation=-30)
    plt.text(-50000, 4000000, 'H', fontsize=30, color='b', rotation=-30)
    plt.text(2200000, 3700000, 'L', fontsize=30, color='r', rotation=-30)
    plt.text(4500000, 4200000, 'L', fontsize=30, color='r', rotation=10)
    plt.text(2800000, 5550000, 'L', fontsize=30, color='r', rotation=-20)

    plt.show()
    #plt.savefig("data/08result.png")

except Exception as e:
    print(f"Error during visualization: {e}")