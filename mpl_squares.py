import matplotlib.pyplot as plt 

squares = []
input_value = []

for i in range(1, 6):
	input_value.append(i)
	squares.append(i ** 2)

# Set the line thickness and width
plt.plot(input_value, squares, linewidth = 5)

#Set title and axis
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

#set tick marks
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()
