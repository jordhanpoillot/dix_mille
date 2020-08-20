#!/usr/bin/python3
#10_000.py créé par GoT le 18.08.2020--13:15:00

import os
from random import randrange

#################################
### Déclaration des variables ###
#################################

score = 0        # score avant lancer de D
score_2 = 0      # score après lancer de D
valeur_D = []
relance = True
nb_D = 6
D_u = 0          # nombre de D qui ont marqués des points
i = 0

################
### Methodes ###
################

def analyseScore(valeur_D):
    gain=0
    valeur_D.sort()
    print ("Résultat des dés : ", valeur_D)
    print("Votre score actuel est de : ", score)
    numeros_presents=set(valeur_D)
    if valeur_D == [1,2,3,4,5,6]:
        print ("Vous avez effectué une suite, et obtenez 2000 points. Vous pouvez relancer la totalité des dés."
        gain = 2000
    else:
        for nbr in range (1,7):
            quantite=0
            for de in valeur_D:
                if de == nbr:
                    quantite+=1
            if quantite == 6:
                if nbr == 1:
                    print ("Vous avez obtenu 6 dés 1, donnant un score de 2000 points. Vous relancez la totalité des dés.")
                    gain = 2000
                else:
                    gain = (100 * nbr * 2)
                    print ("Vous avez obtenu 6 dés ", nbr , " donnant un score de ", gain, " points. Vous pouvez relancer la totalité des dés.")
            elif 6 > quantite >= 3:
                if nbr == 1:
                    gain = (1000 + 100 * (quantite-3))
                    print ("Vous avez obtenu ",  quantite, " dés 1, donnant un score de ", gain, " points")
                    elif nbr ==5:
                    gain = (500 + 50 * (quantite-3))
                    print ("Vous avez obtenu ", quantite, " dés 5, donnant un score de ", gain, " points")
                    else:
                    print("Vous avez obtenu ", quantite, " dés ", nbr, ", donnant un score de ", (100 * nbr), " points")
                    gain = (100 * nbr)
                while True:
                    rep=input("Voulez-vous valider ce score ? : (Tappez \"o\" pour valider ou \"n\" pour choisir les dés à relancer)")
                    if rep=="o":
                        score += gain
                        print("Votre score total passe à : ", score)
                        break
                    elif rep=="n":
                        print("Vous conservez votre score de : ", score)
                        while True:
                            print("Les valeurs possibles sont :", numeros_presents)
                            choix=0
                            choix=input("Choisissez une valeur à conserver : ")
                            for numero in numeros_presents:
                                if int(choix) == int(numero):
                                    print("Vous mettez de côté le ", numero)
                                    break
                        break
                    else:continue

##############
### Script ###
##############

while relance:
    while i < nb_D:
        valeur_D.insert(i+1,randrange(1,7))
        #i += 1
    analyseScore(valeur_D)
    relance=False

