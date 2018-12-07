"""Class for betting scenarios"""
class Scenario():
	"""A class representing a betting scenarios"""
	""" A list of Odds
	Pass/Come 1:1
	Don't Pass 1:1
	Taking Odds
	6 and 8 6:5
	5 and 9 3:2
	4 and 10 2:1
	Laying Odds
	6 and 8 5:6
	5 adn 9 2:3
	4 and 10 1:2
	Place Bets
	6 and 8 7:6
	5 and 9 7:5
	4 and 10 9:5
	"""


	def __init__(self, place_bets, max_odds):
		"""Initialize the variables that will be used in the scenario"""
		self.place_bets = place_bets
		self.max_odds = max_odds
		self.winnings = 0
		self.wager = 5
		self.pass_odds_multiple_limit = 3
		self.bank = 500

	def set_bets(self): #this is after the point is set
		for i in self.place_bets:
			self.bank -= 5
		self.bank -= self.wager * self.pass_odds_multiple_limit

	def point_made(self, dice_sum): #Situation when the shooter makes the point
		"""Pay the pass line and pay the pass line odds"""
		self.winnings += self.wager
		self.bank += self.wager
		if dice_sum == 4 or dice_sum == 10:
			self.winnings += self.wager * 2
			self.bank += self.wager * 2
		elif dice_sum == 5 or dice_sum == 9:
			self.winnings += self.wager * 3/2
			self.bank += self.wager * 3/2
		else:
			self.winnings += self.wager * 6/5
			self.bank += self.wager * 6/5

	def come_out(self):
		self.bank -= self.wager







	def compare_field(self, dice_sum):
		"""Compare the dice value and update the winnings"""
		if dice_sum in self.place_bets:
			#winning on the field bets
			if dice_sum == 4 or dice_sum == 10:
				self.winnings += self.wager * 9/5
				self.bank += self.wager * 9/5
			elif dice_sum == 5 or dice_sum == 9:
				self.winnings += self.wager * 7/5
				self.bank += self.wager * 7/6
			else:
				self.winnings += self.wager * 7/6
				self.bank += self.wager * 7/6
				

