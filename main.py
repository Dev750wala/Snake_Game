from snake import Snake
from turtle import Screen
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    score.update_score()

    if snake.all_snake_parts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.count_score()

    if snake.all_snake_parts[0].xcor() > 280 or snake.all_snake_parts[0].xcor() < -280 or snake.all_snake_parts[0].ycor() > 280 or snake.all_snake_parts[0].ycor() < -280:
        score.reset()
        snake.reset()

    for part in snake.all_snake_parts[1:]:
        if snake.all_snake_parts[0].distance(part) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
