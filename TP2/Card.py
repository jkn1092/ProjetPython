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

    
    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    
    def initPlayer(self, deck):
        player = {}
        player['health'] = 30
        player['mana'] = 1
          
        return player


def loadCardSet(nomFichier):
    f = open(nomFichier)
    deck = []
    for line in f:
        deck.append(Card(line.split()[0],line.split()[1],line.split()[2],line.split()[3]))
        
    return deck
