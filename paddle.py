from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        old_position = self.ycor()
        self.goto(self.xcor(), old_position + 20)

    def down(self):
        old_position = self.ycor()
        self.goto(self.xcor(), old_position - 20)
