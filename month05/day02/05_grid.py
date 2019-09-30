import matplotlib.gridspec as mg
import numpy as np
import matplotlib.pyplot as mp

mp.figure("A Figure",facecolor="lightgray")
gs = mg.GridSpec(3,3)
mp.subplot(gs[0,:2])
mp.text(0.5,0.5,1,va = "center",ha = "center")
mp.xticks([])
mp.yticks([])

mp.subplot(gs[0:2,2])
mp.text(0.5,0.5,2,va = "center",ha = "center")
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1:2,1:2])
mp.text(0.5,0.5,3,va = "center",ha = "center")
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1:,0])
mp.text(0.5,0.5,4,va = "center",ha = "center")
mp.xticks([])
mp.yticks([])

mp.subplot(gs[2:,1:])
mp.text(0.5,0.5,5,va = "center",ha = "center")
mp.xticks([])
mp.yticks([])

mp.tight_layout()

mp.show()