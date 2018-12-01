"""Application to create random walk class"""
from random import choice

class DiceRoll():
	"""A class to generate a string of dice rolls"""

	def __init__(self, num_rolls = 5000):
		"""Initialize attributes of a rollset"""
		self.num_rolls = num_rolls

		#All walks start at (0,0)
		self.die1 = [0]
		self.die2 = [0]

	def fill_rolls(self):
		"""Calculate the number of rolls"""
		#keep taking steps untile the walk reaches the desired length
		print("Filling rolls")
		for i in range(self.num_rolls):

			die1_roll = choice([1,2,3,4,5,6])
			die2_roll = choice([1,2,3,4,5,6])
			self.die1.append(die1_roll)
			self.die2.append(die2_roll)

			