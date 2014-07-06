import pygame
from pygame.locals import *
from Card import Card
from Player import Player
import Fonctions

def majAffichagePlateau(fenetre):
	
	fenetre.blit(fond, (0, 0))
	fenetre.blit(button_turn,(1150,320))
			
	piocheInfos = pygame.font.Font(None, 30).render(str(len(pioche)) + " cartes restantes", 1, (255, 255, 255))
	fenetre.blit(piocheInfos, (1080, 400))
			
			#Affichage infos Joueur
	fenetre.blit(joueur1, (1100, 670))
	vieJoueur1 = pygame.font.Font(None, 30).render("Vie : " + str(player1.health), 1, (255, 255, 255))
	fenetre.blit(vieJoueur1, (1150, 640))
	manaJoueur1 = pygame.font.Font(None, 30).render("Mana : " + str(player1.mana), 1, (255, 255, 255))
	fenetre.blit(manaJoueur1, (1150, 620))
								
	fenetre.blit(joueur2, (20, 0))
	vieJoueur2 = pygame.font.Font(None, 30).render("Vie : " + str(player2.health), 1, (255, 255, 255))
	fenetre.blit(vieJoueur2, (70, 50))
	manaJoueur2 = pygame.font.Font(None, 30).render("Mana : " + str(player2.mana), 1, (255, 255, 255))
	fenetre.blit(manaJoueur2, (70, 70))
			
	#Affichage carte sur terrain
	posCardX = 812
	for c in player1.field:
		carteImage = pygame.image.load("cards/" + c.name +".png").convert_alpha()
		carteImage = pygame.transform.scale(carteImage, (133, 181))
		fenetre.blit(carteImage, (posCardX, 363))
		posCardX -= 153
				
	posCardX = 812
	for c in player2.field:	
		carteImage = pygame.image.load("cards/" + c.name +".png").convert_alpha()
		carteImage = pygame.transform.scale(carteImage, (133, 181))
		fenetre.blit(carteImage, (posCardX, 183))
		posCardX -= 153	


def playTurnGraphic(fenetre, player, ennemy, tourDePlayer1):
	
	# Deployer une carte
	pygame.init()
	turn = True;
	
	souris_x = 0
	souris_y = 0
	cartePlayer = -1
	carteEnnemy = -1
	
	while turn:
		
		for event in pygame.event.get():

			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					souris_x = event.pos[0]
					souris_y = event.pos[1]
					
					if souris_x > 1150 and souris_x < (1150 + 127) and souris_y > 320 and souris_y < (320 + 65):
						turn = False
			
					posCardTerrainX = 812
			
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
								print("Vous n'avez pas assez de mana.")
								souris_x = 0
								souris_y = 0
							else:
								print("Carte placer")
								carteImage = pygame.image.load("cards/" + nomCarte +".png").convert_alpha()
								carteImage = pygame.transform.scale(carteImage, (133, 181))
								
								nbCartesField = len(player.field)
								
								positionNouvelleCarte = 153 * nbCartesField
								
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
					
					PosFieldX = 812
					if tourDePlayer1 :
						posFieldPlayerY = 363
						posFieldEnnemY = 183
					else:
						posFieldPlayerY = 183
						posFieldEnnemY = 363
					
					carteChoisi = 0
					for cardField in player.field:
						
						if souris_x > PosFieldX and souris_x < (PosFieldX + 133) and souris_y > posFieldPlayerY and souris_y < (posFieldPlayerY + 181):
							cartePlayer = carteChoisi
							print("Carte choisi")
						
						PosFieldX -= 153
						carteChoisi += 1
					
					PosFieldX = 812
					if cartePlayer >= 0:
						carteChoisi = 0
						for cardField in ennemy.field:
							
							if souris_x > PosFieldX and souris_x < (PosFieldX + 133) and souris_y > posFieldEnnemY and souris_y < (posFieldEnnemY + 181):
								carteEnnemy = carteChoisi
								player.field[cartePlayer].fight(ennemy.field[carteEnnemy])
								print("Carte attaquer !")
								
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

fenetre = pygame.display.set_mode((1280, 720))

life = 0
app = 1
accueil = 1
jeu = 0

while app:

	if accueil == 1:
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
			accueil = 0
			jeu = 1

		nbPart = 0
		w1 = w2 = 0

	if jeu == 1:
		print("jeu")

		#initialisationAppli()

		fond = pygame.image.load("Images/plateau.jpg").convert()
		#fenetre.blit(fond, (0, 0))

		joueur2 = pygame.font.Font(None, 50).render("Joueur 2", 1, (255, 255, 255))
		#fenetre.blit(joueur2, (100, 0))

		joueur1 = pygame.font.Font(None, 50).render("Joueur 1", 1, (255, 255, 255))
		#fenetre.blit(joueur1, (1080, 670))

		button_turn = pygame.image.load("Images/turn.png").convert_alpha()
		
		pygame.display.flip()

	while jeu:
		
		while player1.isAlive() and player2.isAlive():
						
			souris_x = 0
			souris_y = 0
			for event in pygame.event.get():
				if event.type == QUIT:
					app = 0
					jeu = 0
							
			if tourDePlayer1 == True:
				
				player1.mana += 1				
				if len(pioche) > 0:
					player1.pickUp(pioche)
				
				majAffichagePlateau(fenetre)
				
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
										
				playTurnGraphic(fenetre, player1, player2, tourDePlayer1) 
				tourDePlayer1 = False

			else:
				player2.mana += 1								
				if len(pioche) > 0:
					player2.pickUp(pioche)
				
				majAffichagePlateau(fenetre)
				
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
					
				playTurnGraphic(fenetre, player2, player1, tourDePlayer1) 
				tourDePlayer1 = True
				
			player1.clean()
			player2.clean()
				
				
		
