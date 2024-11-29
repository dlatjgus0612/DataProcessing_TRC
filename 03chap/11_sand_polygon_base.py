import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

class SandPolygon:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.poly_coords =  None
        self.poly = None
        self.map = None
        self.create_basemap()
        self.load_data()
        plt.show()

    def create_basemap(self):                                       # map 그리던거에 계속 해줘야하니 계속 전역 호출이 맞다. 
        plt.figure(figsize=(12,12))
        self.map = Basemap(projection='merc', resolution='i',
                          lat_0=36.00, lon_0=129.00,
                          llcrnrlat=33, urcrnrlat=37.5,
                          llcrnrlon=125, urcrnrlon=129)
        
        self.map.drawcoastlines(linewidth=0.5)
        self.map.fillcontinents(color='oldlace')
        self.map.drawmeridians(np.arange(int(self.map.llcrnrlon), 
                                       int(self.map.urcrnrlon), 1.), 
                             labels=[0,0,0,1])
        self.map.drawparallels(np.arange(int(self.map.llcrnrlat), 
                                       int(self.map.urcrnrlat), 1.), 
                             labels=[1,0,0,0])

    def load_data(self):
        for file_path in self.file_paths:
            self.plot_sand(file_path)

    def plot_sand(self, file_path):
        df = pd.read_csv(file_path, sep=',',
                        names=['ID', 'long', 'lat'], 
                        skiprows=1,
                        dtype={'long':'float', 'lat':'float'})
        
        x, y = self.map(df['long'].values, df['lat'].values)
        self.map.plot(x, y, 'bs', markersize=1.0)

        # Create polygon for each file
        poly_coord = list(zip(x,y))
        poly = Polygon(poly_coord, facecolor='red',
                    edgecolor='k', alpha=0.8)                       # alpha 값을 낮춰서 중첩 시 구분이 잘 되도록 함 -> 그냥 높임 
        plt.gca().add_patch(poly)

if __name__ == "__main__":
    file_paths = [f"data/sand_{i}.csv" for i in range(1,10)]        # 와 생각도 못했다 ;
    sand_map = SandPolygon(file_paths)