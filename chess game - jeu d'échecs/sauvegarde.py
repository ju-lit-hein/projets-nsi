from datetime import date, datetime
import os
import sys

pseudo = ''
filename = str(datetime.now())[:-7] + pseudo

current_save_file =  open(f'saves/{filename}.txt', 'w')


# Faire l'état de la partie


# Ecrire les données dans le fichier de sauvegarde