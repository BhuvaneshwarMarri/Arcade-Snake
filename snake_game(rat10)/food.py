from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__ (self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.8, stretch_wid= 0.8)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        x,y=random.randint(-280,280),random.randint(-280,280)
        self.goto(x,y)