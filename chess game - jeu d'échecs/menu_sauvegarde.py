from tkinter import *
import os
from functools import partial

# Chargement de fichiers de sauvegarde
currentDir = os.path.abspath(os.path.curdir)
files = os.listdir(f'{currentDir}/saves')
for i in range(len(files)):
    files[i] = files[i][:-4]
    files[i] = f'{files[i][:13]}:{files[i][14:]}'

# Lancement de la sauvegarde
def load_game(fichier):
    file = open(f'{currentDir}\\saves\\{fichier[:13]}-{fichier[14:]}.txt', 'r')
    test = Label(wn, text=file.readlines(), font=('montserrat', 35, 'bold', 'italic'), bg='#2CDF85', fg='black')
    test.pack()


#Création de la fenêtre
wn = Tk()


#Personnalisation de la fenêtre
wn.title('Backups')
wn.geometry('1080x720')
wn.minsize(470, 360)
    #Ajout d'un logo:   wn.iconbitmap('')
wn.config(background='#2CDF85')


#Création de la frame principale
frame = Frame(wn, bg='#2CDF85')


#Création de la frame secondaire
frame_bis = Frame(frame, bg='#2CDF85')


#Titre
title = Label(wn, text='Charger une partie', font=('montserrat', 35, 'bold', 'italic'), bg='#2CDF85', fg='black')
title.pack(fill=X)


#Bouton pour lancer la sauvegarde
for i in range(len(files)):
    exec(f'save_{i} = files[i]')
    bc_button = Button(bg='#0CF781', fg='black', activebackground='#2CDF85', command=partial(load_game, f'{files[i]}'))
    sauvegarde = Button(bc_button, text=f'@{files[i][17:]}', font=('montserrat', 20), bg='#0CF781', fg='black', anchor='w', borderwidth=0, activebackground='#2CDF85', command=partial(load_game, f'{files[i]}'))
    date_time = Button(bc_button, text=f'{files[i][:16]}', font=('montserrat', 10), bg='#0CF781', fg='black', anchor='w', borderwidth=0, activebackground='#2CDF85', command=partial(load_game, f'{files[i]}'))
    bc_button.pack(fill=X, padx=100, pady=10)
    sauvegarde.pack(fill=X)
    date_time.pack(fill=X)

#Placement de la frame secondaire à gauche
frame_bis.grid(row=0, column=0, sticky=W)


#Creation de l'image
width = 200
height = 200
img = PhotoImage(file='images/backup-copy.png').zoom(35).subsample(32)
can = Canvas(frame, width=width, height=height, bg='#2CDF85', bd=0, highlightthickness=0)
can.create_image(width/2, height/2, image=img)
can.grid(row=0, column=10, sticky=W)


#Ajout de la frame principale à la fenêtre
frame.pack(expand=YES)


#Affichage de la fenêtre
#wn.update()
wn.mainloop()