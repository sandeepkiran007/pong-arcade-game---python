from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)

screen.title('Pong Game')
screen.tracer(0)
screen.bgpic("background.png")

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
scoreboard = ScoreBoard()
ball = Ball()
screen.update()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up,'Up')
screen.onkey(r_paddle.move_down,'Down')
is_game_over = False
while not is_game_over:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # detect ball at the end.
    if ball.xcor() > 380:
        ball.reset()
        ball.bounce_x()
        scoreboard.l_increment()
    if ball.xcor() < -380:
        ball.reset()
        ball.bounce_x()
        scoreboard.r_increment()


screen.exitonclick()