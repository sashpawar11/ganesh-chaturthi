import turtle as tl
# By Saish Pawar

#Pen&CanvasSettings
tl.fillcolor("red")
top = tl.Turtle()
trunk = tl.Turtle()
eye = tl.Turtle()
tline = tl.Turtle()
ear = tl.Turtle()
tl.bgcolor("red")
top.pencolor("white")
trunk.pencolor("white")
eye.pencolor("white")
tline.pencolor("white")
ear.pencolor("white")
top.pensize(7)
trunk.pensize(7)
eye.pensize(7)
ear.pensize(7)
tl.pensize(7)
top.speed(5)
trunk.speed(5)
eye.speed(5)
tline.speed(5)
ear.speed(5)


def drawtop() :
        top.left(90)
        top.penup()
        top.forward(200)
        top.right(90)
        top.forward(90)
        top.left(90)
        top.pendown()

        top.width(5)
        top.circle(50, 90)
        top.penup()
        top.left(90)
        top.forward(53)
        top.left(90)
        top.forward(38)
        top.left(90)
        top.pendown()
        top.width(7)
        top.circle(40, 110)
        top.penup()
        top.left(90)
        top.forward(53)
        top.left(90)
        top.forward(25)
        top.left(90)
        top.pendown()
        top.width(10)
        top.circle(40, 110)
        top.hideturtle()



def drawtrunk() :
        # trunk
        trunk.penup()
        trunk.left(90)
        trunk.forward(110)
        trunk.left(90)
        trunk.pendown()
        trunk.width(5)
        trunk.circle(100, -150)
        trunk.left(180)
        trunk.width(9)
        trunk.circle(100, 240)
        trunk.penup()
        trunk.hideturtle()

def draweyes() :
        # eyes
        eye.penup()
        eye.left(90)
        eye.forward(80)
        eye.left(90)
        eye.pendown()
        eye.pendown()
        eye.width(9)
        eye.circle(50, -90)
        eye.circle(20, -240)
        eye.hideturtle()


def drawtlines() :
        tline.penup()
        tline.width(7)
        tline.right(90)
        tline.forward(70)
        tline.left(30)

        tline.pendown()
        tline.circle(30,75)
        tline.penup()
        tline.setx(0.00)
        tline.sety(-70.00)
        tline.right(110)
        tline.forward(20)
        tline.pendown()
        tline.width(5)
        tline.circle(15, 140)
        tline.hideturtle()


def drawears() :
        ear.penup()
        ear.width(11)
        ear.left(90)
        ear.forward(100)
        ear.left(90)
        ear.forward(60)
        ear.pendown()

        ear.circle(50,120)
        ear.penup()
        ear.setx(-60.00)
        ear.sety(100.00)

        ear.left(240)
        ear.pendown()
        ear.circle(30, -120)
        ear.right(180)
        ear.circle(60,97)
        ear.hideturtle()




drawtop()
drawtrunk()
draweyes()
drawtlines()
drawears()
tl.done()
