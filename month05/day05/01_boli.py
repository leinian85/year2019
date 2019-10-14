# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo11_loadtxt.py 加载文件
"""
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
# 日期转换函数


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    return t

dates, opening_prices, highest_prices,\
    lowest_prices, closing_prices = np.loadtxt(
        '../素材/da_data/aapl.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6),
        dtype='M8[D], f8, f8, f8, f8',
        unpack=True, converters={1: dmy2ymd})

# 绘制收盘价的折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=16)
mp.xlabel('Date', fontsize=14)
mp.ylabel('closing price', fontsize=14)
mp.grid(linestyle=":")

import matplotlib.dates as md
# 拿到坐标轴
ax = mp.gca()
# 设置主刻度定位器为周定位器（每周一显示主刻度文本）
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
# 设置次刻度定位器为日定位器
ax.xaxis.set_minor_locator(md.DayLocator())

dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, color='dodgerblue',
        label='AAPL', linestyle='--',
        linewidth=2,alpha=0.6)

ma5 = np.zeros(closing_prices.size -4)
for i in range(ma5.size):
    ma5[i] = closing_prices[i:i+5].mean()


ma10 = np.zeros(closing_prices.size-9)
for i in range(ma10.size):
    ma10[i] = closing_prices[i:i+10].mean()


# mp.plot(dates[4:], ma5, color='green',
#         label='MA5', linestyle=':',
#         linewidth=2,alpha=0.6)

# mp.plot(dates[9:], ma10, color='blue',
#         label='MA10', linestyle=':',
#         linewidth=2,alpha=0.6)

kernel = np.ones(5)/5
ma52 = np.convolve(closing_prices,kernel,'valid')
# mp.plot(dates[4:],ma52,color='red',label = 'MA-52',linewidth = 7,alpha = 0.7)

kernel = np.ones(10)/10
ma510 = np.convolve(closing_prices,kernel,'valid')
# mp.plot(dates[9:],ma510,color='red',label = 'MA-510',linewidth = 7,alpha = 0.7)


stds = np.zeros(ma5.size)
for i in range(stds.size):
    stds[i] = closing_prices[i:i+5].std()

upper = ma5 + 2*stds
lower = ma5 - 2*stds

mp.plot(dates[4:],upper,color = 'red',label = 'UPPER')
mp.plot(dates[4:],lower,color = 'red',label = 'LOWER')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
