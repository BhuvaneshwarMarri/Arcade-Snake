#importing statements
from turtle import Screen
import time
from snake_1 import Snake
from food import Food
from score_board import Scoreboard

#Screen setup
scr=Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("Arc_snake")
scr.tracer(0)
snake=Snake()
food = Food()
score = Scoreboard()

#Key controllers
scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")

game_on= True

while game_on:
    #Update after every iteration
    scr.update()
    time.sleep(0.1) 
    snake.move()
    
    #Collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        score.increase_score()
        snake.extend()
        
    #Collision with boundary
    if snake.segments[0].xcor() >280 or snake.segments[0].ycor() >280 or snake.segments[0].xcor() <-280 or snake.segments[0].ycor() <-280:
        game_on=False
        score.game_over()
    
    #Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on = False
            score.game_over()
    

scr.exitonclick()