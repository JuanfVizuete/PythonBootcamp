import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Move cars
    for car in car_manager.cars:
        car_manager.move_car(car)
        if car.xcor() < -315:
            car_manager.reset_car(car)
        # Detect collision with cars
        if player.distance(car) < 25:  # right number for detecting the collision
            game_is_on = False
            scoreboard.game_over()
            print("Game Over")
    # Detect if the player crosses the finish line for advancing to the next level
    if player.finish_line():
        car_manager.increment_speed()
        scoreboard.increase_score()





screen.exitonclick()