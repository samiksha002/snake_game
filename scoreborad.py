from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score=0
        self.color("white")
        self.penup()
        with open("file.txt",mode="r") as file:
            a=file.read()
            self.high_score= int(a)
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",font=("Arial",20,"normal"))

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("file.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()