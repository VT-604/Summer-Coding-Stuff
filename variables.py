#IVT
#6/27
#Variables

#Inititializatio
import turtle
import random
IVT=turtle.Turtle()
turtle.colormode(255)
#Functions
def drawPoly(sides,size,color):
    IVT.fillcolor(color)
    IVT.pencolor(color)
    IVT.begin_fill()
    for i in range(sides):
        IVT.forward(size)
        IVT.left(360/sides)
    IVT.end_fill()

#Main
drawPoly(9,100,(155,24,98))
drawPoly(8,90,(165,59,207))
drawPoly(7,80,(28,255,67))
drawPoly(6,70,(45,57,254))
