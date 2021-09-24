import turtle
#import pieces

#Création du "papier" et du "crayon"
wn = turtle.Screen()
wn.tracer(30)

t = turtle.Turtle()

#Taille, dimension et couleur pour le papier et le crayon
wn.bgcolor("#27415c")
#wn.setup(width=800,height=800)
wn.title("Jeu d'échecs")
t.pensize(2)
t.shape("turtle")
t.color("black")


#Création de l'échiquier
def echiquier(x,y,c,couleur,remplissage):
    t.color('black')
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor('beige')
    if remplissage == 0:
        t.fillcolor(couleur)
    t.begin_fill()
    for _ in range(4):
        t.forward(c)
        t.left(90)
    t.end_fill()
    t.hideturtle()


remplissage = 1

'''MODIFIER LES BOUCLES EN DESSOUS AVEC DES LISTE DE NOMBRES ET DE LETTRES
OU Y = [1,2,3,4,5,6,7,8] ET X = [A,B,C,D,E,F,G,H]
ET UTILISER EXEC POUR SAVOIR QUELLE CASE (X,Y) A QUELLE POSITION (x,y)'''
for y in range(270,-361,-90):
    for x in range(-410,231,180):
        echiquier(x,y,90,"#5c3427",remplissage)
    for x in range(-320,231,180):
        echiquier(x,y,90,"#5c3427",1-remplissage)
    remplissage = 1-remplissage

print(t.pos())
wn.update()
#Attend un clic pour fermer la fenêtre de dessin
wn.mainloop()