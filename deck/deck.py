import random as rand

class Card:
	def __init__(self, value, suite, aceIsHigh, suitePriority = []):
		self.value = value
		self.suite = suite
		self.aceIsHigh = aceIsHigh
		self.suitePriority = suitePriority
	
	def __gt__(self, other):
		return self.value > other.value
	
	def __eq__(self, other):
		return self.value == other.value
	
	def __ge__(self, other):
		return self.value >= other.value

class Deck:
	def __init__(self, cardRange=(1,13), suites=('s','c','d','h'), jokers=0, aceIsHigh=False, enablePriority=False):
		self.cards = []
		for s in suites:
			for c in range(cardRange):
				self.cards.append(Card(c, s, aceIsHigh, suites))
		for _ in range(jokers):
			self.cards.append(Card(-1, 'wild', aceIsHigh, ))
	
	def shuffle(self):
		rand.shuffle(self.cards)
