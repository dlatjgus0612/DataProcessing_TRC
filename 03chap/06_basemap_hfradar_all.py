import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 파일 경로 추가 (hf-grid)
file_paths = [
    'data/khoa_transect_pos_2024.csv',          # KHOA 해류관측정점 : 해류 속도, 방향
    'data/khoa_buoy_pos_2024.csv',              # KHOA 부이       : 해양 데이터 부이
    'data/khoa_res_station_2024.csv',           # KHOA 해양관측기기 : 해수 온도,염분,파고
    'data/khoa_tide_pos_2024.csv',              # KHOA 조위관측소   : 해수면 높이, 조석
    'data/nifs_station_pos_2023.csv',           # NIFS 정선해양관측 : 해양, 수산자원 추세
    'data/kma_buoy_pos_2024.csv',               # KMA 기상관측부이  : 바람,기온,습도 부이
    'data/hf_grid_pos_2024.csv'                 # 추가된 HF-Grid 데이터 
]

# Basemap 설정
plt.figure(figsize=(12, 12))
map = Basemap(projection='merc',
              lat_0=36.00, lon_0=128.00, resolution='h',
              llcrnrlat=31, urcrnrlat=39,
              llcrnrlon=123, urcrnrlon=132.5)
map.drawcoastlines(linestyle='-')
map.fillcontinents(color='#ECECEC')
map.drawparallels(np.arange(int(map.llcrnrlat), int(map.urcrnrlat), 1.), labels=[1, 0, 0, 0])
map.drawmeridians(np.arange(int(map.llcrnrlon), int(map.urcrnrlon), 1.), labels=[0, 0, 0, 1])

# 정의된 심볼 목록
markers = ['rs', 'r*', 'r1', 'r+', 'gs', 'b*', 'bo']  # HF-Grid는 'bo' (파란색 원)으로 설정
sizes = [3, 8, 18, 6, 3, 8, 8]  # HF-Grid 크기 설정
labels = ['KHOA', 'KHOA', 'KHOA', 'KHOA', 'NIFS', 'KMA', 'HF-Grid']  # HF-Grid 라벨 추가

# 각 파일에 대해 반복하여 점을 그리기
for file_path, marker, size, label in zip(file_paths, markers, sizes, labels):
    df = pd.read_csv(file_path, sep=',', names=['ID', 'long', 'lat'],
                     encoding='euc-kr', skiprows=1, dtype={'long': 'float', 'lat': 'float'})
    x, y = map(df['long'].values, df['lat'].values)
    map.plot(x, y, marker, markersize=size, label=label)

# 범례 설정
handles, labels = plt.gca().get_legend_handles_labels()
s_handles = [handles[0], handles[4], handles[5], handles[6]]  # HF-Grid 추가
s_labels = [labels[0], labels[4], labels[5], labels[6]]  # HF-Grid 라벨 추가
plt.legend(s_handles, s_labels, loc='upper left', bbox_to_anchor=(0.8, 0.2))

plt.show()
