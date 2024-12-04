import folium.features
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
    return df, icon_path, outfile

def createmap():
    map_center = [36, 128]
    map1 = folium.Map(location=map_center, zoom_start=7)
    return map1

def ploton(df, icon_path, map1):
    for index, row in df.iterrows():
        custom_icon = folium.features.CustomIcon(icon_image=icon_path, icon_size=(30,30))
        folium.Marker([row['lat'], row['lon']],
                      popup=row['station'], icon=custom_icon).add_to(map1)

if __name__ == "__main__":
    df, icon_path, outfile = setpath()
    m = createmap()
    ploton(df, icon_path, m)
    m.save(outfile)