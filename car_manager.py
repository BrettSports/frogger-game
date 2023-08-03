import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():
        def __init__(self):

            self.all_cars = []
            self.move_distance = STARTING_MOVE_DISTANCE
            # self.deload_cars()

        def create_car(self):
            random_chance = random.randint(1, 6)
            if random_chance == 1:
                new_car = Turtle("square")
                new_car.penup()
                new_car.color(random.choice(COLORS))
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                random_y = random.randint(-240, 240)
                new_car.goto(300, random_y)
                self.all_cars.append(new_car)

        def move_car(self):
            for car in self.all_cars:
                car.backward(self.move_distance)

        def increase_speed(self):
            self.move_distance += MOVE_INCREMENT

# I could not manage to get the following code to work to have the cars clear once they are off screen.  They kept
# appearing in the middle of the screen as black squares

        # def deload_cars(self):
        #     for car in self.all_cars:
        #         if car.xcor() <= -350:
        #             car.reset()
        #             car.clear()
        #             car.penup()
        #     self.all_cars = [car for car in self.all_cars if car.xcor() > -350]
        #     self.clear_deloaded_cars()
        #
        # def clear_deloaded_cars(self):
        #     for car in self.all_cars:
        #         if car.xcor() <= -350:
        #             car.ht()  # Hide the car
        #     self.all_cars = [car for car in self.all_cars if car.xcor() > -350]