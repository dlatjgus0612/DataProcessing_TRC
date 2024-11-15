import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

file_paths = [
    'data/khoa_transect_pos_2024.csv',          # KHOA 해류관측정점
    'data/khoa_buoy_pos_2024.csv',              # KHOA 부이
    'data/khoa_res_station_2024.csv',           # KHOA 해양관측기기
    'data/khoa_tide_pos_2024.csv',              # KHOA 조위관측소
    'data/nifs_station_pos_2023.csv',           # NIFS 정선해양관측
    'data/kma_buoy_pos_2024.csv'                # KMA 기상관측부이
]