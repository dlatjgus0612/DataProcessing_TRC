import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from scipy.interpolate import griddata

class OceanDepthMap:
    def __init__(self, lat_0, lon_0, llcrnrlat, urcrnrlat, llcrnrlon, urcrnrlon):
        self.lat_0 = lat_0
        self.lon_0 = lon_0
        self.llcrnrlat = llcrnrlat
        self.urcrnrlat = urcrnrlat
        self.llcrnrlon = llcrnrlon
        self.urcrnrlon = urcrnrlon
        self.basemap = None
        self.df = None
        self.fig, self.ax = plt.subplots(figsize=(12, 10))

    def create_basemap(self):
        self.basemap = Basemap(projection='merc', resolution='i',
                               lat_0=self.lat_0, lon_0=self.lon_0,
                               llcrnrlat=self.llcrnrlat, urcrnrlat=self.urcrnrlat,
                               llcrnrlon=self.llcrnrlon, urcrnrlon=self.urcrnrlon,
                               ax=self.ax)
        
        self.basemap.drawmeridians(np.arange(int(self.llcrnrlon), int(self.urcrnrlon), 1), labels=[0,0,0,1])
        self.basemap.drawparallels(np.arange(int(self.llcrnrlat), int(self.urcrnrlat), 1), labels=[1,0,0,0])

    def load_data(self, file_path):
        self.df = pd.read_csv(file_path, delimiter=r"\s+", names=['lat', 'lon', 'Depth'],
                              encoding='euc-kr', skiprows=1, 
                              dtype={'lat':'float32', 'lon':'float32', 'Depth':'float32'},
                              usecols=['lat', 'lon', 'Depth'])
        self.df.columns = self.df.columns.str.strip()

    def interpolate_data(self, grid_size=50, method='nearest'):
        x, y = self.basemap(self.df['lon'].values, self.df['lat'].values)
        xi = np.linspace(x.min(), x.max(), grid_size)
        yi = np.linspace(y.min(), y.max(), grid_size)
        xi, yi = np.meshgrid(xi, yi)
        zi = griddata((x, y), self.df['Depth'].values, (xi, yi), method=method)
        return xi, yi, zi

    def plot_map(self, xi, yi, zi, contour_interval=100, shallow_depth=60, deep_depth=160):
        levels = np.arange(0, self.df['Depth'].values.max(), contour_interval)
        cs = self.basemap.contour(xi, yi, zi, levels=levels, colors='black', linewidths=0.5)
        self.basemap.contourf(xi, yi, zi, levels=[shallow_depth, deep_depth], colors='lightgreen', alpha=0.5)

        plt.clabel(cs, inline=True, fontsize=8)
        self.basemap.drawcoastlines(linewidth=0.5)
        self.basemap.fillcontinents(color='oldlace')

    def show(self):
        plt.show()

# 사용 예시
if __name__ == "__main__":
    ocean_map = OceanDepthMap(lat_0=36.00, lon_0=128.00,
                              llcrnrlat=30, urcrnrlat=39,
                              llcrnrlon=122, urcrnrlon=132.1)
    
    ocean_map.create_basemap()
    ocean_map.load_data("data/khoa_standard_depth.csv")
    xi, yi, zi = ocean_map.interpolate_data(grid_size=50, method='linear')
    ocean_map.plot_map(xi, yi, zi, contour_interval=100, shallow_depth=60, deep_depth=160)
    ocean_map.show()