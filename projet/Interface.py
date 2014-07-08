import pygame
from pygame.locals import *
from Card import Card
from Player import Player
import Fonctions

def majAffichagePlateau(fenetre,historiques):
	
	fenetre.blit(fond, (0, 0))
	fenetre.blit(button_turn,(1150,270))
		
	piocheInfos = pygame.font.Font(None, 20).render(str(len(pioche)) + " cartes restantes", 1, (255, 255, 255))
	fenetre.blit(piocheInfos, (1140, 335))

	#Affichage historiques
	posHistoriquesY = 330
	for c in historiques:
		infosPlateau = pygame.font.Font(None,20).render(c, 1, (255, 255, 255))
		fenetre.blit(infosPlateau,(10, posHistoriquesY))
		posHistoriquesY += 21
				
	#Affichage infos Joueur
	fenetre.blit(joueur1, (1100, 670))
	vieJoueur1 = pygame.font.Font(None, 30).render("Vie : " + str(player1.health), 1, (255, 255, 255))
	fenetre.blit(vieJoueur1, (1150, 640))
	manaJoueur1 = pygame.font.Font(None, 30).render("Mana : " + str(player1.mana), 1, (255, 255, 255))
	fenetre.blit(manaJoueur1, (1150, 620))
	fenetre.blit(iconeJoueur1, (1150,400))
									
	fenetre.blit(joueur2, (20, 0))
	vieJoueur2 = pygame.font.Font(None, 30).render("Vie : " + str(player2.health), 1, (255, 255, 255))
	fenetre.blit(vieJoueur2, (70, 50))
	manaJoueur2 = pygame.font.Font(None, 30).render("Mana : " + str(player2.mana), 1, (255, 255, 255))
	fenetre.blit(manaJoueur2, (70, 70))
	fenetre.blit(iconeJoueur2, (70,100))
			
	#Affichage carte sur terrain
	posCardX = 965
	for c in player1.field:
		carteImage = pygame.image.load("cards/" + c.name +".png").convert_alpha()
		carteImage = pygame.transform.scale(carteImage, (133, 181))
		fenetre.blit(carteImage, (posCardX, 363))
		posCardX -= 153
				
	posCardX = 965
	for c in player2.field:	
		carteImage = pygame.image.load("cards/" + c.name +".png").convert_alpha()
		carteImage = pygame.transform.scale(carteImage, (133, 181))
		fenetre.blit(carteImage, (posCardX, 183))
		posCardX -= 153	

	pygame.display.flip()

def majAffichageCards(fenetre, player1, player2):
	infosCards = None
	posCardsY = 0
	for c in player1.field:
		infosCards = pygame.font.Font(None,20).render(c.name + " Sante: " + str(c.health), 1, (255, 255, 255))
		fenetre.blit(infosCards,(1100, posCardsY))
		posCardsY += 21
	
	for c in player2.field:
		infosCards = pygame.font.Font(None,20).render(c.name + " Sante: " + str(c.health), 1, (255, 255, 255))
		fenetre.blit(infosCards,(1100, posCardsY))
		posCardsY += 21
	
	pygame.display.flip()

