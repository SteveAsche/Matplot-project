"""learning to scatter plot"""
import matplotlib.pyplot as plt 



x_values = []
y_values = []

for i in range(1,1001):
	x_values.append(i)
	y_values.append(i ** 3)

#x_values = list(range(1,1001))
#y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values, c = y_values, cmap =  plt.cm.Blues, edgecolor = 'none', s=20)

#Set chart title
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)

#set size if tick marks
plt.tick_params(axis = 'both', which= 'major', labelsize = 14)

plt.axis([0,1100, 0, 1100000000])

plt.show()
