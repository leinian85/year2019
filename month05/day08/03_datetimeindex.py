import pandas as pd

dates = pd.date_range('2019-2-27',periods=7)
print(dates)

dates = pd.date_range('2019-10-1',periods=7,freq='M')
print(dates)

dates = pd.bdate_range('2019-10-1',periods=7)
print(dates)
