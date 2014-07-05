class Player:
	
	def __init__(self, name, deck) :
		self.hand = []
		while len(self.hand) < 4 :
			numCard = random.randint(0, len(deck) - 1)
			self.hand.append(deck[numCard])
			deck.remove(deck[numCard])
		self.name = name
		self.health = 3
		self.mana = 1
		self.field = []
	
	
		
	def pickUp(self, listCard) :
		print(self.name, " pioche une carte")
		numCard = random.randint(0, len(listCard) - 1)
		print(listCard[numCard])
		self.hand.append(listCard[numCard])
		listCard.remove(listCard[numCard])

	
	def deploy(self):
		print("\n =======================DEBUT PHASE ENVOIE SUR TERRAIN======================= \n \n ")
		self.desc()
		choice = False
		print("\nListe de vos serviteur dans votre main")
		for cardPlayer in self.hand :
			cardPlayer.printCard()
		if len(self.hand) > 0 :
			print("\nQuel serviteur voulez vous envoyer sur le terrain ?")
			nameServantGoToField = ""
			while (choice == False) :
				nameServantGoToField = input("Choisisez le nom du serviteur a envoyer ou 0 si vous ne voulez envoyer personne").lower()
				for card in self.hand :
					if nameServantGoToField == card.name.lower() and card.cost <= self.mana:
						choice = True
						self.field.append(card)
						self.hand.remove(card)
						self.setMana(self.mana - card.cost)
					elif nameServantGoToField == "0" :
						choice = True
		else :
			print("Vous n'avez aucune carte dans votre main")
		print("=======================FIN PHASE ENVOIE SUR TERRAIN======================= \n \n")
	

	def clean(self):
		for card in self.field :
			if card.isAlive() == False :
				self.field.remove(card)


	def desc(self) :
		print("Player ", self.name, " - health : ", self.health, " Mana : ", self.mana )	


	def isAlive(self):
		if self.health > 0:
			return True
		else:
			return False
	

	def setMana(self, mana) :
		self.mana = mana