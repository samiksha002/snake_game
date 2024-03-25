from turtle import Turtle
move_distance=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
STARTING_POSITION=((0,0),(-20,0),(-40,0))
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)
    def add_square(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_square(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(move_distance)
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(2000,2000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)


