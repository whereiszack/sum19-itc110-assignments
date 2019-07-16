#assignment 3.pyw
from graphics import *

win = GraphWin("Snowman and Trees", 600, 600)

#set backgrund color
backg = Polygon(Point(0, 0), Point(600, 0), Point(600, 600), Point(0, 600))
backg.setFill("blue")
backg.draw(win)

#make a snowy ground

snow = Polygon(Point(0, 480), Point(600, 480), Point(600, 600), Point(0, 600))
snow.setFill("white")
snow.draw(win)

#draw a snowman base
center = Point(200, 400)
snowmanBase = Circle(center, 100)
snowmanBase.setFill("white")
snowmanBase.setOutline("white")
snowmanBase.draw(win)

#draw a snowman middle
center = Point(200, 260)
snowmanMid = Circle(center, 75)
snowmanMid.setFill("white")
snowmanMid.setOutline("white")
snowmanMid.draw(win)

#draw a snowman head
center = Point(200, 140)
snowmanHead = Circle(center, 50)
snowmanHead.setFill("white")
snowmanHead.setOutline("white")
snowmanHead.draw(win)

#draw a snowman left eye
center = Point(180, 125)
snowmanLeftEye = Circle(center, 8)
snowmanLeftEye.setFill("black")
snowmanLeftEye.draw(win)

#make a copy of the left eye

snowmanRightEye = snowmanLeftEye.clone()
snowmanRightEye.move(40, 0)
snowmanRightEye.draw(win)

#draw a snowman nose

nose = Polygon(Point(195, 140), Point(230, 145), Point(195, 150))
nose.setFill("orange")
nose.draw(win)

#sraw mouth
center = Point(170, 160)
mouth1 = Circle(center, 4)
mouth1.setFill("black")
mouth1.draw(win)

#make a copy of the mouth

mouth2 = mouth1.clone()
mouth2.move(60, 0)
mouth2.draw(win)

#make a third copy of the mouth

mouth3 = mouth1.clone()
mouth3.move(20, 10)
mouth3.draw(win)

#make a fourth copy of the mouth

mouth4 = mouth1.clone()
mouth4.move(40, 10)
mouth4.draw(win)

#draw a snowman hat

hat = Polygon(Point(140, 100), Point(260, 100), Point(260, 90), Point(230, 90), Point(230, 40), Point(170, 40), Point(170,90), Point(140, 90))
hat.setFill("black")
hat.draw(win)

#draw left arm
p1 = Point(75, 200)
p2 = Point(120, 260)
leftArm = Line(p1, p2)
leftArm.setWidth(5)
leftArm.draw(win)

#draw right arm

p3 = Point(325, 200)
p4 = Point(280, 260)
rightArm = Line(p3, p4)
rightArm.setWidth(5)
rightArm.draw(win)

#draw a snowman button
center = Point(200, 260)
button1 = Circle(center, 6)
button1.setFill("black")
button1.draw(win)

#make a second button

button2 = button1.clone()
button2.move(0, -40)
button2.draw(win)

#make a third button

button3 = button1.clone()
button3.move(0, 40)
button3.draw(win)

#make the green of a tree

tree = Polygon(Point(325, 400), Point(575, 400), Point(510, 300), Point(540, 300), Point(475, 200), Point(500, 200), Point(450, 100), Point(400, 200), Point(425, 200), Point(360, 300), Point(390, 300))
tree.setFill("green")
tree.draw(win)

#make a tree trunk

trunk = Polygon(Point(410, 500), Point(490, 500), Point(480, 400), Point(420, 400))
trunk.setFill("brown")
trunk.draw(win)

#draw ball on top of tree

center = Point(450, 90)
ball = Circle(center, 20)
ball.setFill("yellow")
ball.setOutline("red")
ball.draw(win)
