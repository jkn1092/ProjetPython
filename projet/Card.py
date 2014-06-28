'''
Created on 23 mai 2014

@author: Jkn1092
'''
class Card:
    
    def __init__(self,name,health,attack,cost):
        self.name = name
        self.health = health
        self.attack = attack
        self.cost = cost
    
    
    def printCard(self,displayMana = True):
        if displayMana:
            print(self.name , " (" , self.attack , "/" , self.health , ") : " , self.cost)
        else:
            print(self.name, " (" , self.attack , "/" , self.health , ")")
    
    
    def fight(self, card):
        self.health = self.health - card.attack
        card.health = card.health - self.attack

    
    def cardAlive(self):
        if self.health > 0:
            return True
        else:
            return False
        
