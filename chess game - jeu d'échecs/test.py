import turtle
from os import path

#WARNING: IMAGES MUST BE .GIF
currentDir = path.abspath(path.curdir) #get the python file location

wn = turtle.Screen()
wn.setup(width=700,height=400)
wn.title("image test")

wn.addshape(currentDir+"\\pieces\\roi blanc.gif") #u can make images in a new folder

myImage = turtle.Turtle()
myImage.speed(2) #so it will draw the image instantly
myImage.shape(currentDir+"\\pieces\\roi blanc.gif") #give your object the image
myImage.penup() #if you dont do this, it will draw a line
myImage.goto(0,0) #give your image a location

def click_myImage2():
    myImage2.goto(300,100)

wn.addshape(currentDir+"\\pieces\\fou blanc.gif") #u can make images in a new folder

myImage2 = turtle.Turtle()
myImage2.speed(2) #so it will draw the image instantly
myImage2.shape(currentDir+"\\pieces\\fou blanc.gif") #give your object the image
myImage2.penup() #if you dont do this, it will draw a line
myImage2.goto(-300,100) #give your image a location


myImage2.onclick(None)
myImage2.onclick(click_myImage2())

while True:
  wn.update() #update your window