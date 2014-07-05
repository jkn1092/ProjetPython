class Card:
    
    def __init__(self,name,health,attack,cost,provoke = False,shield = False,hide = False):
        self.name = name
        self.health = health
        self.attack = attack
        self.cost = cost
        self.provoke = provoke
        self.shield = shield
        self.hide = hide
    
    
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
    
    def hasProvoke(self):
        return self.provoke
    
    def hasShield(self):
        return self.shield
    
    def isHidden(self):
        return self.hide