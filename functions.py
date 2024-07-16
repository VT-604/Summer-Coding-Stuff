#IVT
#6/24
#Functions Assignment

#Initialization
import turtle
IVT = turtle.Turtle()
nora = turtle.Turtle()
#Functions
def catHead():
    IVT.goto(0,0)
    IVT.circle(125,360)
def catBody():
    IVT.penup()
    IVT.goto(35,50)
    IVT.right(30)
    IVT.pendown()
    IVT.left(225)
    IVT.circle(175,90)
    IVT.circle(100,90)
    IVT.circle(175,90)
    IVT.circle(100,90)
def catLeg():
    IVT.right(25)
    IVT.circle(100,70)
    IVT.circle(20,110)
    IVT.circle(100,70)
    IVT.circle(19,110)
def catFoot():
    IVT.circle(15,110)
    IVT.circle(75,70)
    IVT.circle(14,110)
    IVT.circle(75,70)
def drawCat():
    IVT.speed(0) #head
    IVT.fillcolor("black")
    IVT.begin_fill()
    catHead()
    IVT.end_fill()
    
    IVT.penup() #back left paw
    IVT.goto(50,-230)
    IVT.pendown()
    IVT.left(30)
    catFoot()
    
    IVT.begin_fill() #torso
    catBody()
    IVT.end_fill()

    IVT.fillcolor("white") #back right paw
    IVT.begin_fill()
    IVT.penup()
    IVT.goto(150,-220)
    IVT.pendown()
    catFoot()
    IVT.end_fill()
    
    IVT.penup() #back right leg
    IVT.goto(175,-100)
    IVT.pendown()
    IVT.left(35)
    IVT.fillcolor("black")
    IVT.begin_fill()
    catLeg()
    IVT.end_fill()
    
    IVT.penup() #front left leg
    IVT.goto(10,-120)
    IVT.pendown()
    IVT.begin_fill()
    catLeg()
    IVT.end_fill()
    
    IVT.penup() # front right leg
    IVT.goto(120,-130)
    IVT.pendown()
    IVT.left(60)
    IVT.begin_fill()
    catLeg()
    IVT.end_fill()

    IVT.fillcolor("white")
    IVT.begin_fill()
    IVT.penup()#front right paw
    IVT.goto(115,-230)
    IVT.pendown()
    IVT.right(30)
    catFoot()
    IVT.end_fill()

    IVT.begin_fill()
    IVT.penup()#front left paw
    IVT.goto(-55,-230)
    IVT.pendown()
    IVT.right(0)
    catFoot()
    IVT.end_fill()

    IVT.fillcolor("black")
    IVT.begin_fill() #covers weird white line and makes cat rounder
    IVT.right(180)
    catBody()
    IVT.end_fill()
    
#Main
drawCat()
