import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import pearsonr, spearmanr, kendalltau

# Load data
file_path = 'data/ulsan_kma_buoy_2016.csv'
df = pd.read_csv(file_path, names=['station', 'date', 'wind_spd', 
                                   'wind_dir', 'air_pr', 'air_temp', 
                                   'sea_temp', 'max_W_H', 'sig_W_H', 
                                   'wave_peri', 'wave_dir'],
                 skiprows=1, encoding="euc-kr")
df['date'] = pd.to_datetime(df['date'])  # Convert date column to datetime format

# Calculate wind speed and direction components
theta_rad = np.deg2rad(270 - df.wind_dir)
u_wind = df.wind_spd * np.cos(theta_rad)
v_wind = df.wind_spd * np.sin(theta_rad)

# Scatter Plot: Relationship between Wind Speed and Wave Height
plt.figure(figsize=(12, 6))

# Subplot 1: Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(df.wind_spd, df.max_W_H, alpha=0.2, color='blue')
plt.title('Relationship between Wind Speed and Wave Height')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Highest Wave Height (m)')
plt.grid(True)

# Subplot 2: Dual Axis Time Series
plt.subplot(2, 2, 2)
fig, ax1 = plt.gca(), plt.gca()

# Wind Speed Time Series
ax1.plot(df.date, df.wind_spd, color='orange', label='Wind Speed (m/s)')
ax1.set_ylabel('Wind Speed (m/s)', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# Significant Wave Height Time Series (Secondary Axis)
ax2 = ax1.twinx()
ax2.plot(df.date, df.sig_W_H, color='green', label='Significant Wave Height (m)')
ax2.set_ylabel('Significant Wave Height (m)', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Legend and title
fig.legend(loc='upper right')
plt.title('Time Series of Wind Speed and Significant Wave Height')

# Subplot 3: Cross-Correlation between Wind Speed and Significant Wave Height
lags = np.arange(-30, 31)  # Lag range from -30 to +30 days
cross_corr = [df['wind_spd'].corr(df['sig_W_H'].shift(lag)) for lag in lags]

plt.subplot(2, 2, 3)
plt.plot(lags, cross_corr, marker='o')
plt.title('Cross-Correlation between Wind Speed and Significant Wave Height')
plt.xlabel('Lag (days)')
plt.ylabel('Correlation Coefficient')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)

# Subplot 4: Rolling Correlation (7-day window) between Wind Speed and Significant Wave Height
rolling_corr = df['wind_spd'].rolling(window=7).corr(df['sig_W_H'])

plt.subplot(2, 2, 4)
plt.plot(df.date, rolling_corr, color='green')
plt.title('7-Day Rolling Correlation between Wind Speed and Significant Wave Height')
plt.xlabel('Date')
plt.ylabel('Rolling Correlation Coefficient')
plt.grid(True)

# Adjust the layout and show the plots
plt.tight_layout()
plt.show()

#----------------------------------------------------
# Clean the data by removing rows with missing values
df_cleaned = df.dropna(subset=['wind_spd', 'sea_temp', 'max_W_H'])

# Prepare data for Linear Regression
X = df_cleaned[['wind_spd', 'sea_temp']]  # 두 특성 모두 사용
# X2 = df_cleaned[['wind_spd']]  # wind_spd만 사용
y = df_cleaned['max_W_H']
# y2 = df_cleaned['max_W_H']

# Model training
model = LinearRegression()
model.fit(X, y)  # X에는 두 특성이 포함됨
# model.fit(X2, y2)  # X2는 wind_spd만 포함

# Predictions
y_pred = model.predict(X)  # X는 wind_spd와 sea_temp 모두 포함
# y_pred2 = model.predict(X2)  # X2는 wind_spd만 포함

# 결과 출력
print(f"R² Score between Wind Speed, Sea Temperature and Max Wave Height: {r2_score(y, y_pred)}")
# print(f"R² Score between Wind Speed and Max Wave Height: {r2_score(y2, y_pred2)}")


# Pearson Correlation
pearson_corr, _ = pearsonr(df_cleaned['wind_spd'], df_cleaned['max_W_H'])
print(f"Pearson Correlation between Wind Speed and Max Wave Height: {pearson_corr}")

# Spearman Correlation
spearman_corr, _ = spearmanr(df_cleaned['wind_spd'], df_cleaned['max_W_H'])
print(f"Spearman Correlation between Wind Speed and Max Wave Height: {spearman_corr}")

# Kendall Correlation
kendall_corr, _ = kendalltau(df_cleaned['wind_spd'], df_cleaned['max_W_H'])
print(f"Kendall Correlation between Wind Speed and Max Wave Height: {kendall_corr}")
