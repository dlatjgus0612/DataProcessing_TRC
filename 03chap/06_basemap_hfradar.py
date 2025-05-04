import os
import csv

'''
1) Extract Flag or coordinate from folder
HF grid file format. / only Flag 0 calculate total vector
961 !   27  Number of grid points,  n   (Columns: x, y, flag, lon, lat, !, x-index, y-index)
        -22.50000   -22.50000   1   125.7670836 37.2533232  !   -15 -15
'''
folder_path = 'data/HF_grid'
output_path = 'data/grid_used_out.csv'

# take *.grd file list
grid_files = [f for f in os.listdir(folder_path) if f.endswith('.grd')]

# Open csv files by writing mode
with open(output_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for grid_file in grid_files:
        file_path = os.path.join(folder_path, grid_file)

        with open(file_path, "rb") as f:
            grid_data = f.readlines()

        # Extract row 3~5 data after column 27
        for row in grid_data[27:]:
            data = row.split()[2:5]
            if data[0].decode() == '0':          # data[0]'s flag (result) == 0
                writer.writerow([data[1].decode(), data[2].decode()]) #save only lat, lon

