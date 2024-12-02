import pygmt
import os

import pandas as pd
import pygmt
import os

# set Path 
work_path = "/home/ish/DataProcessing_TRC/data/"
out_file = os.path.join(work_path, "contour_pygmt1.pdf")

fig = pygmt.Figure()
grid = pygmt.datasets.load_earth_relief(resolution='30s', region=[144.0, 145.5, 13, 14.0],
                                        registration="gridline")

# 온라인으로 기복 data 가져옴, : 인터넷 연결 필수
fig.grdimage(grid = grid, projection = 'M10c', cmap = 'oleron', frame = ['af', 'WSne'])
fig.grdcontour(grid=grid, levels = 500, annotation = 1000)

fig.basemap(map_scale="g145.16667/13.16667+w20k+f+l",
            box = "+gwhite")
fig.colorbar(frame = ["a1000", "x+lElvation", "y+lm"])

fig.savefig(out_file)
fig.show()