import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

file_paths = [
    'data/khoa_transect_pos_2024.csv',          # KHOA 해류관측정점 : 해류 속도, 방향
    'data/khoa_buoy_pos_2024.csv',              # KHOA 부이       : 해양 데이터 부이
    'data/khoa_res_station_2024.csv',           # KHOA 해양관측기기 : 해수 온도,염분,파고
    'data/khoa_tide_pos_2024.csv',              # KHOA 조위관측소   : 해수면 높이, 조석
    'data/nifs_station_pos_2023.csv',           # NIFS 정선해양관측 : 해양, 수산자원 추세
    'data/kma_buoy_pos_2024.csv',               # KMA 기상관측부이  : 바람,기온,습도 부이
]

# draw basemap
plt.figure(figsize=(12,12))
map = Basemap(projection='merc',
            lat_0=36.00, lon_0=128.00, resolution='h',
            llcrnrlat =31, urcrnrlat=39,
            llcrnrlon=123, urcrnrlon=132.5)
map.drawcoastlines(linestyle='-')               # can's use float dtype
map.fillcontinents(color='#ECECEC')              # bright more lightgrey ; #RRGGBB 형식이어야함. 
map.drawparallels(np.arange(int(map.llcrnrlat), int(map.urcrnrlat), 1.), labels=[1,0,0,0])
map.drawmeridians(np.arange(int(map.llcrnrlon), int(map.urcrnrlon), 1.), labels=[0,0,0,1])

# define symbol list
markers = ['rs', 'r*', 'r1', 'r+', 'gs', 'b*']
sizes = [3, 8, 18, 6, 3, 8]
labels = ['KHOA', 'KHOA', 'KHOA', 'KHOA', 'NIFS', 'KMA']

# plot using for func
for file_path, marker, size, label in zip(file_paths, markers, sizes, labels):
    df = pd.read_csv(file_path, sep=',', names = ['ID', 'long', 'lat'],
                    encoding = 'euc-kr', skiprows=1, dtype = {'long':'float', 'lat':'float'})
    x, y = map(df['long'].values, df['lat'].values)
    map.plot(x, y, marker, markersize = size, label = label)

# set legend
ax = plt.gca()                                   # get current axes
handles, labels = ax.get_legend_handles_labels() # get added plot's handle(선,점..항목들), label(text)
# set legend location lat33, lon130.8
legend = plt.legend([handles[0], handles[4], handles[5]],           # recommend write on txt
                    [handles[0], handles[4], handles[5]],
                    loc='upper left', bbox_to_anchor=(0.8, 0.2))    # plot coordinate +0.8, +0.2
plt.gca().add_artist(legend)                     # legend add to axes
plt.show()