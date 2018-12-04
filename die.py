from random import randint

class Die():
	"""a class representing a single die"""

	def __init__(self, num_sides=6):
		"""default a six side die"""
		self.num_sides = num_sides

	def roll(self):
		"""Return a random value between 1 and 6"""

		return randint(1, self.num_sides)
		