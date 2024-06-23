from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INITIAL_CARS = 15
LIMIT_ROAD = 235


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_cars()
        self.moving_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(random.randint(-LIMIT_ROAD, LIMIT_ROAD), random.randint(-LIMIT_ROAD, LIMIT_ROAD))
        new_car.setheading(180)
        self.cars.append(new_car)

    def remove_car(self, car):
        self.cars.remove(car)

    def generate_cars(self):
        for i in range(INITIAL_CARS + 1):
            self.add_car()

    def move_car(self, car):
        car.forward(self.moving_speed)

    def reset_car(self, car):
        car.goto(320, random.randint(-LIMIT_ROAD, LIMIT_ROAD))
        car.color(random.choice(COLORS))

    def increment_speed(self):
        self.moving_speed += MOVE_INCREMENT




