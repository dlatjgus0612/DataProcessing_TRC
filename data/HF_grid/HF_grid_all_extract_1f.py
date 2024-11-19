# 특정 폴더에 있는 grd 파일을 전부 읽어 위경도 자료만 추출하는 코드 
# dev date : 2024.2.7
# development by Peter
# file name : HF_grid_all_extract_1f.py

# # HF-radar 그리드 파일 포멧은 다음과 같으며 flag 0만 실제 사용하는 격자임
# 961 ! 27 Number of grid points, n (Columns: x, y, flag, lon, lat, !, x-index, y-index)
#     -22.50000     -22.50000    1    125.7670836   37.2533232   ! -15  -15
#     -22.50000     -21.00000    1    125.7670382   37.2668387   ! -15  -14

import os
import csv

# HF_gridfile 폴더의 경로
folder_path = "C:/Python312_2023/HF_grid"
# 저장할 csv 파일 경로
output_path = "C:/Python312_2023/HF_grid/grid_all.csv"

# *.grd 파일 목록을 가져옵니다.
grid_files = [f for f in os.listdir(folder_path) if f.endswith(".grd")]

# csv 파일을 쓰기 모드로 열어줍니다.
with open(output_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # 파일들을 차례차례 불러옵니다.
    for grid_file in grid_files:
        # 파일 경로
        file_path = os.path.join(folder_path, grid_file)

        # 파일을 읽습니다.
        with open(file_path, "rb") as f:
            grid_data = f.readlines()

        # 28행 이후의 4열과 5열의 데이터를 추출합니다.
        for row in grid_data[27:]:
            data = row.split()[3:5]  # 4열과 5열만 추출
            writer.writerow([data[0].decode(), data[1].decode()])