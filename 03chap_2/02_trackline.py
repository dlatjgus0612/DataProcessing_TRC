import pandas as pd
import pygmt
import os

# set Path 
work_path = "/home/ish/DataProcessing_TRC/data/"
track_data = work_path + "track_XY.txt"
out_file = os.path.join(work_path, "track_line_map.pdf")
with open(track_data, 'r', encoding='euc-kr') as file:
    df = pd.read_csv(file, sep= r'\s+', names=['longitude', 'latitude'],
                     dtype = {'longitude' : float, 'latitude' : float})
    
pygmt.config(FONT_TITLE = "6p")

fig = pygmt.Figure()
fig.basemap(projection='M8c', 
            region = [125.5, 127.5, 32.75, 33.75],
            frame = True)
# 온라인으로 기복 data 가져옴, : 인터넷 연결 필수
fig.grdimage(grid = "@earth_relief_01m", shading = "+d")
fig.coast(shorelines = "0.5p")

# Draw Ship track line
fig.plot(x = df['longitude'], y = df['latitude'],
         style = "c0.01c", 
         pen = "0.05p,red",
         label = "Survey track (Badaro-1)")

fig.legend(position="JTR+jTR+o0.2c", box = "+gwhite+pblack+p0.5p")
fig.basemap(map_scale="g127/32.9+w50k+f+l",
            frame = ["a", "+tSurvey track line"])

fig.savefig(out_file)
fig.show()