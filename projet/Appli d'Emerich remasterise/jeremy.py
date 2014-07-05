import pygame
from pygame.locals import *
from Card import Card
from Player import Player
import Fonctions


pioche = Fonctions.loadCardSet("../Deck.txt")
player1 = Player(pioche)
player2 = Player(pioche)
	
def afficheVie(life):
	if life <= 30 and life >= 22.6:
		vie = pygame.image.load("barre100.png").convert_alpha()
	elif life <= 22.5 and life >= 15:
		vie = pygame.image.load("barre75.png").convert_alpha()
	elif life <= 14.5 and life >= 7.6:
		vie = pygame.image.load("barre50.png").convert_alpha()
	elif life <= 7.5 and life >= 1:
		vie = pygame.image.load("barre25.png").convert_alpha()
	else:
		vie = pygame.image.load("barre0.png").convert_alpha()
	fenetre.blit(vie, (965, 674))
	pygame.display.flip()

def afficheCard(fene, liste):
	toto = 1

'''def name(j1):
	#pygame.init()
	screen = pygame.display.set_mode((800, 100))
	name = ""
	font = pygame.font.Font(None, 50)
	continu = 1
	while continu == 1:
		for evt in pygame.event.get():
			if evt.type == KEYDOWN:
				if evt.unicode.isalpha():
					name += evt.unicode
				elif evt.key == K_BACKSPACE:
					name = name[:1]
				elif evt.key == K_RETURN:
					j1 = name
					continu = 0
					print(continu)
					return j1
			elif evt.type == QUIT:
				continu = 0
		screen.fill((0, 0, 0))
		block = font.render(name, True, (255, 255, 255))
		rect = block.get_rect()
		rect.center = screen.get_rect().center
		screen.blit(block, rect)
		pygame.display.flip()'''

pygame.init()

fenetre = pygame.display.set_mode((1280, 720))

life = 0
app = 1
accueil = 1
jeu = 0

while app:

	if accueil == 1:
		print("accueil")
		fond = pygame.image.load("accueil.jpg").convert()
		fenetre.blit(fond, (0, 0))

		button_play = pygame.image.load("play_game.png").convert_alpha()
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

		fond = pygame.image.load("../Images/plateau.jpg").convert()
		fenetre.blit(fond, (0, 0))

		'''carte = pygame.image.load("../cards/Ace.png").convert_alpha()
		carte = pygame.transform.scale(carte, (133, 181))
		fenetre.blit(carte, (400, 0))'''

		joueur2 = pygame.font.Font(None, 50).render("Joueur 2", 1, (255, 255, 255))
		fenetre.blit(joueur2, (100, 0))

		joueur1 = pygame.font.Font(None, 50).render("Joueur 1", 1, (255, 255, 255))
		fenetre.blit(joueur1, (1080, 670))


		#fenetre.blit(button_retour, (button_retour_x, button_retour_y))
		#fenetre.blit(button_pioche,(button_pioche_x, button_pioche_y))
		#afficheVie(25)
		pygame.display.flip()
		#life = 30

	while jeu:
		souris_x = 0
		souris_y = 0
		for event in pygame.event.get():
			if event.type == QUIT:
				app = 0
				jeu = 0
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					souris_x = event.pos[0]
					souris_y = event.pos[1]
		posCardX = 400
		for card in player1.hand:
			carteImage = pygame.image.load("../cards/" + card.name + ".png").convert_alpha()
			#print("../cards/" + card.name + ".png")
			carteImage = pygame.transform.scale(carteImage, (133, 181))
			fenetre.blit(carteImage, (posCardX, 540))
			if souris_x > posCardX and souris_x < posCardX + 143 and souris_y > 0 and souris_y < 540

			posCardX += 153

		posCardX = 400
		for card in player2.hand:
			carteImage = pygame.image.load("../cards/dos.png").convert_alpha()
			carteImage = pygame.transform.scale(carteImage, (133, 181))
			fenetre.blit(carteImage, (posCardX, 0))
			posCardX += 153
		pygame.display.flip()
		
		vieJoueur1 = pygame.font.Font(None, 30).render("Vie : " + str(player1.health), 1, (255, 255, 255))
		fenetre.blit(vieJoueur1, (150, 50))
		vieJoueur2 = pygame.font.Font(None, 30).render("Vie : " + str(player2.health), 1, (255, 255, 255))
		fenetre.blit(vieJoueur2, (1130, 640))

		manaJoueur1 = pygame.font.Font(None, 30).render("Mana : " + str(player1.mana), 1, (255, 255, 255))
		fenetre.blit(manaJoueur1, (150, 70))
		manaJoueur2 = pygame.font.Font(None, 30).render("Mana : " + str(player2.mana), 1, (255, 255, 255))
		fenetre.blit(manaJoueur2, (1130, 620))
