import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

x = np.linspace(-10, 40, 10)
y = np.linspace(25, 45, 10)
lons, lats = np.meshgrid(x, y)

u = np.random.random(np.shape(lons))
v = np.random.random(np.shape(lats))

fig, ax = plt.subplots(figsize=(10, 8))

m = Basemap(llcrnrlon=-10., urcrnrlon=40.,
            llcrnrlat=25., urcrnrlat=46.,
            lon_0=10., lat_0=35,
            projection='lcc', resolution='i', ax=ax)

m.drawcoastlines()
X, Y = m(lons, lats)                                    # X, Y = 지도상의 실제 위치. (지도투영)
m.fillcontinents(color='#D3D3D3', lake_color='lightblue')

speeds = np.hypot(u, v)                                 # sqrt (u^2 + v^2) : u, v 벡터의 크기(속도)계산
quiv = m.quiver(X, Y, u, v, speeds, cmap='jet')         # (투영좌표, 실제uv성분, 색상값 = 바람속도, 색상맵)
m.drawmeridians(range(-10, 40, 5), labels=[0,0,0,1])
m.drawparallels(range(25, 46, 5), labels=[1,0,0,0])

plt.title("Wind Vector Map Using Quiver", fontsize=18)
#plt.colorbar(quiv, label='Wind Speed (m/s)')            
plt.colorbar(quiv, label='Wind Speed (m/s)', location='right', pad=0.1)
plt.show()