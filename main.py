from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen=Screen()
screen.title("PONK")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

paddler = Paddle(380)
paddlel = Paddle(-380)
ball=Ball()
score=Score()
screen.listen()
screen.onkey(paddler.goup, "Up")
screen.onkey(paddler.godown, "Down")
screen.onkey(paddlel.goup, "w")
screen.onkey(paddlel.godown, "s")
gameison = True

while gameison:
    screen.update()
    ball.move()

    #detect collision with ball
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        #need to bounce
        ball.bouncey()

    if (ball.distance(paddler)<50 and ball.xcor()>340) or (ball.distance(paddlel)<50 and ball.xcor()<-340):
        ball.bouncex()

    if ball.xcor()>380:
        ball.resetposition()
        score.lscore+=1
        score.wri()

    if ball.xcor()<-380:
        ball.resetposition()
        score.rscore+=1
        score.wri()

    if score.rscore==10 or score.lscore==10:
        gameison=False
        score.finish()

screen.exitonclick()