from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((370, 0))

l_paddle = Paddle((-370, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

scorecard = Scorecard()

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 278 or ball.ycor() < -278:
        ball.bounce()

    if ball.distance(r_paddle) < 100 and ball.xcor() > 335 or ball.distance(l_paddle) < 100 and ball.xcor() < -335:
        ball.reversed()

     # detect when paddles misses the ball
    if ball.distance(r_paddle) > 100 and ball.xcor() > 380:
        ball.reset_position()
        scorecard.l_point()

    if ball.distance(r_paddle) > 100 and ball.xcor() < -380:
        ball.reset_position()
        scorecard.r_point()



screen.exitonclick()
