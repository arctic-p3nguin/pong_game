from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddles import Paddles
from ball import Ball
import time

# set up the screen
screen = Screen()
screen.setup(800, 500)
screen.bgcolor("black")

turtle = Turtle()
turtle.hideturtle()
turtle.pensize(4)
turtle.pencolor("white")
turtle.penup()
turtle.goto(0, 250)
turtle.setheading(270)
for i in range(24):
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()

# set up the scoreboard
scoreboard = Scoreboard()

# set up the paddle


l_paddle=Paddles((-360, 0))
r_paddle=Paddles((360, 0))
# set up the ball
ball = Ball()

# move the paddle
screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_is_on = True
ball.serve_right()

while game_is_on:
    screen.update()
    time.sleep(0.03)

    ball.move()

    if ball.xcor() > 380:
        time.sleep(1)
        scoreboard.scored(1)
        l_paddle.generate_paddle((-360, 0))
        r_paddle.generate_paddle((360, 0))
        ball.serve_left()

    if ball.xcor() < -380:
        time.sleep(1)
        l_paddle.generate_paddle((-360, 0))
        r_paddle.generate_paddle((360, 0))
        scoreboard.scored(2)
        ball.serve_right()

    if ball.ycor() >= 240:
        ball.head_bounce()

    if ball.ycor() <= -232:
        ball.bottom_bounce()

    if (-45 <= ball.ycor() - r_paddle.ycor() <= 45) and 350 <= ball.xcor() <= 380:
        ball.paddle_bounce()

    if (-45 <= ball.ycor() - l_paddle.ycor() <= 45) and -350 >= ball.xcor() >= -380:
        ball.paddle_bounce()

    if scoreboard.score_a == 5 or scoreboard.score_b == 5:
        game_is_on = False

screen.exitonclick()
