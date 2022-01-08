from tkinter import *


#Création de la fenêtre
wn = Tk()


#Personnalisation de la fenêtre
wn.title("Chess Game Menu")
wn.geometry('720x480')
wn.minsize(480, 360)
    #Ajout d'un logo:   wn.iconbitmap('')
wn.config(background='#2CDF85')


#Création de la frame
frame = Frame(wn, bg='#2CDF85')


#Création du titre et du sous-titre
title = Label(frame, text='Chess Game', font=('montserrat', 35, 'bold'), bg='#2CDF85', fg='black')
subtitle = Label(frame, text='Created by Julien and Lukas', font=('montserrat', 10, 'bold', 'italic'), bg='#2CDF85', fg='black')
title.pack()
subtitle.pack()


#Ajout des boutons pour lancer les parties
JvJ = Button(frame, text='J v J', font=('montserrat', 20), bg='#36B23D', fg='black')
JvIA = Button(frame, text='J v IA', font=('montserrat', 20), bg='#36B23D', fg='black')
IAvIA = Button(frame, text='IA v IA', font=('montserrat', 20), bg='#36B23D', fg='black')
Quit_button = Button(frame, text='Quit', font=('montserrat', 20), bg='#36B23D', fg='black', command = quit)
JvJ.pack(pady=12.5, fill=X)
JvIA.pack(pady=12.5, fill=X)
IAvIA.pack(pady=12.5, fill=X)
Quit_button.pack(pady=12.5, fill=X)

#Ajout de la frame
frame.pack(expand=YES)


#Affichage de la fenêtre
wn.mainloop()