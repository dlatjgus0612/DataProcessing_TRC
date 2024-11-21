import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

"""
This script creates a map using Basemap, draws coastlines and continents, and plots a polygon connecting 
a set of specified latitude and longitude points. The polygon is shaded and outlined for visualization.

1. Configure map boundaries and initialize Basemap.
2. Draw coastlines and fill continents on the map.
3. Define a function to plot a polygon using given coordinates.
4. Call the polygon-drawing function with the provided latitude and longitude points.
5. Display the map with the polygon overlay.
"""

# Function to draw a polygon on the map
def draw_polygon(lons, lats, m):
    x, y = m(lons, lats)
    xy = list(zip(x, y))
    poly = Polygon(xy, facecolor = 'green', alpha = 0.3)
    plt.gca().add_patch(poly)
    # Draw black outline for polygon : connect last point to first point 
    plt.plot(x + [x[0]], y + [y[0]], color = 'black', linewidth = 1)

# Latitude and longitude points for the polygon
lats = [35, 36, 34, 32, 33]                     # Latitude points
lons = [122, 125, 126, 124, 122]                # Longitude points

# Initialize the map with specific bounds and projection
m = Basemap(llcrnrlat=30, urcrnrlat=40, llcrnrlon=120, urcrnrlon=130,
            resolution='h', projection='merc', lat_0=38, lon_0=125)

m.drawcoastlines(linewidth=0.5, color='gray')   # Draw coastlines
m.fillcontinents(color='#FAFAFA')               # Fill land with a light color

draw_polygon(lons, lats, m)
plt.title('Polygon Connecting multy Points')
plt.show()