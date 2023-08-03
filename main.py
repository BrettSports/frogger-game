import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

sleep_time = 0.1
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if player.distance(car) < 22:
            player.reset()
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= 285:
        player.reset()
        scoreboard.increase_score()
        car_manager.increase_speed()


screen.exitonclick()