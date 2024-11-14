import matplotlib.pyplot as plt 
x=[1,2,3,4,5]
y1=[10,15,13,18,20]
y2=[8,12,10,15,17]
plt.plot(x,y1,linestyle='-',label='Solid Line')
plt.plot(x,y2,linestyle='--',label='Dashed Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.legend()
plt.show()