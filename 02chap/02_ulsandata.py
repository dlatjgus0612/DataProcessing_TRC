import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

work_path = '/Users/imseohyeon/Documents/TRC/DataProcessing_TRC/'
data = pd.read_csv('/Users/imseohyeon/Documents/TRC/DataProcessing_TRC/data/ulsan_tide_9503.dat',
                   sep = r'\s+',
                   skiprows = 1,
                   names= ['year', 'month', 'day', 'hour', 'minute', 'tide'],
                   dtype=str )

# generate new column 'data_info', integrate data and time info
data['date_info'] = data['year'] + "-" + data['month'] + "-" + data['day'] + " " + data['hour'] + ":" + data['minute']
# Extract tide data that str was changed to float
tide_level = data['tide'].astype('float64')

fig, ax = plt.subplots(figsize = (10,6))
ax.plot(pd.to_datetime(data["date_info"]),          #translate ax to datetime
        tide_level, 
        'b. ', 
        markersize=2, 
        alpha=0.40, 
        label = "tide level (cm)")

plt.title("Ulsan tide timeseries data", fontsize = 15)
plt.xlabel("Year", fontsize = 13)
plt.ylabel("Tide Level (cm)", fontsize = 13)
plt.grid(True)

dateFmt = mdates.DateFormatter('%Y')               #define time ax lable format
ax.xaxis.set_major_formatter(dateFmt)
plt.xticks(rotation = 45)
plt.show()
