import random
import turtle
from turtle import Turtle, Screen


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race enter colour")
colors = ["red","green", "yellow", "blue","purple"]
y_positions = [-70, -40, -10 ,20, 50, 80]
all_turtle = []

for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! winnning color is {winning_color}")
            else:
                print(f"You'have lost. winning color is {winning_color}")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
