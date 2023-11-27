from turtle import Screen
import time
import food
from snake import Snake

screen = Screen()

screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

time.sleep(0.1)
snake.snake_body()


game_is_on = True


def quit_game():
    global game_is_on
    game_is_on = False


while game_is_on:
    time.sleep(0.1)
    snake.move_straight()
    screen.listen()
    screen.onkey(key="Right", fun=snake.turn_right)
    screen.onkey(key="Left", fun=snake.turn_left)
    screen.onkey(key="Escape", fun=quit_game)
    
screen.exitonclick()
