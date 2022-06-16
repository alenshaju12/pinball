from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove=10
        self.movespeed=0.1

    def move(self):
        x=self.xcor()+self.xmove
        y=self.ycor()+self.ymove
        time.sleep(self.movespeed)
        self.goto(x,y)

    def bouncey(self):
        self.ymove*=-1

    def bouncex(self):
        self.xmove*=-1
        self.movespeed+=0.01

    def resetposition(self):
        self.goto(0,0)
        self.bouncex()
        self.movespeed=0.1