import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[10,15,13,18,20]
y2=[8,12,10,15,17]
y3=[5,10,15,10,5]
plt.plot(x,y1,color='red',label='Line1')
plt.plot(x,y2,color='green',label='Line2')
plt.plot(x,y3,color='blue',label='Line3')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('3 Line plot')
plt.legend()
plt.show()