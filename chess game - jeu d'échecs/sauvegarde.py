'''CEST EN CHANTIER 
NE MODIFIE PAS DIRECTEMENT CE FICHIER
CEST NORMAL QUE RIEN NEST LOGIQUE'''

import json


# si la partie existe, ouvrir en 'w+'
# 
def sauvegarde_partie_en_cours(nom,etat):
    exec('partie_de_' + nom + " = etat")
    save = open('partie_de_' + nom, 'w')
    save.write(etat)

# Chercher comment récupérer la position des pièces sur le plateau selon leur cases 
def etat_de_partie():
    etat = {
        'pion1' : ['', ''],
        'pion2' : ['', ''],
        'pion3' : ['', ''],
        'pion4' : ['', ''],
        'pion5' : ['', ''],
        'pion6' : ['', ''],
        'pion7' : ['', ''],
        'pion8' : ['', ''],
        'tourl' : ['', ''],
        'tourr' : ['', ''],
        'cavalierl' : ['', ''],
        'cavalierr' : ['', ''],
        'foun' : ['', ''],
        'foub' : ['', ''],
        'reine' : ['', ''],
        'roi' : ['', ''],
        'check' : False
    }
    return etat

# On regarde l'état de la partie
etat = etat_de_partie()

# On récupère le nom du joueur
nom = input('Veuilez écrire votre nom/pseudo.')

# On sauvegarde la partie
sauvegarde_partie_en_cours(nom, etat)
