import pygame
from pygame.locals import *
import cards
import Player

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
		fond = pygame.image.load("medieval.jpg").convert()
		fenetre.blit(fond, (0, 0))

		button_play = pygame.image.load("play.png").convert_alpha()
		button_play_x = 479
		button_play_y = 260
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
		button_retour = pygame.image.load("retour.png").convert_alpha()
		button_retour_x = 1092
		button_retour_y = 597

		button_pioche = pygame.image.load("piocher.png").convert_alpha()
		button_pioche_x = 945
		button_pioche_y = 597


		fond = pygame.image.load("mapff.png").convert()
		fenetre.blit(fond, (0, 0))
		fenetre.blit(button_retour, (button_retour_x, button_retour_y))
		fenetre.blit(button_pioche,(button_pioche_x, button_pioche_y))
		afficheVie(25)
		pygame.display.flip()
		life = 30

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
		if souris_x > button_retour_x and souris_x < (button_retour_x + 150) and souris_y > button_retour_y and souris_y < (button_retour_y + 69):
			jeu = 0
			accueil = 1
		if souris_x > button_pioche_x and souris_x < (button_pioche_x + 170) and souris_y > button_pioche_y and souris_y < (button_pioche_y + 69):
			life -= 10
			afficheVie(life);