l=[1,2,3,4,5,6,7,8,9]

l_premier = l[0:3]
l_dernier = l[-3:]
l_pair = l[::2]

l.append(10)
l[0:0] = [0]
l[1:4] = 'un','deux','trois'

del l[0]
del l[-1]
del l[::3]

l2 = l
l = l[-1::-1]
l3 = l[:3]*3

#print(l3)


#Tableau
d = {'nombre' : 1, 'mot' : 'mot', 'pi' : 3.14}
d['complexe'] = (1,2)
d['nombre'] = 42

#del d['pi']
#print(d)


#Test
#mot = input("Saisir : ")

#if mot in d.keys():
#    print("La valeur associée à ", mot ," est ", d[mot])
#else:
#    print(mot + " n'est pas une clé valide")

#if mot.lower == mot[::-1]:
#    print(mot," est un palindrome.")
#else:
#    print(mot," n'est pas un palindrome.")


#Boucles
#for l in d:
#    print(l)

#for k in d.keys():
#    print(k,d[k])

phrase = input("Saisir une phrase : ")

table = {}

for lettre in phrase.lower():
    if lettre in table:
        table[lettre]+=1
    else:
        table[lettre] = 1

alpha = "abcdefghijklmnopqrstuvwxyz"
for a in alpha:
    if a in table:
        print(a, " -> ", table[a])
    










