from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake1=Snake()
food1=Food()
scoreboard1=ScoreBoard()

screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()

    # detect collision with food
    if snake1.head.distance(food1) < 15:
        food1.refresh()
        snake1.extend()
        scoreboard1.inc_score()

    #detect collision with wall

    if snake1.head.xcor() >280 or snake1.head.xcor() <-280 or snake1.head.ycor() >280 or snake1.head.ycor() <-280:
        game_is_on=False
        scoreboard1.game_over()

    #detect collision with tail
    for segment in snake1.segments[1:]: #from the second item to the end, we dont want to check the head
        if snake1.head.distance(segment)<10:
            game_is_on=False
            scoreboard1.game_over()
    #if head collides with any segment in the tail
    #trigger game_over


screen.exitonclick()