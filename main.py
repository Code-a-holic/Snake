from turtle import Screen
import random
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

# -- Screen Setup -- #

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

# -- Game Setup -- #

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_straight()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_points()
        scoreboard.show_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.gameover()
        scoreboard.refresh_points()
        game_is_on = False

    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.refresh_points()
            scoreboard.gameover()

screen.exitonclick()
