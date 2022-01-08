from tkinter import *


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
sauvegarde = Button(frame_bis, text='@Pseudo', font=('montserrat', 20), bg='#0CF781', fg='black')
sauvegarde.pack(pady=12, fill=X)

#Placement de la frame secondaire à gauche
frame_bis.grid(row=0, column=0, sticky=W)


#Creation de l'image
width = 200
height = 200
img = PhotoImage(file='chessgame_menu/backup-copy.png').zoom(35).subsample(32)
can = Canvas(frame, width=width, height=height, bg='#2CDF85', bd=0, highlightthickness=0)
can.create_image(width/2, height/2, image=img)
can.grid(row=0, column=10, sticky=W)


#Ajout de la frame principale à la fenêtre
frame.pack(expand=YES)


#Affichage de la fenêtre
wn.mainloop()