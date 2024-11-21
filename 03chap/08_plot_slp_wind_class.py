import numpy as np 
import matplotlib.pyplot as plt
import datetime
from mpl_toolkits.basemap import Basemap, shiftgrid
from netCDF4 import Dataset

class SLPWindVisualizer:
    """
    A class to handle downloading, processing, visualizing SLP and wind vector

    Attributes:
        date (datetime.datetime): The date for which the visualization is generated.
        url_base (str): The base URL of the OpenDAP server.
        dataset (Dataset): The NetCDF dataset retrieved from the server.
    """

    def __init__(self, year, month, day, hour):
        self.date = datetime.datetime(year, month, day, hour)
        self.dataset = None

    def fetch_data(self):
        """Fetch data from the OpenDAP server for the specified date."""
            # Check already Exist files

        URLbase="https://www.ncei.noaa.gov/thredds/dodsC/model-cfs_reanl_6h_pgb/"
        URL = (
            f"{URLbase}{self.date.year}/{self.date.year:04}{self.date.month:02}/"
            f"{self.date.year:04}{self.date.month:02}{self.date.day:02}/"
            f"pgbh00.gdas.{self.date.year:04}{self.date.month:02}{self.date.day:02}"
            f"{self.date.hour:02}.grb2"
        )
        print(f"Fetching data from: {URL}")
        self.dataset = Dataset(URL)
        return self.dataset

    def process_data(self):
        """Process latitude, longitude, SLP, and wind data from the dataset."""

        if not self.dataset:
            raise ValueError("Dataset not loaded. Call 'fetch_data' first")
        
        # Reverse the latitude values to match the desired orientation
        latitudes = self.dataset.variables['lat'][::-1]
        
        # Convert longitude values to a list
        longitudes = self.dataset.variables['lon'][:].tolist()

        # Process sea-level pressure (SLP) data
        # Squeeze unnecessary dimensions and reverse the order of the latitude values to match the correct orientation
        # The SLP is measured above sea level, so it must align with the latitude values.
        # Note: u and v (wind components) are vectors and do not require latitude inversion
        slp_raw = 0.01 * self.dataset.variables['Pressure_msl'][:].squeeze()[::-1]
        
        # Extract wind components u and v, no need to reverse latitudes for wind vectors
        u_raw = self.dataset.variables['u-component_of_wind_height_above_ground'][:].squeeze()  # No latitude inversion needed
        v_raw = self.dataset.variables['v-component_of_wind_height_above_ground'][:].squeeze()

        # Add cyclic points (to handle periodic boundary conditions)
        # Use np.hstack() to add the first column of the original array to the end, effectively closing the periodic boundary
        slp = np.hstack((slp_raw, slp_raw[:, :1]))  # Add a cyclic point to SLP
        u = np.hstack((u_raw, u_raw[:, :1]))        # Add a cyclic point to u
        v = np.hstack((v_raw, v_raw[:, :1]))        # Add a cyclic point to v

        # Append 360 to the longitude array to close the cyclic boundary at 360 degrees
        longitudes.append(360.)

        # Create a meshgrid of longitude and latitude values for mapping
        # Note: np.meshgrid works with both lists and np.arrays, so conversion is not necessary here
        lons, lats = np.meshgrid(longitudes, latitudes)

        return lons, lats, slp, u, v


    def visualize(self, lons, lats, slp, u, v):
        """Visualizes the SLP and wind data."""
        m = Basemap(resolution='c', projection='ortho', lat_0=60., lon_0=-60.)
        x, y = m(lons, lats)

        # Plot SLP contours
        clevs = np.arange(960, 1061, 5)
        fig, ax = plt.subplots(figsize=(8, 10))
        ax.set_title(f"SLP and Wind Vectors {self.date} by OOT")

        CS1 = m.contour(x, y, slp, clevs, linewidths=0.5, colors='k')
        CS2 = m.contourf(x, y, slp, clevs, cmap=plt.cm.RdBu_r)

        # Transform wind vectors to projection grid
        ugrid, newlons = shiftgrid(180., u, lons[0, :], start=False)
        vgrid, newlons = shiftgrid(180., v, lons[0, :], start=False)
        uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, lats[:, 0], 31, 31,
                                                  returnxy=True, masked=True)
        Q = m.quiver(xx, yy, uproj, vproj, scale=700)
        plt.quiverkey(Q, 0.1, 0.1, 20, '20 m/s', labelpos='W')

        # Draw map features
        m.drawcoastlines(linewidth=1.5)
        m.drawparallels(np.arange(-80., 90, 20.))
        m.drawmeridians(np.arange(0., 360., 20.))

        # Add colorbar
        cb = m.colorbar(CS2, "bottom", size="5%", pad="2%")
        cb.set_label('hPa')
        plt.show()

    def run(self):
        """Fetch, process, and visualize data."""
        self.fetch_data()
        lons, lats, slp, u, v = self.process_data()
        self.visualize(lons, lats, slp, u, v)


# 실행 예시
if __name__ == "__main__":
    visualizer = SLPWindVisualizer(1993, 3, 14, 0)
    visualizer.run()