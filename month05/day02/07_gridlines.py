import matplotlib.pyplot as mp

mp.figure("Grid",facecolor="lightgray")
ax = mp.gca()

# mp.ylim(1,2000)
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(100))
ax.yaxis.set_minor_locator(mp.MultipleLocator(10))

ax.grid(which="major",axis = "both",color="red",linewidth=0.75)

y = [1,10,100,1000,100,10,1]
# mp.plot(y,"o-",color = "dodgerblue")
mp.semilogy(y,"o-",color = "dodgerblue")
mp.show()