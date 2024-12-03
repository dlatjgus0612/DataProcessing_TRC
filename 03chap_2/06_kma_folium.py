import pandas as pd
import folium
import os

def setpath():
    work_path = '/home/ish/DataProcessing_TRC/data/'
    icon_path = os.path.join(work_path, 'weather_station_icon.png')
    data_path = os.path.join(work_path, 'kma_sun_st.csv')
    df = pd.read_csv(data_path, names=['station', 'lat', 'lon'],
                    encoding='euc-kr')
    outfile = os.path.join(work_path, 'my_folium_map.html')
    return outfile, df

def createmap():
    map_center = [36, 128]
    map = folium.Map(location=map_center, zoom_start=7)
    return map

def ploton(df):
    for index, row in df.iterrows():

if __name__ == "__main__":
    main()