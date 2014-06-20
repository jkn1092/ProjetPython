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
            
    