from turtle import  Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.wri()

    def wri(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("courier", 80, "normal"))

    def finish(self):
        self.goto(0,0)
        if self.lscore==10:
            self.write(f"LEFT WON", align="center", font=("courier", 100, "normal"))
        else:
            self.write(f"RIGHT WON", align="center", font=("courier", 100, "normal"))