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
months = ['Jan.', 'Feb.', 'Mar.', 'Apr', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']

# Hourly Significant wave 
axs[0].plot(tot_monthly_avg['month'], tot_monthly_avg[choose_item],
            color = "yellow", linewidth = 6, alpha = 0.4)
for year, group in monthly_avg.groupby('year'):                             # plot loop for monthly item by grouped year
    axs[0].plot(group['month'], group[choose_item], '-o', label = str(year))
axs[0].set_xlabel("Month")
axs[0].set_ylabel("Significant Wave Height (m)")
axs[0].set_title("Significant Wave Height", fontsize = 14)
axs[0].legend(loc = 'upper left')
axs[0].grid(True)
axs[0].set_xticks(range(1,13))
axs[0].set_xticklabels(months)
axs[0].set_ylim(0, 3)                                                       # set range y ticks 0 ~ 5

# Calculate Monthly mean data 
monthly_data = df.groupby(['year', 'month'])[choose_item].mean().reset_index()

# Box plot for monthly wave height
sns.boxplot(x='month', y=choose_item, data=monthly_data, ax= axs[1])
axs[1].set_xlabel("Month")
axs[1].set_ylabel("Average Significant Wave Height (m)")
axs[1].set_title("Average Significant Wave Height", fontsize = 14)
axs[1].set_xticks(range(12))
axs[1].set_xticklabels(months)
axs[1].set_ylim(0, 3)                                                       # set range y ticks 0 ~ 5

plt.tight_layout()
plt.show()