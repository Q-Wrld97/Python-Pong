from turtle import Turtle


class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.writer = Turtle()
        self.writer2 = Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.color("white")
        self.writer.goto(0, 250)
        self.writer.shapesize(20, 20, 10)


    def update_scoreboard(self, Lscore, Rscore):
        self.writer.clear()
        self.writer.goto(0, 250)
        self.writer.write(f" {Lscore}               {Rscore}  ", font=("Times New Roman", 40, "normal"), align="center")

    def game_over(self):
        self.writer.goto(0, 0)
        self.writer.write("GAME OVER", font=("Times New Roman", 20, "normal"), align="center")
