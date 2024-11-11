import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os 

work_path = '/Users/imseohyeon/Documents/TRC/DataProcessing_TRC'
file_path = 'data/pohang_sun_2021-2023.csv'
out_file1 = work_path + '/data/sun_monthly_avg_pohang.csv'
out_file2 = work_path + '/data/sun_3yr_avg_pohang.csv'
out_file3 = work_path + '/data/sun_3yr_insolation_pohang.png'

df = pd.read_csv(file_path, sep=',', names= ['ID', 'station', 'obs_date', 'sun_hr', 'sun_insolation'], encoding='euc-kr', skiprows=1)

# Extract year, month 
df["obs_date"] = pd.to_datetime(df["obs_date"])
df["year"] = df["obs_date"].dt.year
df["month"] = df["obs_date"].dt.month

# Mean monthly Insolation (월평균 일조량) & Sunshine_hour (일사량)
monthly_avg = df.groupby(['year', 'month'])[['sun_insolation', 'sun_hr']].mean().reset_index()
# Calculate mean of monthly Insolation / 월별 평균 일조량 전체 평균 계산
tot_monthly_avg = monthly_avg.groupby('month')['sun_insolation'].mean().reset_index()

months = ['Jan.', 'Feb.', 'Mar.', 'Apr', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']

# plot yearly 
for year, monthly_avg_group in monthly_avg.groupby('year'):
    plt.plot(monthly_avg_group['month'], monthly_avg_group['sun_insolation'], '-o', label=str(year))
    plt.plot(tot_monthly_avg['month'], tot_monthly_avg['sun_insolation'], color = 'darkgray', linewidth = 6, alpha = 0.4)

# Specify plt
plt.xlabel('Month')
plt.ylabel(r'Monthly Averaged Insolation (ML/m$^2$)')
plt.title('Sun Insolation (Pohang)')
plt.legend()
plt.grid(True)
# Specify legend
plt.legend(loc = 'best')
plt.xticks(range(1, 13), months)
plt.ylim(0.5, 2.0)

plt.savefig(out_file3)
plt.show()

monthly_avg.to_csv(out_file1, header=True, index=False, encoding='euc-kr', float_format='%.2f')
tot_monthly_avg.to_csv(out_file2, header=True, index=False, encoding='euc-kr', float_format='%.2f')
print("CSV 파일로 저장 성공. ")
