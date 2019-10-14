import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#将数据集分为五组，设定标签
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]   #男性的平均得分
women_means = [25, 32, 34, 20, 25]   #女性的平均得分

x = np.arange(len(labels))  # 标签位置
width = 0.35  # 宽度

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men') #在x - width/2处绘制男性平均得分的柱状图
rects2 = ax.bar(x + width/2, women_means, width, label='Women')   #在x + width/2处绘制女性平均得分的柱状图

#加上标签，标题和自定义x轴刻度标签等信息
ax.set_ylabel('Scores') #设置y轴文本
ax.set_title('Scores by group and gender') #设置柱状图标题
ax.set_xticks(x) #设置x轴刻度值
ax.set_xticklabels(labels) #设置x轴刻度标签文本
ax.legend()

#给每个矩阵添加上数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        #添加备注
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),  #备注目标点的坐标
                    xytext=(0, 3),  # 在x轴偏移0，在y轴偏移3
                    textcoords="offset points",  #备注文本所使用的坐标系
                    ha='center', va='bottom')
'''  
xy=(横坐标，纵坐标)  即目标点的坐标
xytext=(横坐标，纵坐标) 文字的坐标，指的是文字框最左边的坐标
xycoords='data',			#备注目标点所使用的坐标系（data表示数据坐标系）
textcoords='offset points',	#备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
ha=horizontalalignment 垂直对齐
va=verticalalignment 水平对齐
'''

autolabel(rects1)
autolabel(rects2)
#设置紧凑布局
fig.tight_layout()
plt.show()

