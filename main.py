from turtle import Screen
from player import Player
import time
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Grossing The Road")
screen.setup(width=600, height=600)
is_game_on = True
screen.tracer(0)
speed = 0.1

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.goup, "Up")

while is_game_on:
    time.sleep(speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detecting Collision with Car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            score.total_score()

    # Detecting Finish Line
    if player.ycor() > 280:
        speed *=0.9
        player.goto(0, -280)
        player.setheading(90)
        score.print_score()


screen.exitonclick()