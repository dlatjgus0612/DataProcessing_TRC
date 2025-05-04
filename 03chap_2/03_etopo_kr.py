import pygmt
import os
import pandas as pd


# set Path 
work_path = "/home/ish/DataProcessing_TRC/data/"
out_file = os.path.join(work_path, "contour_kr_bathymetry.pdf")

region = [124, 132, 33, 38]
# 온라인으로 기복 data 가져옴, : 인터넷 연결 필수
grid = pygmt.datasets.load_earth_relief(resolution='01m',               # 01m = 1분 (약 1.85km) 해상도를 의미
                                        region=region)                  

fig = pygmt.Figure()
fig.basemap(region = region, projection = 'M15c', frame = True)         # 메르카토르 투영법, 15cm 지도 크기 설정
fig.grdimage(grid = grid, cmap = 'geo')                                 # ground, ocean color
fig.grdcontour(grid=grid, levels = 100, annotation = 1000,              # contour set & draw 등고선 추가.
               limit = [-2500, 0], pen = '0.5p,black')                  # 100m 간격 등고선, 1000m마다 주석, -2500 ~ 0m 사이에서만 등고선 표시

fig.colorbar(frame = ["a2000f500", "x+lDepth (m)", "y+lm"])
fig.text(x=128, y=38.5, text="Bathymetry Map of Korea", 
         font = "15p,Helvetica-Bold",                                   # 잘 안보여서 글씨 키우기
         no_clip=True)                                                  # True 하면 안짤리고 나옴 
#fig.basemap(frame=['af', 'WSen+tBathymetry Map of Korea'])             # 그냥 축, frame으로 넣어줘도됨.
fig.savefig(out_file, dpi = 500)
fig.show()