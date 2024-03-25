from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreborad import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
food = Food()
screen.update()
game_is_on=True
score=Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<=15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.reset()
        snake.reset_snake()
    for squares in snake.segments[1:]:
        if snake.head.distance(squares)<=10:
            score.reset()
            snake.reset_snake()
screen.exitonclick()