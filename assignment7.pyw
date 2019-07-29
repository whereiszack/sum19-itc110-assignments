#drawFace.py
#Zack Robertson
#7-28-19

from graphics import*

win = GraphWin("drawFace", 600, 600)

def drawFace():
    center = Point(150, 150)
    head = Circle(center, 50)
    head.setFill("yellow")
    head.setOutline("black")
    head.setWidth(1)
    head.draw(win)

drawFace()  
    
