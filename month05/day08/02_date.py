import pandas as pd

date1 = pd.Series(['1905','2019-07','2018/1/09','2015/01-20 12:12:12','01-20-2015','01/Jun-2015'])
date1 = pd.to_datetime(date1)
print(date1)

print((date1-pd.to_datetime('2015-01-1')).dt.days)
print((date1-pd.to_datetime('2015-01-1')).dt.seconds)
for date in date1-pd.to_datetime('2015-01-1'):
    print(date,type(date))