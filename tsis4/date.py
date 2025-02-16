from datetime import datetime, timedelta, date

tday = date.today()

#1
five_days = timedelta(days=5)
print("Date 5 Days Ago:", tday-five_days)
print()

#2
yesterday  = tday - timedelta(days = 1)
tomorrow = tday + timedelta(days = 1)
print("Yesterday:", yesterday)
print("Today:", tday)
print("Tomorrow:", tomorrow)
print()

#3
now = datetime.now()

now2 = now.replace(microsecond=0)
print("Datetime without microseconds:", now2)
print()


#4
date1_str = input("Enter first date (yyyy-mm-dd): ")
date2_str = input("Enter second date (yyyy-mm-dd): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

diff = abs(date1 - date2)  
print("Difference in seconds:", int(diff.total_seconds()))

