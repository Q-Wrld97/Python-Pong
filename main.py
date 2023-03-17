import time
from turtle import Screen

from Ball import ball
from Paddle import Paddle
from ScoreBoard import scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)

R_paddle = Paddle((350, 0))
L_paddle = Paddle((-350, 0))
ball = ball()
Score = scoreboard()

screen.listen()

screen.onkey(R_paddle.go_up, "Up")
screen.onkey(R_paddle.go_down, "Down")
screen.onkey(L_paddle.go_up, "w")
screen.onkey(L_paddle.go_down, "s")

game_is_on = True
l = 0
r = 0
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()

    if ball.distance(R_paddle) < 50 and ball.xcor() > 320 or ball.distance(L_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        l += 1
        Score.update_scoreboard(l,r)

    if ball.xcor() < -380:
        ball.reset_position()
        r += 1
        Score.update_scoreboard(l,r)
screen.exitonclick()
