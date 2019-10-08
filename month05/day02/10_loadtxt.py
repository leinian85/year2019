import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    data = str(dmy, encoding='utf-8').split('-')
    return data[2] + "-" + data[1] + "-" + data[0]


dates, open_prices, max_prices, min_prices, clo_prices = np.loadtxt('../素材/da_data/aapl.csv',
                                                                    delimiter=',',
                                                                    usecols=(1, 3, 4, 5, 6),
                                                                    dtype='M8[D],f8,f8,f8,f8',
                                                                    unpack=True,
                                                                    converters={1: dmy2ymd})

mp.figure('AAPL',facecolor = 'lightgray')
mp.title('AAPL',fontsize = 18)
mp.xlabel('dates',fontsize = 16)
mp.ylabel('min prices',fontsize = 16)

ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_minor_locator(md.DayLocator())
mp.plot(dates,min_prices,color='red',label = 'APPL',linestyle='-',linewidth = 2)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
