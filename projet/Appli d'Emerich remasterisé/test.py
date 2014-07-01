import pygame
from pygame.locals import *
import cards
import Player

pygame.init()

fenetre = pygame.display.set_mode((1280, 720))

#Chargement et collage du fond
fond = pygame.image.load("medieval.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
button_play = pygame.image.load("play.png").convert_alpha()
button_play_x = 479
button_play_y = 260
fenetre.blit(button_play, (button_play_x, button_play_y))
#bouton practice
button_pratice = pygame.image.load("pratice.png").convert_alpha()
button_pratice_x = 451.5
button_pratice_y = 360
fenetre.blit(button_pratice, (button_pratice_x, button_pratice_y))
#bouton retour 
button_retour = pygame.image.load("retour.png").convert_alpha()
button_retour_x = 1092
button_retour_y = 597

button_pioche = pygame.image.load("piocher.png").convert_alpha()
button_pioche_x=945
button_pioche_y=597

souris_x=0
souris_y=0

pygame.display.flip()

def changeMenu (posx,posy,menu):
	if posx > button_play_x and posx < (button_play_x+322) and posy > button_play_y and posy < (button_play_y+69):
		return 1
	elif posx > button_pratice_x and posx < (button_pratice_x+322) and posy > button_pratice_y and posy < (button_pratice_y+69):
		return 2
	elif posx > button_retour_x and posx < (button_retour_x+185) and posy > button_retour_y and posy < (button_retour_y+60):
		return 0
	else : 
		return menu
def afficheVie(fene,life):
	#bouton vie 
	
	if life <=30 and life >=22.6 :
		vie = pygame.image.load("barre100.png").convert_alpha()
	elif life<=22.5 and life >=15 :
		vie = pygame.image.load("barre75.png").convert_alpha()
	elif life<=14.5 and life >=7.6 :
		vie = pygame.image.load("barre50.png").convert_alpha()
	elif life <=7.5 and life >=1 :
		vie = pygame.image.load("barre25.png").convert_alpha()
	else :
		vie = pygame.image.load("barre0.png").convert_alpha()
	fenetre.blit(vie,(965,674))
	
def afficheCard(fene,liste):
	toto=1

def name(j1):
	pygame.init()
	screen = pygame.display.set_mode((800, 100))
	name = ""
	font = pygame.font.Font(None, 50)
	cotinu=1
	while cotinu==1:
		for evt in pygame.event.get():
			if evt.type == KEYDOWN:
				if evt.unicode.isalpha():
					name += evt.unicode
				elif evt.key == K_BACKSPACE:
					name = name[:-1]
				elif evt.key == K_RETURN:
					j1=name
					cotinu=0
					print(cotinu)
					pygame.quit()
					return j1
			elif evt.type == QUIT:
				cotinu=0
		screen.fill ((0, 0, 0))
		block = font.render(name, True, (255, 255, 255))
		rect = block.get_rect()
		rect.center = screen.get_rect().center
		screen.blit(block, rect)
		pygame.display.flip()


#BOUCLE INFINIE
ssmenu=0
continuer = 1
while continuer:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:	#Si clic gauche
				souris_x = event.pos[0]
				souris_y = event.pos[1]
	
	ssmenu=changeMenu(souris_x,souris_y,ssmenu)
	if ssmenu !=0 :
		fond = pygame.image.load("mapff.png").convert() 
	else:
		fond = pygame.image.load("medieval.jpg").convert() 		
	#Re-collage
	fenetre.blit(fond, (0,0))
	if ssmenu ==0 :
		fenetre.blit(button_play, (button_play_x, button_play_y))
		fenetre.blit(button_pratice, (button_pratice_x, button_pratice_y))
	else :
		fenetre.blit(button_retour,(button_retour_x,button_retour_y))
		fenetre.blit(button_pioche,(button_pioche_x,button_pioche_y))
		afficheVie(fenetre,25)
		j1Name="toto"
		j1Name=name(j1Name)
		print (j1Name)
		j2Name = "toto"

	nbPart = 0
	w1 = w2 = 0

	pygame.display.flip()