def playTurnGraphic(fenetre, player, ennemy, tourDePlayer1,historiques):
	
	# Deployer une carte
	pygame.init()
	turn = True;
	
	souris_x = 0
	souris_y = 0
	cartePlayer = -1
	carteEnnemy = -1
	
	while turn:
		
		for event in pygame.event.get():
			if event.type == QUIT:
					pygame.display.quit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					souris_x = event.pos[0]
					souris_y = event.pos[1]
					
					#Passer son tour
					if souris_x > 1150 and souris_x < (1150 + 100) and souris_y > 270 and souris_y < (270 + 60):
						turn = False

					#Placer un joueur
					if len(player.field) < 5:	
						
						posCardTerrainX = 965
						if tourDePlayer1 :
							posCardX = 965
							posCardY = 540
							posCardTerrainY = 363
						else:
							posCardX = 200
							posCardY = 0
							posCardTerrainY = 183
						
						carteChoisi = 0
						carteDeploy = False
						for card in player.hand:
							
							nomCarte = card.name
							if souris_x > posCardX and souris_x < (posCardX + 133) and souris_y > posCardY and souris_y < (posCardY + 181):
								carteDeploy = player.deploy(carteChoisi)
								if carteDeploy == False:
									historiques.append("Vous n'avez pas assez de mana.")
									souris_x = 0
									souris_y = 0
								else:
									historiques.append("Vous avez placer la carte " + nomCarte + ".")
									carteImage = pygame.image.load("cards/" + nomCarte +".png").convert_alpha()
									carteImage = pygame.transform.scale(carteImage, (133, 181))
									
									nbCartesField = len(player.field)
									
									#Enlever le -1 pour decaler la carte
									positionNouvelleCarte = 153 * (nbCartesField - 1)
									
									fenetre.blit(carteImage, ((posCardTerrainX - positionNouvelleCarte) , posCardTerrainY))
									pygame.display.flip()
									souris_x = 0
									souris_y = 0
							
							carteChoisi += 1
				
							if tourDePlayer1 :    
								posCardX -= 153
							else:
								posCardX += 153
				
					#Attaque un sbire
					PosFieldX = 965
					if tourDePlayer1 :
						posFieldPlayerY = 363
						posFieldEnnemY = 183
						posEnnemyX = 70
						posEnnemyY = 100
					else:
						posFieldPlayerY = 183
						posFieldEnnemY = 363
						posEnnemyX = 1150
						posEnnemyY = 400
						
					carteChoisi = 0
					for cardField in player.field:
						
						if souris_x > PosFieldX and souris_x < (PosFieldX + 133) and souris_y > posFieldPlayerY and souris_y < (posFieldPlayerY + 181):
							cartePlayer = carteChoisi
							historiques.append("Vous avez choisi la carte : " + cardField.name + ".")
						
						PosFieldX -= 153
						carteChoisi += 1
					
					PosFieldX = 965
					if cartePlayer >= 0:
						
						if souris_x > posEnnemyX and souris_x < (posEnnemyX + 100) and souris_y > posEnnemyY and souris_y < (posEnnemyY + 214):
							ennemy.health = ennemy.health - player.field[cartePlayer].attack
							historiques.append("Vous avez attaque le joueur.")
						
						
						carteChoisi = 0
						for cardField in ennemy.field:
							
							if souris_x > PosFieldX and souris_x < (PosFieldX + 133) and souris_y > posFieldEnnemY and souris_y < (posFieldEnnemY + 181):
								carteEnnemy = carteChoisi
								player.field[cartePlayer].fight(ennemy.field[carteEnnemy])
								historiques.append("Vous avez attaque la carte " + cardField.name + ".")
								
								cartePlayer = -1
								carteEnnemy = -1
								souris_x = 0
								souris_y = 0
							
							PosFieldX -= 153	
							carteChoisi += 1

pioche = Fonctions.loadCardSet("Deck.txt")
player1 = Player(pioche)
player2 = Player(pioche)

tourDePlayer1 = True

pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)

fenetre = pygame.display.set_mode((1280, 720))
sonFight = pygame.mixer.Sound("sound/fight.wav")
sonWin = pygame.mixer.Sound("sound/win.wav")
sonThemeCombat = pygame.mixer.Sound("sound/combat.wav")

historiques = []

app = True
accueil = True
jeu = False

