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


dates,bhp_closing_prices = np.loadtxt('../素材/da_data/bhp.csv',delimiter=',',unpack=True,usecols=(1,6),
                                      dtype='M8[D],f8',converters={1:dmy2ymd})
vale_closing_prices = np.loadtxt('../素材/da_data/vale.csv',delimiter=',',unpack=True,usecols=(6),
                                 dtype='f8')

# 绘制收盘价的折线图
# mp.figure('AAPL', facecolor='lightgray')
# mp.title('AAPL', fontsize=16)
# mp.xlabel('Date', fontsize=14)
# mp.ylabel('closing price', fontsize=14)
# mp.grid(linestyle=":")

mp.figure('BHP VALE',facecolor='lightgray')
mp.title('BHP',fontsize=16)
mp.xlabel('DATE',fontsize=16)
mp.ylabel('prices',fontsize=16)
mp.grid(linestyle=":")

xa = mp.gca()

import matplotlib.dates as md


# import matplotlib.dates as md
# # 拿到坐标轴
# ax = mp.gca()
# # 设置主刻度定位器为周定位器（每周一显示主刻度文本）
# ax.xaxis.set_major_locator(
#     md.WeekdayLocator(byweekday=md.MO))
# ax.xaxis.set_major_formatter(
#     md.DateFormatter('%d %b %Y'))
# # 设置次刻度定位器为日定位器
# ax.xaxis.set_minor_locator(md.DayLocator())
#
# dates = dates.astype(md.datetime.datetime)
# mp.plot(dates, closing_prices, color='dodgerblue',
#         label='AAPL', linestyle='--',
#         linewidth=2)
# mp.legend()
# mp.gcf().autofmt_xdate()
# mp.show()
