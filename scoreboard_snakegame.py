from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../Desktop/python codes/snake_game/snake_game_data.txt") as highscore_data:
            self.highscore=int(highscore_data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("../Desktop/python codes/snake_game/snake_game_data.txt",mode="w") as new_highscore_data:
                new_highscore_data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()