"""Class for betting scenarios"""
class Scenario():
	"""A class representing a betting scenarios"""

	def __init__(self, field_bets, max_odds):
		"""Initialize the variables that will be used in the scenario"""
		self.field_bets = field_bets
		self.max_odds = max_odds
		self.winnings = 0
		self.wager = 5


	def compare_field(self, dice_sum):
		"""Compare the dice value and update the winnings"""
		for i in self.field_bets:
			if dice_sum == self.field_bets:
				#winning on the field bets
				self.winnings += self.wager
				

