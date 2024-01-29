from turtle import Screen,Turtle
import time
UP,DOWN,LEFT,RIGHT=90,270,180,0

class Snake:
    def __init__(self):
        self.starting_position =[(0,0),(-20,0),(-40,0)]
        self.segments=[]
        for pos in self.starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)
    
    def add_segment(self,pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)
    

    
    def up(self):
        if self.segments[0].heading()!= DOWN:
            self.segments[0].setheading(UP)
        
    def down(self):
        if self.segments[0].heading()!= UP:
            self.segments[0].setheading(DOWN)
    
    def left(self):
        if self.segments[0].heading()!= RIGHT:
            self.segments[0].setheading(LEFT)
    
    def right(self):
        if self.segments[0].heading()!= LEFT:
            self.segments[0].setheading(RIGHT)