from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from wire import Wire
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Score()

l_name = screen.textinput(title="Configure name", prompt="Input the LEFT player name: ").upper()
r_name = screen.textinput(title="Configure name", prompt="Input the RIGHT player name: ").upper()

score.l_player_name(l_name[0:4])
score.r_player_name(r_name[0:4])
score.update_score()
wire = Wire()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -250:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 450:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -450:
        score.r_point()
        ball.reset_position()

    if score.l_score == 10 or score.r_score == 10:
        game_is_on = False
        wire.clear()
        score.winner()


screen.exitonclick()
