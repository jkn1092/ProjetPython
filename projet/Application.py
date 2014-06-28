'''
Created on 28 juin 2014

@author: Jkn1092
'''
from projet import Fonctions
from Card import Card
from Player import Player

pioche = Fonctions.loadCardSet("Deck.txt")
    
player1 = Player(pioche)
player2 = Player(pioche)

tourDePlayer1 = True
    
while player1.isAlive() and player2.isAlive():
    
    if tourDePlayer1:
        print("Au tour de player 1 :")
        if len(pioche) > 0:
            player1.pickUp(pioche)
            
        Fonctions.playTurn(player1, player2)     
        tourDePlayer1 = False
        
    else:
        print("Au tour de player 2 :")
        if len(pioche) > 0:
            player2.pickUp(pioche) 
            
        Fonctions.playTurn(player2, player1)       
        tourDePlayer1 = True
        
    player1.clean()
    player2.clean()
        
if player1.isAlive():
    print("Player 1 a gagne. Player 2 a perdu.")
else:
    print("Player 2 a gagne. Player 1 a perdu.") 
    
print("Partie terminee !")
    