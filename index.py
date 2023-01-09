# The infamous Snake game
import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("The Infamous Snake Game")
# The screen will have animations when our boxes moves, it will not give it snaky look, so we will off them using tracer
screen.tracer(0)   # We have to update screen later also after changes are done
# Tracer and update is just like GIFs, they are images, but turned so fast that it looks like video


# Dimension analysis
# the center is (0,0), so x-axis is (-300, 300) since width is 600, y-axis is (-300, 300) since height is 600
# the snake will be made using boxes or square which are by default size of 20x20, there will be 3 of them in starting

#! Creating snake and necessities

snake = Snake()

# snake's food
food = Food()

# Score
score = Score()

#! Event Handler

# now we will listen to events by user
screen.listen()

# The arrow keys are defined in turtle as following

screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")


#! The Game

gameOn = True

while gameOn:

    # Updating the screen
    screen.update() # We will only update when all segments have moved

    # Now to slow the iterations
    time.sleep(0.1)
    
    # now we will move snake
    snake.move()

    #* To Detect collision with food
    # to detect the collision, we will use distance() which will give distance of an object from our turtle
    
    if snake.head.distance(food) < 15: # the size of the turtle is 20x20, so 15 distance is good for this condition
        
        # if the food is eaten, then update the score
        score.increaseScore()

        # produce new food
        food.refresh()  

        # increasing size of snake as he eats
        snake.extend()


    #* To Detect collision with wall
    
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or (snake.head.ycor() > 280) or (snake.head.ycor() < -280):
        
        gameOn = False

        score.gameOver()

    #* To detect collisions with own tail

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif (snake.head.distance(segment) < 10):
    #         gameOn = False
    #         score.gameOver()

    # OR

    # since we don't wanna loop through the snake head [0]
    for segment in snake.segments[1:]:    # from second element till the last
        if(snake.head.distance(segment) < 10):
            gameOn = False
            score.gameOver()

















screen.exitonclick()
