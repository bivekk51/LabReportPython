import numpy as np
import matplotlib.pyplot as plt 
x=np.random.rand(100)
y=np.random.rand(100)
colors=np.random.rand(100)
sizes=100*np.random.rand(100)
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='viridis')
plt.colorbar()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter plot with color and size")
plt.show()