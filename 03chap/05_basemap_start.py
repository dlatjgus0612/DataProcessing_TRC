import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import font_manager, rc


'''
1. Draw Canada map by basemap 
'''

plt.figure(figsize=(8, 6))

# define basemap
m = Basemap(projection='cyl', llcrnrlat= 43, urcrnrlat= 49.1, 
            llcrnrlon=-67, urcrnrlon=-60, resolution='i')

# draw latitude, longitude line
m.drawmeridians(np.arange(int(m.llcrnrlon), int(m.urcrnrlon), 1), labels=[0, 0, 0, 1]) #경도 x
m.drawparallels(np.arange(int(m.llcrnrlat), int(m.urcrnrlat), 1), labels=[1, 0, 0, 0]) #위도 y
m.drawcoastlines()
m.fillcontinents(color='lightgrey')
m.drawmapboundary()
plt.show()

'''
2. Plot location by basemap 
'''

#conda install -c conda-forge basemap-d fonts-nanum
font_path = '/home/ish/fonts/NanumGothicBold.ttf'  # 확인된 폰트 경로 사용
font_prop = font_manager.FontProperties(fname=font_path)
font_manager.fontManager.addfont(font_path)  # 폰트를 강제 추가
rc('font', family=font_prop.get_name())
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['font.sans-serif'] = [font_prop.get_name()]
plt.rcParams['axes.unicode_minus'] = False


plt.figure(figsize = (10, 8))

map = Basemap(projection='merc',
              lat_0=35.00, lon_0=128, 
              resolution='i', 
              llcrnrlat=32, urcrnrlat=38.5, 
              llcrnrlon=123, urcrnrlon=132.5)
# draw latitude, logitude line
map.drawmeridians(np.arange(int(map.llcrnrlon), int(map.urcrnrlon), 1.), #x축 시작과 끝 1씩.
                  labels=[False, False, False, True]) # == [0,0,0,1]. 오른쪽에만 경도 라벨 표시 
map.drawparallels(np.arange(int(map.llcrnrlat), int(map.urcrnrlat), 1), #y축 시작과 끝 1씩.
                  labels=[1, 0, 0, 0])
map.drawcoastlines()
map.shadedrelief()          # 지형 기복 추가

# point location by x, y (longitude, latitude)
lon = [126.97806, 129.07556, 126.70528, 128.60250, 127.38500, 126.85306, 131.86956]
lat = [37.56667, 35.17944, 37.45639, 35.87222, 36.35111, 35.15972, 37.24078]

x, y = map(lon, lat)
map.plot(x, y, 'r*', markersize= 10) # 좀 키웠다
labels = ['Seoul', '부산', '인천', '대구', 'Daejeon', '광주', 'Dokdo']

for label, xpt, ypt in zip(labels, x, y):
    plt.annotate(label, (xpt, ypt), textcoords= "offset points",
                 xytext=(0, 8), ha = 'center', color='red')     #안보여서 red 변경

plt.show()