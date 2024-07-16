#Ivan Tan
#6/26
#RGB and Random

#Initialize
import turtle
import random
IVT=turtle.Turtle()
turtle.colormode(255)
IVT.speed(0)
#Functions
def randdot():
    randred=random.randint(0,255)
    randgrn=random.randint(0,255)
    randblu=random.randint(0,255)
    randsze=random.randint(1,200)
    randpos()
    IVT.dot(randsze,(randred,randgrn,randblu))
def randtri():
    randred=random.randint(0,255)
    randgrn=random.randint(0,255)
    randblu=random.randint(0,255)
    randsze=random.randint(1,200)
    randleg=random.randint(1,200)
    randdir=random.randint(0,360)
    randpos()
    IVT.left(randdir)
    IVT.fillcolor((randred,randgrn,randblu))
    IVT.pencolor((randred,randgrn,randblu))
    IVT.begin_fill()
    for i in range(3):
        IVT.forward(randleg)
        IVT.left(120)
    IVT.end_fill()
def randsqr():
    randred=random.randint(0,255)
    randgrn=random.randint(0,255)
    randblu=random.randint(0,255)
    randsze=random.randint(1,200)
    randleg=random.randint(1,200)
    randdir=random.randint(0,360)
    randpos()
    IVT.left(randdir)
    IVT.fillcolor((randred,randgrn,randblu))
    IVT.pencolor((randred,randgrn,randblu))
    IVT.begin_fill()
    for i in range(4):
        IVT.forward(randleg)
        IVT.left(90)
    IVT.end_fill()
def randpnt():
    randred=random.randint(0,255)
    randgrn=random.randint(0,255)
    randblu=random.randint(0,255)
    randsze=random.randint(1,200)
    randleg=random.randint(1,125)
    randdir=random.randint(0,360)
    randpos()
    IVT.left(randdir)
    IVT.fillcolor((randred,randgrn,randblu))
    IVT.pencolor((randred,randgrn,randblu))
    IVT.begin_fill()
    for i in range(5):
        IVT.forward(randleg)
        IVT.left(72)
    IVT.end_fill()
def randhex():
    randred=random.randint(0,255)
    randgrn=random.randint(0,255)
    randblu=random.randint(0,255)
    randsze=random.randint(1,200)
    randleg=random.randint(1,150)
    randdir=random.randint(0,360)
    randpos()
    IVT.left(randdir)
    IVT.fillcolor((randred,randgrn,randblu))
    IVT.pencolor((randred,randgrn,randblu))
    IVT.begin_fill()
    for i in range(6):
        IVT.forward(randleg)
        IVT.left(60)
    IVT.end_fill()
def randsep():
    randred=random.randint(0,255)
    randgrn=random.randint(0,255)
    randblu=random.randint(0,255)
    randsze=random.randint(1,200)
    randleg=random.randint(1,125)
    randdir=random.randint(0,360)
    randpos()
    IVT.left(randdir)
    IVT.fillcolor((randred,randgrn,randblu))
    IVT.pencolor((randred,randgrn,randblu))
    IVT.begin_fill()
    for i in range(7):
        IVT.forward(randleg)
        IVT.left(51.43)
    IVT.end_fill()
def randoct():
    randred=random.randint(0,255)
    randgrn=random.randint(0,255)
    randblu=random.randint(0,255)
    randsze=random.randint(1,200)
    randleg=random.randint(1,100)
    randdir=random.randint(0,360)
    randpos()
    IVT.left(randdir)
    IVT.fillcolor((randred,randgrn,randblu))
    IVT.pencolor((randred,randgrn,randblu))
    IVT.begin_fill()
    for i in range(8):
        IVT.forward(randleg)
        IVT.left(45)
    IVT.end_fill()
def randpos():
    IVT.penup()
    randx=random.randint(-450,450)
    randy=random.randint(-450,450)
    IVT.goto(randx,randy)
    IVT.pendown()
def randshp():
    randnum=random.randint(1,7)
    if randnum==1:
        randdot()
    if randnum==2:
        randtri()
    if randnum==3:
        randsqr()
    if randnum==4:
        randpnt()
    if randnum==5:
        randhex()
    if randnum==6:
        randsep()
    if randnum==7:
        randoct()
#Main
for i in range(1000):
    randshp()
