import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,15,13,18,20]
plt.plot(x,y)
plt.grid(True,linestyle='--',linewidth=0.5)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot with dashed grid line")
plt.show()