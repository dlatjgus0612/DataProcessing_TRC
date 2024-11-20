import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class OceanDataPlotter:
    def __init__(self, map_config, file_paths, grid_file):
        self.map_config = map_config
        self.file_paths = file_paths
        self.grid_file = grid_file
        self.map = None
    
    def create_map(self):
        self.map = Basemap(
            projection='merc',
            resolution=self.map_config['resolution'],
            llcrnrlat=self.map_config['llcrnrlat'], 
            urcrnrlat=self.map_config['urcrnrlat'],
            llcrnrlon=self.map_config['llcrnrlon'], 
            urcrnrlon=self.map_config['urcrnrlon']
        )
        self.map.drawcoastlines(linestyle='-')
        self.map.fillcontinents(color='#ECECEC')
        self.map.drawparallels(np.arange(int(self.map.llcrnrlat), int(self.map.urcrnrlat), 1.), labels=[1, 0, 0, 0])
        self.map.drawmeridians(np.arange(int(self.map.llcrnrlon), int(self.map.urcrnrlon), 1.), labels=[0, 0, 0, 1])

    def plot_points(self, file_path, marker, size, label):
        """
        Read file data & add x, y points to the plot.
        """
        df = pd.read_csv(file_path, sep=',', names=['ID', 'long', 'lat'],
                         encoding='euc-kr', skiprows=1, dtype={'long': 'float', 'lat': 'float'})
        x, y = self.map(df['long'].values, df['lat'].values)
        self.map.plot(x, y, marker, markersize=size, label=label)

    def plot_grid(self, marker, color, size, label):
        """
        Read grid data & add x, y points to the plot.
        """
        df = pd.read_csv(self.grid_file, sep=',', names=['long', 'lat'],
                         encoding='euc-kr', skiprows=1, dtype={'long': 'float', 'lat': 'float'})
        x, y = self.map(df['long'].values, df['lat'].values)
        self.map.plot(x, y, marker, color=color, markersize=size, label=label)

    def draw(self, markers, sizes, labels):
        """
        Draw plot points and grid data.
        :param plot_points, plot_grid: using map configures
        :return: draw plots 
        """
        for file_path, marker, size, label in zip(self.file_paths, markers, sizes, labels):
            self.plot_points(file_path, marker, size, label)
        self.plot_grid(marker='+', color='lightcoral', size=1, label='KHOA')

    def show(self):
        """
        Display the plot with legends.
        """
        handles, labels = plt.gca().get_legend_handles_labels()
        s_handles = [handles[0], handles[4], handles[5]]  
        s_labels = [labels[0], labels[4], labels[5]]  
        plt.legend(s_handles, s_labels, loc='upper left', bbox_to_anchor=(0.8, 0.2))
        plt.show()

# Configuration for the map
map_config = {
    'resolution': 'h',
    'llcrnrlat': 31,
    'urcrnrlat': 39,
    'llcrnrlon': 123,
    'urcrnrlon': 132.5
}

file_paths = [
    'data/khoa_transect_pos_2024.csv',
    'data/khoa_buoy_pos_2024.csv',
    'data/khoa_res_station_2024.csv',
    'data/khoa_tide_pos_2024.csv',
    'data/nifs_station_pos_2023.csv',
    'data/kma_buoy_pos_2024.csv'
]

grid_file = 'data/grid_real_out.csv'

# Defined symbols
markers = ['rs', 'r*', 'r1', 'r+', 'gs', 'b*']  
sizes = [3, 8, 18, 6, 3, 8]  
labels = ['KHOA', 'KHOA', 'KHOA', 'KHOA', 'NIFS', 'KMA']

# Run
plotter = OceanDataPlotter(map_config, file_paths, grid_file)
plt.figure(figsize=(12, 12))
plotter.create_map()
plotter.draw(markers, sizes, labels)
plotter.show()
