import matplotlib.pyplot as mp

mp.figure("A Figure",facecolor="lightgray")
for i in range(9):
    mp.subplot(3,3,i+1)
    mp.text(0.5,0.5,i+1,size="18",va = "center",ha="center")
    mp.xticks([])
    mp.yticks([])
mp.tight_layout()

mp.figure("B Figure",facecolor="lightgray")
for i in range(9):
    mp.subplot(3,3,i+1)
    mp.text(0.5,0.5,i+1,size="18",va = "center",ha="center")
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout()

mp.show()