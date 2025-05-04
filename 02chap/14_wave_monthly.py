import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = "data/KMA_Ulleungdo_2014-2023.csv"
out_file = "data/Ulleungdo_monthly_avg.csv"
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
# Group month+year, calculate mean -> group month only, calculate mean
monthly_avg = df.groupby(['year', 'month'])[choose_item].mean().reset_index()
tot_monthly_avg = monthly_avg.groupby('month')[choose_item].mean().reset_index()

# Generate figure
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Hourly Significant wave 
axs[0].plot(df['obs_date'], df[choose_item], marker = 'o', markersize= 1.5, linestyle='none')
axs[0].set_ylabel("Significant Wave Height (m)")
axs[0].set_title("Time Series of Significant Wave Height", fontsize = 14)
axs[0].grid(True)

# Monthly Significant wave
axs[1].plot(monthly_avg.index, monthly_avg[choose_item], marker = 'o', color='b', linestyle='-')
axs[1].set_xticks(range(0, len(monthly_avg), 12))
axs[1].set_xticklabels(monthly_avg['year'].unique(), rotation=45)           # Set ticks with row's unique row. rotation 45 degree label
axs[1].set_xlabel("Year")
axs[1].set_ylabel("Significant Wave Height (m)")
axs[1].set_title("Monthly Average of Wave Height (sig.)")
axs[1].grid(True)

plt.tight_layout()
plt.show()

monthly_avg.to_csv(out_file, index=False, encoding="euc-kr", float_format='%.2f')
print("CSV로 파일 저장 성공")