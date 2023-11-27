from turtle import Turtle, Screen

screen = Screen()

class Snake:
    snake_body_build = []
    location = [(0,0),(20,0),(40,0)]

    def snake_body(self):
        input = 3
        while input > 0:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("White")
            segment.goto(Snake.location[input-1])
            Snake.snake_body_build.append(segment)
            input = input - 1
        screen.update()
    
    def turn_right(self):
        screen.update()
        for segment in range(len(Snake.snake_body_build)-1,0,-1):
            new_x = Snake.snake_body_build[segment-1].xcor()
            new_y = Snake.snake_body_build[segment-1].ycor()
            Snake.snake_body_build[segment].goto(new_x,new_y)
        Snake.snake_body_build[0].forward(20)
        Snake.snake_body_build[0].right(90)
        screen.update()

    def turn_left(self):
        screen.update()
        for segment in range(len(Snake.snake_body_build)-1,0,-1):
            new_x = Snake.snake_body_build[segment-1].xcor()
            new_y = Snake.snake_body_build[segment-1].ycor()
            Snake.snake_body_build[segment].goto(new_x,new_y)
        Snake.snake_body_build[0].forward(20)
        Snake.snake_body_build[0].left(90)
        screen.update()

    def move_straight(self):
        for segment in range(len(Snake.snake_body_build)-1,0,-1):
            new_x = Snake.snake_body_build[segment-1].xcor()
            new_y = Snake.snake_body_build[segment-1].ycor()
            Snake.snake_body_build[segment].goto(new_x,new_y)
        Snake.snake_body_build[0].forward(20)
        screen.update()