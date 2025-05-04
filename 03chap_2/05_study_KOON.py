"""
KHOA All data with Observatory Location

This script generates a map with observatory locations from KHOA tide, ocean, buoy, radar, and stations.
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

# 지도를 그릴 객체 설정
fig = pygmt.Figure()

# 지도의 위경도 범위
region = [123, 132.6, 31, 39]
work_path = "/home/ish/DataProcessing_TRC/data/"

# 범위, 도곽, scale bar, 해안선 설정
pygmt.config(FONT_TITLE="13p")
fig.coast(region=region, projection="M12c", 
        water="white", land="lightgray", shorelines="1/0.25p",
        frame=["af", "WSne+tThe Korea Ocean Observation Network"])
        #frame="afg")   # 위경도 라인을 그리기
fig.basemap(map_scale="g124.5/31.5+w200k+f+l")

# 관측소별 symbol 작성(조위관측소, 해양관측소, 해양관측부이, HF-Radar, 해양과학기지)
file_path1 = os.path.join(work_path, "khoa_tide_pos_2024.csv")  # 조위관측소
file_path2 = os.path.join(work_path, "khoa_ocean_sta_2024.csv")  # 해양관측소
file_path3 = os.path.join(work_path, "khoa_buoy_all_2024.csv")  # 해양관측부이
file_path4 = os.path.join(work_path, "khoa_HF_grid_all_2024.csv")  # HF-Radar
file_path5 = os.path.join(work_path, "khoa_res_station_2024.csv")  # 해양과학기지

df1 = pd.read_csv(file_path1, sep=',', names=['sta', 'long', 'lat'], encoding="euc-kr", 
                skiprows=1, dtype={'long': 'float', 'lat': 'float'})
df2 = pd.read_csv(file_path2, sep=',', names=['sta', 'long', 'lat'], encoding="euc-kr", 
                skiprows=1, dtype={'long': 'float', 'lat': 'float'})
df3 = pd.read_csv(file_path3, sep=',', names=['sta', 'long', 'lat'], encoding="euc-kr", 
                skiprows=1, dtype={'long': 'float', 'lat': 'float'})
df4 = pd.read_csv(file_path4, sep=',', names=['long', 'lat'], encoding="euc-kr",  # HF-radar는 위경도만 있음
                skiprows=1, dtype={'long': 'float', 'lat': 'float'})
df5 = pd.read_csv(file_path5, sep=',', names=['sta', 'long', 'lat'], encoding="euc-kr", 
                skiprows=1, dtype={'long': 'float', 'lat': 'float'})

x1, y1 = (df1['long'].values, df1['lat'].values)
x2, y2 = (df2['long'].values, df2['lat'].values)
x3, y3 = (df3['long'].values, df3['lat'].values)
x4, y4 = (df4['long'].values, df4['lat'].values)
x5, y5 = (df5['long'].values, df5['lat'].values)

# 관측소별 symbol 뿌리기
fig.plot(x=x1, y=y1, style="s0.2c", fill="red", pen="black",
        label="Tidal Station (53)")  # 조위관측소 (십자가 모양)
fig.plot(x=x2, y=y2, style="d0.2c", fill="green", pen="black",
        label="Ocean Station (3)")  # 해양관측소 diamond (d)
fig.plot(x=x4, y=y4, style="c0.02c", fill="blue", 
        label="HF-Radar (44)")  # HF-radar circle
fig.plot(x=x3, y=y3, style="a0.2c", fill="black", pen="black", 
        label="Ocean Buoy (36)")  # Buoy star (a)
fig.plot(x=x5, y=y5, style="t0.3c", fill="blue", pen="black", 
        label="Ocean Research Station (3)")  # 해양과학기지

# 범례 표시 및 폰트 지정
with pygmt.config(FONT_ANNOT_PRIMARY="9p"):
        fig.legend(box="+gwhite+pblack", position="JBR+jBR+o0.2c")

# 파일 저장 및 지도 표출
out_file = os.path.join(work_path, "study_map_khoa.pdf")
fig.savefig(out_file)
fig.show()