import pygmt
import os
import pandas as pd
import numpy as np 

# set Path 
work_path = "/home/ish/DataProcessing_TRC/data/"
out_file = os.path.join(work_path, "contour_pygmt1.pdf")

# set figure and grid (need network)
fig = pygmt.Figure()
grid = pygmt.datasets.load_earth_relief(resolution='30s', region=[144.0, 145.5, 13, 14.0],
                                        registration="gridline")

# set expression


# plot and save
fig.savefig(out_file)
fig.show()