# To keep track of the user's score

from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        self.color("white")

        self.hideturtle()

        self.penup()

        self.goto(0, 270)

        self.updateScore()


    def increaseScore(self):
        """To update the score by +1"""
        self.score += 1

        self.clear()

        self.updateScore()


    def updateScore(self):
        """To update the score on screen"""

        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def gameOver(self):
        """The Game is over"""

        self.goto(0,0)

        self.color("red")

        self.write("Game Over!", align="center", font=("simsun", 24, "bold"))

        self.goto(0, -30)

        self.write(f"You scored {self.score} points", align="center", font=("simsun", 14, "bold"))



    
