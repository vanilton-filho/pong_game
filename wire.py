from turtle import Turtle


class Wire(Turtle):

    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.shape("circle")
        self.setheading(-90)
        self.color("white")
        self.drawer()

    def drawer(self):
        self.shapesize(2)
        self.stamp()
        self.penup()
        self.goto(0, 340)
        self.pendown()
        self.pensize(8)
        while self.ycor() > -340:
            self.forward(15)
            self.penup()
            self.forward(15)
            self.pendown()
