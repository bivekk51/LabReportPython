import matplotlib.pyplot as plt 
import numpy as np 
data_bar=[5,10,15,7,12]
data_hist=np.random.normal(0,1,1000)
data_pie=[30,25,20,15,10]
data_box=np.random.normal(0,1,1000)

plt.figure()
plt.bar(range(len(data_bar)),data_bar)
plt.bar(range(len(data_bar)), data_bar)
plt.title("Bar Graph")
plt.show()

plt.figure()
plt.hist(data_hist, bins=20)
plt.title("Histogram")
plt.show()

plt.figure()
plt.pie(data_pie, labels=['A', 'B', 'C', 'D', 'E'], autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

plt.figure()
plt.boxplot(data_box)
plt.title("Box Plot")
plt.show()