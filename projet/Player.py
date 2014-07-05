'''
Created on 3 juin 2014

@author: Jkn1092
'''
import random
from Card import Card

class Player:
    
    def __init__(self, deck):
        self.health = 30
        self.mana = 1
        self.field = []
        self.hand = []
        
        cpt = 0
        while cpt < 4:
            nb = random.randint(1,len(deck) - 1)
            self.hand.append(deck[nb])
            del deck[nb]
            cpt += 1
            
    
    def pickUp(self, deck):
        pickUpCard = random.randint(0,len(deck)-1)
        self.hand.append(deck[pickUpCard])
        del deck[pickUpCard]
    
    
    def deploy(self,deployedCard):
        
        if self.hand[deployedCard].cost > self.mana:
            return False
        else:
            self.mana = self.mana - self.hand[deployedCard].cost
            self.field.append(self.hand[deployedCard])
            del self.hand[deployedCard]
            return True
    
    
    def clean(self):
        
        i = 0
        for c in self.field:
            if c.health < 1:
                del self.field[i]
            i += 1
    
    
    def isAlive(self):    
        
        if(self.health > 0):
            return True
        else:
            return False
    
    
    def setMana(self, mana):
        self.mana = mana
    
    def hasProvoke(self):
        j = 0
        for card in self.field:
            if card.hasProvoke():
                return j
            j += 1
        return -1
    
    def hasShield(self):
        for card in self.field:
            if card.hasShield():
                return True
        return False
    
    def hasHidden(self):
        for card in self.field:
            if card.isHidden():
                return True
        return False