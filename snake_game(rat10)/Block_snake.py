from turtle import Turtle,Screen
import time
from Snake import Snake
from food import Food
from score_board import Scoreboard

def nothing():
    # seg_1= Turtle("square")
    # seg_1.color("white")

    # seg_2= Turtle("square")
    # seg_2.color("white")
    # seg_2.goto(-20,0)

    # seg_3= Turtle("square")
    # seg_3.color("white")
    # seg_3.goto(-40,0)
    pass
    
#SCREEN SETUP    
scr=Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("Arc_snake")
scr.tracer(0) 
snake=Snake()
food = Food()
score = Scoreboard()

def nothing():
    # Used to stop animation
    # t=Turtle()
    # starting_position =[(0,0),(-20,0),(-40,0)]

    # segments=[]


    # for pos in starting_position:
    #     new_segment = Turtle("square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     new_segment.goto(pos)
    #     segments.append(new_segment) 
    # scr.update()
    pass
    
#GAME CONTROLS
scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")

#GAME STARTS
game_on= True

while game_on:
    scr.update()
    time.sleep(0.1) 
    snake.move()
          
    # To detect collisions
    
    if snake.segments[0].distance(food) <15:
        food.refresh()
        score.increase_score()
        
    # Detect collision with wall
    if snake.segments[0].xcor() >280 or snake.segments[0].ycor() >280 or snake.segments[0].xcor() <-280 or snake.segments[0].ycor() <-280:
        game_on=False
        score.game_over()














scr.exitonclick()