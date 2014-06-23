'''
Created on 3 juin 2014

@author: Jkn1092
'''
import random

class Player:
    
    def __init__(self, deck):
        self.health = 30
        self.mana = 1
        self.field = []
        self.hand = []
        
        cpt = 0
        while cpt < 4:
            nb = random.randint(0,deck.length-1)
            self.hand.append(deck[nb])
            del deck[nb]
            cpt += 1
            
    
    def pickUp(self, listCard):
        pickUpCard = random.randint(0,listCard.length-1)
        self.hand.append(listCard[pickUpCard])
        del listCard[pickUpCard]
    
    
    def deploy(self,deployedCard):
        
        if self.hand[deployedCard].cost > self.mana:
            return False
        else:
            self.mana = self.mana - self.hand[deployedCard].cost
            self.field.append(self.hand[deployedCard])
            del self.hand[deployedCard]
            return True
    
    
    def clean(self):
        
        for c in self.hand:
            if c.health < 1:
                del self.hand[c]
    
    
    def isAlive(self):    
        
        if(self.health > 0):
            return True
        else:
            return False
    
    
    def setMana(self, mana):
        self.mana = mana
        
    
def playTurn(player, ennemy):
    
    print("Qui voulez-vous attaquer ? ")
    i = 1
    for c in ennemy.field:
        print(i ," : ", c.printCard)
        i =+ 1
    carteEnnemy = input()
    
    print("Avec qui voulez-vous attaquer ? ")
    i = 1
    for c in player.field:
        print(i ," : ", c.printCard)
        i =+ 1
    cartePlayer = input()
    
    player.field[cartePlayer].fight(ennemy.field[carteEnnemy])
    
    carteDeploy = False
    while carteDeploy == False:     
        print("Quels serviteurs voulez-vous placer sur le terrain ?")
        i = 1
        for c in player.hand:
            print(i ," : ", c.printCard)
            i =+ 1
        cartePlacer = input()
        carteDeploy = player.deploy(player.hand[cartePlacer])
        