# simple pong game in python for beginners
# Part  1 getting started

# import turtle
# wn = turtle.Screen()
# wn.title("Pong by Mr_Ojha")
# wn.bgcolor("black")
# wn.setup(width=800, height=600)
# wn.tracer(0)

# # score 
# score_a=0
# score_b=0

# # Paddle A 
# paddle_a = turtle.Turtle()
# paddle_a.speed(0)
# paddle_a.shape("square")
# paddle_a.color("white")
# paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# paddle_a.penup()
# paddle_a.goto(-350,0)


# # Paddle B 
# paddle_b = turtle.Turtle()
# paddle_b.speed(0)
# paddle_b.shape("square")
# paddle_b.color("white")
# paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# paddle_b.penup()
# paddle_b.goto(350,0)

# # Ball 
# ball = turtle.Turtle()
# ball.speed(0)
# ball = turtle.Turtle()
# ball.shape("square")
# ball.color("white")
# ball.penup()
# ball.goto(0,0)
# ball.dx = 0.4
# ball.dy = -0.4
 
# # pen 
# pen= turtle.Turtle()
# pen.speed(0)
# pen.color("white")
# pen.penup()
# pen.hideturtle()
# pen.goto(0,260)
# pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

# # Functions
# def paddle_a_up():
#     y=paddle_a.ycor()
#     y+=20
#     paddle_a.sety(y)

# def paddle_a_down():
#     y=paddle_a.ycor()
#     y-=20
#     paddle_a.sety(y)

# def paddle_b_up():
#     y=paddle_b.ycor()
#     y+=20
#     paddle_b.sety(y)

# def paddle_b_down():
#     y=paddle_b.ycor()
#     y-=20
#     paddle_b.sety(y)

# # keyboard binding
# wn.listen()
# wn.onkeypress(paddle_a_up,"w")
# wn.onkeypress(paddle_a_down,"s")
# wn.onkeypress(paddle_b_up,"Up")
# wn.onkeypress(paddle_b_down,"Down")

# # Main game loop 
# while True:
#     wn.update()

#     # move the ball 
#     ball.setx(ball.xcor() +ball.dx)
#     ball.sety(ball.ycor() +ball.dy)

#     # Border checking 
#     if ball.ycor()>290:
#         ball.sety(290)
#         ball.dy *= -1

#     if ball.ycor()<-290:
#         ball.sety(-290)
#         ball.dy *= -1

#     if ball.xcor()>390:
#         ball.goto(0,0)
#         ball.dx *= -1
#         score_a +=1
#         pen.clear()
#         pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier",24,"normal"))

#     if ball.xcor()<-390:
#         ball.goto(0,0)
#         ball.dx *= -1
#         score_b +=1
#         pen.clear()
#         pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier",24,"normal"))


#     # paddle and ball collision
#     if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
#         ball.setx(340)
#         ball.dx*=-1

#     if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
#         ball.setx(-340)
#         ball.dx*=-1


import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Pong by Mr_Ojha")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score variables
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = -0.4

# Pen (for score display)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball goes past paddle B (right side)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Ball goes past paddle A (left side)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision detection
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Check for a winner
    if score_a == 10:
        pen.clear()
        pen.write("Player A wins!", align="center", font=("Courier", 24, "normal"))
        break

    if score_b == 10:
        pen.clear()
        pen.write("Player B wins!", align="center", font=("Courier", 24, "normal"))
        break

# Keep the window open
wn.mainloop()
