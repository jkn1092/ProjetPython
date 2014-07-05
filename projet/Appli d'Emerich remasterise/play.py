#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

#Partie A 
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

def menu(enable) :

	options =[ ') Attaquer', ') Placer un nouvel esclave', ') Piocher', ') Passer son tour', ') Abandonner']

	choices = [0]
	for i in range(len(options)) :
		if i < len(enable) :
			if enable[i]:
				print(choices[-1] + 1, options[i])
				choices.append(choices[-1] + 1)
		else:
			print(choices[-1] + 1, options[i])
			choices.append(choices[-1] + 1)

	return choices[1:]

def selectCard(field, slaveWanted) :
	for s in field :
		if s.name == slaveWanted :
			return s
	return None

def place( player ) :
	while True:
		answer = input( "Quel joueur voulez-vous placer?  " )
		card = selectCard(player.hand, answer)
		if card == None :
			print( "Vous n'avez pas d'esclave ", answer, " en main." )
		else:
			break

	player.field.append( card )
	player.hand.remove( card )
	



def draw( player , deck ) :
	player.hand.append( deck.pop( deck.index( random.choice( deck ) ) ) )

    

def attack( player, ennemy ) :

	if len(player.field) > 1 :
		while True :
			answer = input( "Avec qui voulez-vous attaquer ? \n" )
			card1 = selectCard( player.field, answer )
			if card1 == None :
				print( "Vous n'avez pas d'esclave", answer, "sur le terrain" )

			elif card1.cost > player.mana :
				print( "Vous n'avez pas suffisament de mana pour utiliser cet esclave \n" )
			
			else :
				break
	else :
		card1 = player.field[0]


	if len(ennemy.field) <= 0:
		print( "L'ennemie n'a pas d'esclave sur le terrain " )
		print( "Attaque sur l'ennemie\n" )
		card1.fight( ennemy )
		return

	for slave in ennemy.field :
		slave.printCard( )

	print( "Chef de l'armée adverse: ", ennemy.name, " ,points de vie:", ennemy.health)

	while True :
		answer = input( "Qui voulez-vous attaquer ? " )

		card2 = selectCard( ennemy.field, answer )
		
		if card2 == None and answer != ennemy.name :
			print( "Il y n'y a pas d'ennemie", answer )
		
		else :
			break

	if card2 == None :
		card2 = ennemy
		
	card1.fight( card2 )
	if card2!= ennemy :
		if card2.isAlive()==False:
			ennemy.field.remove(card2)
	if card1.isAlive()==False:
		player.field.remove(card1)
	
	
def playerTurn(player, ennemy,deck):
	print("=======================DEBUT PHASE DE JEU JOUEUR ", player.name ,"=======================\n\n")
	choice = False
	winner = None
	player.desc()

	enable = [ False, False, False ]

	if len(player.field) <= 0 :
		print( "Pas d'esclave sur le terrain" )

	else :
		print( "Esclave(s) sur le terrain:" )
		for slave in player.field :
			slave.printCard(  )
			if slave.cost <= player.mana :
				enable[0] = True

	print()

	if len(player.hand) <= 0 :
		print( "Pas d'esclaves en main" )
		
	else :
		print( "Esclave(s) en main:" )
		for slave in player.hand :
			slave.printCard()
		enable[1] = True

	print()

	if deck:
		enable[2] = True

	available = menu(enable)

	while True:
		try:
			answer = int(input("Quel est votre choix? "))
			if answer not in available:
				raise ValueError()
			break
		except ValueError:
			print("Option non valide\n\n")


	for i in range(len(enable)):
		if enable[i] == False and answer - 1 >= i:
			answer += 1


	if answer == 1 :
		attack(player,ennemy)
	elif answer == 2 :
		place(player)
	elif answer == 3 :
		draw(player, deck)
	elif answer == 4 :
		return True
	else :
		return False

	return True
	
def loadCardSet(nameFile) :

		file = open(nameFile)
		listServant = []
		for line in file:
			cardSet = []
			for word in line.split():
				if word.isnumeric():
					cardSet.append(int (word))
				else:
					cardSet.append(word)
			listServant.append(Card(cardSet[0], cardSet[2], cardSet[1], cardSet[3]))
		file.close
		listCard = listServant
		return listServant
		
def main():
	nbPart = 0
	w1 = w2 = 0

	j1Name = input( "Comment voulez-vous appeler le joueur 1? " )
	j2Name = input( "Comment voulez-vous appeler le joueur 2? " )

	while True:

		print('-------------------')
		print('| Nouvelle partie |')
		print('-------------------')

		deck = loadCardSet("slaveList.txt")
		p1 = Player( j1Name,deck  )
		p2 = Player( j2Name,deck  )

		turn = 0

		while True:
			if turn % 2 == 0 : 
				if playerTurn( p1, p2,deck ) == False :
					p1.health = 0
				p1.mana += 1
			else :
				if playerTurn( p2, p1,deck ) == False :
					p2.health = 0
				p2.mana += 1

			if p1.health <= 0 or p2.health <= 0 :
				break

			turn += 1

		print( "\n" )

		if p1.health <= 0 and p2.health <= 0 :
			print( "Match nul!" )
		elif p1.health <= 0 :
			print( "Victoire de", p2.name, "en", turn, "tour(s)!" )
			w1 += 1
		else :
			print( "Victoire de", p1.name, "en", turn, "tour(s)!" )
			w2 += 1

		while True:
			answer = input( "Voulez-vous rejouer ? (o/n) " )
			if answer.lower() not in ( 'oui', 'non', 'o', 'n') :
				print( "Mauvaise réponse" )
			break

		nbPart += 1

		if answer.lower() in ( 'n', 'non'):
			break

	print( "\n\n" )
	print( "Nombre de partie(s) total:", nbPart )
	print( "Nombre de victoire(s) de", p1.name, ":", w1 , "=>", 100*w1/nbPart, "%")
	print( "Nombre de victoire(s) de", p2.name, ":", w2 , "=>", 100*w2/nbPart, "%")
	return 0


if __name__ == "__main__":
	main()
