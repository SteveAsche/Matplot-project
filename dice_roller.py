"""Plotting a random walk"""
import matplotlib.pyplot as plt 
from dice_roll import DiceRoll 
from die import Die 
import pygal

def check_win(sumup, point_on, point_set=0):
	win = "Continue"
	if sumup == 7 and point_on:
		# this is a losing role
		win = "lose"
		
	elif (sumup == 2 or sumup == 3 or sumup == 12) and not point_on:
		#this is a losing role
		win = "lose"
		
	elif not point_on and sumup == 7:
		#This is a win
		win = "win"
		
	elif point_on and sumup == point_set:
		win = "win"
	return win


def takeSecond(elem):
	return elem[1]


#Create a randomwalk set
numrolls = 400
dicrole = DiceRoll(numrolls)
dicrole.fill_rolls()

numset = list(range(2,13))
x_values = list(range(2,13))

# BTW rolls per hour are about 102

#print(type(x_values))
streak_count = 1
streak_dict = {}
point_on = False
point_set = 0

lose_count = 0
win_count = 0
pass_count = 0
money_pass = 0


	#Set the size of the plotting window
	#plt.figure(figsize=(10, 6))
for i in range(len(dicrole.die1)):
	sumup = dicrole.die1[i] + dicrole.die2[i]
	#print(sumup)

	outcome = check_win(sumup, point_on, point_set)


	if not point_on: #if the point is not on, the point will stay off if the roll is 2, 3, 12, 7
		if sumup == 2 or sumup == 3 or sumup == 12 or sumup == 7:
			point_set = 0
			point_on = False
		else:
			point_set = sumup
			point_on = True
	#the outcome of the roll is based on whether the point is on or off 


	if outcome == "lose":
		lose_count += 1
		point_on = False
		point_set = 0
	elif outcome == "win":
		win_count += 1
		point_on = False
		point_set = 0
	else:
		pass_count += 1
		if sumup == 2 or sumup == 3 or sumup == 12 or sumup == 11:
			pass
		else:
			money_pass +=1

	#numset is the list that tallies the number of times a given number comes up
	numset[(sumup-2)] += 1

	#a 7 ends the streak no matter what
	
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
x_value_string_list = []
for i in x_values:
	x_value_string_list.append(str(i))

#Visualize the results

hist = pygal.Bar()

hist.title = "Results of rolling two dice " + str(numrolls) + " times"
hist.x_labels = x_value_string_list
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('DiceRolls', numset)
hist.render_to_file('die_vidual.svg')

	#plot it
#plt.scatter(x_values, numset, edgecolor='none', s=15)



	#Remove the axes

#plt.show()

print(streak_dict)
print("Wins: " + str(win_count))
print("Losses: " + str(lose_count))
print("Passes: " + str(pass_count))
print("Field payoffs: " + str(money_pass))

print("Total Rolls: " + str(win_count + lose_count + pass_count))

roll_listy = list(streak_dict.values())
roll_listx = list(streak_dict.keys())

#Zip the lists ans sort them 


zipped_lists = list(zip(roll_listx, roll_listy))
print(zipped_lists)

#sorted(zipped_lists, key=takeSecond, reverse=True)
new_zippy = sorted(zipped_lists, key = lambda x: x[0])
new_zippy = sorted(new_zippy, key=lambda x: x[1], reverse = True)

print(new_zippy)

holdlistx = []
holdlisty = []

for i in new_zippy:
	holdlistx.append(i[0])
	holdlisty.append(i[1])

print(holdlistx)
print(holdlisty)



roll_listx_string = []
for i in holdlistx:
	roll_listx_string.append(str(i))

#Zip the lists ans sort them 



print(roll_listy)
print(roll_listx)
print(len(roll_listy))
print(len(roll_listx))

hist = pygal.Bar()

hist.title = "Freqency of streaks rolling two dice " + str(numrolls) + " times"
hist.x_labels = roll_listx_string
hist.x_title = "Length of streak"
hist.y_title = "Occurrence of streak"

hist.add('Streaks', holdlisty)
hist.render_to_file('streak_vidual.svg')


#plt.scatter(roll_listx, roll_listy, edgecolor = 'none', s = 15)

#plt.show()
