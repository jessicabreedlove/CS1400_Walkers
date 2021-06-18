"""
Name: Jessica Reece
Project 6
April 2021

"""
from math import hypot, sqrt
import statistics as stat
from turtle import *
from random import choice
import sys


def main():

    command_prompt = sys.argv
    if len(command_prompt) < 4:
        print("Not enough arguments")

    step_list = list(map(int, command_prompt[1].split(",")))
    num_trials = int(command_prompt[2])
    pattern = command_prompt[3].capitalize()
    names = ["Pa", "Mi-ma", "Reg"]
    walker = []

    if pattern == "All":
        for i in names:
            walker.append(i)
    else:
        walker.append(pattern)

    t = Turtle()
    s = Screen()
    t.penup()

    for i in walker:
        pattern = i
        create_turtle(t, pattern)
        for i in range(len(step_list)):
            steps = step_list[i]
            distances = move_it(steps, num_trials, pattern)
            total_distances = []
            for i in distances:
                t.goto(i)
                t.stamp()
                total_distances.append(find_distance(i))
            calculations(pattern, total_distances, steps)

    s.exitonclick()


def get_direction(pattern):
    directions = {
        "Pa": ["north", "south", "east", "west"],
        "Mi-ma": ["north", "south", "east", "west", "south"],
        "Reg": ["east", "west"]
    }
    way = choice(directions[pattern])
    return way


def find_location(way, current):
    if way == "north":
        current[1] += 1
    elif way == "south":
        current[1] -= 1
    elif way == "east":
        current[0] += 1
    else:
        current[0] -= 1
    return current


def move_it(step_list, num_trials, pattern):
    distances = []
    for trial in range(num_trials):
        current = [0, 0]
        for walk in range(step_list):
            way = get_direction(pattern)
            current = find_location(way, current)
        distances.append(current)
    return distances


def find_distance(distances):
    x, y = distances[0], distances[1]
    total_distance = x**2 + y**2
    total_distance = sqrt(total_distance)
    return total_distance


def calculations(walker, distances, step_count):
    print(f"{walker} random walk of {step_count} steps.")
    print(
        f"Mean = {stat.mean(distances):.1f} CV = {stat.stdev(distances)/stat.mean(distances):.1f}")
    print(f"Max = {max(distances):.1f} Min = {min(distances):.1f}")


def create_turtle(t: Turtle, name):
    if name == "Pa":
        t.shape("triangle")
        t.color("black")
        t.speed(0)
    elif name == "Mi-ma":
        t.shape("circle")
        t.color("red")
        t.speed(0)
    else:
        t.shape("turtle")
        t.color("blue")
        t.speed(0)


if __name__ == "__main__":
    main()
