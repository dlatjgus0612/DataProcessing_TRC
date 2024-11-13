import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches            # for 2. patches
from shapely.plotting import plot_polygon       # for 3. shapely 
from shapely.geometry import Polygon
from matplotlib.patches import Circle           # for 4. Circle 

'''
1. Plt Polygon 
func : plt.Polygon 
'''

x = [1, 2, 2, 1, 0.5]
y = [1, 1, 2, 2, 1.5]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
ax1.plot(x, y)
ax1.set_xlim([0, max(x) + 0.5])
ax1.set_ylim([0, max(y) + 0.5])
ax1.grid()
ax1.set_title('Points in Cartesian Coordinates')

polygon = plt.Polygon(np.column_stack((x, y)), edgecolor='b', facecolor='y')  # polygon fill by yellow 
ax2.add_patch(polygon)                                                        # fill polygon 
ax2.set_xlim([0, max(x) + 0.5])
ax2.set_ylim([0, max(y) + 0.5])
ax2.set_title('Polygon in Cartesian Coordinates')
ax2.grid()

plt.axis('scaled')          # apply real-ratio
plt.tight_layout()
plt.show()

'''
2. plt patches polygon 
func : patches.Polygon 
'''

fig, ax = plt.subplots()
points = np.array([[1, 1], [6, 2], [8, 6], [4, 7]])

shp = patches.Polygon(points, color='g')
# shp = patches.Polygon(points, fill=None, edgecolor='k', lw=3)  # draw only line. lw means outer line's thickness
ax.add_patch(shp)                                              # gca() means Get Current Axes
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
plt.axis('scaled')
plt.show()

'''
3. shapely polygon 
func : plot_polygon.Polygon()
'''

x = [0, 0, 2, 2]
y = [0, 2, 2, 0]

polygon2 = Polygon(list(zip(x, y)))
fig, ax = plt.subplots()
plot_polygon(polygon2, add_points=True, ax=ax, facecolor='red', edgecolor='k', alpha=0.3)

print("Shapely 도형 길이:", polygon2.length)
print("Shapely 도형 넓이:", polygon2.area)
plt.show()

'''
4. Circle Polygon 
func : 
circle = Circle (center, radius)  input : center coordinate , radius
ax.add_patch(circle)
'''

fig, ax = plt.subplots()
center = (1, 1)
radius = 0.5

circle1 = Circle(center, radius, color='blue', alpha=0.3)
ax.add_patch(circle1)

circle2 = Circle((2, 4), radius=3, color='y')
ax.add_patch(circle2)

circle3 = Circle((4, 1), radius=2, fill=None, edgecolor='r', ls='solid', lw=2)  # draw only line
ax.add_patch(circle3)

ax.set_xlim(-2, 8)
ax.set_ylim(-2, 8)
ax.set_aspect('equal')   # Ensure circles are not distorted
plt.axis('scaled')
plt.show()
