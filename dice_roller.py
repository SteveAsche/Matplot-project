"""Plotting a random walk"""
import matplotlib.pyplot as plt 
from dice_roll import DiceRoll 



#Create a randomwalk set
dicrole = DiceRoll()
dicrole.fill_rolls()

numset = list(range(2,13))
x_values = list(range(2,13))

#print(type(x_values))
streak_count = 1
streak_dict = {}
	#Set the size of the plotting window
	#plt.figure(figsize=(10, 6))
for i in range(len(dicrole.die1)):
	sumup = dicrole.die1[i] + dicrole.die2[i]
	#print(sumup)
	numset[(sumup-2)] += 1
	if sumup == 7:
		if streak_count in streak_dict:
			streak_dict[streak_count] += 1
			streak_count = 1
		else:
			streak_dict[streak_count] = 1
			streak_count = 1
	else:
		streak_count += 1

if streak_count in streak_dict:
	streak_dict[streak_count] += 1
	streak_count = 1
	
else:
	streak_dict[streak_count] = 1
	streak_count = 1




	#point_numbers = list(range(rw.num_points))


	#plot it
plt.scatter(x_values, numset, edgecolor='none', s=15)



	#Remove the axes

plt.show()

print(streak_dict)
