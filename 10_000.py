#!/usr/bin/python3
#10_000.py créé par GoT le 18.08.2020--13:15:00

import os
from random import randrange

#################################
### Déclaration des variables ###
#################################

score = 0        # score avant lancer de D
gain = 0
valeur_D = []
calcul_G = []
relance = True
nb_D = 6
i = 0


#############################
### Déclaration des types ###
#############################

score = int(score)
gain = int(gain)
relance = bool(relance)
nb_D = int(nb_D)
i = int(i)


################
### Methodes ###
################

##############
### Script ###
##############

while relance:
    i = 0
    del valeur_D[:]
    calcul_G = [0,0,0,0,0,0]
    while i < nb_D:
        valeur_D.insert(i+1,randrange(1,7))
        i += 1

    print ("Résultat des dés : ", valeur_D)

    numeros_presents=set(valeur_D)
    for nbr in range (1,7):
        for de in valeur_D:
            if de == nbr:
                if nbr ==1:
                    calcul_G[0] +=1
                elif nbr ==2:
                    calcul_G[1] +=1
                elif nbr ==3:
                    calcul_G[2] +=1
                elif nbr ==4:
                    calcul_G[3] +=1
                elif nbr ==5:
                    calcul_G[4] +=1
                elif nbr ==6:
                    calcul_G[5] +=1

    gain = 0
    position = 0
    if calcul_G == [1,1,1,1,1,1]:
        gain += 2000
        nb_D -= 6
    else:
        print(calcul_G)
        for de in calcul_G:
            while de >= 3:
                de -= 3
                nb_D -= 3
                if position == 0:
                    gain += 1000
                elif position >= 0:
                    gain += (position+1)*100
            if position == 0:
                gain += de*100
                nb_D -= de
            elif position == 4:
                gain += de*50
                nb_D -= de
            position += 1

    score += gain
    print(gain)
    print(score)
    if gain ==0:
        relance = False
        print("Vous avez perdu après avoir fait un score de", score, "points")
    elif nb_D == 0:
            nb_D = 6
            print("On relance les 6 dés")
    elif relance:
            print("on relance ce qu'il reste")
