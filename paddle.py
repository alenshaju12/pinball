from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5,1)
        self.setposition(position,0)

    def goup(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def godown(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)