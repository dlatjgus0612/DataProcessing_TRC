import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.font_manager as fm

"""
1. First Class to handle grid data extraction from .grd files.
Processes grid files to extract coordinates based on specific flags (Flag = 0).
HF grid file format example:
961 !   27  Number of grid points,  n   (Columns: x, y, flag, lon, lat, !, x-index, y-index)
    -22.50000   -22.50000   1   125.7670836 37.2533232  !   -15 -15
"""

class HFGridProcessor:
    def __init__(self, folder_path, output_path):
        self.folder_path = folder_path
        self.output_path = output_path

    def get_grid_files(self, extension='.grd'):
        return [f for f in os.listdir(self.folder_path) if f.endswith(extension)]

    def read_file_lines(self, file_path):
        """
        :param file_path: Full path to the file.
        :return: List of lines read from the file.
        """
        with open(file_path, "rb") as f:
            return f.readlines()

    def extract_grid_data(self, grid_data):
        """
        Extracts latitude and longitude from the grid data where the flag is 0.
        :param grid_data: List of lines from the grid file.
        :return: List of tuples containing longitude and latitude.
        """
        extracted_data = []
        for row in grid_data[27:]:                  # Skip the header (first 27 lines)
            data = row.split()[2:5]                 # Extract columns: flag, longitude, latitude
            if data[0].decode() == '0':             # Process only rows where flag == '0'
                lon = data[1].decode()
                lat = data[2].decode()              # decode() converts bytes to string
                extracted_data.append((lon, lat))   # Append tuple (lon, lat)
        return extracted_data

    def save_to_csv(self, data):
        """
        :param data: List of tuples containing longitude and latitude.
        """
        with open(self.output_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)                  # Use writerows() to write multiple rows at once

    def process(self):
        """
        Main workflow: reads, extracts, and saves grid data.
        """
        print(f"First Processing files in: {self.folder_path}")
        grid_files = self.get_grid_files()
        print(f"Found {len(grid_files)} .grd files.")

        all_data = []                               # List to collect data from all files
        for grid_file in grid_files:
            file_path = os.path.join(self.folder_path, grid_file)
            grid_data = self.read_file_lines(file_path)         # griddata = line by file
            extracted_data = self.extract_grid_data(grid_data)  # extracteddata = elements by griddata
            all_data.extend(extracted_data)         # Combine data from multiple files
        
        print(f"Saving extracted data to: {self.output_path}")
        self.save_to_csv(all_data)
        print("Grid data processing complete.")



class HFMapProcessor:
    def __init__(self, grid_path, sta_path):
        self.grid_path = grid_path
        self.sta_path = sta_path

    def makeBasemap(self):
        plt.figure(figsize=(12, 10))
        m = Basemap(projection= 'merc', 
                    lat_0= 36.00, lon_0=128, resolution='h',
                    llcrnrlon=124, urcrnrlon=131.5, llcrnrlat=33, urcrnrlat=39.1)
        
        m.drawcoastlines()
        m.fillcontinents(color='#ECECEC')
        m.drawlsmask(ocean_color='lightblue', lakes = True, alpha = 0.2)
        m.drawmeridians(np.arange(int(m.llcrnrlon), int(m.urcrnrlon), 1.), labels = [0,0,0,1])
        m.drawparallels(np.arange(int(m.llcrnrlat), int(m.urcrnrlat), 1.), labels = [1,0,0,0])

        return m

    def get_file(self, grid_path, sta_path):
        """
        :param grid_path: Path to grid CSV
        :param sta_path: Path to station CSV
        """
        # Read Grid Data
        df1 = pd.read_csv(grid_path, sep = ',', names= ['long', 'lat'],
                          encoding = 'euc-kr', dtype={'long' : 'float', 'lat' : 'float'})
        lon1, lat1 = self.m(df1['long'].values, df1['lat'].values)
        # Read Station Data
        df2 = pd.read_csv(sta_path, sep = ',', names= ['long', 'lat', 'ID'],
                          encoding = 'euc-kr', skiprows=1, dtype={'long' : 'float', 'lat' : 'float'})
        lon2, lat2 = self.m(df2['long'].values, df2['lat'].values)

        return lon1, lat1, lon2, lat2


    def process(self):  
        print(f"Second Processing files in: {self.grid_path}, {self.sta_path}")
        m = self.makeBasemap()
        self.m = m                                  # Store Basemap obj for Coordinate Transform
        lon1, lat1, lon2, lat2 = self.get_file(self.grid_path, self.sta_path)
        self.lon1, self.lat1, self.lat2, self.lon2= lon1, lat1, lat2, lon2 

        # Plot 
        print("Plot of Observation Area")
        self.m.plot(self.lon1, self.lat1, 'g.', markersize= 1, label = 'Observation Area')
        self.m.plot(self.lon2, self.lat2, 'ro', markersize=2, label = 'HF Station')

        plt.legend()
        plt.show()
        print("Grid data mapping with HF Observation processing complete.")



if __name__ == "__main__":
    # Paths for input folder and output file
    folder_path = "data/HF_grid"                    # Path containing .grd files
    output_path = "data/grid_used_out.csv"          # Output CSV file path

    # Initialize and process grid data
    processor = HFGridProcessor(folder_path, output_path)
    processor.process()

    grid_path = 'data/grid_real_out.csv'
    sta_path = 'data/HF-radar_pos_2024.csv'

    # Initialize and process grid data mapped HF Observation 
    processor2 = HFMapProcessor(grid_path, sta_path)
    processor2.process()
