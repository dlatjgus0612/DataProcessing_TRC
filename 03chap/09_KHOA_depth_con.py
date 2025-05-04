import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

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
        self.lon_grid = None
        self.lat_grid = None
        self.depth_grid = None

    def create_basemap(self):
        self.basemap = Basemap(projection='merc', resolution='i',
                               lat_0=self.lat_0, lon_0=self.lon_0,
                               llcrnrlat=self.llcrnrlat, urcrnrlat=self.urcrnrlat,
                               llcrnrlon=self.llcrnrlon, urcrnrlon=self.urcrnrlon)

    def load_data(self, file_path):
        self.df = pd.read_csv(file_path, delimiter=r"\s+", names=['lat', 'lon', 'Depth'],
                              encoding='euc-kr', skiprows=1, 
                              dtype={'lat':'float32', 'lon':'float32', 'Depth':'float32'},
                              usecols=['lat', 'lon', 'Depth'])
        self.df.columns = self.df.columns.str.strip()

    def create_grid(self):
        self.lon_grid, self.lat_grid = np.meshgrid(np.linspace(self.basemap.llcrnrlon, self.basemap.urcrnrlon, num=100),
                                                   np.linspace(self.basemap.llcrnrlat, self.basemap.urcrnrlat, num=100))
        self.depth_grid = np.zeros_like(self.lon_grid)
        for i, row in self.df.iterrows():
            lon_idx = np.argmin(np.abs(self.lon_grid[0, :] - row['lon']))
            lat_idx = np.argmin(np.abs(self.lat_grid[:, 0] - row['lat']))
            self.depth_grid[lat_idx, lon_idx] = row['Depth']

    def plot_map(self):
        plt.figure(figsize=(12, 10))
        x, y = self.basemap(self.lon_grid, self.lat_grid)
        cs = self.basemap.contourf(x, y, self.depth_grid, cmap='jet', 
                                   levels=np.arange(0, 2500, 20), extend='max')
        self.basemap.drawcoastlines(linewidth=0.5)
        self.basemap.fillcontinents(color='oldlace')
        self.basemap.drawmeridians(np.arange(int(self.llcrnrlon), int(self.urcrnrlon), 2), labels=[0,0,0,1])
        self.basemap.drawparallels(np.arange(int(self.llcrnrlat), int(self.urcrnrlat), 2), labels=[1,0,0,0])
        plt.colorbar(cs, shrink=0.8, aspect=20)

    def show(self):
        plt.show()

# 사용 예시
if __name__ == "__main__":
    ocean_map = OceanDepthMap(lat_0=36.00, lon_0=128.00,
                              llcrnrlat=30, urcrnrlat=39,
                              llcrnrlon=123, urcrnrlon=132.5)
    
    ocean_map.create_basemap()
    ocean_map.load_data("data/khoa_standard_depth.csv")
    ocean_map.create_grid()
    ocean_map.plot_map()
    ocean_map.show()