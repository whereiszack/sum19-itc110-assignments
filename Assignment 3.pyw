
from graphics import *

win = GraphWin("Eyes", 400, 600)

#draw a left eye
leftEye = Oval(Point (80, 150), Point(160, 200))
leftEye.setFill("white")
leftEye.draw(win)

#draw pupil and iris together
center = Point(120, 175)
leftPupil = Circle(center, 20)
leftPupil.setFill("black")
leftPupil.setOutline("lightblue")
leftPupil.setWidth(10)
leftPupil.draw(win)

#make a clown nose

noseCenter = Point(200, 300)
nose = Circle(noseCenter, 50)
nose.setFill("red")
nose.draw(win)

#make a copy of the left eye

rightEye = leftEye.clone()
rightEye.move(150, 0)
rightEye.draw(win)

rightPupil = leftPupil.clone()
rightPupil.move(150, 0)
rightPupil.draw(win)
