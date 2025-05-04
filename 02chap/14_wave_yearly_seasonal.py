import pandas as pd
import matplotlib.pyplot as plt

data_path = "data/KMA_Ulleungdo_2014-2023.csv"
out_file = "data/Ulleungdo_seasonal_avg.csv"
choose_item = "sig_wave_ht"
df = pd.read_csv(data_path, sep=',', 
                 names= ['ID', 'obs_date', 'wind_speed', 'wind_direction', 
                         'air_pr', 'air_temp', 'water_temp', 'max_wave_hi', 'sig_wave_ht', 
                         'wave_period', 'wave_direction'],
                         encoding="EUC-KR", skiprows=1)

# Extract year and month 
df['obs_date'] = pd.to_datetime(df['obs_date'])
df['year'] = df['obs_date'].dt.year
df['month'] = df['obs_date'].dt.month

seasons = {'Spring' : [3,4,5], 'Summer' : [6,7,8], 'Fall' : [9,10,11], 'Winter' : [12, 1, 2]}
df['season'] = df['month'].map(lambda x : next(k for k, v in seasons.items() if x in v))

seasonal_avg = df.groupby(['year', 'season'])[choose_item].mean().reset_index()
season_colors = {'Spring' : "green", 'Summer' : "red", 'Fall' : "yellow", 'Winter' : "blue"}

# Generate figure
fig, axs = plt.subplots(figsize=(8, 4))
for season_name, group in seasonal_avg.groupby('season'):
    axs.scatter(group['year'], group[choose_item], 
                label = season_name, s = 60, marker='o', 
                color = season_colors[season_name], alpha = 0.5)
    axs.plot(group['year'], group[choose_item], color = season_colors[season_name], alpha = 0.7)
axs.set_title('Seasonal Averaged Significant Wave Height (2014-2023)')
axs.set_xlabel('Year')
axs.set_ylabel('Significant Wave Height (m)')
axs.legend()
axs.set_ylim(0, 2.5)
axs.set_yticks([0, 0.5, 1, 1.5, 2, 2.5])
axs.grid(True)
plt.show()
seasonal_avg.round(2).to_csv(out_file, index=False)