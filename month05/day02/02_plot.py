import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-np.pi, np.pi, 1000)
y = np.sin(x)
cosx = np.cos(x) / 2
# 设置坐标轴的范围
# mp.xlim(0,np.pi)
# mp.ylim(0,1.5)

# 修改x轴的刻度文本
values = [-np.pi, - np.pi / 2, 0, np.pi / 2, np.pi]
texts = [r"$-\pi$",r"$-\frac{\pi}{2}$","0","π/2","π"]
mp.xticks(values, texts)

# 修改坐标轴
ax = mp.gca()
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))

mp.yticks([-0.5,-1,0,1,1.5])



mp.plot(x, y,label=r"$y=sin(x)$")
mp.plot(x, cosx, linestyle="-.", linewidth=2, color="orangered",label=r"$y=\frac{1}{2}cos(x)$")

# 绘制特殊点
pointsx = [np.pi/2,np.pi/2]
pointsy = [1,0]
# mp.scatter(pointsx,pointsy,marker="o",s=70,color="red",label="smaple points",zorder=3)
mp.scatter(pointsx,pointsy)

# 在图表中为某个点添加备注。包含备注文本，备注箭头等图像的设置。
mp.annotate(
    r'$\frac{\pi}{2}$',			#备注中显示的文本内容
    xycoords='data',			#备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(np.pi/2, 1),	 				#备注目标点的坐标
    textcoords='offset points',	#备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(np.pi/2+2,3),				#备注文本的坐标
    fontsize=14,				#备注文本的字体大小
    arrowprops=dict()			#使用字典定义文本指向目标点的箭头样式
)

# 设置图例
mp.legend(loc="best")
mp.show()
