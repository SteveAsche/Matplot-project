"""This is a weird testcase"""
import matplotlib.pyplot as plt 
from dice_roll import DiceRoll 


dicrole = DiceRoll()
print("Hello World")
shortlist = list(range(2,13))
print(type(shortlist))
print(dicrole.num_rolls)

print(len(dicrole.die1))
dicrole.fill_rolls()
print(len(dicrole.die1))

for item in range(len(dicrole.die1)):
	print(item)
