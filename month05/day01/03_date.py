import numpy as np
date = ["2011-01-01", "2011", "2011-02", "2012-01-01", "2012-02-01 10:10:00"]

dates = np.array(date)

# 时间类型转换
dates = dates.astype("M8[D]")
print(dates,dates.dtype)
print(dates[2]-dates[1])