while app:
		
	if accueil:
		print("accueil")
		fond = pygame.image.load("Images/accueil.jpg").convert()
		fenetre.blit(fond, (0, 0))

		button_play = pygame.image.load("Images/play_game.png").convert_alpha()
		button_play_x = 550
		button_play_y = 350
		fenetre.blit(button_play, (button_play_x, button_play_y))
		
		pygame.display.flip()
	
	while accueil:
		souris_x = 0
		souris_y = 0
		for event in pygame.event.get():
			if event.type == QUIT:
				app = 0
				accueil = 0
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					souris_x = event.pos[0]
					souris_y = event.pos[1]
		if souris_x > button_play_x and souris_x < (button_play_x + 322) and souris_y > button_play_y and souris_y < (button_play_y + 69):
			accueil = False
			jeu = True

		nbPart = 0
		w1 = w2 = 0

	if jeu:
		print("jeu")
		historiques.append("Commencement de la partie")
		
		sonFight.play()
		#initialisationAppli()

		fond = pygame.image.load("Images/plateau.jpg").convert()

		joueur2 = pygame.font.Font(None, 50).render("Joueur 2", 1, (255, 255, 255))
		iconeJoueur2 = pygame.image.load("Images/player.png").convert_alpha()
		iconeJoueur2 = pygame.transform.scale(iconeJoueur2, (100, 214))

		joueur1 = pygame.font.Font(None, 50).render("Joueur 1", 1, (255, 255, 255))		
		iconeJoueur1 = pygame.image.load("Images/player.png").convert_alpha()
		iconeJoueur1 = pygame.transform.scale(iconeJoueur1, (100, 214))
		
		button_turn = pygame.image.load("Images/pass.png").convert_alpha()
		
		pygame.display.flip()
		quitte = 0
	while jeu:
		sonThemeCombat.play(1000)
		
		while player1.isAlive() and player2.isAlive() and quitte == 0:				
			souris_x = 0
			souris_y = 0
			for event in pygame.event.get():
				if event.type == QUIT:
					quitte = 1
					app = 0
					jeu = 0
					print(quitte)
							
			if tourDePlayer1 == True:
				historiques.append("Au tour du joueur 1")
				
				player1.mana += 1				
				if len(pioche) > 0 and len(player1.hand) < 6:
					player1.pickUp(pioche)
				
				majAffichagePlateau(fenetre, historiques)
				majAffichageCards(fenetre, player1, player2)
				
				#Affichage carte en mains
						
				posCardX = 965
				for card in player1.hand:
					carteImage = pygame.image.load("cards/" + card.name + ".png").convert_alpha()
					carteImage = pygame.transform.scale(carteImage, (133, 181))
					fenetre.blit(carteImage, (posCardX, 540))
					posCardX -= 153
		
				posCardX = 200
				for card in player2.hand:
					carteImage = pygame.image.load("cards/dos.png").convert_alpha()
					carteImage = pygame.transform.scale(carteImage, (133, 181))
					fenetre.blit(carteImage, (posCardX, 0))
					posCardX += 153
				pygame.display.flip()
										
				playTurnGraphic(fenetre, player1, player2, tourDePlayer1, historiques) 
				tourDePlayer1 = False

			else:
				historiques.append("Au tour du joueur 2")
				
				player2.mana += 1								
				if len(pioche) > 0 and len(player2.hand) < 6:
					player2.pickUp(pioche)
				
				majAffichagePlateau(fenetre, historiques)
				majAffichageCards(fenetre, player1, player2)
				
				#Affichage carte en mains
						
				posCardX = 965
				for card in player1.hand:
					carteImage = pygame.image.load("cards/dos.png").convert_alpha()
					carteImage = pygame.transform.scale(carteImage, (133, 181))
					fenetre.blit(carteImage, (posCardX, 540))
					posCardX -= 153
		
				posCardX = 200
				for card in player2.hand:
					carteImage = pygame.image.load("cards/" + card.name + ".png").convert_alpha()
					carteImage = pygame.transform.scale(carteImage, (133, 181))
					fenetre.blit(carteImage, (posCardX, 0))
					posCardX += 153
				pygame.display.flip()
					
				playTurnGraphic(fenetre, player2, player1, tourDePlayer1, historiques) 
				tourDePlayer1 = True
				
			player1.clean()
			player2.clean()
			#sonThemeCombat.stop()
				
		if player1.isAlive():
			print("Player 1 a gagne. Player 2 a perdu.")
			historiques.append("Joueur 1 win. Joueur 2 lose.")
		else:
			print("Player 2 a gagne. Player 1 a perdu.")
			historiques.append("Joueur 2 win. Joueur 1 lose.")
			
		sonWin.play()
		jeu = False
		#app = False
	
		
