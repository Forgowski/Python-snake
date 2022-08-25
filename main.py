import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def change_direct():
    screen.onkey(snake.turn_right, "Right")
    screen.onkey(snake.turn_left, "Left")
#Window setup
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

#object intialization
snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()

#loop flag
game_is_on=True

while(game_is_on):
    time.sleep(0.1)
    snake.move_snake()
    change_direct()
    screen.update()

    #food colision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_refresh()
        snake.grow_up()
    #wall colision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:

        game_is_on = False
        score.game_over()
        

    #tail colision
    for segment in snake.snake[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()









screen.exitonclick()