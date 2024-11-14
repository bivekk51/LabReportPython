import numpy as np 
import matplotlib.pyplot as plt
x=np.random.rand(50)
y=np.random.rand(50)
plt.scatter(x,y,marker='o',label='Circle')
plt.scatter(x+0.5,y+0.5,marker='s',label='Square')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()