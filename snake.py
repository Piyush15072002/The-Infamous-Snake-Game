
#!  SNAKE

# The snake will move like how a caterpillar or a worm moves, the behind body pushes the front body
# 3-2-1, -32-1, 3--21, 3-2-1
# 3 came to 2 place, 2 came to 1 place and 1 went to new place, this way each box can be linked

from turtle import Turtle

#! Requirements
# constant are defined by uppercase in python as part of developer ethics

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

    """Class to create the Snake"""
    def __init__(self):
        """Function to initialize the Snake"""
        self.segments = []  # Empty in starting

        self.createSnake()

        self.head = self.segments[0]    # assigning the first box as head

    
    def createSnake(self):

        for position in STARTING_POSITIONS:
            self.addSegment(position)


    def addSegment(self, position):
        """To add another segment or box to snake body"""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position) # Aligning the boxes so they don't overlap
        self.segments.append(segment)



    def extend(self):
        """To increase snake's size as he eats"""
        self.addSegment(self.segments[-1].position())   # -1 means the last element of the list


    def move(self):
        # like we discussed about snake's movement, how 3rd box will come at place of 2nd box, 
        # and 2nd will go to 1st place, then 1st will move.

        # So first we will contain position of 1st, then update position of 2nd to 1st, 
        # then contain position of 2nd and update the 3rd and so on till nth box, so we will use for loop

        # Now we will go from LAST to FIRST
        for index in range(len(self.segments)-1, 0, -1):
            # This loop will start from the end of boxes, and finish on the first box

            # storing coordinates of the next box
            newX = self.segments[index-1].xcor()
            newY = self.segments[index-1].ycor()
            # segments[3].goto => segment(2) which is 3-1
            self.segments[index].goto(newX, newY)
        
        # now after the segments moved to the position of its next segment, we will update the 1st segment position
        self.head.forward(MOVE_DISTANCE)
        # now because of this, if 1st go forward, 2nd will take its place, then 3rd will take 2nd place


    # Event listening
    # Up-90, Down-270, Left-180, Right-0        (in degrees)

    def up(self):
        # To ensure, user cannot turn back when going forward (against game rule)
        if(self.head.heading() != DOWN):    # if current heading is not down
            self.head.setheading(UP)
        
    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)


