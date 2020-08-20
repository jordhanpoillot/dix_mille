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
    print ("Résultat des dés : ", valeur_D)
    print("Votre score actuel est de : ", score)
    numeros_presents=set(valeur_D)
    if valeur_D == [1,2,3,4,5,6]:
        print ("Vous avez effectué une suite, et obtenez X points")
    else:
        for nbr in range (1,7):
            quantite=0
            for de in valeur_D:
                if de == nbr:
                    quantite+=1
            if quantite >= 3:
                if nbr == 1:
                    print ("Vous avez obtenu ",  quantite, " dés 1, donnant un score de 1000 points")
                    score_2 = 1000
                else:
                    print("Vous avez obtenu ", quantite, " dés ", nbr, ", donnant un score de ", (100 * nbr), " points")
                    score_2 = (100 * nbr)
                while True:
                    rep=input("Voulez-vous valider ce score ? : (Tappez \"o\" pour valider ou \"n\" pour choisir les dés à relancer)")
                    if rep=="o":
                        print("Votre score passe à : ", ( score + score_2))
                        break
                    elif rep=="n":
                        print("Vous conservez votre score de : ", score)
                        while True:
                            print("Les valeurs possibles sont :", numeros_presents)
                            choix=input("Choisissez une valeur à conserver : ")
                            for numero in numeros_presents:
                                if rep == numero:
                                    print("Vous mettez de côté le ", numero)
                                    #reste à proposer la suite
                                    break
                                else:
                                    print("Choisissez une valeur parmis les dés obtenus")
                                    continue
                        break
                    else:continue

##############
### Script ###
##############

while relance:
    while i < nb_D:
        valeur_D.insert(i+1,randrange(1,7))
        i += 1
    analyseScore(valeur_D)
    relance=False

