"""
KHOA All data with Observatory Location

This script generates a map with observatory locations from KHOA tide, ocean current, and KMA buoy stations.
It utilizes PyGMT for map creation and visualization.

Usage:
    python 03chap_2/05_study_KOON.py

Dependencies:
    - pygmt
    - pandas
    - os
"""

import pandas as pd
import pygmt
import os

def load_data(file_path):
    return pd.read_csv(file_path, sep=',', names=['sta', 'long', 'lat'], encoding="euc-kr", 
                       skiprows=1, dtype={'long': 'float', 'lat': 'float'})

def plot_stations(fig, df, style, color, label):
    fig.plot(x=df['long'].values, y=df['lat'].values, style=style, fill=color, pen="black", label=label)

# 설정
work_path = "/home/ish/DataProcessing_TRC/data/"
region = [128.79, 131.5, 35.10, 36.60]
out_file = os.path.join(work_path, "study_map_pohang.pdf")

# 데이터 로드
data_files = {
    'tide': "khoa_tide_pos_2024.csv",
    'current': "khoa_transect_pos_2024.csv",
    'buoy': "kma_buoy_pos_2024.csv"
}
data = {key: load_data(os.path.join(work_path, file)) for key, file in data_files.items()}

# 지도 생성
fig = pygmt.Figure()
fig.coast(region=region, projection="M12c", water="white", land="oldlace", shorelines="1/0.25p", frame=["af"])
fig.basemap(map_scale="g131/35.52+w50k+f+l", region=region)

# 관측소 플로팅
plot_stations(fig, data['tide'], "s0.3c", "red@30", "Tidal Station (KHOA)")
plot_stations(fig, data['current'], "c0.2c", "blue@40", "Ocean current Obs. (KHOA)")
plot_stations(fig, data['buoy'], "a0.3c", "blue", "Ocean Buoy (KMA)")

# 도시 이름 표시
cities = [("Pohang", 129.36, 36.00), ("Ulsan", 129.31, 35.56)]
for city, x, y in cities:
    fig.text(x=x, y=y, text=city, font="10p,Helvetica-Bold,black", justify="CM")

# 범례 추가
with pygmt.config(FONT_ANNOT_PRIMARY="8p"):
    fig.legend(box="+gwhite+pblack", position="JBR+jBR+o0.2c")

# 저장 및 표시
fig.savefig(out_file)
fig.show()