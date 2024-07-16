#Name IVT
#Date 7/1
#Initial
import turtle
import random
turtle.colormode(255)
IVT=turtle.Turtle()
IVT.speed(0)
#Function
def ocean(wave,frequency,size):
    IVT.pensize(size)
    IVT.penup()
    IVT.goto(0,0)
    IVT.pendown()
    IVT.right(90)
    for i in range(45):
        randblu=random.randint(75,255)
        randgrn=random.randint(0,50)
        IVT.pencolor((0,randgrn,randblu))
        for i in range(13):
            IVT.circle(wave,180)
            IVT.forward(frequency)
            IVT.right(180)
            IVT.circle(wave,-180)
            IVT.right(180)
            IVT.forward(frequency)
        IVT.penup()
        IVT.right(90)
        IVT.forward(520)
        IVT.left(90)
        IVT.pendown()
        IVT.forward(size)
def cityFoundation():
    IVT.goto(0,25)
    IVT.left(90)#change to 0 if testing this function only change to 90 in final
    IVT.color("black")
    IVT.pensize(1)
    IVT.begin_fill()
    IVT.forward(150)
    IVT.right(80)
    IVT.forward(500)
    IVT.right(100)
    IVT.forward(900)
    IVT.right(90)
    IVT.forward(493)
    IVT.right(90)
    IVT.forward(575)
    IVT.end_fill()
def cityBuildings():
    for i in range(100):
        randx=random.randint(-500,140)
        randy=random.randint(-450,0)
        randwidth=random.randint(20,40)
        randlength=random.randint(20,100)
        IVT.pensize(1)
        IVT.penup()
        IVT.goto(randx,randy)
        IVT.pendown()
        IVT.fillcolor("gray")
        IVT.begin_fill()
        IVT.forward(randwidth)
        IVT.left(90)
        IVT.forward(randlength)
        IVT.left(90)
        IVT.forward(randwidth)
        IVT.left(90)
        IVT.forward(randlength)
        IVT.left(90)
        IVT.end_fill()
#Main
ocean(10,1,10)
cityFoundation()
cityBuildings()
