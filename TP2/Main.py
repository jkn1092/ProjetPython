'''
Created on 14 juin 2014

@author: Jkn1092
'''

import pygame
from pygame.locals import*

if __name__ == '__main__':
    pygame.init()
    
    fenetre = pygame.display.set_mode((640, 480)) #Creation d'une fenetre
    #fond = pygame.image.load("wall.bmp").convert()
    #fenetre.blit(fond, (0,0))  
    
    #Chargement et collage du personnage
    carte = pygame.image.load("Cards/Zoro.png").convert()
    fenetre.blit(carte, (100,300))

    pygame.display.flip()
    
    fenetreActive = 1 #Permet de garder la fenetre active
    
    while(fenetreActive):
        continue