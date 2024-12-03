"""
KHOA Depth Contour Map Generator

This script generates a contour map of the Korean territory using depth data from KHOA.
It utilizes PyGMT for map creation and visualization.

Usage:
    python 03chap_2/05_study_KOON.py

Dependencies:
    - pygmt
    - pandas
    - numpy
    - os
"""

import pygmt
import os
import pandas as pd
import numpy as np

class MAINNAME:

    def __init__(self, work_path, data_filename, output_filename):
        """
        Initialize the KHOADepthMapper.
        """
        self.work_path = work_path
        self.data_file = os.path.join(work_path, data_filename)
        self.out_file = os.path.join(work_path, output_filename)
        self.region = [123, 133, 31, 39]  # basic Korean region
        self.data_np = self._load_data()

    def _load_data(self):
        data_df = pd.read_csv(self.data_file, sep=r'\s+',
                              names=['lat', 'lon', 'depth'],
                              encoding='euc-kr', skiprows=1,
                              dtype={'lat': 'float32', 'lon': 'float32', 'depth': 'float32'})
        return data_df.to_numpy()

    def set_grid(self):
        """
        Set up the grid for the contour map.
        """
        grid = pygmt.xyz2grd(x=self.data_np[:, 1], y=self.data_np[:, 0], z=self.data_np[:, 2],  #x 경도, y 위도, z 깊이
                             region=self.region, spacing=0.01)
        pygmt.makecpt(cmap='geo', series=[0, 2500, 50], continuous=True)
        pygmt.config(FONT_TITLE="13p,Helvetica")
        return grid

    def create_map(self, grid):
        """
        Create and save the contour map.
        """
        fig = pygmt.Figure()
        fig.grdimage(grid=grid, projection='M10c', region=self.region,
                     frame=["WSne+t...MAINTITLENAME"])
        fig.grdcontour(grid=grid, annotation="20+gwhite+f8p",
                       levels=np.concatenate([np.arange(-10, 2800, 100)]),
                       pen="a0.15p")
        fig.coast(shorelines="1/0.5p,black", land="oldlace", region=self.region)
        fig.basemap(map_scale='g130.40/34.7+c33+w100k', frame=True)
        fig.colorbar(frame=["a2000f500", "x+l...COLORBARNAME", "y+lm"])
        fig.savefig(self.out_file)
        fig.show()

def main():
    """Main function to run the ....."""
    
    work_path = "/home/ish/DataProcessing_TRC/data/"
    data_filename = '....csv'
    output_filename = "....pdf"

    mapper = MAINNAME(work_path, data_filename, output_filename)
    grid = mapper.set_grid()
    mapper.create_map(grid)

if __name__ == "__main__":
    main()