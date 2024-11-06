import datetime

now = datetime.datetime.now()       #save current time
now_year = now.strftime('%Y')       #4-digits year
now_date = now.strftime('%y.%m.%d') #2-digits year, month, day
now_time = now.strftime('%H:%M')    #2-digits hour, minute
print(now_year, now_date, now_time)