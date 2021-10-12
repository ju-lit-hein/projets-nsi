from tkinter import Button, Frame, Label, PhotoImage, Tk
from tkinter.constants import X
from tkinter.font import Font
import time # je sais plus pourquoi c'est là 

'''CONSTANTES'''
FONT_TITRE = ('Courrier', 50)


window = Tk()
window.title("Jeu d'échecs")
window.config(bg='#27415c')
window.attributes('-fullscreen',True)
window.iconbitmap(r'pieces/icon.ico')


frame_titre = Frame(window)
label_titre = Label(frame_titre, bg='#27415c', fg='#000000', text="Jeu d'échecs", font=FONT_TITRE)

label_titre.pack(fill=X)
frame_titre.pack(fill=X, pady=0.2)



window.mainloop()
