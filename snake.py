from turtle import Turtle, Screen

location = [(0,0),(-20,0),(-40,0)]
screen = Screen()
snake_body = []
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    
    def create_snake(self):
        for loc in location:
            self.add_segment(loc)

    def add_segment(self, coordinate):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("White")
        segment.goto(coordinate)
        self.snake_body.append(segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def turn_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def turn_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    
    def turn_up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    
    def turn_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def move_straight(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(20)
