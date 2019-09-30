#encoding:utf-8
import matplotlib.pyplot as mp

mp.figure("A Figure",facecolor = "gray")
mp.plot([0,1],[0,1])
mp.plot([1,2],[1,0])
# mp.figure("B figure",facecolor="lightgray")
# mp.plot([1,0],[1,0])

# 设置窗口的参数
mp.title("A Figure",fontsize = 18)
mp.xlabel("time",fontsize = 14)
mp.ylabel("prince",fontsize = 14)
mp.tick_params(labelsize = 18)
mp.grid(linestyle = ":")
mp.tight_layout()
mp.show()