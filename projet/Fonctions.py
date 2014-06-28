'''
Created on 28 juin 2014

@author: Jkn1092
'''

from Card import Card

def loadCardSet(nomFichier):
    f = open(nomFichier)
    deck = []
    
    for line in f:
        name = line.split()[0]
        health = int(line.split()[1])
        attack = int(line.split()[2])
        mana = int(line.split()[3])
        deck.append(Card(name,health,attack,mana))
              
    f.close()    
    return deck


def playTurn(player, ennemy):
    
    
    #Attaquer joueur
    
    print("Qui voulez-vous attaquer ? ")
    
    i = 0
    for c in ennemy.field:
        print(i , ":")
        c.printCard(False)
        i += 1
    
    print(i ," : Joueur ennemi (", ennemy.health, " points de sante)")
    print (i + 1 ," : Ne rien faire ")
        
    carteEnnemy = input()
    carteEnnemy = int(carteEnnemy)
    
    if carteEnnemy <= i:
        print("Avec qui voulez-vous attaquer ? ")
        
        j = 0  
        for c in player.field:
            print(j , ":")
            c.printCard()
            j += 1
        
        print (j ," : Annuler l'attaque ")
            
        cartePlayer = input()
        cartePlayer = int(cartePlayer)
        
        if cartePlayer < j:
            if carteEnnemy < i:
                player.field[cartePlayer].fight(ennemy.field[carteEnnemy])
            elif carteEnnemy == i:
                ennemy.health = ennemy.health - player.field[cartePlayer].attack    
            
    # Deployer une carte
    
    print("Vous avez ", player.mana ," point(s) de mana.")
    
    carteDeploy = False
    while carteDeploy == False:     
        print("Quels serviteurs voulez-vous placer sur le terrain ?")
        i = 0
        for c in player.hand:
            print(i , ":")
            c.printCard()
            i += 1
        print(i ," : Aucune carte") 
            
        cartePlacer = input()
        cartePlacer = int(cartePlacer)
        
        if cartePlacer < i:
            carteDeploy = player.deploy(cartePlacer)
            if carteDeploy == False:
                print("Vous n'avez pas assez mana.")
        else:
            carteDeploy = True
            
    player.mana += 1
        