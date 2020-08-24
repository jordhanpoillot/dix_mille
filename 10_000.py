#!/usr/bin/python3
#10_000.py créé par GoT le 18.08.2020--13:15:00

from random import randrange
import collections

#################################
### Déclaration des variables ###
#################################

# Gestion du score
score = 0           # Score personnel du joueur avant le lancer de dés
gain = 0            # Score obtenu sur un tour après le lancer de dés

# Gestion des dés
valeur_D = []       # La liste représantant le resultat des dés
nb_D = 6            # Nombre de dés utilisables
D_u = 0             # Nombre de dés qui ont marqués des points

# Gestion des tours
tour = 0            # Numéro du premier tour
nombre_partie = 100 # Nombre de partie pour réaliser des stats
stats_score = []    # On ajoute le score de chaque partie pour réaliser des stats

################
### Methodes ###
################

def analyseGain(valeur_D,gain):
	resultat_D = collections.Counter(valeur_D)
	if valeur_D.sort()==[1,2,3,4,5,6]:
		gain=2000
	elif resultat_D[1]==6:
		gain=2000
	else:
		for valeur in resultat_D.keys():
			if resultat_D[valeur] >= 3:
				if valeur == 1:
					gain+=(1000+(resultat_D[1]-3)*100)
				elif valeur == 5:
					gain+=(500+(resultat_D[5]-3)*50)
				else:
					gain+=(valeur*100)
			else:
				if valeur == 1:
					gain+=(resultat_D[1]*100)
				elif valeur == 5:
					gain+=(resultat_D[5]*50)
	return gain


def analyseStats(stats_score):
	print("Fin de partie")
	stats = collections.Counter(stats_score)
	print(stats)


##############
### Script ###
##############

while tour < nombre_partie :
	valeur_D.clear()
	for i in range (1,nb_D+1):
		valeur_D.insert(i,randrange(1,7))
	gain=analyseGain(valeur_D,gain)
	if gain == 0:
		stats_score.insert(tour,score)
		score=0
		tour += 1
	elif gain >= 650:
		score+=gain
		stats_score.insert(tour,score)
		score=0
		gain=0
		tour+=1
	else:
		if score == 0:
			stats_score.insert(tour,0)
			gain=0
			tour += 1

analyseStats(stats_score)
