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
    print ("Votre score est : ", valeur_D)
    #Ici on ajoute le calcul du score

##############
### Script ###
##############

while relance:
    while i < nb_D:
        valeur_D.insert(i+1,randrange(1,7))
        i += 1
    analyseScore(valeur_D)
    relance=False

