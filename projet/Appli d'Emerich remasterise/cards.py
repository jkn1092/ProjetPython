class Card:
	
	def __init__(self, name, health, attack, cost):
		self.name = name
		self.health = health
		self.attack = attack
		self.cost = cost
		
	def printCard(self, displayMana=True):
		if displayMana:
			print( self.name, "( attack : ", self.attack, "/ life : ", self.health, ") : cost :", self.cost )
		else:
			print( self.name, "(", self.attack, "/", self.health, ")")

	def fight(self, slave):
		slave.health -= self.attack
		if hasattr( slave , 'attack' ) :
			self.health -= slave.attack
	
	def isAlive(self):
		if self.health > 0:
			return True
		else:
			return False