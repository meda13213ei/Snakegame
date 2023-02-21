from turtle import Screen
from food import Food
from snake import Snake
from scorecard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_started = True
while game_is_started:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score = 0
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.update()
        print("nom nom")
    # detect collision with food

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.gameover()
        game_is_started = False

    # detect collision with tail.
    for segment in snake.segments[1::1]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_started = False
            scoreboard.gameover()

screen.exitonclick()
