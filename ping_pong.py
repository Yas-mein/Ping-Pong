import turtle

scr = turtle.Screen()
scr.title("ping pong")
scr.bgcolor("brown")
scr.setup(width=1000,height=600)

##  lefth مضرب اليسار
lefth = turtle.Turtle()
lefth.speed(0)
lefth.shape("square")
lefth.shapesize(stretch_wid=6,stretch_len=2)
lefth.color("blue")
lefth.penup()
lefth.goto(-400,0)

##  Righth مضرب اليمين
righth = turtle.Turtle()
righth.speed(0)
righth.shape("square")
righth.shapesize(stretch_wid=6,stretch_len=2)
righth.color("red")
righth.penup()
righth.goto(400,0)

##   Balll
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

## التحكم فى اعلان  النتيجه
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0,260)
score.hideturtle()
Left_player = 0
Right_player = 0
score.write("Left_player : 0    Right_player: 0" , align="center", font=("Courier", 24, "normal"))

### dynamic functions
##players move

def left_up():
    y = lefth.ycor()
    y += 20
    lefth.sety(y)
def left_down():
    y = lefth.ycor()
    y -= 20
    lefth.sety(y)

def right_up():
    y = righth.ycor()
    y += 20
    righth.sety(y)
def right_down():
    y = righth.ycor()
    y -= 20
    righth.sety(y)

scr.listen()
scr.onkeypress(left_up, "e")
scr.onkeypress(left_down, "x")
scr.onkeypress(right_up, "Up")
scr.onkeypress(right_down, "Down")

## ball loob
while True :
    scr.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
         ball.goto(0, 0)
         ball.dy *= -1
         Left_player += 1
         score.clear()
         score.write("Left_player : {}    Right_player: {}".format(
            Left_player, Right_player), align="center",
            font=("Courier", 24, "normal"))

    if  ball.xcor() < -500:
         ball.goto(0, 0)
         ball.dy *= -1
         Right_player += 1
         score.clear()
         score.write("Left_player : {}    Right_player: {}".format(
            Left_player, Right_player), align="center",
            font=("Courier", 24, "normal"))

    if (ball.xcor() > 360 and ball.xcor() < 370)and \
            (ball.ycor() < righth.ycor()+40 and ball.ycor() > righth.ycor()-40) :

        ball.setx(360)
        ball.dx *=-1

    if (ball.xcor()<-360 and ball.xcor()>-370) and\
            (ball.ycor()<lefth.ycor()+40 and ball.ycor()>lefth.ycor()-40) :

        ball.setx(-360)
        ball.dx *= -1


