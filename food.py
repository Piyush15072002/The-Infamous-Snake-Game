# Food for the snake

import random
from turtle import Turtle


# we will use inheritance of OOPs, and inherit the Turtle class(parent class) to Food class (child class)
class Food (Turtle):

    def __init__(self):

        super().__init__()  # Constructor of the Turtle class

        self.shape("circle")

        self.penup()

        # to stretch the turtle (food) but in this case, we will reduce size
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)  # default - (20x20), new - (10x10)
        
        self.color("lime")

        self.speed("fastest")

        self.refresh()  # to produce a food
        

    def refresh(self):
        """To produce another food when the previous food is eaten"""

        # Food at a random coordinate on the screen
        x = random.randint(-270, 270)   # we should not take 300, cuz it will be at border, remember the dimension of screen
        y = random.randint(-270, 270)
        self.goto(x, y)
