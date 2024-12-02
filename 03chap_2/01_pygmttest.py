import pygmt
import os

work_path = "/home/ish/DataProcessing_TRC/data/"
out_file = os.path.join(work_path, "my_pygmt_map.pdf")

pygmt.show_versions()

region = [123, 132.6, 31, 39]
fig = pygmt.Figure()
fig.coast(region=region, shorelines = True)
fig.show()
fig.savefig(out_file)