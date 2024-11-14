import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[8,10,15,13,18]
y2=[10,15,18,16,20]
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
ax1.plot(x,y1)
ax1.set_title("First Subplot")
ax2.plot(x,y2)
ax2.set_title("Second Subplot")
plt.suptitle("Figure with two subplots")
plt.show()