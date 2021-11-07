from turtle import Turtle

FONT = ("Monospace", 50, "normal")
FONT_PLAYER = ("Courier", 42, "bold")
ALIGNMENT = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.l_name = ""
        self.r_name = ""

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto((-100, 200))
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto((-220, 200))
        self.write(self.l_name, align=ALIGNMENT, font=FONT)

        self.goto((100, 200))
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto((220, 200))
        self.write(self.r_name, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def l_player_name(self, name):
        self.l_name = name

    def r_player_name(self, name):
        self.r_name = name

    def winner(self):
        self.home()
        if self.l_score > self.r_score:
            self.write(f"{self.l_name} WINNER", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"{self.r_name} WINNER", align=ALIGNMENT, font=FONT)
