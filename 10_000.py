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
D_u = 0          # nombre de D qui ont marqués des points
i = 0


#############################
### Déclaration des types ###
#############################

score = int(score)
gain = int(gain)
relance = bool(relance)
nb_D = int(nb_D)
D_u = int(D_u)
i = int(i)


################
### Methodes ###
################

##############
### Script ###
##############

while relance:
    i=0
    del valeur_D[:]
    while i < nb_D:
        valeur_D.insert(i+1,randrange(1,7))
        i += 1

    print ("Résultat des dés : ", valeur_D)

    gain = 0
    D_u = 0
    calcul_G=[0,0,0,0,0,0]

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
                    else:
                        break
    if calcul_G == [1,1,1,1,1,1]:
        gain=gain+2000
    else:
        if calcul_G[0]==6:
            gain=gain+2000
            D_u=D_u+6
        elif calcul_G[0]==5:
            gain=gain+1200
            D_u=D_u+5
        elif calcul_G[0]==4:
            gain=gain+1100
            D_u=D_u+4
        elif calcul_G[0]==3:
            gain=gain+1000
            D_u=D_u+3
        elif calcul_G[0]==2:
            gain=gain+200
            D_u=D_u+2
        elif calcul_G[0]==1:
            gain=gain+100
            D_u=D_u+1

        if calcul_G[1]==6:
            gain=gain+400
            D_u=D_u+6
        elif calcul_G[1]==5:
            gain=gain+200
            D_u=D_u+3
        elif calcul_G[1]==4:
            gain=gain+200
            D_u=D_u+3
        elif calcul_G[1]==3:
            gain=gain+200
            D_u=D_u+3

        if calcul_G[2]==6:
            gain=gain+600
            D_u=D_u+6
        elif calcul_G[2]==5:
            gain=gain+300
            D_u=D_u+3
        elif calcul_G[2]==4:
            gain=gain+300
            D_u=D_u+3
        elif calcul_G[2]==3:
            gain=gain+300
            D_u=D_u+3

        if calcul_G[3]==6:
            gain=gain+800
            D_u=D_u+6
        elif calcul_G[3]==5:
            gain=gain+400
            D_u=D_u+3
        elif calcul_G[3]==4:
            gain=gain+400
            D_u=D_u+3
        elif calcul_G[3]==3:
            gain=gain+400
            D_u=D_u+3

        if calcul_G[4]==6:
            gain=gain+1000
            D_u=D_u+6
        elif calcul_G[4]==5:
            gain=gain+600
            D_u=D_u+5
        elif calcul_G[4]==4:
            gain=gain+550
            D_u=D_u+4
        elif calcul_G[4]==3:
            gain=gain+500
            D_u=D_u+3
        elif calcul_G[4]==2:
            gain=gain+100
            D_u=D_u+2
        elif calcul_G[4]==1:
            gain=gain+50
            D_u=D_u+1

        if calcul_G[5]==6:
            gain=gain+1200
            D_u=D_u+6
        elif calcul_G[5]==5:
            gain=gain+600
            D_u=D_u+3
        elif calcul_G[5]==4:
            gain=gain+600
            D_u=D_u+3
        elif calcul_G[5]==3:
            gain=gain+600
            D_u=D_u+3

    score = score + gain
    print(gain)
    print(score)
    if gain ==0:
        relance = False
        print("Vous avez perdu après avoir fait un score de", score, "points")
    else:
        nb_D = nb_D - D_u

    if nb_D == 0:
        nb_D = 6
        print("On relance les 6 dés")
    elif relance:
        print("on relance ce qu'il reste")
